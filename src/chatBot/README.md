# EtherBot DataService

Using for serving data to EtherBot application.

## ⚙️ How to install service

***For dev***
Please make sure you install python environment control suchas pipenv, conda and etc

1. Install package
```
pip install -r requirements.txt
```

***For production***
```
docker build -t ehter-bot_data-service .
```

## 🚀 How to run service

***For dev***
1. After install package, run this script
```
uvicorn main:app --reload --host 0.0.0.0 --port 8080 --workers 4
```

***For production***
1. After build image
```
docker run --name dataservice_ethbot -p 8080:80 -e API_KEY=[API Key from Ehterscan] ehter-bot_data-service
```