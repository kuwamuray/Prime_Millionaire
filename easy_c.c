
#include <boost/multiprecision/cpp_int.hpp>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <time.h>

namespace mp = boost::multiprecision;
using namespace std;

int check_count = 0 ;
int even_count = 0 ;
int r,x;
mp::cpp_int p_max = 0 ;

mp::cpp_int pow(mp::cpp_int b, mp::cpp_int e, mp::cpp_int m){
	mp::cpp_int result = 1;
	while (e > 0) {
		if ((e & 1) == 1) result = (result * b) % m ;
		e >>= 1 ;
		b = (b * b) % m ;
	}
	return result;
}



bool is_prime3(mp::cpp_int p, int k = 50){
	check_count += 1 ;
	if(!(p & 1)){
		//cout << "hoge" << endl ;
		return false;
	}
    	mp::cpp_int d = (p - 1) >> 1 ;
    	while(!(d & 1)){
        	d = d >> 1 ;
	}
	for(int i=0; i<k; i++){
		mp::cpp_int a = rand() + 1 ;
		if(a >= p){
			a = a % (p-1) + 1 ;
		}
		//cout << "a = " << a << endl ;
		mp::cpp_int t = d ;
		mp::cpp_int y = pow(a,d,p) ;
		while((t != (p-1)) && (y != 1) && (y != p-1)){
			y = pow(y,2,p) ;
			//cout << "p = " << p << endl ;
			//cout << "t = " << t << endl ;
			//cout << "y = " << y << endl ;
			//cout << " " << endl ;
			t = t << 1 ;
		}
		///cout << "d = " << d << endl ;
		if(y != p-1 && !(t & 1)){
			//cout << "poyo" << endl ;
			return false;
		}
	}
	return true;
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
	return mp::cpp_int(std::string(SSS)) ;
}



void check3(string S){
	int N = 0 ;
	for(int i=0; i<S.length(); i++){
		cout << N << endl ;
		if(S[i] == 't'){
			N += 10 ;
		}else if(S[i] == 'j'){
			N += 11 ;
		}else if(S[i] == 'q'){
			N += 12 ;
		}else if(S[i] == 'k'){
			N += 13 ;
		}else{
			N += (int(S[i]) - 48 ) ;
		}
	}
	if(N % 3 == 0){
		cout << "SUM : " << N << endl ;
		cout << " " << endl ;
		cout << "input error: multiple 3" << endl ;
		cout << " " << endl ;
		exit(0);
	}
}



void combination(string P, string Q){
	mp::cpp_int N ;
	if(Q.length() == 1){
		N = card2number(P+Q) ;
		///cout << typeid(N).name() << endl ;
		bool B = is_prime3(N) ;
		cout << N << " : " << B << endl ;
		if(B){
			//cout << "done!!!" << endl ;
			p_max = N ;
		}
	}else{
		for(int i=0; i<Q.length(); i++){
			string PPP(Q,i,1);
			PPP = P + PPP ;
			string QQQ = "" ;
			for(int j=0; j<i; j++){
				QQQ += Q[j] ;
				//cout << QQQ << endl ;
			}
			for(int j=i+1; j<Q.length(); j++){
				QQQ += Q[j] ;
				//cout << QQQ << endl ;
			}
			if(p_max == 0){
				combination(PPP, QQQ);
			}
		}
	}
}



int main(){
	srand((unsigned)time(NULL));
	string input ;
        cout << " " << endl ;
	cout << "INPUT CARD : " ;
	cin >> input ;
	cout << " " << endl ;
	cout << input << endl;
	cout << " " << endl ;
	
	check3(input);

	string card = "" ;
	string idea = "98765432kqj1t";
	string even = "24568tq";
	for(int i=0; i<13; i++){
		for (int j=0; j<input.length(); j++){
			if(idea[i] == input[j]){
				card += idea[i] ;
				cout << i << " : " << idea[i] << " : " << int(idea[i]) << endl ;
				if(even.find(idea[i]) != std::string::npos){
					even_count += 1 ;
				}else{
					even_count  = 0 ;
				}
			}
		}
	}

	clock_t t1 = clock();
	combination("", card) ;
	clock_t t2 = clock();
	const double time = static_cast<double>(t2 - t1) / CLOCKS_PER_SEC ;

	cout << " " << endl ;
	cout << "p_max = " << p_max << endl ;
	cout << " " << endl ;
	cout << "check_count = " << check_count << endl ;
	cout << "even_count = " << even_count << endl ;
	cout << "num_card = " << input.length() << endl ;
	cout << "TIME : " << time << endl ;
	cout << " " << endl ;

	mp::cpp_int x = 1;

	for(int i=0; i<20; i++){
		r = rand() ;
		///cout << r << endl ;
		x *= r ;
	}

	cout << " " << endl ;
	cout << x << endl ;
	cout << " " << endl ;

	mp::cpp_int X = rand();
	mp::cpp_int Y = rand();
	mp::cpp_int Z = rand();
	/*
	cout << "X = " << X << endl ;
	cout << "X & 1 = " << (X & 1) << endl ;
	cout << "X & 1 == 0 : " << (X & 1 == 0) << endl ;
	cout << "Y = " << Y << endl ;
	cout << "Y & 1 = " << (Y & 1) << endl ;
	cout << "Y & 1 == 0 : " << (Y & 1 == 0) << endl ;
	cout << "Z = " << Z << endl ;
	cout << "Z & 1 = " << (Z & 1) << endl ;
	cout << "Z & 1 == 0 : " << (Z & 1 == 0) << endl ;
	*/
	mp::cpp_int XYZ = pow(X,Y,Z);
	cout << " " << endl ;
	cout << "(X^Y)%Z = " << XYZ << endl ;
	cout << " " << endl ;
	/*
	bool b = false ;
	while(!(b)){
		int pn = rand() ;
		b = is_prime3(pn) ;
		cout << pn << " : " << b << endl ;
	}
	cout << " " << endl ;
	*/
	return 0;
}

