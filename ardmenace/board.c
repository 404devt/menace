#include <stdio.h>

enum _ttt_symbol_{
	SYMBOL_X,
	SYMBOL_O,
	SYMBOL_E
};
typedef enum _ttt_symbol_ ttt_symbol;

struct _boardtype_ 
{
	ttt_symbol arr[9];
};
typedef struct _boardtype_ boardtype;

char get_char_from_symbol(ttt_symbol symb)
{
	if (symb == SYMBOL_X)
		return 'X';
	else if (symb == SYMBOL_O)
		return 'O';
	else
		return '-';
}

void print_board(boardtype b)
{
	printf("\n");
	for(int i = 0; i < 9; i++)
	{

		printf("%c",get_char_from_symbol(b.arr[i]));
		printf(" ");
		if (i % 3 == 2)
		{
			printf("\n");
		}
	}
	print("\n")
}

int main()
{
	boardtype board;
	for(int i = 0; i < 9; i++)
	{
		if (i % 3 == 1)
			board.arr[i] = SYMBOL_X;
		else
			board.arr[i] = SYMBOL_E;
	}
	print_board(board);
	printf("lmao\n");
}