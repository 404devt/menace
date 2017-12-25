
#include "mainunix.h"

const uint8_t bbb[9] ={0, 2, 0,
			 0, 1, 0,
			 0, 0, 0};

int main()
{
	board_t a;
	for (int i = 0; i < 9; i++)
		a.arr[i] = bbb[i];
	printf("Orig board:\n");
	print_board(&a);
	int key = board_to_key(&a);
	board_fill_from_key(&a, key);
	printf("FILLED BOARD\n");
	print_board(&a);
	printf("END FILLED BOARD\n");


	// uint8_t moves[9];
	// board_fill_empty_moves(key,moves);
	// printf("MOVES: [");
	// for(int i = 0; i < 9; i++)
	// {
	// 	printf("%d",moves[i]);
	// 	if(i != 8)
	// 		printf(",");
	// }
	// printf("]\n");

	// board_t to;
	// for (int i = 0; i <= 5; i++)
	// {
	// 	board_transform_generic(&a,&to,i);
	// 	print_board(&to);
	// }

	// ht_print_fulltable();

	ht_put(key);

	ht_print_fulltable();

	ht_element_t* tofill;

	int indx = -1;

	printf("indx:%d pt:%d Key:%d and \n\n", indx, tofill,tofill->key);

	indx = ht_find_element_slot(key);
	ht_get_element(indx , &tofill);

	printf("indx:%d pt:%d Key:%d and \n\n", indx, tofill,tofill->key);

}


