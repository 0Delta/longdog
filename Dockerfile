FROM python:3.7

RUN apt update && \
	apt install -y libsixel-bin && \
	pip install pillow libsixel-python && \
	apt clean all -y

COPY ./ /home
WORKDIR /home
ENTRYPOINT ["python","/home/longdog.py"]
