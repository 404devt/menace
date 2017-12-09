#ifndef _BOARD_H_
#define _BOARD_H_

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

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

const symb_t bbb[9] ={SYMBOL_X, SYMBOL_O, SYMBOL_E,
			 SYMBOL_E, SYMBOL_O, SYMBOL_O,
			 SYMBOL_X, SYMBOL_E, SYMBOL_E};

struct _boardtype_ 
{
	symb_t arr[9];
};
typedef struct _boardtype_ board_t;



#endif