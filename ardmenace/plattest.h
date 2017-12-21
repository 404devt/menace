#ifndef _PLATTEST_H_

#define _PLATTEST_H_
	#if defined(__AVR_ATmega168__) ||defined(__AVR_ATmega168P__) ||defined(__AVR_ATmega328P__)
		#define _ARDUINOZ_
    #endif
	#if defined(__AVR_ATmega1280__) || defined(__AVR_ATmega2560__)
		#define _ARDUINOZ_
    #endif

	#if defined(__AVR_ATmega644__) || defined(__AVR_ATmega644P__) || defined(__AVR_ATmega1284P__)
		#define _ARDUINOZ_
    #endif

	#if defined(__AVR_ATmega32U4__) || defined(__AVR_AT90USB646__) || defined(__AVR_AT90USB1286__)
		#define _ARDUINOZ_
    #endif

	#ifndef _ARDUINOZ_
		#include <stdio.h>
		#include <string.h>
		#include <stdbool.h>
		#include <stdint.h>
		#include <stdlib.h>
	#endif

#endif
