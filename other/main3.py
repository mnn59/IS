import csv
import os
from itertools import product
from string import ascii_letters

import joblib as joblib


def convertTuple(tup):
    str = ''.join(tup)
    return str


def check_ping(address, domain):
    url = "{}{}".format(address, domain)
    response = None
    try:
        # response = ping(url, verbose=False)

        response = os.system("ping -c 1 " + url)
        # and then check the response...
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network Error"

        with open('results.csv', mode='a') as url_file:
            employee_writer = csv.writer(url_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # response time reached request time
            # if response is None or "2000" in str(response):
            if response == 0:
                print("time out! there is no such site")
                employee_writer.writerow([url, 'fail'])

            else:
                print("success! there is a site with this url ({})".format(url))
                employee_writer.writerow([url, 'success'])
    except ValueError as ve:
        print(ve)


# clear csv
f = open("results2.csv", "w")
f.truncate()
f.close()

print("enter the number of characters:")
n = int(input())
print("enter domain:")
domain = str(input())

# generation all possible addresses

# eliminating to only lower case letters
ascii_letters = ascii_letters[0:26]

with joblib.Parallel(n_jobs=2) as parallel:
    accumulator = 0.
    n_iter = 0
    while accumulator < 1000:
        results = parallel(joblib.delayed(check_ping)(convertTuple(i), domain)
                           for i in product(ascii_letters, repeat=n))
        if results is not None:
            accumulator += sum(results)  # synchronization barrier
            n_iter += 1

# joblib.Parallel(n_jobs=4, backend='multiprocessing')(
#     [joblib.delayed(check_ping)(convertTuple(i),
#                                 domain)
#      for i in product(ascii_letters, repeat=n)])

# for i in product(ascii_letters, repeat=n):
#     address = convertTuple(i)
#     check_ping(address, domain)
