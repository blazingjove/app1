import math

small = {
        1 : 15,
        2 : 24,
        3 : 28,
        4 : 32,
        5 : 36,
        6 : 40,
        7 : 44,
        8 : 48,
        9 : 52,
        10 : 56,
        11 : 60,
        12 : 64,
        13 : 68,
        14 : 72,
        15 : 76,
    }

medium = {
        1 : 15,
        2 : 24,
        3 : 28,
        4 : 32,
        5 : 36,
        6 : 42,
        7 : 47,
        8 : 51,
        9 : 56,
        10 : 60,
        11 : 65,
        12 : 69,
        13 : 74,
        14 : 78,
        15 : 83,
    }

large = {
        1 : 15,
        2 : 24,
        3 : 28,
        4 : 32,
        5 : 36,
        6 : 45,
        7 : 50,
        8 : 55,
        9 : 61,
        10 : 66,
        11 : 72,
        12 : 77,
        13 : 82,
        14 : 88,
        15 : 93,
    }

giant = {
        1 : 12,
        2 : 22,
        3 : 31,
        4 : 38,
        5 : 45,
        6 : 49,
        7 : 56,
        8 : 64,
        9 : 71,
        10 : 79,
        11 : 86,
        12 : 93,
        13 : 100,
        14 : 107,
        15 : 114,
    }

def dogCalc(h_age, type):
  if h_age < 1:
    return
  elif type == "small":
    d_age = small[h_age];
  elif type == "medium":
    d_age = medium[h_age];
  elif type == "large":
    d_age = large[h_age];
  else:
    d_age = large[h_age];  
  return d_age