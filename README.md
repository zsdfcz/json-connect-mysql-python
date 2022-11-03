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
      
      
추가 해야할 사항
db 데이터 체크 (추가한 json파일인지에 따라 확인)
경로 및 파일이름 입력
클린코드로 바꿔보기
OOP의 장점을 살려 코딩해보기
json파일에 따라서 데이터 테이블 생성하기
  -json파일의 데이터에 다른 키값이 들어갈 때에 따라 맞춰 테이블 생성


빠른 시간 내에 코딩해보는것을 목표로 단시간 코딩하였다.
수정 할 점이 많다.
