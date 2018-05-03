#include<stdlib.h>
#include<iostream>
#include<bits/stdc++.h>

int main()
{
	int n;
	
	std::cout<<"Enter n: ";
	std::cin>>n;
	
	int Ways[n][n];
	
	int row,col,f;
	for(;;){
		std::cout<<"Enter Coordinates of holes?(1/0): ";
		std::cin>>f;
		if(f == 0)
			break;
		std::cout<<"Enter the coordinates of holes(x,y): ";
		std::cin>>row>>col;
		Ways[row-1][col-1] = -1;
	}
	
	for(int i=0;i<n;i++)
		Ways[i][0] = 1;
	for(int i=0;i<n;i++)
		Ways[n-1][i] = 1;
	
	for(int i=n-2;i>=0;i--)
	{
		for(int j=1;j<n;j++)
		{
			int left = Ways[i][j-1],down = Ways[i+1][j];
			
			if(Ways[i][j-1] == -1)
				left = 0;
			if(Ways[i+1][j] == -1)
				down = 0;
			
			Ways[i][j] = left + down;
		}
	}
		
	std::cout<<"No. of ways to reach top-right corner: "<<Ways[0][n-1]<<"\n";
	
	return 0;
}
