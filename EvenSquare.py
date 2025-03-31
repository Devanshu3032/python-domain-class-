# square of even number in list 
list1 = [1,2,3,4,5,6]
 
list2 = [x**2 for x in list1 if x%2 ==0]

print(list2)
    

#extract vowel  from string 
a = "Devanshu"
vowel = "AEIOUaeiou"
c = ""
for i in a:
    if i in vowel :
       c += i
       
print(c)

# find common element in two list 
# list1 = [1,2,3,5]
# list2 = [3,4,6,7,8]
# list3 = list1 +list2
# list4 = []
# for i in list3:
#     for j in list3(i+1):
#         if list3[i]==list3[j]:
#             list
            
# print(list4)

# nested list into single list 

list1 = [[1,2,3,4,5,1]]



#generate prime from 1 to 50 from list comprehension 

primes = [x for x in range(2, 51) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

print(primes)  
    
        
    


    