#include <bits/stdc++.h>
using namespace std;

long long A[10000],n,i,j,cnt;

int finder(long long key)
{
    long long mi = 0,ma = n -1;
    while(mi<ma){

        if((A[mi]+A[ma]) == key)
            return 1;
        else if((A[mi]+A[ma])>key)
            ma -= 1;
        else
            mi += 1;
    }
    return 0;
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>A[i];
    }
    sort(A,A+n);
    for(j=0;j<n;j++)
        cnt += finder(2*A[j]);
    cout<<cnt;
    return 0;
}

