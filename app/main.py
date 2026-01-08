class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        else:
            return Distance(km=self.km + other)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, number: int) -> "Distance":
        self.km = self.km * number
        return self

    def __truediv__(self, number: int) -> "Distance":
        self.km = round(self.km / number, 2)
        return self

    def __lt__(self, number: int) -> bool:
        if self.km < number:
            return True
        return False

    def __gt__(self, number: int) -> bool:
        if self.km > number:
            return True
        return False

    def __eq__(self, number: int) -> bool:
        if self.km == number:
            return True
        return False

    def __le__(self, number: int) -> bool:
        if self.km <= number:
            return True
        return False

    def __ge__(self, number: int) -> bool:
        if self.km >= number:
            return True
        return False
