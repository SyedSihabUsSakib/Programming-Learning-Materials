/* Suppose in a village there are 5 houses situated one after another in a way that first house is the neighbor of the second house.
Going forward in this manner we found that last house is the neighbor of the second last house and the first house.
If a postman is standing in front of a house with a letter and seeing the address of the house he decides to go pass 23 houses to find the recipient
of the letter. In which house will he end up in?
The house number starts from number 1 and the last house number is 5.

Let, the postman is standing in front of house number n. Where n>=1 && n<=30

 */


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


int main()
{
    int arr[]={1,2,3,4,5};
    int n;
    cin>>n;//12

    int destination = 23%5; //3
    destination = (n+destination)%5;
    cout<<(destination==0?5:destination)<<endl;

    /*if(destination==0)cout<<5<<endl;
    else cout<<destination<<endl;*/
}

