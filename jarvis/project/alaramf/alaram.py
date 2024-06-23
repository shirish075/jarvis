import os
import random
import threading
from datetime import datetime

from alaramf.alaram_timing import AlarmTiming


class Alarm(threading.Thread):
    def __init__(self, voice_input):
        threading.Thread.__init__(self)
        self.input = voice_input

    def run(self):
        new = AlarmTiming(self.input).get_expected_time()
        if new:
            new = datetime.strptime(new, "%Y-%m-%d %H:%M:00")
            print('Current time is : ' + str(datetime.now()))
            if datetime.now() > new:
                print('Alarm time is greater than current time sir.')
            else:

                while True:
                    now = datetime.now().strftime('%Y-%m-%d %H:%M:00')
                    now = datetime.strptime(now, "%Y-%m-%d %H:%M:00")
                    if now == new:
                        path = r"C:\Users\GPT SDPT\Music"
                        songs = os.listdir(path)
                        os.startfile(os.path.join(path, songs[random.randint(0, len(songs) - 1)]))
                        print('Sir, You need to wake up now.')
                        break
