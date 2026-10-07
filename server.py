class Server:
    def __init__(self, hostname,status,cpu_usage):
        self.hostname = hostname
        self.status = status
        self.cpu_usage = cpu_usage

    def boot(self):
        self.status = "booting"
        self.cpu_usage = 0

    def shutdown(self):
        self.status = "shutting down"
        self.cpu_usage = 0

    def increase_load(self, amount):
        self.cpu_usage += amount

    def display_status(self):
        print(f"Server {self.hostname}: Status - {self.status}, CPU Usage - {self.cpu_usage}")
server1 = Server("Server01", "online", 25)
server1.display_status()
