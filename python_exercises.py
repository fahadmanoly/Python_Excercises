
#--------------------------------------------------------------------------------------------------------
# skip two elements after the occurance of a prime number
def skippin(n):
    s=int(n**.5)+1
    for i in range(2,s):
        if n%i == 0:
            return False
    else:
        
        return True
        
arr=[1,3,2,5,8,9,6,11,23,21,29,47,39,31]
print('The given array is ',arr)
for j in arr:
    if skippin(j):
        ind=arr.index(j)
        fi=ind+1
        if fi <len(arr):
            arr.pop(fi)
        if fi < len(arr):
            arr.pop(fi)
print('The array after skipping 2 elements while a prme number occured is',arr,'\n')

#---------------------------------------------------------------------------------------------------------


# program to count the total number of duplicate elements in a list.

a=[1,2,4,2,3,5,7,5,6,8,1,4,6,78,2,9,11,98,45,33,1]
print('The given array is ',a)

count = 0
for i in range(len(a)):
    for j in range(i,len(a)):
        if i != j:
            if a[i]==a[j]:
                count=count+1
                break
        else:
            continue
print('The count of duplicate elamenets is the list is ',count,'\n')

#---------------------------------------------------------------------------------------------------------

# Write a program to find duplicate elements and remove all duplicate elements in a list.

ab=[1,2,4,2,3,5,7,5,6,8,1,4,6,78,2,9,11,98,45,33,1]
print('The given array is ',ab)
b=[]
for i in range(len(ab)):
    for j in range(i,len(ab)):
        if i != j:
            if ab[i]==ab[j]:
                b.append(ab[i])
                break
        else:
            continue
for j in b:
    ab.remove(j)
print('The duplicate elements in the array are',b)
print('list after removing duplicate elements is',ab,'\n')

#--------------------------------------------------------------------------------------------------------

#Write a program to print all prime numbers in an array and find the count of prime numbers

ap=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17]
print('The given array is ',ap)
countap=0
l2=[]
for i in ap:
    s=int(i**.5)+1
    for j in range(2,s):
        if i%j ==0:
            break
    else:
        countap=countap+1
        l2.append(i)
print('The count of prime nos in list are',countap)
print('The prime numbers contained in the list are',l2,'\n')

#---------------------------------------------------------------------------------------------------------

#Write a program to remove all prime numbers and duplicate elements in an array
a3=[1,2,3,11,4,5,2,6,7,8,9,3,11,12,4,13,5,14,6,15,16,9,17,10,12]
print('The given array is ',a3)
l3=[]
l4=[]
for i in a3:
    if i <=1:
        continue
    if i ==2 or i ==3:
        l3.append(i)
    s=int(i**.5)+1
    for j in range(2,s):
        if i%j ==0:
            break             
    else:
        l3.append(i) 
        
for k in l3:
    if k in a3:
        a3.remove(k)

for m in range(len(a3)):
    for n in range(m,len(a3)):
        if m!=n:
            
            if a3[m]==a3[n]:
                
                l4.append(a3[m])
               
for l in l4:
    if l in a3:
        a3.remove(l)
print('The list after removing prime numbers and duplicate numbers are',a3,'\n')

#---------------------------------------------------------------------------------------------------------
# Write a program to merge two arrays sorted in descending order
# Method 1
a4=[1,2,3,4,5]
b4=[9,8,7,6,5]
print('the given arrays are',a4,' and',b4)
l5=sorted(list(set(a4+b4)))
print('ascending',l5)
l5.sort(reverse=True)
print('descending',l5)

# Method 2
for i in b4:
    if i not in a4:
        a4.append(i)
print('The second method of merging ',a4,'\n')

#---------------------------------------------------------------------------------------------------------

# write a program to count the frequency of each element of an array.
af=[1,2,3,1,5,7,3,8,9,6,5,2,6,8,3,6,8,2,111,3,4,1,8,7,9,5,4,2,6,2,1,6,3,2]
count=[1]*len(af)
for i in range(len(a)):
    for j in range(len(af)):
        if i != j:
            if af[i]==af[j]:
                count[i]=count[i]+1
print('The given array is',af)
print('count of elements are',count)
b=[a.count(x) for x in a ]
print('b',b)

#---------------------------------------------------------------------------------------------------------

#Write a program to find the largest and smallest number in an array.
ass=[1,2,3,1,5,7,3,8,9,6,5,2,6,8,3,6,8,2,111,3,4,1,8,7,9,5,4,2,6,2,1,6,3,2]
max=0
min=10
for i in range(len(ass)-1):
    for j in range(1,len(ass)):
        if ass[i]<ass[j]:
            if max < ass[j]:
                max=ass[j]
            if min>ass[i]:
                min=ass[i]
print(max)
print(min)

#---------------------------------------------------------------------------------------------------------

#Write a program to separate odd and even numbers in separate arrays.
a=[1,2,3,1,5,7,3,8,9,6,5,2,6,8,3,6,8,2,111,3,4,1,8,7,9,5,4,2,6,2,1,6,3,2]
l1=[]
l2=[]
for i in a:
    if i%2==0:
        l1.append(i)
    else:
        l2.append(i)
print('even',l1)
print('odd',l2)

#---------------------------------------------------------------------------------------------------------

#Write a program to delete an element at a specific position from an array.
a=[4,1,6,3,8,2,9,5,7]
b=[]
pos=4
for i in range(len(a)):
    if i==4:
        continue
    else:
        b.append(a[i])
print('b is',b)
# or in other ways
c=a[:4]+a[5:]
print('c is',c)
# or simple way
a.pop(4)
print(a)

#---------------------------------------------------------------------------------------------------------


# Write a program to find the second largest number and second smallest number in an array.

def largest(l1):
    n=len(l1)
    largest=l1[0]
    second_lar=float()
    for i in range(n):
        if largest < l1[i]:
            second_lar=largest
            largest=l1[i]
    print('largest is',largest)
    print('second largest is',second_lar)
            
a=[1,2,3,1,5,7,3,8,9,6,5,2,6,8,3,6,8,2,111,111,3,4,1,8,7,9,5,118,118,118,4,2,6,2,1,6,3,2,118]
largest(a)

#--------------------------------------------------------------------------------------------------------


#Write a program to find the second smallest number in an array
def smal(l2):
    n=len(l2)
    sml=l2[0]
    sec_sml=10
    for i in range(n):
        if sml > l2[i]:
            sec_sml = sml
            sml = l2[i]
        elif l2[i] != sml and l2[i] < sec_sml:
            sec_sml=l2[i]
        
    print('smallest is',sml)
    print('second smallest is',sec_sml)
    
a=[1,5,8,2,1.5,3,1,5,7,3,8,9,6,5,2,6,8,3,6,8,2,111,111,3,4,1,8,7,9,5,118,118,118,4,2,6,2,1,6,3,2,118]
smal(a)

#---------------------------------------------------------------------------------------------------------
    
# shifting zeros to the left
a=[0,1,2,0,3,4,0,0,5,9,2,0,2,0,7,0]
b=[]
count=0
for i in a:
    if i!=0:
        b.append(i)
    else:
        count+=1
print(count)
b=b+[0]*count
print(b)

#---------------------------------------------------------------------------------------------------------

# write a program to count the frequency of each element of an array.
a=[1,2,3,2,3,4,2,5,6,7,8]
two_count=0
count=[1]*len(a)
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                count[i]=count[i]+1
for k in range(len(count)):
    if count[k]==2:
        two_count=a[k]
print(two_count)


#---------------------------------------------------------------------------------------------------------
print('fahad')
print('manoly')
