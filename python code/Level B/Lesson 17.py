
#! Making Classes

# class class_name: *indented code
        #* PascalCase: Uppercase on each word within variable name 
        #* camelCase: Uppercase on each word that isn't the first word in variable name
        #* snake_case: Lowercase with each word separated by underscore

class User:     ## Classes use PascalCase
        #* 'self' keyword referes to the object created by Class

    def __init__(self, user_id, username): ## Constructor: Initialize attributes; called each time class is called
        self.user_id = user_id
        self.username = username ## Attribute created here
        self.followers = 0
        self.following = 0

    def follow(self, user): ## Method must have self parameter to call back to this Class
        user.followers += 1
        self.following += 1
        

## To be in included in Class; requires indentation

user_1 = User("001", "Terry")
user_2 = User("002", "Jerry")
# user_2 = User() ## Error created with missing positional arguments

print(user_1) ## Confirm the existence of Object made from User() class

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
