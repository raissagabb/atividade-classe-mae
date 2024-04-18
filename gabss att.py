class Veiculo:
    def __init__(self, marca , modelo):
        self.marca = marca
        self.modelo = modelo
    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando.")
    def freiar(self):
        print(f"{self.marca} {self.modelo} está freiando.")
class Carro(Veiculo):
    def __init__(self,marca , modelo):
        super().__init__(marca,modelo)
    def abrir_portas(self):
        print(f"{self.marca} {self.modelo} está abrindo as portas ")
class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    def empinar(self):
        print(f"{self.marca} {self.modelo} está empinando.")

if __name__ == '__main__':
    carro1 = Carro('chevrolet','onix')
    moto1 = Moto('Honda','Sahara') 

    carro1.abrir_portas()
    carro1.acelerar()
    carro1.freiar()
    moto1.acelerar()
    moto1.freiar()
    moto1.empinar()