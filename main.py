HEIGHT = 5
WIDTH = 25
YESCHAR = "1"
NOCHAR = "2"
GOOD = 100

import ngram_prob as ns
import random
import math

class dropQuote:
  def __init__(self, string, l):
    letters = l
    out = []
    myLetters = []
    for col in range(WIDTH):
      thisCol = string[col*HEIGHT:col*HEIGHT+HEIGHT]
      out.append([entry for entry in range(HEIGHT) if thisCol[entry] == YESCHAR])
    self.body = out

    for col in self.body:
      myLetters.append(letters[:len(col)])
      letters = letters[len(col):]
    self.letters = myLetters

  def __repr__(self):
    return str(self.body) + str(self.letters)

dq1 = "11222111111211211121211111211111111211111112111211211111111111122121111111121211121111111211112112121112212112112121111212112"

l1 = "MNIMOSWEHSEIOTFFNNEORTEFOSVAEMRCRUYEISTHNPWEGHOTARSDPTVEHRSWEEICFMNLLOTEILYDLVEEUCPPABTAGIYEOT"

dq2 = "21211211111211111121111112221211112111221111211112222121111211112111121121222112111121112211212211121111211112111221111221112"

l2 = "ITVIOOWNOSTDEHRADEKONDOTWHIPAEITHNNNDAMRUCEILALNTDILOTDHHNAEEESTDEVCEEMDORTIRUCDEVEET"

dq3 = "22112111111111221221121111111111121112121111121111111111212121111112121111212122111121111212122112121111211112111221211212112"

l3 = "BIAABMUAENTLYEIOTHHNTVAEEGCNPCOPTWEHMOAENORDFIANOSLNSEILWGHABINCITYFHIOOCDNNACEEENSCCIENR"

dq4 = "21111111111112111111121111121111112221111111112121211111111111111112112111211122212121211212122111121112212112111121111221112"

l4 = "EHSVACEISCLSTAHILTCOSVEOOTCILRHOPAIINUERSAFLPIILNOBMOSYEERTADIANRAYCLTEOACILLTTCEUCCORELOTILN"

dq5 = "21111111111121112121111111121212111111112112211111122112111111111112111112211111221112112111211111111111111121111121121212212"

l5 = "EITTHNNNOCEGOBETEHIMSINODINSGOSTTHNBEEEIESXAIOWCDNORGORTDLNDEOOREFNERVEEITHMOSVAEEEVDEIRNRSYCSTHI"

dq6 = "212221111111111211111112111111211111111111111121111111111211111111121112112112112122111112111112211122112112111212211112111112122112111112111212211122"

l6 = "CIADOSTYIINOSFNSSUAGILPRILNPUCEGIPRELMPTAAEIOPGNRRSEEEEGIDNNSISTTEINORTTYEENOORSUEEOTFNSXEOTWCIMSWATUHHNSTAEEYAES"

DQ = dropQuote(dq5, l5)

sowpods = {}

def processDict():
  f = open("sowpods.txt","r")
  l = [s.strip() for s in f.readlines()]
  for s in l:
    sowpods[s] = 1

processDict()

def getString(dqObj, customLetters):
  out = ""
  for row in range(HEIGHT):
    for col in range(WIDTH):
      if row in dqObj.body[col]:
        out += customLetters[col][dqObj.body[col].index(row)]
      else:
        out += " "
  return out

def swapTwo(letterset):
  num = random.randint(0, len(letterset) - 1)
  while len(letterset[num]) <= 1:
    num = random.randint(0, len(letterset) - 1)
  s = letterset[num]
  s1, s2 = random.randint(0, len(s)-1), random.randint(0, len(s)-1)
  while s2 == s1:
    s2 = random.randint(0, len(s)-1)
  if s1 > s2:
    t = s2
    s2 = s1
    s1 = t
  c1, c2 = s[s1], s[s2]
  s = s[:s1] + c2 + s[s1+1:s2] + c1 + s[s2+1:]
  letterset[num] = s
  return letterset

fitness = ns.ngram_score(('english_quadgrams.txt'))

def specialScore(string):
  out = 0
  for word in string.split():
    if word in sowpods:
      out += (len(word) + (len(word) == 1)) * GOOD
  out += fitness.score(string.replace(" ", ""))
  return out
    

def attack(dqObj):
  key = dqObj.letters
  plain = getString(dqObj, key)
  parentScore = specialScore(plain)

  for TEMP in range(10,-1,-1):
    for count in range(50000):
      child = swapTwo(key.copy())
      plainChild = getString(dqObj, child)
      childScore = specialScore(plainChild)
      df = childScore-parentScore
      if df > 0 :
        key = child
        parentScore = childScore
        plain = plainChild
      elif df<= 0 and TEMP != 0 :
        prob = random.random()
        magicNumber = math.exp(float(df/TEMP))
        if prob < magicNumber:
          key = child
          parentScore = childScore
          plain=plainChild
      if count% 2500 == 0:
        print("Gen "+str(count)+": "+plain+" with certainty of: "+str(parentScore)) 
  print("Final result: "+plain+" with certainty of: "+str(parentScore))
  
attack(DQ)
