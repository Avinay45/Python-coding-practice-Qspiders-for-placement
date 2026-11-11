

# index
# index is a method in python which is used to find the index of a substring in a string. It returns the index of the first occurrence of the substring. If the substring is not found, it raises a ValueError.
# s = "kevin is a good boy"
# print(s.index("good"))
# s = "mike is good at python"
# print(s.index("good", 10, 20)) # it will raise a ValueError because "good" is not found in the specified range
# s = "naveen is good at english communication"
# print(s.index("good", 10, 20)) # it will raise a ValueError because "good" is not found in the specified range
# print(s.index())
# print(s.index("Communication")) # it will raise a ValueError because "Communication" is not found in the string
# s2 = "sky is the limit"
# print(s2.index("the")) # it will raise a ValueError because "the" is not found in the specified range    
# s3 = "don't chase success, chase excellence"
# print((s3.index("success"))) # it will return the index of the first occurrence of "success" in the string
'''-------------------------------------------------------------------------------------------------------------------------------'''
#rindex
# rindex is a method in python which is used to find the index of a substring in a string. It returns the index of the last occurrence of the substring. If the substring is not found, it raises a ValueError.
# s = "kevin is a good boy"
# print(s.rindex("good"))
# s = "mike is good at python"
# print(s.rindex("good", 10, 20)) # it will raise a ValueError because "good" is not found in the specified range
# s = "naveen is good at english communication"
# print(s.rindex("good", 10, 20)) # it will raise a ValueError because "good" is not found in the specified range
# s2 = "sky is the limit"
# print(s2.rindex("the")) # it will raise a ValueError because "the" is not found in the specified range  
# s3 = "don't chase success, chase excellence"
# print((s3.rindex("success"))) # it will return the index of the last occurrence of "success" in the string  
'''--------------------------------------------------------------------------------------------------'''
#find
# find is a method in python which is used to find the index of a substring in a string. It returns the index of the first occurrence of the substring. If the substring is not found, it returns -1.
# s = "kevin is a good boy"
# print(s.find("goood"))
# s = "mike is good at python"
# print(s.find("good", 10, 20)) # it will return -1 because "good" is not found in the specified range   
# s = "naveen is good at english communication"
# print(s.find("good", 10, 20)) # it will return -1 because "good" is not found in the specified range
# s2 = "sky is the limit"
# print(s2.find("the")) # it returns the index of the first occurrence of "the" in the string
# s3 = "don't chase success, chase excellence"
# print((s3.find("success"))) # it will return the index of the first occurrence of "success" in the string   
'''--------------------------------------------------------------------------------------------------'''
#rfind
# rfind is a method in python which is used to find the index of a substring in a string. It returns the index of the last occurrence of the substring. If the substring is not found, it returns -1.
# s = "kevin is a good boy"
# print(s.rfind("good"))
# s = "mike is good at python"
# print(s.rfind("good", 10, 20)) # it will return -1 because "good" is not found in the specified range
# s = "naveen is good at english communication"
# print(s.rfind("good", 10, 20)) # it will return -1 because "good" is not found in the specified range
# s2 = "sky is the limit" 
# print(s2.rfind("the")) # it returns the index of the last occurrence of "the" in the string
# s3 = "don't chase success, chase excellence"
# print((s3.rfind("success"))) # it will return the index of the last occurrence of "success" in the string 
'''--------------------------------------------------------------------------------------------------'''
#count
# count is a method in python which is used to count the number of occurrences of a substring in a string. It returns the number of occurrences of the substring. If the substring is not found, it returns 0.
# s = "kevin is a good boy" 
# print(s.count("good"))
# s = "mike is good at python"
# print(s.count("good", 10, 20)) # it will return 0 because "good" is not found in the specified range
# s = "naveen is good at english communication"
# print(s.count("good", 10, 20)) # it will return 0 because "good" is not found in the specified range
# s2 = "sky is the limit"  
'''--------------------------------------------------------------------------------------------------'''
#replace
# replace is a method in python which is used to replace a substring in a string with another substring. It returns a new string with the specified substring replaced. If the substring is not found, it returns the original string.
# s = "kevin is a good boy"
# print(s.replace("good", "bad"))
# s = "mike is good at python"
# print(s.replace("good", "bad", 1)) # it will replace the first occurrence of "good" with "bad"
# s = "naveen is good at english communication"
# print(s.replace("good", "bad", 2)) # it will replace the first two occurrences of "good" with "bad"
# s2 = "sky is the limit"
# print(s2.replace("the", "a")) # it will replace the first occurrence of "the" with "a"
# s3 = "don't chase success, chase excellence"
# print((s3.replace("success", "failure"))) # it will replace the first occurrence of "success" with "failure"
'''--------------------------------------------------------------------------------------------------'''
#title
# title is a method in python which is used to convert the first character of each word in a string to uppercase and the rest of the characters to lowercase. It returns a new string with the specified changes.
# s = "kevin is a good boy"
# print(s.title())
# s = "mike is good at python"
# print(s.title())
# s = "naveen is good at english communication"
# print(s.title())
# s2 = "sky is the limit"
# print(s2.title())
# s3 = "don't chase success, chase excellence"
# print((s3.title()))


'''-----------------------------------------------------------------------------------------------------'''
#capitalize()
s = "kevin is a good boy"
print(s.capitalize())

#upper()
s = "don't underestimate the power of a common man"
print(s.upper())

#lower()
s = "DON'T UNDERESTIMATE THE POWER OF A COMMON MAN"
print(s.lower())

#split()
s = "don't chase the butterflies, create the garden to attract them"
print(s.split())

#join()
s = ["don't", 'chase', 'the', 'butterflies,', 'create', 'the', 'garden', 'to', 'attract', 'them']
print(" ".join(s))

#strip()
s = "### sky is the limit###"
print(s.rstrip("#"))
print(s.lstrip("#"))
