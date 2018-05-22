from . import constants as const

import pandas as pd
import queue
import threading
import time


class default_dict(dict):
	def __missing__(self, key):
		return '{' + key + '}'

