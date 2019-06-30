Distributed Crawling with RMQ
=============================

## Description

This is a showcase for a distributed website crawler using one producer and multiple workers. The basic idea is to use RMQ's worker queue to schedule tasks for scraping/parsing many pages by running multiple workers simultaneously.

## Input

The input for this project is the UK Area Codes website: 

	http://www.area-codes.org.uk/full-uk-area-code-list.php

## Output

The worker crawlers scrape the passed url's passed by the producer and parse the city/town name along with their area codes. The workers run in parallel.

## Dependencies

To run the code you need to setup RabbitMQ and also install pika, requests and BeautifulSoup Python libraries.

Create a virtual environment for your crawling project:

conda create -n crawler python=3.7.2 anaconda

# Activate this environment, use

conda activate crawler

pip install requests

pip install BeautifulSoup4

Pika is a pure-Python implementation of the AMQP 0-9-1 protocol:

pip install pika


#Steps to install RMQ in MacOS: https://www.rabbitmq.com/install-homebrew.html

brew update

brew install rabbitmq

# To have launchd start rabbitmq now and restart at login:
brew services start rabbitmq

#Start producer:

python producer.py

#Start workers:

python worker.py


# To deactivate an active environment, use
conda deactivate

