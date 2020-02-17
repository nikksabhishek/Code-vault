
"""
Author  : Abhishek Nikkudala
Date    : 17/02/2020
Version : Python 2.7
"""

'''
Helper Function to move elements around a pivot element,
it places elements greater than pivot to the right
and elements lesser than pivot to its left. 

Swap the pivot element to its correct position.

'''
def partition(fileNames,low,high): 
    i = ( low-1 )         
    pivot = fileNames[high]     
  
    for j in range(low , high): 
        if   fileNames[j] <= pivot: 
            i = i+1 
            fileNames[i],fileNames[j] = fileNames[j],fileNames[i] 
  
    fileNames[i+1],fileNames[high] = fileNames[high],fileNames[i+1] 
    return ( i+1 ) 

'''
Quick sort function which recursively calls 
helper to sort the array.
'''
def quickSort(fileNames,low,high): 
    if low < high: 
        pi = partition(fileNames,low,high) 
        quickSort(fileNames, low, pi-1) 
        quickSort(fileNames, pi+1, high)

def main():
        
    fileNames = ['mallika_1.jpg', 'dog005.jpg', 'grandson_2018_01_01.png', 'dog008.jpg', 'mallika_6.jpg', 
    'grandson_2018_5_23.png','dog01.png', 'mallika_11.jpg', 'mallika2.jpg', 'grandson_2018_02_5.png', 
    'grandson_2019_08_23.jpg', 'dog9.jpg', 'mallika05.jpg' ]

    n = len(fileNames) 
    quickSort(fileNames,0,n-1) 
    
    for file in fileNames:
        print file

if __name__ == '__main__':
    main()
