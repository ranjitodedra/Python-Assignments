#ID : 20ce062
#Name : Odedra Ranjit Jakharabhai 

"""
AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
"""

#Github link : 

ab = int(input())

dict = {}
for i in range(ab):
    str = input()
    if str in dict:
        dict[str] +=1
    else:
        dict[str] = 1
print(len(dict))
for i in dict.values():
    print(i ,end=' ')