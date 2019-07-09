#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int isPrime(unsigned long long int v){
	int i;
	if(v < 25){
		if(v==2 || v==3 || v==5 || v==7 || v==11 || v==17 || v==19 || v==23){
			return 1;
		}else{
			return 0;
		}
	}
	for(i = 3; i <= sqrt(v); i += 2){
		if(v%i == 0){
			return 0;
		}
	}
	return 1;
}

int main(){
  int num;
  scanf("%d", &num);
	if(isPrime(num)){
    printf("É primo\n");
  }else{
    printf("Não é primo\n");
  }
	return 0;
}
