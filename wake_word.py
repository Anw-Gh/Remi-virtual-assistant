import pvporcupine
from pvrecorder import PvRecorder



def ww_detect():
    try:
        pp = 'path_to_your_model'
    
        porcupine = pvporcupine.create(access_key='API_KEY',
                                       keyword_paths =[pp])
        recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    
        recoder.start()
    
        print('lestinning...')
        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                return 'detected wake word'
    
    
    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()

