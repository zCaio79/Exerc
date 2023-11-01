class Computador:
    def __init__(self,id_computador):
        self.id_computador = id_computador
        self.monitor = None

    def conectarMonitor(self,monitor):
        self.monitor = monitor

    def mostrarSetup(self):
        print("Computador: ",self.id_computador,"\nMonitor: ",self.monitor)
    
class Monitor:
    def __init__(self,id_monitor):
        self.id_monitor = id_monitor

computador1 = Computador("1")
monitor1 = Monitor("1")
computador1.conectarMonitor(monitor1.id_monitor)
computador1.mostrarSetup()