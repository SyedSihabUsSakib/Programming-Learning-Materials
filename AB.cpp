#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*b)/gcd(a,b)
#define ff first
#define ss second
#define pb push_back
#define endl '\n'
#define w(t) ll test;cin>>test;while(test--)
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(0);
#define iof  freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#define pi acos(-1)
int fx[]={0,0,1,-1,1,1,-1,-1};
int fy[]={1,-1,0,0,-1,1,-1,1};
const int mxn=1e9+7;


void message(); //Function declaration

int sum(int a, int b)
{
    int total = a+b;
    return total; //return value of the function
}

int main() {
    int N;
    cin>>N;
    string str;
    cin>>str;
    bool flag = 0;
    for(int i=0;i<=str.size()-2;i++)
    {
        if(str[i]=='a')
        {
            if(str[i+1]=='b'){
                flag = 1;
            }
        }
        else if(str[i]=='b')
        {
            if(str[i+1]=='a')
            {
                flag = 1;
            }
        }
    }
    if(flag==1)cout<<"Yes"<<endl;

    else cout<<"No"<<endl;

}
void message() //Function definition
{
    cout<<"welcome to the shop!"<<endl;
}


