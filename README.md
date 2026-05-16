## How to Run
To run the distributed system locally, you need to open multiple terminal instances.

#### 1. Install dependencies

Install the dependencies that are in the requirements file:
```bash
pip install -r requirements.txt
```

#### 2. Start the Pyro5 Name Server
The name server maps the logical names of the sectors to their physical network locations.

```bash
python -m Pyro5.nameserver
```

#### 3. Start the servers

Open a new terminal for each server and run:
```bash
python -m servers.hydroponic
python -m servers.temprerature
python -m servers.uv-lighting
python -m services.report
```

#### 4. Run the client terminal

Finally, open a terminal to interact with the system:
```bash
python -m client.client
```
