#include <stdio.h>
#include <string.h>
#include <stdbool.h>

enum _ttt_symbol_{
	SYMBOL_X,
	SYMBOL_O,
	SYMBOL_E
};
typedef enum _ttt_symbol_ symb_t;

struct _boardtype_ 
{
	symb_t arr[9];
};
typedef struct _boardtype_ board_t;

char get_char_from_symbol(symb_t symb)
{
	if (symb == SYMBOL_X)
		return 'X';
	else if (symb == SYMBOL_O)
		return 'O';
	else
		return '-';
}

int sprint_board(char* buf, board_t b)
{
	int count = 0;
	count += sprintf(buf+count,"\n");
	for(int i = 0; i < 9; i++)
	{

		count += sprintf(buf + count,"%c",get_char_from_symbol(b.arr[i]));
		count += sprintf(buf+count," ");
		if (i % 3 == 2)
		{
			count += sprintf(buf+count,"\n");
		}
	}
	count += sprintf(buf + count,"\n");
	return count;
}

void print_board(board_t b)
{
	char buf[30];
	sprint_board(buf,b);
	printf("%s",buf);
}

bool boards_hard_equal(board_t a, board_t b)
{
	for (int i = 0; i < 9; i++)
	{
		if (a.arr[i] != b.arr[i])
			return false;
	}
	return true;
}

int main()
{
	board_t a;
	for(int i = 0; i < 9; i++)
	{
		if (i % 3 == 1)
			a.arr[i] = SYMBOL_X;
		else
			a.arr[i] = SYMBOL_E;
	}
	board_t b;
	for(int i = 0; i < 9; i++)
	{
		if (i % 3 == 1)
			b.arr[i] = SYMBOL_X;
		else
			b.arr[i] = SYMBOL_E;
	}
	board_t c;
	for(int i = 0; i < 9; i++)
	{
		if (i / 3 == 2)
			c.arr[i] = SYMBOL_X;
		else
			c.arr[i] = SYMBOL_E;
	}
	print_board(a);
	print_board(b);
	print_board(c);
	printf("A = B? -> %d\n", boards_hard_equal(a,b));
	printf("B = C? -> %d\n", boards_hard_equal(b,c));
	printf("C = A? -> %d\n", boards_hard_equal(c,a));
}