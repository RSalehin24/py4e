from multiprocessing import context
import urllib.request
from bs4 import BeautifulSoup
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE