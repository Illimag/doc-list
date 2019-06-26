    /*

    "To work with any number of nested loops, so that you have a function:

        function NameOfGod(n) // n is number of letters
        name_of_god = NameOfGod( 9 )
    "

    #include <stdio.h>

    int main(){

        char a,b,c;

            for(a='A';a<='Z';++a){
                for(b='A';b<='Z';++b){
                    for(c='A';c<='Z';++c){
                        printf("%c%c%c\t",a,b,c);
                    }
                }
        }

    }

    
	"
	NameOfGod( n ) {
	    recustive_function( n, string1, "", whatever)
	}

	recursive_function( n, string1, result, whatever ){
	    check if n or whatever is "done" () -> return result
	    addition = recursive_function(n-1, modified string1, result,  modified whatever)
	    result += addition to result
	    return result
	}
	"

*/

I want to write this program so it can handle a depth of any number.

So need to rewrite this without using a,b,c variables.
