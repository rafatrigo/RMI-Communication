import Pyro5.api as Pyro
import utils

@Pyro.expose
class Report:
    def daily_report(self):
        print("[LOG] Daily report requested.")

        report_data = {}

        # hydroponics
        try:
            with Pyro.Proxy("PYRONAME:hydroponics-sector") as hydroponics:
                report_data["water"] = hydroponics.verify_water_level()
                report_data["irrigating"] = hydroponics.verify_irrigation()
        except Exception as e:
            print("[WARNIG] Fail to connect to hydroponics.")
            report_data["water"] = "OFFLINE"
            report_data["irrigating"] = "OFFLINE"

        # climate control
        try:
            with Pyro.Proxy("PYRONAME:temperature-sector") as climate_control:
                report_data["temperature"] = climate_control.verify_temperature()
                
                if climate_control.exhauster_is_open():
                    report_data["exhauster"] = "Open"
                else:
                    report_data["exhauster"] = "Closed"
        except Exception as e:
            print(f"[WARNIG] Fail to connect to climate control.{e}")
            report_data["temperature"] = "OFFLINE"
            report_data["exhauster"] = "OFFLINE"

        # lighting
        try:
            with Pyro.Proxy("PYRONAME:uv-lighting-sector") as lighting:
                report_data["light_intensity"] = lighting.verify_light_intensity()
                report_data["light_spectrum"] = lighting.verify_light_spectrum()
        except Exception as e:
            print("[WARNIG] Fail to connect to lighting.")
            report_data["light_intensity"] = "OFFLINE"
            report_data["light_spectrum"] = "OFFLINE"

        print("[LOG] Report created.")

        return report_data
        
def main():
    report = Report()
    
    utils.create_daemon(report, "report-service")

if __name__ == "__main__":
    main()

