# Definición de la clase Roll para representar un lanzamiento de bola de bolos
class Roll:
    def __init__(self, pins: int):
        self.pins = pins  # El número de pines derribados en el lanzamiento


# Definición de la clase abstracta Frame que servirá como base para los frames de bolos
class Frame:
    def __init__(self):
        self.rolls = []  # Lista para almacenar los lanzamientos en este frame

    def add_roll(self, pins: int):
        self.rolls.append(Roll(pins))  # Agrega un lanzamiento a la lista de lanzamientos

    def score(self) -> int:
        pass  # Método abstracto para calcular la puntuación del frame

    def is_strike(self) -> bool:
        pass  # Método abstracto para verificar si es un strike

    def is_spare(self) -> bool:
        pass  # Método abstracto para verificar si es un spare


# Definición de la clase NormalFrame que hereda de la clase Frame
class NormalFrame(Frame):
    def score(self) -> int:
        pass  # Implementación específica para un frame normal para calcular la puntuación

    def is_strike(self) -> bool:
        pass  # Implementación específica para un frame normal para verificar si es un strike

    def is_spare(self) -> bool:
        pass  # Implementación específica para un frame normal para verificar si es un spare


# Definición de la clase TenthFrame que hereda de la clase Frame
class TenthFrame(Frame):
    def __init__(self):
        super().__init__()
        self.extra_roll = None  # Lanzamiento adicional en el décimo frame

    def add_roll(self, pins: int):
        if len(self.rolls) < 2:
            self.rolls.append(Roll(pins))  # Agrega un lanzamiento normal al frame
        elif len(self.rolls) == 2 and self.rolls[0].pins + self.rolls[1].pins >= 10:
            self.extra_roll = Roll(pins)  # Agrega el lanzamiento extra si es necesario

    def score(self) -> int:
        pass  # Implementación específica para el décimo frame para calcular la puntuación

    def is_strike(self) -> bool:
        pass  # Implementación específica para el décimo frame para verificar si es un strike

    def is_spare(self) -> bool:
        pass  # Implementación específica para el décimo frame para verificar si es un spare


# Definición de la clase Game que representa un juego completo de bolos
class Game:
    def __init__(self):
        self.frames = []  # Lista para mantener los frames del juego

    def roll(self, pins: int):
        if not self.frames or len(self.frames[-1].rolls) >= 2:
            if len(self.frames) < 10:
                self.frames.append(NormalFrame())  # Agrega un frame normal
            else:
                self.frames.append(TenthFrame())  # Agrega el décimo frame si es necesario
        self.frames[-1].add_roll(pins)  # Agrega un lanzamiento al frame actual

    def score(self) -> int:
        total_score = 0
        for i, frame in enumerate(self.frames):
            total_score += frame.score()  # Calcula la puntuación del frame actual
            if frame.is_strike() and i < 9:
                next_frame = self.frames[i + 1]
                total_score += next_frame.rolls[0].pins  # Agrega los puntos del siguiente frame si es un strike
                if next_frame.is_strike() and i < 8:
                    total_score += self.frames[i + 2].rolls[0].pins  # Agrega puntos adicionales si hay dos strikes seguidos
            elif frame.is_spare() and i < 9:
                total_score += self.frames[i + 1].rolls[0].pins  # Agrega puntos adicionales si es un spare
        return total_score  # Devuelve la puntuación total del juego
