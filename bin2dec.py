 def bin2dec(num):
  # takes a binary numver as in input and returns the pinary equivalent
  # num is a string representing a binary number like "10101"
  result = 0
  for index in range(len(num)):
    digit = num[index]
    if digit == "1":
      result = result + pow(2,len(num)-index-1)
    return result 