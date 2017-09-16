#include<iostream>
#include<stdlib.h>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long m,n,lo,hi,a[100000],t;
    cin>>t;
    while(t--){
    cin>>n>>m;

    int i;
    for(i=0;i<n;i++)
        cin>>a[i];

    sort(a,a+n);
    lo = 1;
    hi = a[n-1];
    int x;
    while(lo<hi)
    {
		x = lo + (hi-lo+1)/2;
		int ncows = 1,p=a[0];
		for(i=1;i<n;i++)
		{
			if((a[i] - p) >= x)
			{
				ncows++;
				p = a[i];
			}
		}
		if(ncows>=m)
			lo = x;
		else
			hi = x-1;
	}
	cout<<lo<<"\n";
	}
    return 0;
}
