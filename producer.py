import pika, sys, helper
from bs4 import BeautifulSoup

BASE_URL = 'https://www.area-codes.org.uk/'
AREA_CODE_URL = BASE_URL + 'full-uk-area-code-list.php'


def dispatch(channel, message):
    channel.basic_publish(exchange='', 
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(delivery_mode = 2)) #make message persistent
    print("Sent %r" % message)


def run():
    connection, channel = helper.setup('task_queue')
    data = helper.scrape(AREA_CODE_URL)
    soup = BeautifulSoup(data)
    trs = soup.findAll("tr")
    for tr in trs:
        a_elems = tr.findAll("a")
        for a_elem in a_elems:
            ac_url = BASE_URL + a_elem['href']
            dispatch(channel, ac_url)
    connection.close()

if __name__ == "__main__":
    run()