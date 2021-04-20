# SEARCHING TECHNIQUES:
# 1)LINEAR/SEQUENTIAL SEARCH
# 2)BINARY SEARCH

# def SequentialSearch(arr, ele):
#     pos = 0
#     found = False
#     while pos < len(arr) and not found:
#         if arr[pos] == ele:
#             found = True
#         else:
#             pos = pos + 1
#
#     return found
# arr = [1,9,2,8,3,4,7,5,6]
# print(SequentialSearch(arr,1))


# def OrderedSeqSearch(arr, ele):
#     pos = 0
#     found = False
#     stopped = False
#     while pos < len(arr) and not found and not stopped:
#         if arr[pos] == ele:
#             found = True
#         else:
#             if arr[pos] > ele:
#                 stopped = True
#             else:
#                 pos = pos + 1
#     return found
# arr=[1,9,2,8,3,4,7,5,6]
# arr.sort()
# print(OrderedSeqSearch(arr, 3))


# def BinarySearch(arr, n):
#     arr.sort()
#     first = 0
#     last = len(arr) - 1
#     found = False
#     while first <= last and not found:
#         mid = (first + last) // 2
#         if n == arr[mid]:
#             found = True
#         else:
#             if n < mid:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     if found:
#         return "Element is present in array"
#     else:
#         return "No element is found"
#
#
# arr = [1, 9, 2, 8, 3, 4, 7, 5, 6]
# print(BinarySearch(arr, 8))

# ----------------------------------------------------------------------------------

# SORTING TECHNIQUES:
# 1)BUBBLE SORT
# 2)SELECTION SORT
# 3)INSERTION SORT
# 4)SHELL SORT
# 5)MERGE SORT
# 6)QUICK SORT

# def BubbleSort(arr):
#     for i in range(len(arr) - 1, 0, -1):
#         for j in range(i):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]
#                 arr[j + 1] = temp
#     return arr
#
#
# if __name__ == '__main__':
#     arr = [9, 3, 1, 7, 8, 2, 6, 4, 5]
#     sortedarr = BubbleSort(arr)
#     print("BubbleSort",sortedarr)

# def SelectionSort(arr):
#     for i in range(len(arr) - 1, 0, -1):
#         maxpos = 0
#         for j in range(i):
#             if arr[j] > arr[maxpos]:
#                 maxpos = j
#         temp = arr[i]
#         arr[i] = arr[maxpos]
#         arr[maxpos] = temp
#
#     return arr
#
#
# if __name__ == '__main__':
#     arr = [9, 3, 1, 7, 8, 2, 6, 4, 5]
#     sortedarr = SelectionSort(arr)
#     print("SelectionSort:", sortedarr)

# def InsertionSort(arr):
#     for i in range(1,len(arr)):
#         c=arr[i]
#         position=i
#         while position>0 and arr[position-1]>c:
#             arr[position]=arr[position-1]
#             position-=1
#         arr[position]=c
#     return arr
#
#
# if __name__ == "__main__":
#     arr = [9, 3, 1, 7, 8, 2, 6, 4, 5]
#     sortedarr=InsertionSort(arr)
#     print("InsertionSort:", sortedarr)

# def ShellSort(arr):
#     gap=len(arr)//2
#     while gap>0:
#         for i in range(gap, len(arr)):
#             c=arr[i]
#             position=i
#             while position>=gap and arr[position-gap]>c:
#                 arr[position]=arr[position-gap]
#                 position-=gap
#             arr[position]=c
#         gap=gap//2
#     return arr
#
#
# if __name__ == "__main__":
#     arr= [9, 3, 1, 7, 8, 2, 6, 4, 5]
#     sortedarr=ShellSort(arr)
#     print("ShellSort:", sortedarr)
#
# def MergeSort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         leftarr=arr[:mid]
#         rightarr=arr[mid:]
#         MergeSort(leftarr)
#         MergeSort(rightarr)
#         i=0
#         j=0
#         k=0
#         while i<len(leftarr) and j<len(rightarr):
#             if leftarr[i]<rightarr[j]:
#                 arr[k]=leftarr[i]
#                 i+=1
#             else:
#                 arr[k]=rightarr[j]
#                 j+=1
#             k+=1
#         while i < len(leftarr):
#             arr[k] = leftarr[i]
#             i+= 1
#             k+=1
#         while j<len(rightarr):
#             arr[k]=rightarr[j]
#             j+=1
#             k+=1
#     return arr
#
#
# if __name__ == "__main__":
#     arr = [9, 3, 1, 7, 8, 2, 6, 4, 5]
#     sortedarr=MergeSort(arr)
#     print("MergeSort:",sortedarr)
#
# def QuickSort(arr):
#     _QuickSort(arr, 0, len(arr) - 1)
#     return arr
#
#
# def _QuickSort(arr, first, last):
#     if first < last:
#         splitpoint = partition(arr, first, last)
#
#         _QuickSort(arr, first, splitpoint - 1)
#         _QuickSort(arr, splitpoint + 1, last)
#
#
# def partition(arr, first, last):
#     pivotvalue = arr[first]
#
#     leftmark = first + 1
#     rightmark = last
#
#     done = False
#     while not done:
#
#         while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1
#
#         while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
#             rightmark = rightmark - 1
#
#         if rightmark < leftmark:
#             done = True
#         else:
#             temp = arr[leftmark]
#             arr[leftmark] = arr[rightmark]
#             arr[rightmark] = temp
#
#     temp = arr[first]
#     arr[first] = arr[rightmark]
#     arr[rightmark] = temp
#
#     return rightmark
#
#
# arr = [9, 3, 1, 7, 8, 2, 6, 4, 5]
# print(QuickSort(arr))
