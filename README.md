
# Welcome to the Activity Tracker repository!

This software is made in **Python** and dedicated to developing an open-source activity tracking application that can be used to monitor and track various computer activities. The app is designed to log keywords typed by the user and take screenshots of their screen at specified intervals. This data is then sent to a **Redis database** hosted on **Upstash or any other platform**, where you can see the data.










## Authors

- [@AyanProgrammer11](https://www.github.com/AyanProgrammer11)


## Disclaimer

**This software is for Educational Purposes only!**

It's important to note that using such a software on others devices without the owner permission could potentially infringe on individual privacy rights and could be considered illegal in some jurisdictions.
## Features

- Realtime Data Storing
- Key Logging
- Takes a Screenshot after every **15 seconds** (You can modify the code to change the timing)
- Uses a Redis Database for faster read and write.


## Use Cases


* Employee monitoring in the workplace to improve productivity and identify potential security risks.

* Parental control to monitor children's computer activity and ensure they are not engaging in inappropriate behavior online.
* Investigative purposes, such as tracking the online activity of suspects in criminal cases.
* Educational settings, such as monitoring student computer activity during online exams to prevent cheating.
* Personal use, such as monitoring your own computer activity to identify areas where you can optimize productivity and reduce distractions.
## How to run the project

*To run this project, follow the following steps:*

* **Clone** the repository: `https://github.com/Ayanprogrammer11/Activity-Tracker.git` or with a Github CLI `gh repo clone Ayanprogrammer11/Activity-Tracker`

* Before running the program in console, Make *sure* to first install the **required packages** in the `requirements.txt` file. For automatically installing the required packages in the file use the command `pip install -r requirements.txt`.

* If you don't have an **Upstash** account then create one here (https://upstash.com), then create a Redis Database with **TLS/SSL** enabled, choosing eviction is your choice

* Now add environment variables by creating a `.env` file and add the following variables with your **own credentials and replace "Goes here"** with your own credentials:
`REDIS_HOST=Goeshere`   
`REDIS_PORT=Goeshere`  
`REDIS_PASSWORD=Goeshere`

* Make sure you are in `root/code` directory. Now run the program in terminal by `python main.py`

* Do some activity type some words letters anywhere and press enter, wait 20-30 seconds or more and then stop the program by `Ctrl + C` in terminal. **Note:** *The data is stored realtime so the data would saved in database even when you don't terminate the process*

**Yoo! Data Saved!**








## Extract Logs and Images

 You can see the stored data ofcourse on **Upstash**, but sometimes when there is large data it fails to show it. For that reason, you could run the file named `extractImagesandText.py` in the terminal. Change directory onto `data` from the root directory. And run the command `python extractImagesandText.py`, It would extract the logs and images on the same directory where you will execute the command.
## Open Source

***Feel free to modify and sell/post the code or use for your educationaly/personal purposes. If you had any ideas on how to improve it then please submit a pull request along with detailed commit :)***
## Feedback

If you have any feedback, please reach to me at ayanliaqat48@gmail.com

