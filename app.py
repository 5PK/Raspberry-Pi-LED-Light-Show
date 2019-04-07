
# FLASK_APP=app.py flask run

from flask import Flask, render_template, request
from myThreads import blinkThread, playLightThread , playMusicThread
from lightshow import blink_all, all_pins_off, getInterval
import os
import RPi.GPIO as GPIO

import pyaudio
import wave

app = Flask(__name__)
# __name__ = '__main__'




# if __name__ == '__main__':

    # Create threads

blink_thread = blinkThread()
playmusic_thread = playMusicThread("music/song3.wav")
playlights_thread = playLightThread(0)
    

threads = [
    blink_thread,
    playmusic_thread,
    playlights_thread
]
    


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blink", methods=["GET"])
def blink_view():
    global blink_thread, threads
    


    for thread in threads:
        if thread.is_alive():
            thread.kill()


    blink_thread = blinkThread()
    blink_thread.start()

    # Unpause and execute function
    return "blink started"


@app.route("/lightshow", methods=["GET"])
def lightshow_view():
    
    global  playlights_thread, playmusic_thread
    song = 'music/' + request.args.get('song') + '.wav'

    interval = getInterval(song)
   
    print(interval)


    for thread in threads:
        if thread.is_alive():
            thread.kill()


    playlights_thread = playLightThread(interval)
    playmusic_thread = playMusicThread(song)
    
    playlights_thread.start()
    playmusic_thread.start()

    return "show started"


@app.route("/shutdown", methods=['GET'])
def shutdown():
    global blink_thread

    blink_thread.kill()
    playlights_thread.kill()
    playmusic_thread.kill()

    all_pins_off()
    any(thread.kill() for thread in threads)

    return "all threads paused"




app.run(
    host='0.0.0.0', 
    debug=True,
    threaded=True)


'''

if __name__ == '__main__':

    # Create threads

    blink_thread = RaspberryThread(function=blink_all)
    playmusic_thread = RaspberryThread(function=playMusic)
    playlights_thread = RaspberryThread(function=playLights)
    

    threads = [
        blink_thread,
        playmusic_thread,
        playlights_thread
    ]
    
    # Run server
    app.run(
        host='0.0.0.0', 
        debug=True,
        threaded=True)

'''        
