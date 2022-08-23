#Notificador para Desktop
import time
from plyer import notification

if __name__ == '__main__':
    notification.notify(
        title = "ALERTA !!!!",
        message = "Faça uma pausa corno!",
        timeout = 10
    )
    time.sleep(3600)