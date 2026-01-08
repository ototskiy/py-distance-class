class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, number: float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: float) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
            return False
        else:
            if self.km < other:
                return True
            return False

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
            return False
        else:
            if self.km > other:
                return True
            return False

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            if self.km == other.km:
                return True
            return False
        else:
            if self.km == other:
                return True
            return False

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
            return False
        else:
            if self.km <= other:
                return True
            return False

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
            return False
        else:
            if self.km >= other:
                return True
            return False
