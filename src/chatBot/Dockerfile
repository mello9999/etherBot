FROM python:3.8
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN rm requirements.txt

ENV TZ=Asia/Bangkok

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]
