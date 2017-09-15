#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  ll a[1000000],n,m,count=1,ans,temp;
  queue <ll> q1,q2;

  cin>>n>>m;
  int i;
  for(i=0;i<n;i++)
    cin>>a[i];

  sort(a,a+n);

  for(i=n-1;i>=0;i--)
    q1.push(a[i]);

  while(m--){
    cin>>temp;
    for(;count<=temp;count++)
    {
      if(q1.front()>=q2.front())
      {
        ans = q1.front();
        q1.pop();
      }
      else{
        ans = q2.front();
        q2.pop();
      }
      q2.push(ans>>1);
    }
    cout<<ans<<"\n";
  }

  return 0;
}
