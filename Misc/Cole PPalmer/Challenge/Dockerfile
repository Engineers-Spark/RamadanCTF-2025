#in case the task requeries python to be installed:
#FROM python:3.9-slim-buster
#else if its just a system : 
FROM ubuntu:22.04

RUN apt-get install libc6
# Install some libs
RUN apt-get update && apt-get -y upgrade

Run apt-get install -y g++
# create ctf-user
RUN  groupadd -r ctf && useradd -r -g ctf ctf
#libs
COPY main.cpp /home/ctf/
COPY launch.sh /home/ctf/
COPY ynetd /home/ctf/
COPY flag.txt /home/ctf
#set some proper permissions
#RUN pip install inputimeout 
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/main.cpp
RUN chmod 750 /home/ctf/ynetd
RUN chmod 750 /home/ctf/launch.sh
RUN chmod 440 /home/ctf/flag.txt
WORKDIR /home/ctf/
RUN g++ -o main main.cpp
USER ctf
EXPOSE 4020

CMD /home/ctf/ynetd -p 4020 /home/ctf/launch.sh
