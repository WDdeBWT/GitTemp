#include <stdio.h>
#include <malloc.h>

#include "data_structure_predefined.h"
#include "AlgorithmADT3.h"

int main()
{
    SqStack S; //创建顺序栈模板
    int num, low, up, i;
	char ch[2];

    printf("------Algorithm3_Test------\n");
	srand((unsigned)time(0));

	InitStack(&S); //初始化空栈(给栈分配对应空间)
	printf("随机生成若干个顺序栈元素，请输入要生成的元素个数：");
	scanf("%d", &num);
	printf("\n请输入要生成的元素值（整数）范围。\n下限：");
	scanf("%d", &low);
	printf("上限：");
	scanf("%d", &up);
    for (i = 0; i < num; i++) Push(&S, rand() % (up - low + 1) + low);
    printf("\n线性表L中的所有元素为：\n");
	StackTraverse(&S);
	
    printf("\n\n---请选择菜单程序（输入数字）---\n");
    printf("1：遍历全栈\t2：压入新元素\t3：取出栈顶元素\t\n4：获取栈长度\t5：清空顺序栈\t6：结束程序\t\n选择：");
	scanf("%1s", ch);
	while (ch[0] != '6')
	{
		switch (ch[0])
        {
            case '1':
                StackTraverse(&S);
                break;
            case '2':
                printf("请输入待插入的元素值：");
		        scanf("%d", &num);
                Push(&S, num);
                break;
            case '3':
                Pop(&S, &num);
                printf("栈顶元素为：%d，该元素已从栈中删除\n", num);
                break;
            case '4':
                num = StackLength(&S);
                printf("栈当前长度为：%d\n", num);
                break;
            case '5':
                ClearStack(&S);
                printf("清空栈成功，当前为空栈\n");
                break;
            default:
                printf("---输入有误---\n");
        }
        printf("\n---执行完成，请选择菜单程序（输入数字）---\n");
        printf("1：遍历全栈\t2：压入新元素\t3：取出栈顶元素\t\n4：获取栈长度\t5：清空顺序栈\t6：结束程序\t\n选择：");
	    scanf("%1s", ch);
	}
	DestroyStack(&S);
    printf("\n------程序结束------\n");
	system("pause");
    return 0;
}