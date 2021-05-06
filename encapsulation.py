class User:

    def __init__(self, userName=None):
        # private attribute. When an object is instantiated it will have this userName attribute set to the default value of None
        self.__userName = userName

    def setUserName(self, userName):
        self.__userName = userName

    def getUserName(self):
        return self.__userName

user1 = User()

print(user1.getUserName())          # terminal output: None
user1.setUserName('johni123')
print(user1.getUserName())          # terminal output: johni123


