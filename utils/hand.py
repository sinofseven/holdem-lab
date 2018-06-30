from card import Card
from util import check_same_cards, check_strait, check_suit_and_num, check_cards, make_value_string


class Hand:
  def __init__(self, cards):
    check_cards(cards)
    self.cards = cards
    is_flash, num_map = check_suit_and_num(cards)
    is_strait, strait_kicker = check_strait(num_map)
    if is_flash and is_strait:
      self.rank = 8
      self.kicker = strait_kicker
    elif is_strait:
      self.rank = 4
      self.kicker = strait_kicker
    else:
      rank, kicker = check_same_cards(num_map)
      self.rank = 5 if is_flash else rank
      self.kicker = kicker
    self.str_value = make_value_string(self.rank, self.kicker)
    self.value = int(self.str_value)
  @staticmethod
  def make(one, two, three, four, five):
    cards = [one, two, three, four, five]
    return Hand(cards)
  @staticmethod
  def make_ordinal_list(cards):
    true_card = []
    for i in cards:
      true_card.append(Card(i))
    return Hand(true_card)
  def __eq__(self, other):
    return self.value == other.value
  def __lt__(self, other):
    # self < other
    if self.__eq__(other):
      return False
    return self.value < other.value
  def __le__(self, other):
    if self.__eq__(other):
      return True
    return self.__lt__(other)
  def __ge__(self, other):
    return not self.__lt__(other)
  def __gt__(self, other):
    return not self.__le__(other)
  def __str__(self):
    return "<Hand rank={0}, kicker={1}>".format(self.rank, self.kicker)
  def get_ordinal_list(self):
    cards = []
    for i in self.cards:
      cards.append(i.origin)
    return sorted(cards)
  def data_str(self):
    print("({0}, {1})".format(self.rank, self.kicker))
  @staticmethod
  def order(list_hand):
    if not isinstance(list_hand, list):
      raise TypeError("list_hand is not list. ({0})".format(type(list_hand)))
    for i, v in enumerate(list_hand):
      if not isinstance(v, Hand):
        raise TypeError("list_hand[{0}] is not Hand. ({1})".format(i, type(v)))
    list_sorted = sorted(list_hand, reverse=True)
    tmp_map = {}
    for hand in list_sorted:
      num = tmp_map.get(hand.str_value)
      if num == None:
        num = 0
      num += 1
      tmp_map[hand.str_value] = num
    result = []
    count = 1
    for k, v in tmp_map.items():
      result.append({
        "rank": count,
        "value": int(k),
        "chop": v > 1
      })
    return result
