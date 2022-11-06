FROM python:3.8-alpine
LABEL maintainer='Wojciech Repiński "wrepinski@gmail.com"'
LABEL name="evio_stb-auto_login_helper"
LABEL version="1.1"
LABEL description="Automatic login helper of Evio IPTV decoders like Z123"
ADD evio_stb-auto_login_helper.tar.xz /
RUN pip install --upgrade pip
RUN apk add --no-cache gcc g++ make libffi-dev openssl-dev
RUN pip install -r requirements.txt
EXPOSE 5000
WORKDIR /app
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]
