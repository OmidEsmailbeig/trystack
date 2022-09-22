FROM python:slim

LABEL maintainer="Omid Esmailbeig <omid.delta96@gmail.com"

EXPOSE 8080

ENV TRYSTACK_API_ENV=production
ENV TRYSTACK_API_DEBUG=0
ENV TRYSTACK_API_DATABASE_URI=None

EXPOSE 8080/tcp

WORKDIR /opt/src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ./start.sh
