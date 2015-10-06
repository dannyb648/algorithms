//check if string is a substring c++
#include <iostream>
#include <string>
using namespace std;

bool isSubString()
{
	string input1;
	string input2;
	string stringA;
	string stringB;
	cout << "Please input a string\n";
	getline(cin, input1);
	cout << "Please input another string\n";
	getline(cin, input2);
	if (input1.size() >= input2.size())
	{
		stringA = input2;
		stringB = input1;
	}
	else
	{
		stringB = input2;
		stringA = input1;
	}
	return true;
}
