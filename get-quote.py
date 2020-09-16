
import random

def primordial():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 27
  x = random.randint(0, last)
  y = random.randint(0, last)
  while x == y:
    y = random.randint(0, last)

  print(quotes[x], end="")
  print(quotes[y])

if __name__== "__main__":
  primordial()
