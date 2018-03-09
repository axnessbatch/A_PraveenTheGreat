s="Hi {name} wow! Is a \tsaddist your age : {age} Fluß$ wow suma wow!!!"
k="064"
h="PraveeN Kumar"
m={'name':"suma",'age':22}
#print(s.capitalize())#Initial letter will become capital
#print(s.casefold())#returns the lowercase of any string including any special characters
#print(s.center(50,'#'))#string will be centered with char '#'
#print(s.count('e',1,10))#serches and returns the occurence of 'e' here, it searches from 1st index to 10th index
#print(s.encode('utf-32','strict'))#By default encodes with utf-8
#print(s.endswith(k,-10,-2))# returns true if the given string is ends with given value
#print(s.expandtabs())#checks from the begining and moves the cursor for muliple of 8 times until it encounters tab
#print(s.find(k))#returns the starting index of the given substring
#print(s.format(name=input("Enter name"),age=input("Enter ur age")))#takes named arguments and keyword arguments and returns in string
#print(s.format_map(m))#According to map it returns the updated string
#print(s.index('wow',1,20))# returs the starting index of substring
#print(k.isalnum())#returns true if string contains either alphabets or numbers but not symbols
#print(k.isalpha())#returns true if string contains only alphabets
#print(k.isdecimal())#returns true if the string contains only numbers
#print(k.isdigit())
#print(s.isidentifier())#returns true if the string is valid identifier,false otherwise
#print(k.isnumeric())#returns true if the string contains number
#print(s.islower())#returns true if the string is in lower case, false otherwise
#print(k.isprintable())#returns true if string is one of the letters and symbols, digits, punctuation,whitespace
#print(h.isspace())#returns true if the string is whitespace
#print(h.islower())#returns true if the string contains lower case letters
print(h.istitle())#Returns true if the string is title-cased
print(s.isupper())#returns true if the string is upper-cased
print("@".join("Praveen","Kumar"))#P@r@a@v@e@e@n returns joins two strings




