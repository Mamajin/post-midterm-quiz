class Candidate:
    def __init__(self, name, age, followers, genre, status="new"):
        # isinstance is used to check the value of a given parameter if the
        # value is not true to the condition it raises an error
        if not isinstance(name, str):
            raise TypeError()
        if name.strip() == "" or genre.strip() == "":
            raise ValueError()
        if not isinstance(age, int):
            raise TypeError()
        if not isinstance(followers, int):
            raise TypeError()
        if age < 0 or followers < 0:
            raise ValueError
        if not isinstance(genre, str):
            raise TypeError()

        self.__name = name
        self.__age = age
        self.__followers = followers
        self.__genre = genre
        self.__status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if value not in ["new", "qualified", "accepted", "rejected"]:
            raise ValueError()
        self.__status = value

    def __str__(self):
        return f"Candidate: {self.__name}, {self.__age}, {self.__followers}, {self.__genre} ({self.__status})"


can = Candidate("Kenny", 18, 2000, "dog game")
can.status = "new"
print(can)