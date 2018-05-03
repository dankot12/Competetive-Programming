#include<bits/stdc++.h>
#include<stdlib.h>
#include<string>
#include<cstring>

using namespace std;

int main()
{
	string str1,str2;
	
	cout<<"Enter first strings:";
	getline(cin,str1);
	cout<<"Enter second string: ";
	getline(cin,str2);
	
	int len1,len2;
	
	len1 = str1.length();
	len2 = str2.length();
	
	int Subs[len1+1][len2+1];
	
	for(int i=0;i<len1+1;i++)
		Subs[i][0] = 0;
	for(int i=0;i<len2+1;i++)
		Subs[0][i] = 0;
	
	for(int i=1;i<len1+1;i++)
	{
		for(int j=1;j<len2+1;j++)
		{
			if(str1[i-1] == str2[j-1])
				Subs[i][j] = Subs[i-1][j-1] + 1;
			else
				Subs[i][j] = 0;
		}
	}
	
	int h_row,h_no=0;
	for(int i=1;i<len1+1;i++)
	{
		for(int j=1;j<len2+1;j++)
		{
			if(h_no<Subs[i][j])
			{
				h_row = i;
				h_no = Subs[i][j];
			}
		}
	}
	
	char str3[h_no];
	
	str3[h_no] = '\0';
	
	while(h_no>0)
	{
		str3[h_no-1] = str1[h_row-1];
		h_no--;
		h_row--;
	}
	
	cout<<"Longest SubString is "<<str3;
	
	return 0;
}
