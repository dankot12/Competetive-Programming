#include <bits/stdc++.h>
using namespace std;

int main()
{
	long long int n,k,i;
	
	cin>>n>>k;
	
	if(n == 1)
	{
		cout<<0;
		return 0;
	}
	k += -1;
	
	long long int C[n],Df[n],Dr[n];
	
	for(i=0;i<n;i++)
	{
		Dr[i] = 0;
		Df[i] = 0;
	}
	
	for(i=0;i<n;i++)
	{
		cin>>C[i];
	}
	
	Df[0] = C[0];
	Df[1] = C[1]+C[0];
	for(i=2;i<n;i++)
	{
		Df[i] = C[i] + max(Df[i-1],Df[i-2]);
	} 
	/*
	g=LONG_LONG_MIN;
	for(i=k;i<n;i++)
	{
		if(Df[i]>=g){
			g = Df[i];
			p=i;
		}
	}
	*/
	Dr[k-1] = 0;
	Dr[k] = 0;
	
	for(i=k+1;i<n;i++)
	{
		Dr[i] = C[i] + max(Dr[i-1],Dr[i-2]);
	}
	
	long long int ans = Df[k] - C[k]; //Just going back, no forward.
	
	for(i=k;i<n;i++)
		ans = max(ans,Df[i] + Dr[i] - C[i]); //Finding the best score for going forward as well as backward.
		
	cout<<ans;
	
	return 0;
}
