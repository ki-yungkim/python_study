import cx_Oracle

class Member:
    def __init__(self, id=None, pw=None, name=None,email=None):
        self.__id = id
        self.__pw = pw
        self.__name = name
        self.__email = email

    def __str__(self):
        return 'id : ' + self.__id + ' / pw : ' + self.__pw + ' / name : ' + self.__name + ' / email : ' + self.__email

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setPw(self, pw):
        self.__wp = pw

    def getPw(self):
        return self.__pw

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

class Dao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encodings='utf-8')
        return self.conn.cursor()


    def insert(self):
