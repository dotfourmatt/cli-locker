from modules import Locker
from datetime import datetime

if __name__ == "__main__":
    print(f">>> Program intialised at: {datetime.now().strftime('%H:%M:%S')}, on {datetime.now().strftime('%d/%m/%Y')}")
    Locker()