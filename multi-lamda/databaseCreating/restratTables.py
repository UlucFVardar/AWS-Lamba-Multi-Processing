from DataBase import DataBase as DB 

db = DB('innodb')
db.dropTables()
print('[INFO]: Tables have been dropped!')
db.createTables()
print('[INFO]: Tables have been created!')
print('[INFO]: DONE!')
