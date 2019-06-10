# Installation
In case you want to install the application locally, please follow the instructions in this section.

### Download
```
git clone https://github.com/MartinCastroAlvarez/maria
```

### Run
You may or may not need to run this as sudo.
It depends on your local permissions.
```
cd maria
sudo docker-compose build
sudo docker-compose up
```

### Health Check
Validate that the app is up and running.
```
curl -X GET "http://0.0.0.0:5000/health"
```
