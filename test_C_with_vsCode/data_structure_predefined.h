#define TRUE 1
#define FALSE 0
#define OK 0
#define ERROR 1
#define INFEASIBLE -1
#define OVERFLOW -2
//Status�Ǻ��������ͣ���ֵ�Ǻ������״̬����
typedef int Status;

#if   ElemFormat == 0 //char����
#define PFmt "%4c"
#elif ElemFormat == 1 //int����
#define PFmt "%4d"
#elif ElemFormat == 2 //float����
#define PFmt "%2.2f"
#else PFmt "%5.2e"  //double����
#endif

Status VectorAllocFailure()
{
	fprintf(stderr, "�����ռ����ʧ�ܣ�");
	system("pause");
	exit(ERROR);
}

Status NodeAllocFailure()
{
	fprintf(stderr, "���ռ����ʧ�ܣ�");
	system("pause");
	exit(ERROR);
}