
#include "plattest.h"
// #include "board.h"

// const int SIZE_LIST[6] = {101, 211, 431, 863, 1741, 3491}
#define HT_TABLE_SIZE = 431

int ht_used_slots = 0;

struct _ht_element_t_ {
	int key;
	uint8_t moves[9];
};
typedef struct _ht_element_t_ ht_element_t;




