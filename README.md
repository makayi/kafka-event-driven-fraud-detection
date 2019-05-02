# Kafka-event-driven-fraud-detection

This is a sample project for working with the Kafka to create a fraud detection python that gets a stream of messages from Kafka and is able to detector fraudulent transactions.

## Prerequities 
1. Docker
2. Python
3. ArrangoDB

##  Getting started KAFKA 
 To run the application run the following command
 ```
 docker-compose -f "docker-compose.kafka.yml" up -d --build
 ```
This will build the Docker images for Zooker and Kafka and then start containers for these two services.  

## Getting Started with Kafka producer(generator and consumer (detector)
To  build docker images for the Kafka producers and consumers run the following command.

```
docker-compose -f "docker-compose.yml" up -d --build
```
