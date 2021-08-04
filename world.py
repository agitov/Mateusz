class World:
    world = None

    def normalize(self, norm):
        return norm.capitalize()


    def validate(self, val):
        return val in ['Merkury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Ceres', 'Pluto', 'Haumea', 'Makemake', 'Eris']


    def __init__(self, con = "Earth"):
        con = self.normalize(con)
        self.world = con

        if not self.validate(con):
            raise ValueError("Don't known planet " + con + "!")


    def __str__(self):
        if self.world == "Earth":
            return "Hello world!"

        else:
            return "Welcome on " + self.world
