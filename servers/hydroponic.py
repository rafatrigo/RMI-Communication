import Pyro5.api as Pyro
import utils

import random

@Pyro.expose
class Hydroponics():
    def __init__(self):
        # mocked values
        self.water_level = random.randint(50, 100)
        self.irrigating = False

        print("System started. Water level at ", self.water_level)

    def verify_water_level(self):
        print(f"[LOG] Water verification requested. Water level at {self.water_level}")
        return self.water_level

    def activate_irrigation(self):
        print("[LOG] Irrigation requested.")

        if self.irrigating:
            return "Irrigation was already active."


        self.irrigating = True
        return "Irrigation activated."

    def verify_irrigation(self):
        print("[LOG] Checking irrigation.")

        return self.irrigating

def main():
    hydroponics = Hydroponics()

    utils.create_daemon(hydroponics, "hydroponics-sector")

if __name__ == "__main__":
    main()
