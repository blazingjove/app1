import math

def catCalc(h_age):
  if h_age < 6:
    d_age = math.trunc((h_age * 19/3) +1);
  else:
    d_age = math.trunc(((h_age - 6)*4) + 40);

  return d_age