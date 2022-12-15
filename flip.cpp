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

vector< vector<int> > init()
{
	vector< vector<int> > output;
	vector<int> col;

	col.push_back(0);
	col.push_back(0);
	output.push_back(col);
	col.clear();
	
	col.push_back(0);
	col.push_back(1);
	output.push_back(col);
	col.clear();
	
	col.push_back(1);
	col.push_back(0);
	output.push_back(col);
	col.clear();
	
	col.push_back(1);
	col.push_back(1);
	output.push_back(col);
	col.clear();
	
	return output;
}

int flip02(vector<int> input)
{
	vector< vector<int> > mat=init();
	vector<int> restore;
	vector<int> pattern;
	vector<int> inpat;
	vector<int> various;
	vector<int>::iterator itr;
	vector< vector<int> >::iterator row;
	int value=0;
	int idx=0;
	int len=input.size();
	int i=1;
	int k=0;
	
	for(k=0;k<4;++k)
	{
		inpat.push_back(k);
		various.push_back(0);
	}
	
	for(itr=input.begin();itr!=input.end();++itr)
	{
		value += *itr;
	}
	
	for(i=1,itr=input.begin(),row=mat.begin();i<len;++i)
	{
		idx=0;
		restore.clear();
		restore.push_back(*(itr+i-1));
		restore.push_back(*(itr+i));
		while(*(row+idx) != restore)
		{
			++idx;
		}
		pattern.push_back(*(inpat.begin()+idx));
	}
	
	for(itr=pattern.begin();itr!=pattern.end();++itr)
	{
		++*(various.begin()+*itr);
	}
	
	itr=various.begin();
	
	return *(itr+1+*input.begin());
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

void fliptest03(void)
{
	vector<int> arr;
	int idx=0;
	string str;
	
	cin>>str;

	for(idx=0;idx<str.size();++idx)
	{
		arr.push_back(static_cast<int>( str[idx]&1 ) );
	}
	
	cout<<flip02(arr)<<endl;
}

int main(void)
{
	fliptest03();
	
	return 0;
}
