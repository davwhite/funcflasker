FROM registry.access.redhat.com/ubi8.python-38
ARG UID=1000

# RUN yum -y update
#RUN yum -y install python38 python38-pip
#RUN yum -y install python38-pip
RUN pip3 install flask
RUN pip3 install requests bs4
COPY flaskr flaskr
RUN get_the_funcs.py
ENV FLASK_APP=flaskr/main.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
EXPOSE 5000
# ENV LC_ALL=en_US.utf-8
# ENV LANG=en_US.utf-8
ENTRYPOINT ["flask","run","--host","0.0.0.0"]
