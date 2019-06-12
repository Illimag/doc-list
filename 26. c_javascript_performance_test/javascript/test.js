var start = new Date();
function main(){
	for (a=0;a<=25;++a){
		for(b=0;b<=25;b++){
			for(c=0;c<=25;c++){
				for(d=0;d<=25;d++){
					for(e=0;e<=25;e++){
						console.log(a,b,c,d,e)
					}
				}
			}	
		}
	}
}
main();
var time = new Date() - start;
console.log("Call to doSomething took " + (time) + " milliseconds.")