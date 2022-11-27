FROM python:3.10

RUN apt update && apt install -y curl

COPY ./requirements.txt /home/
RUN pip3 install --no-cache-dir --upgrade -r /home/requirements.txt

COPY ./smart_home /home/smart_home

EXPOSE 8000

WORKDIR /home/smart_home

RUN chmod +x /home/smart_home/run.sh

ENTRYPOINT ["/home/smart_home/run.sh"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


