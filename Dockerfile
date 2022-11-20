FROM python:3

WORKDIR /home/mpeter/Docker_Tutorial

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "./src/run.py"]