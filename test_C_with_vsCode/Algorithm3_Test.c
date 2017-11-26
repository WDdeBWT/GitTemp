#include <stdio.h>
#include <malloc.h>

#include "data_structure_predefined.h"
#include "AlgorithmADT3.h"

int main()
{
    SqStack S; //����˳��ջģ��
    int num, low, up, i;
	char ch[2];

    printf("------Algorithm3_Test------\n");
	srand((unsigned)time(0));

	InitStack(&S); //��ʼ����ջ(��ջ�����Ӧ�ռ�)
	printf("����������ɸ�˳��ջԪ�أ�������Ҫ���ɵ�Ԫ�ظ�����");
	scanf("%d", &num);
	printf("\n������Ҫ���ɵ�Ԫ��ֵ����������Χ��\n���ޣ�");
	scanf("%d", &low);
	printf("���ޣ�");
	scanf("%d", &up);
    for (i = 0; i < num; i++) Push(&S, rand() % (up - low + 1) + low);
    printf("\n���Ա�L�е�����Ԫ��Ϊ��\n");
	StackTraverse(&S);
	
    printf("\n\n---��ѡ��˵������������֣�---\n");
    printf("1������ȫջ\t2��ѹ����Ԫ��\t3��ȡ��ջ��Ԫ��\t\n4����ȡջ����\t5�����˳��ջ\t6����������\t\nѡ��");
	scanf("%1s", ch);
	while (ch[0] != '6')
	{
		switch (ch[0])
        {
            case '1':
                StackTraverse(&S);
                break;
            case '2':
                printf("������������Ԫ��ֵ��");
		        scanf("%d", &num);
                Push(&S, num);
                break;
            case '3':
                Pop(&S, &num);
                printf("ջ��Ԫ��Ϊ��%d����Ԫ���Ѵ�ջ��ɾ��\n", num);
                break;
            case '4':
                num = StackLength(&S);
                printf("ջ��ǰ����Ϊ��%d\n", num);
                break;
            case '5':
                ClearStack(&S);
                printf("���ջ�ɹ�����ǰΪ��ջ\n");
                break;
            default:
                printf("---��������---\n");
        }
        printf("\n---ִ����ɣ���ѡ��˵������������֣�---\n");
        printf("1������ȫջ\t2��ѹ����Ԫ��\t3��ȡ��ջ��Ԫ��\t\n4����ȡջ����\t5�����˳��ջ\t6����������\t\nѡ��");
	    scanf("%1s", ch);
	}
	DestroyStack(&S);
    printf("\n------�������------\n");
	system("pause");
    return 0;
}