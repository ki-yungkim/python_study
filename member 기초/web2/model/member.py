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
        self.conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/XE", encoding='utf-8')
        return self.conn.cursor()


    def insert(self, m):
        cursor = self.connect()
        sql = 'insert into member2 values(:1, :2, :3, :4)'
        d = (m.getId(), m.getPw(), m.getName(), m.getEmail())
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def selectById(self, id):
        cursor = self.connect()
        sql = 'select * from member2 where id=:1'
        d = (id, )
        cursor.execute(sql, d)
        row = cursor.fetchone()
        self.conn.close()
        if row is not None:
            return Member(row[0], row[1], row[2], row[3])

    def selectAll(self):
        res = []
        cursor = self.connect()
        sql = 'select * from member2'
        cursor.execute(sql)
        for row in cursor:
            res.append(Member(row[0], row[1], row[2], row[3]))
        self.conn.close()
        return res

    def update(self, m):
        cursor = self.connect()
        sql = 'update member2 set pwd=:1 where id=:2'
        d = (m.getPw(), m.getId())
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

    def delete(self, id):
        cursor = self.connect()
        sql = 'delete from member2 where id=:1'
        d = (id,)
        cursor.execute(sql, d)
        self.conn.commit()
        self.conn.close()

class Service:
    def __init__(self):
        self.__dao = Dao()

    def addMember(self, m):
        self.__dao.insert(m)

    def getMemberById(self, id):
        return self.__dao.selectById(id)

    def editMember(self, m):
        self.__dao.update(m)

    def delMember(self, id):
        self.__dao.delete(id)

    def printAll(self):
        return self.__dao.selectAll()

