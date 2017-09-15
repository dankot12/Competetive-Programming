#include <bits/stdc++.h>
using namespace std;

int N,Q,i,j,mi,ma,num;
char Binary[100000] = {NULL};
char best[100000] = {NULL};
void changer()
{
    for(j=(mi-1);j<ma;j++)
    {
        if(Binary[j] == '0')
            Binary[j] = '1';
        else
            Binary[j] = '0';
    }
    if(strcmp(Binary,best)>0)
    {
        for(int k=0;k<N;k++)
            best[k] = Binary[k];
    }

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>N>>Q;
    for(i=0;i<N;i++){
        Binary[i] = '0';
        best[i] = '0';
    }
    for(i=0;i<Q;i++)
    {
        cin>>mi>>ma;
        changer();
    }
    for(i=0;i<N;i++)
        cout<<best[i];
    return 0;
}
