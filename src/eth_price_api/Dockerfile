FROM python:3.8

ENV TZ=Asia/Bangkok

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN chmod +x /start.sh

RUN rm requirements.txt

CMD ["./start.sh"]
