from datetime import datetime
"""TODO: Terminar el encapsulamiento"""
class User:
    def __init__(self, username, email="", password="", create_time=datetime.now()):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__create_time = create_time

    def __str__(self):
        return "{0} {1} {2}".format(self.getUsername(), self.getEmail(), self.getCreateTime())

#    GETERS
    def getUsername(self):
        return self.__username
    
    def getPassword(self):
        return self.__password
    
    def getEmail(self):
        return self.__email
    
    def getCreateTime(self):
        return self.__create_time
# SETTERS
    # def setUsername(self, username):
    #     self.__username = username

    # def setEmail(self, email):
    #     self.__email = email

    # def setPassword(self, password):
    #     self.__password = password

    # def setCreateTime(self, createTime):
    #     self.__create_time = createTime
