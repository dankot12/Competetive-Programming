#include <bits/stdc++.h>
using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n,p,k,a[1000000],i=0,j,cnt;
    cin>>n;
    while(i<n)
    {
        cin>>p>>k;
        if(p>=k)
            a[i] = k;
        else
            a[i] = p;
        i++;
    }
    sort(a,a+n);
    cnt = 0;
    k = 1;
    for(j=0;j<n;j++)
    {
        if(k<=a[j])
        {
            a[j] = k;
            k++;
        }
        else
            cnt++;
    }
    cout<<(n - cnt);
    return 0;
}
