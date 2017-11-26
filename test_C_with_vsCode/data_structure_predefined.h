#define TRUE 1
#define FALSE 0
#define OK 0
#define ERROR 1
#define INFEASIBLE -1
#define OVERFLOW -2
//Status是函数的类型，其值是函数结果状态代码
typedef int Status;

#if   ElemFormat == 0 //char类型
#define PFmt "%4c"
#elif ElemFormat == 1 //int类型
#define PFmt "%4d"
#elif ElemFormat == 2 //float类型
#define PFmt "%2.2f"
#else PFmt "%5.2e"  //double类型
#endif

Status VectorAllocFailure()
{
	fprintf(stderr, "向量空间分配失败！");
	system("pause");
	exit(ERROR);
}

Status NodeAllocFailure()
{
	fprintf(stderr, "结点空间分配失败！");
	system("pause");
	exit(ERROR);
}