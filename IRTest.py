from gpiozero import DigitalInputDevice
import time

sensor = DigitalInputDevice(17, pull_up=True)



def look_for_piece():
    detection_start = None

    while True:
        if sensor.value:
            if detection_start is None:
                detection_start = time.time()  # start timing

            elapsed = time.time() - detection_start
        
            if elapsed >= 1.0:
                print("Object confirmed (1 second)")
                time.sleep(2)
                break
        else:
            print("no")
            detection_start = None  # reset if signal drops

        time.sleep(0.05)
