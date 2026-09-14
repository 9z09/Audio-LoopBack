import sounddevice as sd

# اختيار معدل العينات (44100HZ)
SAMPLE_RATE = 44100
CHANNELS = 2

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata

print("Ctrl+C To STOP")

try:
    
    with sd.Stream(samplerate=SAMPLE_RATE, channels=CHANNELS, callback=callback):
        while True:
            sd.sleep(1000)
except KeyboardInterrupt:
    print("\nDone")
except Exception as e:
    print(f"Something is Wrong in => {e}")
# 𝗠𝗮𝗱𝗲 𝗕𝘆 𝗣𝗲𝘁𝗲𝗿𝗣𝗮𝗿𝗸𝗲𝗿🕷️