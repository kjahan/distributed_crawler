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
