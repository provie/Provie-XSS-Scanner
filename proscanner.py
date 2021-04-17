#!/usr/bin/env python3
'''
ProScanner - 2021
Copyright under the MIT license
'''
if sys.version_info < (3, 6):
    print('[-] ProScanner requires python >= 3.6')
    sys.exit()
    
import os
import sys
import time
import urllib3
import argparse
import settings
import requests
import subprocess
import mechanize
import sys
import httplib
import argparse
import logging
from urlparse import urlparse

def main():
  print("Start")

if __name__=="__main__":
	try:
      main()
  except KeyboardInterrupt:
      pass
  except SystemExit as e:
      pass
  except RuntimeError as e:
      logger.critical(e)
  except Exception as e:
      logger.critical(e)
  finally:
      if threading.activeCount() > 1:
          os._exit(getattr(os, "_exitcode", 0))
      else:
          sys.exit(getattr(os, "_exitcode", 0))
