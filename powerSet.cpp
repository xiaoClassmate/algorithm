// CPP program to generate power set 
#include <bits/stdc++.h> 
using namespace std; 
  
void powerSet(string str, int index = -1, 
              string curr = "") 
{ 
    int n = str.length(); 
    if (index == n) 
        return; 

    cout << curr << "\n"; 
    for (int i = index + 1; i < n; i++) { 
  
        curr += str[i]; 
        powerSet(str, i, curr); 
        curr.erase(curr.size() - 1); 
    } 
    return; 
} 
  
int main() 
{ 
    string str = "abc"; 
    powerSet(str); 
    return 0; 
} 