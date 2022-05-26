class User:
    def __init__(self, id, name,):
        self.id = id
        self.name = name
        self.followers=0
        self.following=0
    def follow(self, user):
        user.followers+=1
        self.following+=1


user = User(1, "Baba")
user_2= User(2,"toto")
print(user.name)
print(user.id)
user.follow(user_2)
print(user.following)
print(user_2.followers)

