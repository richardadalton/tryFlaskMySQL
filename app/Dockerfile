FROM python:3.8

WORKDIR /
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host", "0.0.0.0" ]