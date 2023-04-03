import logging
import time

try:

    logging.basicConfig(filename="practice.log" ,datefmt="%H-%M" , level=logging.INFO)

    logging.info('User logged in time ')

except Exception as e:
    print(e)
