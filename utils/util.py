from card import Card

def check_suit_and_num(cards):
  if not isinstance(cards, list):
    raise TypeError("cards is not list. ({0})".format(type(cards)))
  if len(cards) != 5:
    raise ValueError("length of cards is not 5. ({0})".format(len(cards)))
  is_flash = True
  first_suit = None
  nums = {}
  for i in range(13):
    nums[str(i)] = 0
  for (i, card) in enumerate(cards):
    if not isinstance(card, Card):
      raise TypeError("cards[{0}] is not Card. ({1})".format(i, type(card)))
    if i == 0:
      first_suit = card.suit
    else:
      if is_flash and first_suit != card.suit:
        is_flash = False
    nums[str(card.num)] += 1
  return (is_flash, nums)
def check_strait(num_map):
  is_strait = False
  kicker = None
  if num_map["9"]  == 1 and \
     num_map["10"] == 1 and \
     num_map["11"] == 1 and \
     num_map["12"] == 1 and \
     num_map["0"]  == 1:
    is_strait = True
    kicker = [13]
  else:
    for i in range(9):
      if num_map[str(i)] == 1:
        if num_map[str(i + 1)] == 1 and \
           num_map[str(i + 2)] == 1 and \
           num_map[str(i + 3)] == 1 and \
           num_map[str(i + 4)] == 1:
          is_strait = True
          kicker = [i + 4]
  return (is_strait, kicker)
def check_same_cards(num_map):
  single = []
  pair = []
  three = None
  four = None
  for i, num in num_map.items():
    card = 13 if i == "0" else int(i)
    if num == 1:
      single.append(card)
    elif num == 2:
      pair.append(card)
    elif num == 3:
      three = card
    elif num == 4:
      four = card
  if four != None:
    return (7, [four, single[0]])
  elif three != None and len(pair) == 1:
    return (6, [three, pair[0]])
  elif three != None:
    single.sort(reverse=True)
    kicker = [three]
    kicker.extend(single)
    return (3, kicker)
  elif len(pair) != 0:
    rate = len(pair)
    pair.sort(reverse=True)
    single.sort(reverse=True)
    kicker = pair
    kicker.extend(single)
    return (rate, kicker)
  else:
    single.sort(reverse=True)
    return (0, single)
def check_cards(cards):
  if not isinstance(cards, list):
    raise TypeError("cards is not list. ({0})".format(type(cards)))
  if len(cards) != 5:
    raise ValueError("length of cards is not 5. ({0})".format(len(cards)))
  for i, v in enumerate(cards):
    if not isinstance(v, Card):
      raise TypeError("cards[{0}] is not Card. ({1})".format(i, type(v)))

def check_community(cards):
  check_cards(cards)

def check_role(cards):
  if not isinstance(cards, list):
    raise TypeError("cards is not list. ({0})".format(type(cards)))
  if len(cards) != 2:
    raise ValueError("length of cards is not 2. ({0})".format(len(cards)))
  for i, v in enumerate(cards):
    if not isinstance(v, Card):
      raise TypeError("cards[{0}] is not Card. ({1})".format(i, type(v)))

def make_value_string(rank, kicker):
  pudding_kicker = []
  length = len(kicker)
  for i in range(5):
    num = 0
    if i < length:
      num = kicker[i]
    pudding_kicker.append(num)
  list_str = map(lambda x: "{0:02d}".format(x), pudding_kicker)
  str_kicker = "".join(list(list_str))
  value = "{0}{1}".format(rank, str_kicker)
  return value