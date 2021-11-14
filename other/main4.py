# from itertools import product
#
#
# def convertTuple(tup):
#     str = ''.join(tup)
#     return str
#
#
# from string import ascii_letters
#
# ascii_letters = ascii_letters[0:26]
#
# # print(convertTuple(('a', 'b')))
# # print(ascii_letters)
# for i in product(ascii_letters, repeat=3):
#     print(convertTuple(i))


# s = '89.43.3.0'
# print(s)
# s = '.'.join(s.split('.')[:-1]) + '.' + '60'
# print(s)



# import datetime
# import time
#
# start = time.time()
# time.sleep(2)  # 2sec
# end = time.time()
# dt = end - start
# print(dt)
# print(str(datetime.timedelta(seconds=dt)))



import subprocess
process = subprocess.Popen(['ping','-c' ,'1', '8.8.8.8'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
returncode = process.returncode
print(returncode)
print(type(returncode))