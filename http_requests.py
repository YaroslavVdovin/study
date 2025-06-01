import requests
from multiprocessing.pool import ThreadPool
import time

def get_html(link):
    response = requests.get(link)
    if response.status_code == 200:
        return response.text
    else:
        return response.status_code
links = ['https://brunoyam.com/',
         'https://developer.mozilla.org/ru/docs/Web/HTTP/Reference/Status/403',
         'https://pypi.org/', 'https://www.wikipedia.org/',
         'https://packaging.python.org/en/latest/guides/using-manifest-in/']

if __name__ == '__main__':
    parallel = time.time()

    with ThreadPool(processes = len(links)) as executor:
        executor.map(get_html, links)

    parallel = time.time() - parallel
    consecutive = time.time()

    for i in links:
        get_html(i)

    consecutive = time.time() - consecutive

    print(f'Параллельное выполнение {parallel} секунд ' 
          f'\nПоследовательное выполнение {consecutive} секунд')
