from bs4 import BeautifulSoup
import requests

from operator import itemgetter

import model
from sqlalchemy.orm import sessionmaker

RFD_DEALS_URL = 'http://forums.redflagdeals.com/hot-deals-f9/'
RFD_URL = 'http://forums.redflagdeals.com'


saved_threads = []


def start(pages):
    # load db
    model.Base.metadata.bind = model.engine
    DBSession = sessionmaker(bind=model.engine)
    session = DBSession()

    # clear db
    session.query(model.Thread).delete()
    session.commit()
    
    # do crawling
    for i in range(1, pages):
        url = RFD_DEALS_URL + str(i)
        print 'Getting page ' + str(i)
        r = requests.get(url)
        print 'Parsing page ' + str(i)
        parse_page(r.text)

    # sort threads by views
    global saved_threads
    saved_threads = sorted(saved_threads, key=itemgetter('views'), reverse=True)

    # write to db
    for thread in saved_threads:
        new_thread = model.Thread(thread['id'], thread['title'], thread['views'], thread['url'], thread['lastpostdate'])
        session.add(new_thread)
    session.commit()

    # debug
    # pretty_print(saved_threads)


def parse_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    threads = soup.find_all('li', class_='threadbit')
    for thread in threads:
        parse_threadbit(thread)


def parse_threadbit(tbit):
    print 'parsing threadbit'

    # create thread object
    thread = {}

    # get id
    thread_id = tbit['id']
    print 'thread id: ' + thread_id

    # get number of thread views
    views_div = tbit.find_all(class_='threadstats')[1]
    views_str = views_div.get_text().strip().replace(',','')
    if views_str == '-':
        print 'Thread moved, skipping.'
        return
    views_num = int(views_str)
    print 'views: ' + str(views_num)

    # get thread title and url
    title_div = tbit.find('a', class_='title')
    title = title_div.get_text().strip()
    print 'title: ' + title.encode('utf-8')

    thread_url = RFD_URL + title_div['href']
    print 'url: ' + thread_url

    # get last post date
    lastpost_div = tbit.find(class_='threadlastpost')
    lastpost_date = lastpost_div.find_all('dd')[1]
    lastpost_date_str = lastpost_date.get_text().strip()[:-8]
    print 'last post date: ' + lastpost_date_str

    thread['id'] = thread_id
    thread['views'] = views_num
    thread['title'] = title
    thread['url'] = thread_url
    thread['lastpostdate'] = lastpost_date_str

    # add to map
    saved_threads.append(thread)


# useless debug method
def pretty_print(threadlist):
    count = 0
    for thread in threadlist:
        if count==10:
            return
        print thread
        count += 1


if __name__ == '__main__':
    start(5)