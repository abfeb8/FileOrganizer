import sqlite3

conn = sqlite3.connect('database/DB.db')
c = conn.cursor()


class Tabel():
    def __init__(self, tableName):
        self.tableName = tableName

    def createTable(self):
        SQLstring = '''
                    CREATE TABLE {}(
                        file TEXT
                    )
                    '''.format(self.tableName)
        c.execute(SQLstring)

    def dropTable(self):
        SQLstring = '''
                    DROP TABLE {}
                    '''.format(self.tableName)
        c.execute(SQLstring)

    def insertFile(self, file):
        SQLstring = '''
                    INSERT INTO {} VALUES('{}')
                    '''.format(self.tableName, file)
        c.execute(SQLstring)

    def showTable(self):
        SQLstring = '''
                    SELECT * FROM {}
                    '''.format(self.tableName)
        c.execute(SQLstring)


Exclude = Tabel('Exclude')
Exclude.dropTable()

# listing tables
print(c.fetchall())

# closing db connection
conn.commit()
conn.close()
