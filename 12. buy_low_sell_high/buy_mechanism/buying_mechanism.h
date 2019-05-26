#ifndef BUYING_MECHANISM_H
#define BUYING_MECHANISM_H

#include <stdio.h>
int check_price(){}

#include <stdlib.h>

int buy_order(){
    // First check to see if there is currency in the wallet
    system("stellar-wallet-cli balance GAMFIAAEFPXEJ2SYNK24N4S4EX6F5B5G7IOIFYS6VQ644LIV3OQKMATP");
    system("cd stellarx_automation && ./buy_ripple_command.sh ; cd ..");
    printf("buy complete\n");
}

#endif