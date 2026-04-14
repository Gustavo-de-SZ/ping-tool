import subprocess
import time
from datetime import datetime
import os


TARGET_URL = "www.globo.com.br"
LOG_FILE = "ping_log.txt"
INTERVAL = 1  


def log_failure():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"[{timestamp}] FALHA: O ping para {TARGET_URL} falhou.\n"
    
    with open(LOG_FILE, "a") as f:
        f.write(msg)
    print(msg.strip())

print(f"Monitorando {TARGET_URL}... Feche a janela preta ou pressione Ctrl+C aqui para parar.")

try:
    while True:
        result = subprocess.run(
            f"cmd /c ping -n 1 -w 1000 {TARGET_URL}", 
            shell=True
        )

        if result.returncode != 0:
            log_failure()
        
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\nend.")