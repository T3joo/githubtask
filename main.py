class Student:

    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def displayscore(self):
        print(self.score)


Bob = Student("Bob", 26, "FE,BE", 20.90)


# Expected methods
Bob.change_name = "Peter"
Bob.change_age = 34
Bob.add_track = "UI/UX"

print(Bob.change_name)
print(Bob.change_age)
print(Bob.add_track)
print(getattr(Bob, 'score'))
