# 1. Every Three Numbers:
# Create a function called every_three_nums that has one parameter named start.

# The function should return a list of every third number between start and 100 (inclusive). 
# For example, every_three_nums(91) should return the list [91, 94, 97, 100]. 
# If start is greater than 100, the function should return an empty list.

#Write your function here
def every_three_nums(start):
  lst = []
  if start > 100:
    return lst
  else:
    for i in range(start, 100 + 1):
      lst.append(i)    
    #print(lst)
    new_lst = lst[::3]
    #print(new_lst)
    return new_lst

#Uncomment the line below when your function is done
print(every_three_nums(91))


# 2. Remove Middle
# Create a function named remove_middle which has three parameters named lst, start, and end.

# The function should return a list where all elements in lst with an index 
# between start and end (inclusive) have been removed.

# For example, the following code should return [4, 23, 42] 
# because elements at indices 1, 2, and 3 have been removed:

#Write your function here
def remove_middle(lst, start, end):
  #Write your function here

def remove_middle(lst,start,end):
  # There are 2 good methods:
  # method 1:
  # del lst[start:(end+1)]
  # return lst

  # method 2:
  # new_lst = lst[:(start)] + lst[(end+1):]
  # return new_lst
  
  #This is my approach but is has a bug:
  sub_lst = []
  new_lst = []
  for i in range(start, end + 1):
    sub_lst.append(lst[i])
  #print(sub_lst)
  #if casting list to set, indexing will be messed up
  new_lst = list(set(lst) - set(sub_lst))
  return new_lst

#Uncomment the line below when your function is done
remove_middle([4, 8, 15, 16, 23, 42], 1, 3)
#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))




# 3. More Frequent Item
# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

# Return either item1 or item2 depending on which item appears more often in lst.

# If the two items appear the same number of times, return item1.

#Write your function here
def more_frequent_item(lst, item1, item2):
  count_item1 = lst.count(item1)
  print("item 1 appears " + str(count_item1) + " times")

  count_item2 = lst.count(item2)
  print("item 2 appears " + str(count_item2) + " times")
  
  if count_item2 > count_item1:
    return item2
  else:
    return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))



# 4. Double Index
# Create a function named double_index that has two parameters: a list named lst and a single number named index.

# The function should return a new list where all elements are the same as in lst except for the element at index. 
# The element at index should be double the value of the element at index of the original lst.

# If index is not a valid index, the function should return the original list.

# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

# double_index([1, 2, 3, 4], 2)
# After writing your function, un-comment the call to the function that we’ve provided for you to test your results.

#Write your function here
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    double = lst[index] * 2
    # print(double)
    lst.remove(lst[index])
    #print(lst)
    lst.insert(index, double)
    # print(lst)
  return lst
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))




# 5. Middle Item
# Create a function called middle_element that has one parameter named lst.

# If there are an odd number of elements in lst, the function should return the middle element. 
# If there are an even number of elements, 
# the function should return the average of the middle two elements.

#Write your function here
def middle_element(lst):
   
  if len(lst) % 2 != 0:
    middle_ele = lst[len(lst)//2]
    return middle_ele
  else:
    avg_two_middle = (lst[len(lst)//2]  + lst[len(lst)//2 - 1]) / 2
    return avg_two_middle
    

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 10]))