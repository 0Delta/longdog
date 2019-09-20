FROM python:3.7

RUN apt update
RUN apt install -y libsixel-bin
RUN pip install pillow
RUN apt clean all -y
RUN easy_install libsixel-python
COPY ./ /home
WORKDIR /home
ENTRYPOINT python longdog.py
