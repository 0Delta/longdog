FROM python:3.7

RUN apt update && \
	apt install -y libsixel-bin && \
	pip install pillow && \
	apt clean all -y && \
	easy_install libsixel-python

COPY ./ /home
WORKDIR /home
ENTRYPOINT python longdog.py
