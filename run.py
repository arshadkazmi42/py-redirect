import time

from multiprocessing.pool import ThreadPool as Pool


from arguments import Arguments
from file import File
from redirect import Redirect


MAX_POOL_SIZE = 5


def start():

    arguments = Arguments()
    filename = arguments.get_filename()

    fyle = File(filename)
    file_lines = fyle.get_lines()

    start_process(file_lines)


def start_process(file_lines):

    pool = Pool(MAX_POOL_SIZE)

    for line in file_lines:
        pool.apply_async(process_redirect, (line,))

    pool.daemon = True
    pool.close()
    pool.join()


def process_redirect(url):

    redirect = Redirect(url)
    redirect_request = redirect.get_redirect_request()

    if not redirect_request.is_redirect():
        return False

    redirect_response = redirect_request.get_response()

    print(f'{redirect_response.get_redirect_url()} {redirect_response.get_redirect_status_code()}')


start_time = time.time()
start()
print("Processed in %s minutes" % ((time.time() - start_time) / 60))