#  Imagine you are creating a Super Mario game. You need to define a
# class to represent Mario. What would it look like? If you aren't familiar
# with SuperMario, use your own favorite video or board game to model
# a player.

class Mario():
    def __init__(self, cap, n_h, glove, gun_got, shirt_color, body_size, n_l, pant_color, shoe_color):
        self.cap = cap
        self.no_of_hand = n_h
        self.glove_color = glove
        self.gun_got = gun_got
        self.shirt_color = shirt_color
        self.body_size = body_size
        self.number_of_leg = n_l
        self.pant_color = pant_color
        self.shoe_color = shoe_color

    def head(self):
        cap = self.cap
        print("this is mario head with ", cap, "cap")

    def hand(self, no_of_hand, glove_color, gun_got):
        no_of_hand = self.no_of_hand
        glove_color = self.glove_color
        gun_got = self.gun_got
        print("mario has ", no_of_hand, "hand", ", with ",
              glove_color, "'s color globe gun=", gun_got)

    def body(self, shirt_color, body_size):
        shirt_color = self.shirt_color
        body_size = self.body_size

    def leg(self, number_of_leg, pant_color, shoe_color):
        number_of_leg = self.number_of_leg
        pant_color = self.pant_color
        shoe_color = self.shoe_color
