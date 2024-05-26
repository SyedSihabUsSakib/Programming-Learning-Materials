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

//Appending a node in the last position of a linkedList

void appendLast(struct node *H, int val){


    if(H==NULL)
    {
        struct node *newNode = new node();
        newNode->data = val;
        newNode->link = NULL;
        H = newNode;
        header = newNode;

        return;
    }

    while(H->link!=NULL)
    {
        H=H->link;
    }

    struct node *newNode = new node();
    newNode->data = val;
    newNode->link = NULL;
    H->link = newNode;

}


//Appending a new node at the first position of the linkedList

void appendFirst(struct node *H,int val)
{

    if(H==NULL)//When linkedList's size is zero or, linkedList is empty
    {
        struct node *newNode = new node();
        newNode->data = val;
        newNode->link = NULL;
        header = newNode;

    }
    else{ //When the the size of the linkedList is not zero
        struct node *newNode = new node();
        newNode->data = val;
        newNode->link = header;
        header = newNode;
    }

}

//Appending a new node at the nth position of the linkedList. N.B-> LinkedList's size will never be zero

void appendN(struct node* H, int n, int val){

    int cnt = 1;
    while(cnt!=n-1&&n!=1){
        H = H->link;
        cnt++;
    }

    if(n==1)
    {
        struct node *newNode = new node();
        newNode->data = val;
        newNode->link = header;
        header = newNode;
    }
    else
    {
        struct node *newNode = new node();
        newNode->data = val;
        newNode->link = H->link;
        H->link = newNode;
    }

}


int main()
{
    //Created linkedList by appending new node in the last position without using function
   /*struct node *A = new node();

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
   printLinkedList(header);*/
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


    //Appending a new node in the last position of the linkedList using function

    //appendLast(header,10);
    //appendLast(header,20);
    //appendLast(header,30);
    //printLinkedList(header);

    //Appending a node at the first position of a linkedList

   // appendFirst(header,10);
    //printLinkedList(header);
   // appendFirst(header,20);
   // printLinkedList(header);
   // appendFirst(header,30);
   // printLinkedList(header);

   //Appending a node at the nth position of a linkedList. N.B-> LinkedList's size will never be zero
   appendLast(header,10);
   appendLast(header,20);
   appendLast(header,30);
   appendLast(header,40);
   cout<<"Before appending node"<<endl;
   printLinkedList(header);
   int pos,val;
   cin>>pos>>val;
   appendN(header,pos,val);
   cout<<"After appending new node"<<endl;
   printLinkedList(header);
    return 0;
}


