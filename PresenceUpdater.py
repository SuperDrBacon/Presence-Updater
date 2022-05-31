import os
import asyncio
import time
from time import sleep
from configparser import ConfigParser
from pypresence import Presence


config = ConfigParser()
config.read('/'.join([os.path.abspath(os.getcwd()), "config.ini"]))

bacon_id = config['DEFAULT']['id']
kirkbot_id = ''
print(f"bacon_id: {bacon_id}")

rpc = Presence(str(bacon_id))
rpc.connect()
x=0

while True:
    rpc.update(state=f"up to {x}", 
                details="whooo how high can it count?", 
                large_image="klomp", 
                #    large_image_text="My wife", 
                #    small_image="icon", 
                #    small_image_text="icon"
                )
    x+=1
    time.sleep(1)
