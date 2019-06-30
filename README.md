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

## Create a virtual environment for your crawling project:

conda create -n crawler python=3.7.2 anaconda

## Activate this environment, use

conda activate crawler

## Install all required packages:

pip install requests

pip install BeautifulSoup4

pip install pika

## Steps to install RMQ in MacOS and starting rabbitmq:

brew update

brew install rabbitmq

brew services start rabbitmq

## Start the crawling producer and workers:

python producer.py

python worker.py


## To deactivate an active environment, use
conda deactivate