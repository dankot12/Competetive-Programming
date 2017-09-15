#include <bits/stdc++.h>
using namespace std;

long long Start[1000000],End[1000000],Contest[1000000][2],conlen,startlen,endlen;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int i;
    cin>>conlen>>startlen>>endlen;
    for(i=0;i<conlen;i++)
    {
        cin>>Contest[i][0]>>Contest[i][1];
    }
    for(i=0;i<startlen;i++)
    {
        cin>>Start[i];
    }
    for(i=0;i<endlen;i++)
    {
        cin>>End[i];
    }
    sort(Start,Start + startlen);
    sort(End,End + endlen);

    i = 0;
    long long best = INT_MAX;
    long long cnt;

    for(i=0;i<conlen;i++){
        long long mi = Contest[i][0];
        if (mi < Start[0])
            continue;
        long long ma = Contest[i][1];
        if (ma > (End[endlen - 1]))
            continue;
        long long *st = std::upper_bound(Start,Start + startlen,mi);
            --st;
        long long *ed = std::lower_bound(End,End + endlen,ma);
        cnt = *ed - *st + 1;
        best = min(best,cnt);
    }
    cout<<best;
    return 0;
}
