import math

def dogCalc(h_age):
  d_age = math.trunc(31 * math.log(h_age) + 31);

  return d_age