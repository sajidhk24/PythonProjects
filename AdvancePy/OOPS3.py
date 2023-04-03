class User:
    def __init__(self, user_id, user_name):     # if we don't initialize we need to use eg:- user1.id= 1
        self.user_id = user_id
        self.user_name = user_name
        self.follower = 0  # to set follower to 0 for class and for all user object at once
        self.following = 0
        # print('the user we have created')

    def follow(self, user):
        user.follower += 1
        user.following += 1


user1 = User(1, 'sajid')
user2 = User(2, 'khan')
user3 = User(3, 'hussain')
# user1.id = "001"
# user1.username = 'sajid'
print(user1.user_name)
print(user1.user_id)
print(user2.user_id)
print(user2.user_name)

user1.follow(user2)
print(user2.follower)
print(user2.following)
##################################


