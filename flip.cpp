#include <cstdlib>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

int compare(int a, int b)
{
	int f[3]={a,b,b};
	
	int k=a-b;
	while((k!=1 && k!=-1)&& k!=0)
	{
		k/=2;
	}
//	cout<<k<<", "<<f[-1]<<", "<<f[k]<<endl;
	return f[k+1];
}

vector<int> flip(vector<int> arr)
{
	int restore=arr[0];
	vector<int> newarr=arr;
	vector<int>::iterator itr;
	int count=0;

	for(itr=newarr.begin()+1;itr!=newarr.end();)
	{
		if(restore== *(itr))
		{
			newarr.erase(itr);
		}
		else
		{
			restore= *(itr);
			++itr;
		}
	}
	for(itr=newarr.begin();itr!=newarr.end();++itr)
	{
		count+= *itr;
	}
//	cout<<"for flip : "<<compare(count,newarr.size()-count);
//	cout<<count<<", "<<newarr.size()<<endl;
	cout<<compare(count,newarr.size()-count);
	return newarr;
}

void fliptest(void)
{
	vector<int> arr;
	vector<int> newarr;
	vector<int>::iterator itr;
	vector<char>::iterator c_itr;
	int idx=0;
	string str;
	
	cin>>str;

//	for(c_itr=str.begin();c_itr!=str.end();++itr)
	for(idx=0;idx<str.size();++idx)
	{
		arr.push_back(static_cast<int>(str[idx]-48));
	}
/*	
	for(idx=0;idx<=100;++idx)
	{
		arr.push_back(rand()%2);
	}*/
	
/*	
	for(itr=arr.begin();itr!=arr.end();++itr)
	{
		cout<<*itr<<" | ";
	}
	cout<<endl;*/
	newarr=flip(arr);
/*	cout<<"to flip : "<<endl;
	for(itr=newarr.begin();itr!=newarr.end();++itr)
	{
		cout<<*itr<<" | ";
	}*/
}

void fliptest02(void)
{
	vector<int> arr;
	vector<int> newarr;
	vector<int>::iterator itr;
	vector<char>::iterator c_itr;
	int idx=0;
	string str;
	
	cin>>str;

	for(idx=0;idx<str.size();++idx)
	{
		arr.push_back(static_cast<int>( str[idx]&1 ) );
	}

	newarr=flip(arr);
}

int main(void)
{
	fliptest02();
	
	return 0;
}
