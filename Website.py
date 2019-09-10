import os
import random
from gps import *
from time import *

x = random.randint(1000, 9999)
from App import app
if __name__ == "__main__":
    app.debug = True
    host = os.environ.get('IP', '192.168.1.14')
    port = int(os.environ.get('PORT', x))
    app.run(host=host, port=port)
