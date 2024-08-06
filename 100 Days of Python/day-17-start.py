# class User:
#     def __init__(self) -> None:
#         print("adding new username...")

# user1 = User()
# user1.id = "001"
# user1.username = "NicholasKinberg"
# # object.attribute format

# print(user1.id)
# print(user1.username)

class UserTwo:
    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username
        # if you add other parameters and set them to values, whether strings, lists, integers, or others, 
            # setting anything to a value is setting a default that will print 
            # when you fail to provide a value for the parameter in calling the class

userNew = UserTwo("002", "nkinberg")
print(userNew.id, userNew.username)
# the two above statements equal each other, they do the exact same thing