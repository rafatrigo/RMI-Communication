import Pyro5.api as Pyro
import utils

import random

"""
a more technical way to represent the light sprectrum would be to use
nanometers to represent the wavelenght of each color, since this
would allow for much more precise control. However, using the color name
is a more visual way to demonstrate how it works.
"""
valid_spectrum = [
    "blue",
    "red",
    "white",
    "purple"
]

@Pyro.expose
class UVLighting():
    def __init__(self):
        self.light_intensity = random.randint(50,100)
        self.light_spectrum = "white"
        
        print(f"System started. Light intensity at {self.light_intensity}% and light sprectrum equal '{self.light_spectrum}'")

    def change_intensity(self, intensity):
        print(f"[LOG] Light intensity chenge to {intensity}% requested.")

        self.light_intensity = intensity

        return f"Light intensity changed to {self.light_intensity}%"

    def change_spectrum(self, spectrum):
        print(f"[LOG] Light spectrum chaange to {spectrum} requested.")
        
        if spectrum in valid_spectrum:
            self.light_spectrum = spectrum
            return f"Light spectrum changed to {self.light_spectrum}."
        else:
            return f"Invalid spectrum. The valid values are {valid_spectrum}"

def main():
    uv_lighting = UVLighting()

    utils.create_daemon(uv_lighting, "uv-lighting-sector")

if __name__ == "__main__":
    main()

