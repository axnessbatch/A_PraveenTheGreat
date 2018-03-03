s="Hi {name} wow! Is a \tsaddist your age : {age} Fluß$ wow suma wow!!!"
k="wow!"
m={'name':"suma",'age':22}
print(s.capitalize())#Initial letter will become capital
print(s.casefold())#returns the lowercase of any string including any special characters
print(s.center(50,'#'))#string will be centered with char '#'
print(s.count('e',1,10))#serches and returns the occurence of 'e' here, it searches from 1st index to 10th index
print(s.encode('utf-32','strict'))#By default encodes with utf-8
print(s.endswith(k,-10,-2))# returns true if the given string is ends with given value
print(s.expandtabs())#checks from the begining and moves the cursor for muliple of 8 times until it encounters tab
print(s.find(k))#returns the starting index of the given substring
print(s.format(name=input("Enter name"),age=input("Enter ur age")))#takes named arguments and keyword arguments and returns in string
print(s.format_map(m))#According to map it returns the updated string
