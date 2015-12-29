import pika, sys, helper
from bs4 import BeautifulSoup

base_url = 'http://www.area-codes.org.uk/'
area_codes_url = base_url + 'full-uk-area-code-list.php'

def dispatch(channel, message):
    channel.basic_publish(exchange='', 
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode = 2)) #make message persistent
    print("Sent %r" % message)

def run():
    connection, channel = helper.setup('task_queue')
    data = helper.scrape(area_codes_url)
    soup = BeautifulSoup(data)
    cats = soup.findAll("ul", { "class" : "cols-narrow" })
    for cat in cats:
        a_elems = cat.findAll("a")
        for a_elem in a_elems:
            ac_url = base_url + a_elem['href']
            dispatch(channel, ac_url)
    connection.close()

run()
