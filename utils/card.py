class Card(object):
  def __init__(self, num):
    if not isinstance(num, int):
      raise TypeError("num is int.")
    if num < 0:
      raise IndexError("num is 0 or more.")
    if num >= 52:
      raise IndexError("num is less than 52.")
    self.suit = int(num / 13)
    self.num = num % 13
    self.origin = num
  def __str__(self):
    return "<Card suit={0}, num={1}>".format(self.suit, self.num)
  @staticmethod
  def make(suit, num):
    if not isinstance(suit, int):
      raise TypeError("suit is not int. ({0})".format(type(suit)))
    if not isinstance(num, int):
      raise TypeError("num is not int. ({0})".format(type(num)))
    if suit < 0:
      raise IndexError("suit is not 0 or more. ({0})".format(suit))
    if suit > 3:
      raise IndexError("suit is not 3 or less. ({0})".format(suit))
    if num < 0:
      raise IndexError("num is not 0 or more. ({0})".format(num))
    if num > 12:
      raise IndexError("num is 12 or less. ({0})".format(num))
    return Card(suit * 13 + num)