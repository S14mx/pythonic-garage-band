from abc import ABC, abstractmethod


class Musician(ABC):
    @abstractmethod
    def __init__(self, name: str, instrument: str = "instrument", solo: str = "solo"):
        self.name: str = name
        self.instrument: str = instrument
        self.solo: str = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self) -> str:
        return self.instrument

    def play_solo(self) -> str:
        return self.solo


class Band:
    instances: list['Band'] = []

    def __init__(self, name: str, members: list[Musician] = None):
        self.name = name
        self.members = members
        self.__class__.instances.append(self)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self) -> list[str]:
        solo_list = []
        for member in self.members:
            solo_list.append(member.play_solo())
        return solo_list
        # return [member.play_solo() for member in self.members]  == Alternative short solution

    @classmethod
    def to_list(cls):
        return cls.instances


class Guitarist(Musician):
    def __init__(self, name: str):
        super().__init__(name, "guitar", "face melting guitar solo")


class Bassist(Musician):
    def __init__(self, name: str):
        super().__init__(name, "bass", "bom bom buh bom")


class Drummer(Musician):
    def __init__(self, name: str):
        super().__init__(name, "drums", "rattle boom crash")
