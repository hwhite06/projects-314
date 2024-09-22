import random
import secrets 
import timeit
from collections import Counter
num_list_random = []
num_list_secrets = []
big_list_random = []
big_list_secrets = []
sort_list_small = []
sort_list_big = []
long_list = []

n = 100
x = 500

#1 
#a) Fill a data structure with 100 random values using 'random'
for i in range(n) :
    num_list_random.append(random.randint(0,16))
count_rand = Counter(num_list_random)
print ("List generated with Random:", num_list_random)
#c) count the values
print ("Count of repeating values:", count_rand)

#b) Fill a data structure with 100 random values using 'secrets'
for i in range(n) :
    num_list_secrets.append(secrets.randbelow(16))
count_secrets = Counter(num_list_secrets)
print ("List generated with secrets:", num_list_secrets)
print ("Count of repeating values:", count_secrets)

#d) Both methods seem effective at producing a random set of numbers. Using random appears to result in 
# a more even distribution, however a sample of random numbers does not always have a random distribution. 

#2 Run question 1 again using numbers from 1-65535
n = 100
for i in range(n) :
    big_list_random.append(random.randint(0,65535))
count_rand_big = Counter(big_list_random)
print ("List generated with Random, large range:", big_list_random)
print ("Count of repeating values:", count_rand_big) 


for i in range(n) :
    big_list_secrets.append(secrets.randbelow(65536))
count_secrets_big = Counter(big_list_secrets)
print ("List generated with secrets, large range:", big_list_secrets)
print ("Count of repeating values:", count_secrets_big)
#because the range of numbers is bigger, there are no repeats so both lists are more likely to be a good random sample. 


#3 Fill a data structure with 100 elements, a) sort it, and b) time it 
for i in range(n) :
    sort_list_small.append(random.randint(0,16))
print ("unsorted list:", sort_list_small)
#a) sort function 
def bubble_sort(y):
    n = len(y)
    for i in range (n-1):
        swapped = False 
        for j in range (n-i-1):
            if y[j]>y[j+1]:
                y[j], y[j+1] = y[j+1], y[j]
                swapped = True 
        if not swapped:
            break 

start = timeit.default_timer()
bubble_sort(sort_list_small)
end = timeit.default_timer()
delta = end - start
print ("sorted list:", sort_list_small)
print ("time elapsed: ", delta)

for i in range(n) :
    sort_list_big.append(random.randint(0,65535))
print ("unsorted list:", sort_list_big)

#b) time it 
start = timeit.default_timer()
bubble_sort(sort_list_big)
end = timeit.default_timer()
delta = end - start
print ("sorted list:", sort_list_big)
print ("time elapsed: ", delta)

#4 Repeat question 3 with a list 500 elements long. 
for i in range(x) :
    long_list.append(random.randint(0,65535))
print ("unsorted list:", long_list)

start = timeit.default_timer()
bubble_sort(long_list)
end = timeit.default_timer()
delta = end - start
print ("sorted list:", long_list)
print ("time elapsed: ", delta)