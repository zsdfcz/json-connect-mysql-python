import json
import pymysql


FILE_PATH = 'C:\\Users\\User\\Desktop\\jsontest\\' #유동적으로 설정
FILE_NAME = 'example.json' 

def sql_connect():
    'mysql과 연결'
    con = pymysql.connect(host='localhost', user='root', password='root', port=8086,
        db='test', charset='utf8',
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor)
    cur = con.cursor()
    return cur

def sql_settables(func, data):
    '데이터 테이블 세팅 테이블이 없다면 생성'
    sql = "show tables"
    func.execute(sql)
    rows = func.fetchall()
    print(rows)
    if rows == ():
        print('테이블 없음 -> 테이블 생성')
        sql = 'CREATE TABLE {}(num INT NOT NULL AUTO_INCREMENT,path VARCHAR(100),format VARCHAR(20),sample_rate INT,bit_rate INT,PRIMARY KEY(num))CHARSET=utf8'.format(data['type'])
        try: 
            func.execute(sql)
        except:
            print('err')


def sql_insert(data, connect):
    sql = 'INSERT INTO {}(path, format, sample_rate, bit_rate) VALUES(%s,%s,%s,%s)'.format(data['type']) # path, format, simplerate, bitrate 
    tablepath = data['path']
    for v in data['list']:
        try: 
            connect.execute(sql, [tablepath + v['name'],v['format'],v['sampleRate'],v['bitRate']])
        except:
            print('err')

def json_read(filename):
    'json 파일 읽기'
    with open(FILE_PATH + filename, 'r') as f:
        json_data = json.load(f) #json 파일 읽기 json_data 는 딕셔너리
        return json_data


        
def main(filename):
    data = json_read(filename)
    s = sql_connect()
    sql_settables(s,data)
    sql_insert(data , s)
    
    
if __name__ =='__main__':
    main(FILE_NAME)