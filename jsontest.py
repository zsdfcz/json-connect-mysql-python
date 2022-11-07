import json
import sys
import pymysql
import time


# json parsing and Mysql Connect
#mysql version 8.0.^

##############
FILE_PATH = '/Users/mac/py/python_basic/jsondir/' #유동적으로 설정
FILE_NAME = ' ' 
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root1234'
PORT = 3306
DB = 'test'
###############

def sql_connect():
    'mysql DB 연결'
    try:
        con = pymysql.connect(host=HOST, user=USER, password=PASSWORD, port=PORT,
            db=DB, charset='utf8',
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        print('DB 연결 성공')
        return cur
    except Exception as err:
        print('mysql 연결 실패')
        print(err)
        return 'err'


def sql_settables(func, data):
    '데이터 테이블 세팅 테이블이 없다면 생성'
    sql = "show tables like '{}'".format(data['type'])
    #type value -> table이 있는지 확인
    func.execute(sql)
    rows = func.fetchall()
    if rows==() :
        print('테이블 없음 -> 테이블 생성')
        if (data['type'] == 'audio'):
            sql = 'CREATE TABLE {}(num INT NOT NULL AUTO_INCREMENT,path VARCHAR(100),format VARCHAR(20),sample_rate INT,bit_rate INT,PRIMARY KEY(num))CHARSET=utf8'.format(data['type'])
        elif(data['type'] == 'message'):
            sql = 'CREATE TABLE {}(num INT NOT NULL AUTO_INCREMENT,message VARCHAR(100),timestamp INT,PRIMARY KEY(num))CHARSET=utf8'.format(data['type'])
        try: 
            func.execute(sql)
            return data['type']
        except:
            print('err')
    else :
        print('{} 테이블이 존재합니다. '.format(data['type']))


def sql_insert(data, connect , type):
    print('DB에 데이터 Insert')
    if(type =='audio'):
        sql = 'INSERT INTO {}(path, format, sample_rate, bit_rate) VALUES(%s,%s,%s,%s)'.format(data['type']) # path, format, simplerate, bitrate 
        tablepath = data['path']
        for v in data['list']:
            try: 
                connect.execute(sql, [tablepath + v['name'],v['format'],v['sampleRate'],v['bitRate']])
            except:
                print('err')
    elif(type == 'message'):
        sql = 'INSERT INTO {}(message, timestamp) VALUES(%s,%s)'.format(data['type']) # path, format, simplerate, bitrate 
        for v in data['list']:
            try: 
                connect.execute(sql, [v['text'],data['timestamp'] + v['timeOffset']])
            except:
                print('err')


def json_read(filename):
    'json 파일 읽기'
    print('json 파일을 읽습니다.')
    try:
        with open(FILE_PATH + filename, 'r') as f:
            json_data = json.load(f) #json 파일 읽기
            return json_data
    except Exception as err:
        print(err)
        print('파일을 찾을수 없습니다.')
        return 'err'


        
def main(filename):
    data = json_read(filename)
    if (data != 'err'):
        s = sql_connect()
        if(s != 'err'):
            type = sql_settables(s,data)
            sql_insert(data , s, type)
    
class timer:
    start_time = 0

    def  __enter__(self):
        self.start_time = time.time()
        print('시간측정 시작')
   
    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print('시간 측정 완료 : ' ,end='')
        print(end_time - self.start_time , 's 소요 되었습니다')



if __name__ =='__main__':
    'main -> 파일 읽기 -> sql연결 -> 테이블 조회-> 데이터 삽입'
    timers = timer
    while True:
        sys.stdout.flush()
        print('JSON 파일 이름 입력 : ',end='')
        FILE_NAME = sys.stdin.readline().strip()
        with timers():
            main(FILE_NAME)

   