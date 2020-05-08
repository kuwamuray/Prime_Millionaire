
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/miller_rabin.hpp>
#include <boost/random/mersenne_twister.hpp>
#include <boost/timer/timer.hpp>

#include <algorithm>
#include <iostream>
#include <vector>

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

boost::random::mt19937 gen ;
namespace mp = boost::multiprecision;
using namespace std;

int C = 0 ;
int index_of_max = 99 ;
mp::cpp_int N ;
mp::cpp_int p_max = 0 ;
mp::cpp_int prime_list[10];
vector<string> prime_vec = {} ;
string sort_card = "98765432kqj1t" ;
string check3_card = "0123456789tjqk" ;



bool card_comp(const char X, const char Y){
	return sort_card.find(X) < sort_card.find(Y) ;
}



mp::cpp_int card2number(string S){
        string SSS = "" ;
        for(int i=0; i<S.length(); i++){
                if(S[i] == 't'){
                        SSS += "10";
                }else if(S[i] == 'j'){
                        SSS += "11";
                }else if(S[i] == 'q'){
                        SSS += "12";
                }else if(S[i] == 'k'){
                        SSS += "13";
                }else{
                        SSS += S[i];
                }
        }
        return mp::cpp_int(SSS) ;
}



bool check3(string S){
	int N = 0 ;
	for(int i=0; i<S.length(); i++){
		N += check3_card.find(S[i]);
	}
	//cout << "CHECK_3 : " << N << endl ;
	if(N % 3 == 1){
		return true ;
	}else{
		return false ;
	}
}



void search_quad(string S, int I){
	if(check3(S)){
	        sort(S.begin(), S.end(), card_comp) ;
        	do{
                	//cout << S << endl ;
	                ++C;
        	        N = card2number(S) * 10 + 1 ;
                	if(mp::miller_rabin_test(N, 3, gen)){
                        	++C;
	                        N += 2 ;
        	                if(mp::miller_rabin_test(N, 3, gen)){
                	                ++C;
                        	        N += 4 ;
                                	if(mp::miller_rabin_test(N, 3, gen)){
                                        	++C;
	                                        N += 2 ;
        	                                if(mp::miller_rabin_test(N, 3, gen)){
							prime_vec[I] = S ;
							if(N > p_max){
								index_of_max = I ;
								p_max = N ;
							}
                                	        }
	                                }
        	                }
                	}
        	}while(next_permutation(S.begin(), S.end(), card_comp) && prime_vec[I]=="0");
	}
}



string convert_capital(string S){
        string SSS = "";
        for(int i=0; i<S.length(); i++){
                if(check3_card.find(S[i]) == 1){
                        SSS += "A" ;
                }else if(check3_card.find(S[i]) > 9){
                        SSS += S[i] - 32 ;
                }else{
                        SSS += S[i] ;
                }
        }
        return SSS ;
}



int main() {

	for(int i = 0; i<10; i++){
		prime_list[i] = 0 ;
		prime_vec.push_back("0");
	}

	string S ;

	cout << "" << endl ;
	cout << " INPUT STRING : " << flush ;
	cin >> S ;
	cout << "" << endl ;

	boost::timer::cpu_timer timer;

	int num_joker = 0 ;
	while(S.find("x") != string::npos){
		S.erase(S.find("x"),1);
		++num_joker;
	}

	if(num_joker == 0){
		search_quad(S,0);
		cout << " QUAD PRIME : " << convert_capital(prime_vec[0]) << "X" << endl ;

	}else if(num_joker == 1){
		for(int i=10; i<14; i++){
			S += check3_card[i] ;
			search_quad(S,i-10);
			cout << " " << char(check3_card[i] - 32) << " : " << convert_capital(prime_vec[i - 10]) ;
			if(prime_vec[i - 10] != "0"){
				cout << "X" << endl ;
			}else{
				cout << " " << endl ;
			}
			S.erase(S.find(check3_card[i]),1);
		}
		cout << "" << endl ;
		if(index_of_max == 99){
			cout << " MAX QUAD PRIME : 0" << endl ;
		}else{
			cout << " MAX QUAD PRIME : " << convert_capital(prime_vec[index_of_max]) << "X" << endl;
		}

	}else if(num_joker == 2){
		int joker_index[2] = {13,13} ;
		while(p_max == 0){
			S += check3_card[joker_index[0]] ;
			S += check3_card[joker_index[1]] ;
			search_quad(S,0);
			S.erase(S.find(check3_card[joker_index[0]]),1);
			S.erase(S.find(check3_card[joker_index[1]]),1);
			if(joker_index[1] != 10){
				--joker_index[1];
			}else if(joker_index[0] != 10){
				--joker_index[0];
				joker_index[1] = joker_index[0] ;
			}else{
				cout << "PLEASE FIX HERE !!" << endl ;
				exit(0);
			}
		}
	}	

	std::string result = timer.format();

	cout << " COUNT : " << C << endl ;
	cout << "" << endl ;
	cout << result << endl ;
	return 0 ;
}
