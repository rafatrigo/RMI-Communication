import Pyro5.api as Pyro
import utils

import random

@Pyro.expose
class Temperature:
    def __init__(self):
        self.temperature = random.randint(18, 35)
        self._exhauster_is_open = False
        
        print(f"System started. Temperature at {self.temperature}°C")

    def change_temperature(self, temperature):
        print(f"[LOG] Temperature change to {temperature}°C requested.")

        self.temperature = temperature

        return f"Temperature changed to {self.temperature}°C"

    def open_exhauster(self):
        print("[LOG] Exhauster opening requested.")

        if self._exhauster_is_open:
            return "Exhauster already open."

        self._exhauster_is_open = True

        return "Exhauster was opened."

    def verify_temperature(self):
        print("[LOG] Checking temperature.")

        return self.temperature

    def exhauster_is_open(self):
        print("[LOG] Checking if the exhauster is open.")

        return self._exhauster_is_open

def main():
    temperature = Temperature()

    utils.create_daemon(temperature, "temperature-sector")

if __name__ == "__main__":
    main()
