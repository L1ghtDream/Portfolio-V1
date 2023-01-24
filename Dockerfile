# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /root/Portfolio-V1

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "sh", "start.sh" ]
