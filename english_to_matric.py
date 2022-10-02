'''
x cm = inch * 2.54
x kg = lbs / 2.205
x lbs = kg * 2.205
x inch = cm / 2.54
'''

def to_matric(inches, pounds):
  cm = round(inches * 2.54, 2)
  kg = round(pounds / 2.205, 2)
  return cm, kg

def to_english(cm, kg):
  inches = round(cm / 2.54, 2)
  pounds = round(kg * 2.205, 2)
  return inches, pounds

def main():
  c = input("[E]nglish to Matric or [M]atric to English: ").upper()
  if c == "E":
    height = float(input("Inches: "))
    weight = float(input("Pounds: "))
    cm, kg = to_matric(height, weight)
    print("Your height in cm is:", cm)
    print("Your weight in kg is:", kg)

  elif c == "M":
    height = float(input("cm: "))
    weight = float(input("kg: "))
    inches, pounds = to_english(height, weight)
    print("Your height in inches is:", inches)
    print("Your weight in pounds is:", pounds)


if __name__ == "__main__":
  main()
