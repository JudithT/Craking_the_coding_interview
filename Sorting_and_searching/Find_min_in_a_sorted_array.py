# [15,16,19,20,25,1,3,4,5,7,10,14], key = 5 
#                   mid
# left = 0 
# right = len(arr) - 1
# mid = left + right//2 
# mid = left + (right-left)/2 

# compute the mid value
# if arr[mid] < arr[left], we know that the left side is not sorted and we need to explore the right side first and then the left side 

# if arr[right] < arr[mid], we know that the rightt side is not sorted and we need to explore the left side first and then the right side 

# if arr[left] == arr[mid], the left is sorted and I need to evaluate the key value in regard to arr[left], if arr[left]< key, then I need to search the right first and then the left 

# if arr[right] == arr[mid], right or left could be all repeats. 
# if arr[mid] != arr[right], we search the left side else we save the result of the search of teh right side in a variable called result. if result == -1
# we search the left side else we return the result. at the very end, aligning the if statements we return -1 


#if arr[right] > arr[mid]

# def search_in_rotated_array(arr, key):
#     if not arr: return 
#     return binarySearch(arr, 0, len(arr) - 1, key)
 
#  def splitInHalf()
# time complexity is 0(log n ) without duplicates or 0(n) with duplicates

def binarySearch(arr, left, right, key):
    mid = left + (right - left) // 2 
    if key == arr[mid]: 
        return mid
    if right < left:
        return -1 

    if arr[left] >  arr[mid]: # providing a hint that the right side is sorted 
        if arr[mid] < key and  key <= arr[right]: # sort the right side
            return binarySearch(arr, mid + 1, right, key )
        else: 
            return binarySearch(arr, left, mid - 1, key) # searching the left side

    elif arr[left] < arr[mid]: # left side is ordered
        if arr[mid] > key and arr[left] <= key:
            return binarySearch(arr, left, mid - 1, key)
        else:
            return binarySearch(arr, mid + 1, right, key )

    elif arr[left] == arr[mid]: # left and right are all repeats 
        if arr[mid] != arr[right]: # if right side is different, search it
            return binarySearch(arr,mid + 1, right, key) # searching the right side 
        else:
            result =  binarySearch(arr, left, mid - 1, key ) # searching the left side
            if result == -1:
                return binarySearch(arr, left, mid - 1, key) # searching the left side
            else:
                return result
    return -1
        
arr = [15,16,19,20,25,1,3,4,5,7,10,14]
print(binarySearch(arr, 0, len(arr)-1, 25))
# [15,16,19,20,25,1,3,4,5,7,10,14], key = 5 
    
# hint 298: 
# can you modify binary search for this purpose? 

# hint 310: 
# what is the runtime of your algorithm? What will happen if the array has duplicates

# Implement a binary search: 

# def binary_search(arr,l, r, key):
#     if not arr: return 
#     mid = l + (r - l )// 2
#     if arr[mid] == key:
#         return mid
#     elif arr[mid] < key:
#         return binary_search(arr, mid + 1, r, key)
#     elif arr[mid] > key: 
#         return binary_search(arr, l, mid - 1, key  )

# arr = [15,16,19,20,25,1,3,4,5,7,10,14]
# print(binary_search(arr, 0, len(arr)-1,20 ))




