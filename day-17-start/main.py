class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user being created...")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Isaac")
print(user_1.id, user_1.username, user_1.followers)
user_2 = User("002", "Jasmine")
print(user_2.id, user_2.username, user_2.followers)

user_1.follow(user_2)
print(user_1.id, user_1.username, user_1.followers, user_1.following)
print(user_2.id, user_2.username, user_2.followers, user_1.followers)
