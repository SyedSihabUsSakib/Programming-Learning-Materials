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

struct node{
    int data;
    struct node *link;
};

struct node *header = NULL;

void printLinkedList(struct node *H)
{
    while(H!=NULL)
    {
        cout<<H->data<<" ";
        H = H->link;
    }
    cout<<endl;
}
int main()
{
   struct node *A = new node();

   A->data = 10;
   A->link = NULL;
   header = A;

   struct node *B = new node();
   B->data = 20;
   B->link = NULL;
   A->link = B;

   struct node *C = new node();
   C->data = 30;
   C->link = NULL;
   B->link = C;

   printLinkedList(header);
   printLinkedList(header);
  /* while(header!=NULL)
    {
        cout<<header->data<<" ";
        header = header->link;
    }
    cout<<endl;
    while(header!=NULL) //will not execute this code as header is not pointing to the first node rather it is holding NULL
    {
        cout<<header->data<<" ";
        header = header->link;
    }
    cout<<endl;*/

}


