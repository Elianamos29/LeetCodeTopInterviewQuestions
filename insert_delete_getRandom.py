import random

class RandomizedSet:

    def __init__(self):
        self.items = []

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            self.items.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.items)


if __name__ == '__main__':
    obj = RandomizedSet()
    param_1 = obj.insert(val=1)
    param_2 = obj.insert(val=1)
    param_3 = obj.insert(val=2)
    param_4 = obj.remove(val=2)
    param_5 = obj.remove(val=3)
    param_6 = obj.getRandom()
    print(param_1, param_2, param_3, param_4, param_5, param_6)