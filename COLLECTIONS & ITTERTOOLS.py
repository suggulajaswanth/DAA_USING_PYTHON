#COLLECTIONS AND ITERTOOLS

# from itertools import combinations,permutations
# l=[1,3,2,2]
# m=list(combinations(l,2))
# print(m)
# for i in m:
#     if sum(i)==4:
#         print(i)

#
# def pair_sum(arr,k):
#     m=list(combinations(arr,2))
#     for i in m:
#         if sum(i)==k:
#             print(i)
#
# pair_sum([1,3,2,2],4)
# def large_cont_sum(a):
#     l=[]
#     l.append(sum(a))
#     for i in range(1,len(a)):
#         l.append(sum(a[:i]))
#     return max(l)
#
# print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
#
# s='Hello;John;how;are:you'
# m=s.split(";")
# print(m)
# print(" ".join(reversed(m)))
#
# s='ABBBBCCC'
# string=''
# count=0
# temp=s[0]
# for i in s:
#     if i==temp:
#         count+=1
#     else:
#         string=string+(temp+str(count))
#         temp=i
#         count=1
# string = string + (temp + str(count))
# print(string)
# print(set(s))
#
# def r(l):
#     ll=l[::-1]
#     return l1
# def a(l):
#     l1=[]
#     l1.extend(r(l))
#     return l1
# l=[1,3.1,5.31,7.531]
# r=a(l)
# print(r)
# import sys
#
# l1=tuple()
# print(sys.getsizeof(l1),end=" ")
# l2=(1,2)
# print(sys.getsizeof(l2),end=" ")
# l3=(1,2,(3,4))
# print(sys.getsizeof(l3),end=" ")

# n=4321
# print(n%10 ,n/10 ,n//10)
#
# def word_split(phrase, list_of_words, output=None):
#     if output is None:
#         output = []
#     for word in list_of_words:
#         if phrase.startswith(word):
#             output.append(word)
#             return word_split(phrase[len(word):], list_of_words, output)
#     print(output)
# word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])

# from collections import defaultdict
# def changearray(inarr):
#     outarr=[]
#     for i in range(len(inarr)):
#         s=inarr[i]
#         temparr=inarr[i+1:]
#         temparr.sort()
#         d=defaultdict()
#         for j in temparr:
#             if j>s:
#                 if j not in d:
#                     d[j]=1
#                 else:
#                     d[j]+=1
#         if d:
#             outarr.append(max(d,key=d.get))
#         else:
#             outarr.append(-1)
#     return outarr
#
#
# if __name__ == '__main__':
#     inarr=list(map(int,input().split(',')))
#     result=changearray(inarr)
#     print(result)