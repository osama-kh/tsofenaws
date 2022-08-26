from operator import countOf

f = open("Alice.txt", "r")
alice_list = f.read().split()
alice_set =set(alice_list)

for i in alice_set:
    count = countOf(alice_list, i)
    print(i +" ",count)
