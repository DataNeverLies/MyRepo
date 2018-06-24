class cars():
    wheels = 4;

    def __init__(self, make, model):
        self.make = make
        self.model = model

Ford = cars('Mustang','94')
print Ford.make
print Ford.model
print Ford.wheels
