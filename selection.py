def selection(list):
	n=len(list)
	for i in range(0,n):
		max=i
		for j in range(0,n-i-1):
			if list[j]>list[max]:
				max=j
		temp=list[max]
		list[max]=list[i]
		list[i]=temp
	for i in list:
		print str(i)+" "
n=input("enter the number of elements to be sorted")
list=[]
for i in range(0,n):
	x=input()
	list.append(x)
selection(list)
	
