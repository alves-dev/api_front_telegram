FROM python:3

LABEL version="1" description="api_front_telegram"

WORKDIR /project

COPY . /project/

ENV TZ 'America/Sao_Paulo'
RUN echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

RUN apt update && apt install -y vim
RUN pip install -r requirements.txt

ENV ENV_FOR_DYNACONF=production
ENV TOKEN=iuahgiuadga564986a5trhj498516sh
ENV TOKEN_TELEGRAM='1021164880:AAGa84NATX5jhsW7BDbWCeqcA0EG7FMZj7Y'
ENV MY_CHAT_ID='846928818'

EXPOSE 7111

CMD [ "gunicorn", "-b 0.0.0.0:7111", "app:app" ]