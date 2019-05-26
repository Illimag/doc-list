#include <stdio.h>

/**********************************************************/
/*                      Introduction                      */
/**********************************************************/

/* 
*
*
*
*
*

Here is a library of custom functions.
- Jaemin Kim

    1/19/2018
    - Started library
    - Added 1.strip()
    - Added 2.jsw_flush()

Thank you.

*
*
*
*
*
*/

/**********************************************************/
/*                      Function List                     */
/**********************************************************/

/* 
1. strip() - Remove trailing \n character in a string
2. jsw_flush() - Use instead for fflush()/fpurge() 
*/

/**********************************************************/
/*                           Code                         */
/**********************************************************/

/* 
1. strip()
Remove trailing \n character in a string 
*/
/**********************************************************/
int strip(char *s) {
        char *p2 = s;
        while(*s != '\0') {
            if(*s != '\t' && *s != '\n') {
                *p2++ = *s++;
            } else {
                ++s;
            }
        }
        *p2 = '\0';
    }
/**********************************************************/


/* 
2. jsw_flush()
Use instead for fflush()/fpurge() 
*/
/**********************************************************/
int jsw_flush(void){
    int ch; 
            
    do
        ch = getchar();
    while(ch != EOF && ch != '\n' );
    clearerr(stdin);   
}
/**********************************************************/
