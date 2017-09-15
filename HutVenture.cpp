#include <bits/stdc++.h>
using namespace std;

long long N,i,j,petrol,n,oldkey;
std::vector< long long > H,D,P;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>N;
    for(i=0;i<N;i++)
    {
        cin>>n;
        P.push_back(n);
    }
    for(i=0;i<N;i++)
    {
        cin>>n;
        D.push_back(n);
    }
    for(i=0;i<N;i++)
    {
        j = i;
        oldkey = ((N-1)+i)%N;
        petrol = 0;
        while(j!=(oldkey+1))
        {
            petrol += P[j];
        if (D[j] > petrol)
            break;
        else{
            petrol -= D[j];
            j+= 1;
            j = j%N;
            if (j == (oldkey+1))
                H.push_back(i+1);}

        }
        }
    std::reverse(P.begin(),P.end());
    std::reverse(D.begin(),D.end());
    long long k = D[0];
    for(i=0;i<(N-1);i++)
        D[i] = D[i+1];
    D[N-1] = k;
    for(i=0;i<N;i++)
    {
        j = i;
        oldkey = ((N-1)+i)%N;
        petrol = 0;
        while(j!=(oldkey+1))
        {
            petrol += P[j];
        if (D[j] > petrol)
            break;
        else{
            petrol -= D[j];
            j+= 1;
            j = j%N;
            if (j == (oldkey+1))
                H.push_back(abs((N-1)-i)+1);}
        }
        }

    std::sort(H.begin(), H.end());
    H.erase(std::unique(H.begin(), H.end()), H.end());
    cout<<H.size()<<"\n";
    for(i=0;i<H.size();i++)
        cout<<H[i]<<" ";

    return 0;
}

