﻿#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <malloc.h>
#include <time.h>

//指针初始化，给指针分配对应的空间
void pointerInit(int **available, int **max, int **allocation, int **need, int **request, int **secured_sequence, int p_num, int r_num);

//随机分配数据值，获取available, max, allocation, need
void getRandomData(int *available, int *max, int *allocation, int *need, int *request, int *secured_sequence, int p_num, int r_num, int range_max, int range_min, float times_one, float times_two);

//request请求合法性检查，检查此次申请的数量是否合法，即请求量是否超过系统剩余，以及本次分配之后，该进程占有资源量是否超出声明量，返回值为0时代表不合法
int requestInspect(int *available, int *max, int *allocation, int *need, int *request, int *secured_sequence, int p_num, int r_num);

//获得解决方案（安全序列），返回值为0时代表找不到安全序列，即不安全
int getSolution(int *available, int *max, int *allocation, int *need, int *request, int *secured_sequence, int p_num, int r_num);

//拷贝两个指定大小的int形指针的内容，第一个拷贝给第二个
void copyIntPointer(int *a, int *b, int size);

//释放全部指针
void freePointer();


int main()
{
    int i;

    int *available=NULL;//剩余资源向量
    int *max=NULL;//最大所需资源矩阵
    int *allocation = NULL;//已分配资源矩阵
    int *need = NULL;//剩余需求矩阵
    int *request = NULL;//新请求资源向量，最后一个值为request对应的进程号（从0开始）
    int *secured_sequence = NULL;//安全序列向量，全部初始化为-1
    int p_num = 4;//进程数量向量
    int r_num = 3;//资源种类向量
    int range_max = 15;//已分配资源上限（初始化用，设为15就行）
    int range_min = 5;//已分配资源下限（初始化用，设为5就行）
    float times_one = 1.5;//比值系数1（初始化用，设为1.5就行）
    float times_two = 1.5;//比值系数2（初始化用，设为1.5就行）

    pointerInit(&available, &max, &allocation, &need, &request, &secured_sequence, p_num, r_num);
    
    request[0] = 4;
    request[1] = 5;
    request[2] = 2;
    request[3] = 1;
    
    getRandomData(available, max, allocation, need, request, secured_sequence, p_num, r_num, range_max, range_min, times_one, times_two);
    if (!requestInspect(available, max, allocation, need, request, secured_sequence, p_num, r_num))
    {
        printf("request不符合要求\n");
        return 0;
    }
    if (getSolution(available, max, allocation, need, request, secured_sequence, p_num, r_num))
    {
        printf("找到安全序列：");
        for (i = 0; i<p_num - 1; i++)
        {
            printf(" %d -", secured_sequence[i]);
        }
        printf(" %d \n", secured_sequence[p_num - 1]);
    }
    else
    {
        printf("找不到安全序列：");
    }

    scanf(" ");

}

void pointerInit(int **available, int **max, int **allocation, int **need, int **request, int **secured_sequence, int p_num, int r_num)
{
    *available = (int *)calloc(r_num, sizeof(int));
    *max = (int *)calloc(r_num*p_num, sizeof(int));
    *allocation = (int *)calloc(r_num*p_num, sizeof(int));
    *need = (int *)calloc(r_num*p_num, sizeof(int));
    *request = (int *)calloc(r_num + 1, sizeof(int));
    *secured_sequence = (int *)calloc(p_num, sizeof(int));
}

void getRandomData(int *available, int *max, int *allocation, int *need, int *request, int *secured_sequence, int p_num, int r_num, int range_max, int range_min, float times_one, float times_two)
{
    int k;
    for (k = 0; k<r_num; k++)
    {
        request[k] = 0;
    }
    do
    {
        int seed = 0;
        seed = clock()*clock()*clock()*clock()*time(NULL);
        srand(seed);
        int i, j, temp;
        int tempmin, sum;
        printf(" Allocation:");
        for (i = 0; i < p_num*r_num; i++)
        {
            temp = rand() % (range_max - range_min + 1) + range_min;
            allocation[i] = temp;
            printf("%d ", temp);
        }
        printf("\n Max:");
        for (i = 0; i < p_num*r_num; i++)
        {
            temp = rand() % (int)(range_max*times_one - allocation[i] + 1) + allocation[i];
            max[i] = temp;
            printf("%d ", temp);
        }
        tempmin = max[0] - allocation[0];
        printf("\n available:");
        for (i = 0; i < r_num; i++)
        {
            sum = 0;
            tempmin = 0;
            for (j = 0; j < p_num; j++)
            {
                sum += allocation[j*r_num + i];
            }
            for (j = 0; j < p_num; j++)
            {
                if (max[j*r_num + i] - allocation[j*r_num + i] < tempmin)
                    tempmin = max[j*r_num + i] - allocation[j*r_num + i];
            }
            temp = rand() % (int)(times_two * (sum + tempmin) - (sum + tempmin) + 1) + ((sum + tempmin));
            available[i] = temp - sum;
            printf("%d ", available[i]);
        }
        printf("\n-----getRandomData-----\n");
        for (i = 0; i<r_num*p_num; i++)
        {
            need[i] = max[i] - allocation[i];
        }
    } while (!getSolution(available, max, allocation, need, request, secured_sequence, p_num, r_num));
}

int requestInspect(int *available, int *max, int *allocation, int *need, int *request, int *secured_sequence, int p_num, int r_num)
{
    int i;
    for (i = 0; i<r_num; i++)
    {
        if ((allocation[request[r_num] * r_num + i] + request[i]) > max[request[r_num] * r_num + i])
        {
            return 0;//所需资源加已分配资源超过声明最大值，返回false
        }
        if (request[i] > available[i])
        {
            return 0;//请求资源超过系统剩余，返回false
        }
    }
    return 1;//request请求符合基本检查要求，返回true
}

int getSolution(int *available, int *max, int *allocation, int *need, int *request, int *secured_sequence, int p_num, int r_num)
{
    int i, j, m;//循环变量，无实际意义
    int flag;//标识符，标识对应线程是否能安全完成

    int *finish = (int *)calloc(p_num, sizeof(int));//进程完成指示向量，finish[x]的bool值代表第x个进程是否完成

    int *work = (int *)calloc(r_num, sizeof(int));//当前可用资源向量（实时变化，初始值等于available）
    int *allo = (int *)calloc(p_num*r_num, sizeof(int));//当前各进程占用资源矩阵（实时变化，初始值等于allocation）
    int *ned = (int *)calloc(p_num*r_num, sizeof(int));//当前各进程需求资源矩阵（实时变化，初始值等于need）

    for (j=0; j<p_num; j++)//开始寻找安全序列前，将安全序列置为-1
    {
    	secured_sequence[j] = -1;
    }

    copyIntPointer(available, work, r_num);//设置word初始值
    copyIntPointer(allocation, allo, p_num*r_num);//设置allo初始值
    copyIntPointer(need, ned, p_num*r_num);//设置ned初始值

    for (i = 0; i<r_num; i++)//预分配，计算这次资源请求后，系统资源情况
    {
        work[i] = work[i] - request[i];
        allo[request[r_num] * r_num + i] = allo[request[r_num] * r_num + i] + request[i];
        ned[request[r_num] * r_num + i] = ned[request[r_num] * r_num + i] - request[i];
    }
    //开始寻找安全序列
    for (m = 0; m<p_num; m++)//循环p_num次，每次循环寻找一条可以安全完成的进程
    {
        for (j = 0; j<p_num; j++)//循环p_num次，每次循环判断第j条进程是否可以安全完成，若可以完成，则插插入安全序列并释放资源
        {
            flag = 1;//先假设这条进程能够安全完成
            if (finish[j] == 0)
            {
                for (i = 0; i<r_num; i++)
                {
                    if (ned[j*r_num + i] > work[i])
                    {
                        flag = 0;//这条线程所需的资源超过了现有资源（work），不能安全完成
                        break;
                    }
                }
                if (flag == 1)//经过了上面的for循环，flag仍为1，则意味着这条线程所需的所有资源都在现有（work）范围内，则插入安全序列并释放资源
                {
                    secured_sequence[m] = j;//插入安全序列
                    for (i = 0; i<r_num; i++)//释放进程J所占有的资源
                    {
                        work[i] = work[i] + allo[j * r_num + i];
                    }
                    finish[j] = 1;//将第j条进程置为已完成
                    break;//跳出for j循环，即已找到第m个可以完成的进程
                }
                else
                {
                    continue;
                }
            }
            else
            {
                continue;
            }
        }
        if (secured_sequence[m] == -1)//如果安全序列成功找到，那么安全序列的最后一个值就会是最后完成的进程号。反之，若为-1，则代表未找到
        {
            return 0;//无法找到安全序列，返回false
        }
    }
    return 1;//找到安全序列，返回true；安全序列储存在secured_sequence中
}

void copyIntPointer(int *a, int *b, int size)
{
    int i;
    for (i = 0; i<size; i++)
    {
        b[i] = a[i];
    }
}

void freePointer()
{
    //先不free了
    printf("--------------------");
}
