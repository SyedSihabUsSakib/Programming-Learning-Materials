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

void message(); //function declaration

void message() //Function definition
{
    cout<<"welcome to the shop!"<<endl;
}

int main() {
    int number;
    cin>>number;
    for(int i=0;i<5;i++)
    {
        message(); //Calling the function
        message();
    }
}


