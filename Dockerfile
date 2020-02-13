FROM python:3
RUN pip install pip --upgrade
RUN pip install flask sqlalchemy mysql-client pymysql mysqlclient passlib pandas flask-login gunicorn pandasql
WORKDIR /root
ADD ./src /root/
CMD ["gunicorn", "hackbox:app", "-b", "0.0.0.0:5000"]
