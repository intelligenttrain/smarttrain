from TrainController import controller,trainForward,trainStop,call_train
import time

def init_system():

    call_train(20,0,0,0)
    time.sleep(1)
    call_train(20,0,0,0)
    time.sleep(1)
    call_train(20,0,0,0)
    time.sleep(1)
    call_train(20,0,0,0)


if __name__ == "__main__":
    init_system()
