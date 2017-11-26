#define Stack_Init_Size 100   //���������ռ��С
#define Stack_Increment 10    //���������ռ�ķ�������

typedef int SElemType;
typedef struct sqstack    //˳��ջģ������ΪSqStack
{
	SElemType *base;     //ջ��ָ�룬��ջ����֮ǰ������֮��base��ֵΪNULL
	SElemType *top;      //ջ��ָ��
	int stacksize;      //��ǰ�ѷ���Ĵ洢�ռ䣬��Ԫ��Ϊ��λ
}SqStack;

void VisitStack(SElemType e)
{
	//���ʣ������һ�����
	printf("%4d", e);
}

Status InitStack(SqStack *S)
{
	//����һ���յ�˳��ջS
	S->base = (SElemType *)malloc(Stack_Init_Size * sizeof(SElemType));
	if (!S->base) VectorAllocFailure();
	S->top = S->base; //topָ��ջ������һ��Ԫ�أ�����Ԫ�ؼ��������λ��
	S->stacksize = Stack_Init_Size;
	return OK;
}

Status DestroyStack(SqStack *S)
{
	//����˳��ջS
	free(S->base);
	S->base = NULL;
	S->top = NULL;
	S->stacksize = 0;
	return OK;
}

Status ClearStack(SqStack *S)
{
	//��˳��ջS��Ϊ��ջ
	S->top = S->base;
	return OK;
}

Status StackEmpty(SqStack *S)
{
	//�ж�˳��ջS�Ƿ�Ϊ��
	if (S->top == S->base) return TRUE;
	else return FALSE;
}

int StackLength(SqStack *S)
{
	//��˳��ջS�ĳ���
	return (S->top - S->base);
}

Status GetTop(SqStack *S, SElemType *e)
{
	//��e����ջ��Ԫ��
	if (S->top == S->base) return ERROR;
	else
	{
		e = (S->top - 1);
		return OK;
	}
}

Status Push(SqStack *S, SElemType e)
{
	//����eΪ�µ�ջ��Ԫ��
	if (S->top - S->base == S->stacksize)
	{
		//ջ��������
		printf("---��ǰջ��Ԫ������Ϊ��%d��ջ�����Զ�����ing������---\n", S->stacksize);
		SElemType *newbase = (SElemType *)realloc(S->base, (S->stacksize + Stack_Increment) * sizeof(SElemType));
		if (!newbase) VectorAllocFailure();
		S->base = newbase;
		S->top = S->base + S->stacksize;
		S->stacksize += Stack_Increment;
		printf("---�Զ����ݳɹ�������������%d����ǰ������%d---\n", Stack_Increment, S->stacksize);
	}
	 *(S->top++) = e;//Ԫ��e����S->topλ�ã�����ջ��ָ�������һλ
	return OK;
}

Status Pop(SqStack *S, SElemType *e)
{
	//ɾ��S��ջ��Ԫ�أ�����e������ֵ
	if (S->top == S->base) return ERROR; //ջ��
	*e = *(--S->top);//ջ��ָ��ǰ��һλ������ջ��Ԫ��
	return OK;
}

void StackTraverse(SqStack *S)
{
	//����˳��ջS
	SElemType *now = S->base;
	while (now != S->top) VisitStack(*now++);
}
