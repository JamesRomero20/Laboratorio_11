import cv2

class VideoObservable:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, frame):
        for observer in self._observers:
            observer.update(frame)

class VideoViewer:
    def update(self, frame):
        cv2.imshow('Deteccion estados de animo', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            return True