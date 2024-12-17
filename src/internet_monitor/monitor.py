import os
import time
import socket

def is_connected(host="8.8.8.8"):
    try:
        socket.create_connection((host, 53), timeout=5)
        return True
    except OSError:
        return False

def monitor_internet(timeout_hours, check_interval_seconds=60, test_host="8.8.8.8"):
    no_connection_time = 0
    timeout_seconds = timeout_hours * 3600

    while True:
        if is_connected(host=test_host):
            print("Conexão com a internet detectada. Resetando contador.")
            no_connection_time = 0
        else:
            print("Sem conexão com a internet.")
            no_connection_time += check_interval_seconds

        if no_connection_time >= timeout_seconds:
            print(f"Sem conexão por {timeout_hours} horas. Reiniciando o computador...")
            if os.name == 'nt':
                os.system("shutdown /r /t 0")
            else:
                os.system("reboot")
            break

        time.sleep(check_interval_seconds)

if __name__ == "__main__":
    TIMEOUT_HOURS = 1
    CHECK_INTERVAL_SECONDS = 60
    TEST_HOST = "8.8.8.8"
    print("Iniciando monitoramento da conexão com a internet...")
    monitor_internet(TIMEOUT_HOURS, CHECK_INTERVAL_SECONDS, TEST_HOST)

