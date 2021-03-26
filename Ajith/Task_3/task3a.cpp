#include<iostream>
#include<fstream>
#include<regex>
using namespace std;

int main() {
	ifstream infile;
	
	infile.open("input.xml");
	
	if (!infile.is_open()) {
		cout << "File could not be opened" << endl;
		return -1;
	}
	
	bool toBePrinted = false;
	int pos;
	for(string line; getline(infile, line);) {
		if(line.find("<SubscriberDetails>") != string::npos) {
			pos = line.find("<SubscriberDetails>");
			toBePrinted = true;
		}
		if(toBePrinted) {
			regex match_expr ("\\s*<[a-zA-Z]+>[a-zA-Z0-9]+</[a-zA-Z]+>");
			if (regex_match(line, match_expr)){
				regex search_expr ("<([a-zA-Z]+)>([a-zA-Z0-9]+)<");
				smatch m;
				regex_search(line, m, search_expr);
				int count=0;
				for (auto x:m){
					if (count != 0) cout << x << " ";
					count++;
				}
				cout << endl;
			}
		}
		if(line.find("</SubscriberDetails>") != string::npos) {
			toBePrinted = false;
			break;
		}
	}
	
	
	infile.close();
	
	return 0;
}
