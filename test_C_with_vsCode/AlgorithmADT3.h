#define Stack_Init_Size 100   //定义向量空间大小
#define Stack_Increment 10    //定义向量空间的分配增量

typedef int SElemType;
typedef struct sqstack    //顺序栈模板命名为SqStack
{
	SElemType *base;     //栈底指针，在栈构造之前和销毁之后，base的值为NULL
	SElemType *top;      //栈顶指针
	int stacksize;      //当前已分配的存储空间，以元素为单位
}SqStack;

void VisitStack(SElemType e)
{
	//访问（输出）一个结点
	printf("%4d", e);
}

Status InitStack(SqStack *S)
{
	//构造一个空的顺序栈S
	S->base = (SElemType *)malloc(Stack_Init_Size * sizeof(SElemType));
	if (!S->base) VectorAllocFailure();
	S->top = S->base; //top指向栈顶的下一个元素，即新元素即将插入的位置
	S->stacksize = Stack_Init_Size;
	return OK;
}

Status DestroyStack(SqStack *S)
{
	//销毁顺序栈S
	free(S->base);
	S->base = NULL;
	S->top = NULL;
	S->stacksize = 0;
	return OK;
}

Status ClearStack(SqStack *S)
{
	//将顺序栈S清为空栈
	S->top = S->base;
	return OK;
}

Status StackEmpty(SqStack *S)
{
	//判断顺序栈S是否为空
	if (S->top == S->base) return TRUE;
	else return FALSE;
}

int StackLength(SqStack *S)
{
	//求顺序栈S的长度
	return (S->top - S->base);
}

Status GetTop(SqStack *S, SElemType *e)
{
	//用e返回栈顶元素
	if (S->top == S->base) return ERROR;
	else
	{
		e = (S->top - 1);
		return OK;
	}
}

Status Push(SqStack *S, SElemType e)
{
	//插入e为新的栈顶元素
	if (S->top - S->base == S->stacksize)
	{
		//栈满，扩容
		printf("---当前栈内元素数量为：%d，栈满，自动扩容ing···---\n", S->stacksize);
		SElemType *newbase = (SElemType *)realloc(S->base, (S->stacksize + Stack_Increment) * sizeof(SElemType));
		if (!newbase) VectorAllocFailure();
		S->base = newbase;
		S->top = S->base + S->stacksize;
		S->stacksize += Stack_Increment;
		printf("---自动扩容成功，扩容增量：%d，当前容量：%d---\n", Stack_Increment, S->stacksize);
	}
	 *(S->top++) = e;//元素e插入S->top位置，并将栈顶指针移向后一位
	return OK;
}

Status Pop(SqStack *S, SElemType *e)
{
	//删除S的栈顶元素，并用e返回其值
	if (S->top == S->base) return ERROR; //栈空
	*e = *(--S->top);//栈顶指针前移一位，返回栈顶元素
	return OK;
}

void StackTraverse(SqStack *S)
{
	//遍历顺序栈S
	SElemType *now = S->base;
	while (now != S->top) VisitStack(*now++);
}
