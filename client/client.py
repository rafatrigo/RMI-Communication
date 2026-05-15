import Pyro5.api as Pyro
import sys


def display_menu():
    print("\n" + "=" * 35)
    print(" CLIENT TERMINAL - GREENHOUSE ")
    print("=" * 35)
    print("1. Activate Irrigation (Hydroponics)")
    print("2. Adjust Temperature (Climate Control)")
    print("3. Change Light Spectrum (Lighting)")
    print("4. Generate Daily General Report")
    print("5. Verify water level (Hydroponics)")
    print("6. Change light intensity (Lighting)")
    print("7. Open exhausters (Climate Control)")
    print("0. Exit")
    print("-" * 35)
    return input("Choose an option: ")


def main():
    hydroponics = Pyro.Proxy("PYRONAME:hydroponics-sector")
    climate_control = Pyro.Proxy("PYRONAME:temperature-sector")
    lighting = Pyro.Proxy("PYRONAME:uv-lighting-sector")

    #report = Pyro.Proxy("PYRONAME:greenhouse.report")

    while True:
        option = display_menu()

        if option == '1':
            try:
                response = hydroponics.activate_irrigation()

                print(f"{response}")

            except Exception as e:
                print(f"Connection error with Hydroponics sector. {e}")

        elif option == '2':
            try:
                degrees_str = input("Enter the new temperature (in °C): ")
                degrees = float(degrees_str)

                response = climate_control.change_temperature(degrees)

                print(f"{response}")

            except Exception as e:
                print(f"Connection error with Climate sector.")

        elif option == '3':
            color = input("Enter the desired spectrum color: ")

            try:
                response = lighting.change_spectrum(color)

                print(f"{response}")

            except Exception as e:
                print(f"Connection error with Lighting sector.")

        elif option == '4':
            try:
                #data = report.get_daily_report()

                print("\n" + "=" * 30)
                print("DAILY REPORT")
                print("=" * 30)

                #print(f"Water Level:     {data.get('water', 'N/A')}%")
                #print(f"Temperature:    {data.get('temperature', 'N/A')}°C")
                #print(f"Current Spectrum: {data.get('light', 'N/A')}")

                print("=" * 30)

            except Exception as e:
                print(f"Error generating report (Report service may be offline).")

        elif option == '5':
            try:
                response = hydroponics.verify_water_level();

                print(response)

            except Exception as e:
                print(f"Connection error with hydroponics serctor.")

        elif option == '6':
            try:
                light_intensity_str = input("Enter the new percentage of light intensity: ")
                light_intensity = float(light_intensity_str)

                response = lighting.change_intensity(light_intensity)

                print(response)

            except Exception as e:
                print(f"Connection error with lighting serctor.")

        elif option == '7':
            try:
                response = climate_control.open_exhauster();

                print(response)

            except Exception as e:
                print(f"Connection error with climate control serctor. {e}")

        elif option == '0':
            print("Exiting terminal...")

            hydroponics._pyroRelease()
            climate_control._pyroRelease()
            lighting._pyroRelease()
            report._pyroRelease()

            sys.exit(0)

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"A critical error occurred: {e}")
        print("TIP: Make sure the Name Server (python -m Pyro5.nameserver) is running.")
