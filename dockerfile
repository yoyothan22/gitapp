FROM ubuntu
EXPOSE 80
WORKDIR /gitapp
RUN apt-get -y update
RUN apt install -y pip;pip install python-dotenv; apt install -y python3.10-venv;apt install -y git;python3 -m venv env
RUN git clone https://github.com/yoyothan22/gitapp /env
RUN cd /env;python3 gitapp.py
