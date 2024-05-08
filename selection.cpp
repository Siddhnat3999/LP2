#include<bits/stdc++.h>
using namespace std;

void selection_sort(int arr[],int n){
	int i,j,min_ind;
	
	for(i=0;i<n-1;i++){
		min_ind=i;
		for(j=i+1;j<n;j++){
			if(arr[j]<arr[min_ind]){
				min_ind=j;
			}
		}
		if(min_ind!=i){
			swap(arr[min_ind],arr[i]);
		}
	}
}

void display(int arr[],int n){
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
}

int main(){
	int size;
	cout<<"Enter the size of array:";
	cin>>size;
	int arr[size];
	for(int i=0;i<size;i++){
		cin>>arr[i];
	}
	selection_sort(arr,size);
	display(arr,size);
	return 0;
}
