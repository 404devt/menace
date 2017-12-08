#include <stdio.h>
#include <string.h>
#include <stdbool.h>

const uint8_t IND_CIRCLE[8] = {0,1,2,5,8,7,6,3}; 

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

void board_transform_circular(board_t* from, board_t* to, int amount)
{
	for (int i = 0; i < 8; i++)
	{
		int indx = (i+amount) % 8;
		to->arr[IND_CIRCLE[indx]] = from->arr[IND_CIRCLE[i]];
	}
	to->arr[4] = from->arr[4];
}

void board_transform_flip_LR(board_t* from, board_t* to)
{
	for (int i = 0; i < 9; i++)
	{
		if (i%3==0)
			to->arr[i+2] = from->arr[i]
		else if (i%3==2)
			to->arr[i-2] = from->arr[i]
		else
			to->arr[i] = from->arr[i]
	}
}

void board_transform_flip_TB(board_t* from, board_t* to)
{
	for (int i = 0; i < 9; i++)
	{
		if (i/3==0)
			to->arr[6+(i%3)] = from->arr[i]
		else if (i/3==2)
			to->arr[i%3] = from->arr[i]
		else
			to->arr[i] = from->arr[i]
	}
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
	board_t d;
	board_t e;
	board_transform_circular(&b,&d,0);
	board_transform_circular(&d,&e,2);
	print_board(a);
	print_board(b);
	print_board(c);
	print_board(d);
	print_board(e);
	printf("A = B? -> %d\n", boards_hard_equal(a,b));
	printf("B = C? -> %d\n", boards_hard_equal(b,c));
	printf("C = A? -> %d\n", boards_hard_equal(c,a));
	printf("B = D? -> %d\n", boards_hard_equal(b,d));
	printf("D = E? -> %d\n", boards_hard_equal(d,e));
	printf("B = E? -> %d\n", boards_hard_equal(b,e));
}