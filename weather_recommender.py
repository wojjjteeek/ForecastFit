import tkinter
import requests
import json
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()


api_key = (os.getenv("API_KEY"))

print(api_key)