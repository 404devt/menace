#ifndef _BOARD_H_
#define _BOARD_H_

#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#define ID_TRANS_NONE 0
#define ID_TRANS_CLOCKWISE 1
#define ID_TRANS_180 2
#define ID_TRANS_COUNTERCLOCKWISE 3
#define ID_TRANS_FLIP_LR 4
#define ID_TRANS_FLIP_TB 5

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

char get_char_from_symbol(symb_t symb);
int sprint_board(char* buf, board_t* b);
void print_board(board_t* b);
bool boards_hard_equal(board_t a, board_t b);
void board_transform_circular(board_t* from, board_t* to, int amount);
void board_transform_flip_LR(board_t* from, board_t* to);
void board_transform_flip_TB(board_t* from, board_t* to);
void board_transform_generic(board_t* from, board_t* to, uint8_t tid);
bool board_is_full(board_t* board);
int board_to_key(board_t* board);
int main();
#endif