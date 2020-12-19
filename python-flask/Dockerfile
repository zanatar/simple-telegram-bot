FROM ubuntu:latest
RUN apt-get -yqq update
RUN apt-get -yqq install python-pip
RUN apt-get -yqq install git
RUN pip install flask requests
#CMD ["wget", "https://github.com/zanatar/andersen_courses/blob/dev/task_4/bot.py"]
ADD ./bot.py /etc/
#RUN git clone https://github.com/zanatar/andersen_courses/
EXPOSE 6400
CMD [ "python", "/etc/bot.py" ]
