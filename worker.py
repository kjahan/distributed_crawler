import pika, time, helper
from bs4 import BeautifulSoup

DEBUG = False

def callback(ch, method, properties, url):
    if DEBUG:
        print("Received %r" % url)
    data = helper.scrape(url)
    soup = BeautifulSoup(data)
    try:
        area_code = soup.findAll("h1")[0].text.lower().replace(' numbers', '')
        h2_text = soup.findAll("h2")[0].text.lower()
        if 'area code' in h2_text:
            print(h2_text.replace(' area code', '') + ' area code: ' + area_code)
    except:
        pass
    ch.basic_ack(delivery_tag = method.delivery_tag)

def run():
    connection, channel = helper.setup('task_queue')
    print('Waiting for URL to scrape. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,queue='task_queue')
    channel.start_consuming()

run()
