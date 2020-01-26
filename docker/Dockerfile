FROM python:3
# RUN apt-get update && apt-get install python3 python3-pip apache2 -y
RUN pip install flask sqlalchemy mysql-client
RUN pip install pymysql
RUN pip install mysqlclient
RUN pip install passlib
RUN pip install pandas
RUN pip install flask-login
WORKDIR /mnt
ADD . /root/
