class Roll:
    def __init__(self, pins: int):
        self.pins = pins

class Frame:
    def __init__(self):
        self.rolls = []

    def add_roll(self, pins: int):
        self.rolls.append(Roll(pins))

    def score(self) -> int:
        pass

    def is_strike(self) -> bool:
        pass

    def is_spare(self) -> bool:
        pass

class NormalFrame(Frame):
    def score(self) -> int:
        frame_score = sum(roll.pins for roll in self.rolls)
        return frame_score

    def is_strike(self) -> bool:
        return len(self.rolls) == 1 and self.rolls[0].pins == 10

    def is_spare(self) -> bool:
        return len(self.rolls) == 2 and self.score() == 10

class TenthFrame(Frame):
    def __init__(self):
        super().__init__()
        self.extra_roll = None

    def add_roll(self, pins: int):
        if len(self.rolls) < 2:
            self.rolls.append(Roll(pins))
        elif len(self.rolls) == 2 and self.rolls[0].pins + self.rolls[1].pins >= 10:
            self.extra_roll = Roll(pins)

    def score(self) -> int:
        frame_score = sum(roll.pins for roll in self.rolls)
        if self.extra_roll is not None:
            frame_score += self.extra_roll.pins
        return frame_score

    def is_strike(self) -> bool:
        return len(self.rolls) == 1 and self.rolls[0].pins == 10

    def is_spare(self) -> bool:
        return len(self.rolls) == 2 and self.score() == 10

class Game:
    def __init__(self):
        self.frames = []

    def roll(self, pins: int):
        if not self.frames or len(self.frames[-1].rolls) >= 2:
            if len(self.frames) < 10:
                self.frames.append(NormalFrame())
            else:
                self.frames.append(TenthFrame())
        self.frames[-1].add_roll(pins)

    def score(self) -> int:
        total_score = 0
        for i, frame in enumerate(self.frames):
            total_score += frame.score()
            if frame.is_strike() and i < 9:
                next_frame = self.frames[i + 1]
                total_score += next_frame.rolls[0].pins
                if next_frame.is_strike() and i < 8:
                    total_score += self.frames[i + 2].rolls[0].pins
            elif frame.is_spare() and i < 9:
                total_score += self.frames[i + 1].rolls[0].pins
        return total_score

