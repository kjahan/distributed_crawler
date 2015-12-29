Distributed Crawling with RMQ
=============================

## Description

This is a showcase for distributing scraping websites using multiple workers. The basic idea is to use RabbitMQ worker queue to schedule many pages to be scraped and handle scraping/parsing by running multiple workers simultaneously.

## Input

The input for this project is the UK Area Codes website: 

	http://www.area-codes.org.uk/full-uk-area-code-list.php

## Output

The worker crawlers scrape the passed url by the producer and parse the city/town along with their area codes.

## Dependencies

To run the code you need to setup RabbitMQ and install pika, requests and BeautifulSoup Python libraries.
