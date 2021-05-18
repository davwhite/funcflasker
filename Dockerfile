FROM centos:7
ARG UID=1000

# RUN yum -y update
RUN yum -y install python3 python3-pip
RUN pip3 install flask
COPY flaskr flaskr
ENV FLASK_APP=flaskr/main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8
ENTRYPOINT ["flask","run"]