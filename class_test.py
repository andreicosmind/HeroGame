class Warrior():
    ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

    def __init__(self, level=1, experience=100, achievements=[], rank=ranks[0]):
        self.level = level
        self.experience = experience
        self.achievements = achievements
        self.rank = rank

    def training(self, lst):
        if lst[2] <= self.level:
            result = lst[0]

            self.experience += lst[1]

            if self.experience > 10000: self.experience = 10000

            self.achievements.append(lst[0])

            if self.experience > 10000: self.level = 100
            else: self.level = self.experience // 100

            if len(str(self.level)) < 2: self.rank = self.ranks[0]
            elif len(str(self.level)) >= 3: self.rank = self.ranks[-1]
            else: self.rank = self.ranks[int(str(self.level)[0])]

            return result
        else:
            print("Not strong enough")


loki = Warrior()

print(loki.level)         # => 1
print(loki.experience)    # => 100
print(loki.rank)          # => "Pushover"
print(loki.achievements)  # => []
loki.training(["Defeated Chuck Norris", 9000, 1]) # => "Defeated Chuck Norris"
print(loki.experience)    # => 9100
print(loki.level)         # => 91
print(loki.rank)          # => "Master"
loki.training(["Defeated Chuck Norris", 123, 3]) # => "Not strong enough"
print(loki.achievements)  # => []
