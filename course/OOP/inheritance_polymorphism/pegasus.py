class Bird:
    def fly(self):
        print(f"I'm {self.__class__.__name__} flying!")


class Horse:
    def run(self):
        print(f"I'm {self.__class__.__name__} running!")


class Pegasus(Bird, Horse):
    pass


pegasus = Pegasus()
pegasus.fly()
pegasus.run()
