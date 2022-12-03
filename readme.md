# Homework-5

Small Web Service that generate SHA256 key for message and keep these messages on hashmap with these folowing endpoints

1. /messages takes a message (a string) as a POST and returns the SHA256 hash digest of that message (in hexadecimal
   format)

2. /messages/<hash> is a GET request that returns the original message. A request to a non-existent
   <hash> should return a 404 error.

### Public accesible url

https://hello-world-2-nedixiihoq-uc.a.run.app

### How to run

To build the Docker image, run this following command: 

docker build -t my-flask-app.

Once the Docker image is built, you can run it with the following command:
docker run -p 5000:5000 my-flask-app

