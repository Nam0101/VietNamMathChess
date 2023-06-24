FROM python:3.11


WORKDIR /app

ADD main.py .
ADD requirements.txt .
COPY ./ai .
COPY ./game .
COPY ./img .
COPY ./state .
COPY ./ui .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]