#include <iostream>

using namespace std;

class Stack
{
	public:
		Stack();
		Stack(int);
		Stack(const Stack&);
		~Stack();
		void Pop(int&);
		void Push(int);

		bool isEmpty {
			return topStack;
		}
	private:
		int size;
		int topStack;
		int *data;

};