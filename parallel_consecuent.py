from multiprocessing.pool import ThreadPool
from datetime import datetime
import time

def get_thread(name):
    time.sleep(1)
    print(name)


if __name__ == '__main__':
    '''Параллельное выполнение'''
    parallel = datetime.now()
    with ThreadPool(processes=5) as executor:
        executor.map(get_thread, ['Thread ' + str(i) + '\n' for i in range(1,6)])
    parallel = datetime.now() - parallel

    '''Последовательное выполнение'''
    consecutive = datetime.now()
    for i in range(1,6):
        get_thread('Thread ' + str(i))
    consecutive = datetime.now() - consecutive
    print(f'Параллельное выполнение {parallel} секунд '
          f'Последовательное выполнение {consecutive} секунд')