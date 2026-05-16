import Pyro5.api as Pyro

def create_daemon(class_instance, server_namespace):
    with Pyro.Daemon() as daemon: 
        try:
            ns = Pyro.locate_ns()
        except:
            print("Error: make sure that nameserver is running. Command to start nameserver: python -m Pyro5.nameserver")
            return

        uri = daemon.register(class_instance)
        print(f"Server ready. URI: {uri}")

        ns.register(server_namespace, uri)

        daemon.requestLoop()

