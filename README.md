# json-connect-mysql-python

pymysql
docker run mysql

below is docker-compose

db:


    container_name: db
    
    image: mysql:8.0.20
    
    command: mysqld --default-authentication-plugin=mysql_native_password --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    
    restart: always
   
    volumes:
    
        - ./db/init:/docker-entrypoint-initdb.d
        
        - ./db/data:/var/lib/mysql
   
    environment:
   
        MYSQL_ROOT_PASSWORD: root
    
    networks:
    
        - in_net
   
    ports:
   
        - 8086:3306
      
      


빠른 시간 내에 코딩해보는것을 목표로 단시간 코딩하였다.

수정 할 점이 많다.


11/07 바뀐점

file name 입력 받기 -> 파일 읽기 -> DB연결 -> table check -> data INSERT


파일 읽기 ~~ 데이터입력  소요시간 측정



11/08 바뀐점


DB INSERT 시에 중복방지

err.json이 들어왔을 때 처리

