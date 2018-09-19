import pymysql

class DataBase:
    def __init__(self, db):
        self.choosen_DB = db
        self.connection = pymysql.connect(
                host = 'tmcrawler.cb5e4o6zarmq.eu-central-1.rds.amazonaws.com'
                , user = 'tmroot'
                , passwd = 'transfermarktPassw0rd'
                , db = self.choosen_DB,
                charset='utf8')

    def insert(self, ip,layer,number):

        with self.connection.cursor() as cur:
            cur.execute("""insert into innodb.testttt (ip,time,layer,number) values('%s',NOW(),%s,%s)""" % (ip,layer,number))
            print('[INFO]: LEAGUE INSERT OKAY')
            self.connection.commit()
            print('[INFO]: COMMIT')
            cur.close()