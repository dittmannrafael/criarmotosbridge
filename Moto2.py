class Moto:
    # Atributos da moto
    def __init__(self, freios, rodas):
        self.motor = None
        self.tipo_rodas = rodas
        self.tanque = None
        self.quadro = None
        self.para_lamas = None
        self.guidao = None
        self.tipo_freios = freios

    def __str__(self):
        return f"Moto: motor={self.motor}, tipo_rodas={self.tipo_rodas}, tanque={self.tanque}, quadro={self.quadro}, para_lamas={self.para_lamas}, guidao={self.guidao}, tipo_freios={self.tipo_freios}"


class MotoBuilder:
    # Métodos para configurar os atributos da moto individualmente
    def __init__(self, freios, rodas):
        self.moto = Moto(freios, rodas)

    def set_motor(self, motor):
        self.moto.motor = motor

    def set_tanque(self, tanque):
        self.moto.tanque = tanque

    def set_quadro(self, quadro):
        self.moto.quadro = quadro

    def set_para_lamas(self, para_lamas):
        self.moto.para_lamas = para_lamas

    def set_guidao(self, guidao):
        self.moto.guidao = guidao

    def build(self):
        return self.moto


class Freios:
    def __str__(self):
        pass


class FreioDisco(Freios):
    def __str__(self):
        return "Freios a disco"


class FreioLona(Freios):
    def __str__(self):
        return "Freios a lona"


class FreioABS(Freios):
    def __str__(self):
        return "Freios ABS"


class Rodas:
    def __str__(self):
        pass


class RodasLigaLeve(Rodas):
    def __str__(self):
        return "Rodas de liga leve"


class RodasRaiada(Rodas):
    def __str__(self):
        return "Rodas raiadas"


# Construindo as motos
builder = MotoBuilder(FreioDisco(), RodasLigaLeve())

builder.set_motor("Motor 250cc")
builder.set_tanque("Tanque de 15 litros")
builder.set_quadro("Quadro em aço")
builder.set_para_lamas("Para-lamas esportivos")
builder.set_guidao("Guidão esportivo")

moto = builder.build()

print("Moto Naked")
print("Itens da moto:")
print("Motor:", moto.motor)
print("Tipo de rodas:", moto.tipo_rodas)
print("Tanque:", moto.tanque)
print("Quadro:", moto.quadro)
print("Para-lamas:", moto.para_lamas)
print("Guidão:", moto.guidao)
print("Tipo de freios:", moto.tipo_freios)
print("-------------------------------------------")
print("")

builder = MotoBuilder(FreioDisco(), RodasLigaLeve())
builder.set_motor("Esportivo")
builder.set_tanque("Tanque de 15 litros")
builder.set_quadro("Quadro em aço")
builder.set_para_lamas("Para-lamas esportivos")
builder.set_guidao("Guidão esportivo")
moto_esportiva = builder.build()
print("Moto Esportiva")
print("Itens da moto:")
print("Motor:", moto_esportiva.motor)
print("Tipo de rodas:", moto_esportiva.tipo_rodas)
print("Tanque:", moto_esportiva.tanque)
print("Quadro:", moto_esportiva.quadro)
print("Para-lamas:", moto_esportiva.para_lamas)
print("Guidão:", moto_esportiva.guidao)
print("Tipo de freios:", moto_esportiva.tipo_freios)
print("-------------------------------------------")
print("")


builder = MotoBuilder(FreioLona(), RodasRaiada())
builder.set_motor("Custom")
builder.set_tanque("Tanque de 20 litros")
builder.set_quadro("Quadro em aço")
builder.set_para_lamas("Para-lamas cromados")
builder.set_guidao("Guidão alto")
moto_customizada = builder.build()
print("Moto Custom")
print("Itens da moto:")
print("Motor:", moto_customizada.motor)
print("Tipo de rodas:", moto_customizada.tipo_rodas)
print("Tanque:", moto_customizada.tanque)
print("Quadro:", moto_customizada.quadro)
print("Para-lamas:", moto_customizada.para_lamas)
print("Guidão:", moto_customizada.guidao)
print("Tipo de freios:", moto_customizada.tipo_freios)
print("-------------------------------------------")
