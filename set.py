
def Set():
  print("====SET OPERATION====")
  set1 = set()
  set2 = set()
  set3 = set()
  sett__list = [ set1, set2, set3]
  val1 = input("Write your first set Note(seperate each element with comma sign(,)) :")
  val2 = input("Write your second set Note(seperate each element with comma sign(,)) :")
  val3 = input("Write your third set Note(seperate each element with comma sign(,)) :")
  input_arr = [val1, val2, val3]
  
  counter = -1
  for x in input_arr:
    counter += 1
    set_list = x.split(",")
    for y in set_list:
      if y.isdigit():
        y= int(y)
      sett__list[counter].add(y)
  

  while True:
    print(f"this is your sets {sett__list}")
    print("choose the type of operation you want to carry out")
    operation = int(input("""
    1. union
    2. intersection
    3. symmetric_difference
    4. isdisjoint
    5. issubset
    6. issupperset
    7. exit the app
    """))

    if operation == 7:
      break
    if operation <7:
      sets_type = int(input("choose your set number e.g 1 : \n"))
      sets_type2 = int(input("choose your second set number e.g 2  : \n"))
      if sets_type != sets_type2:
        if sets_type <= 3 or sets_type2 <= 3:
          if operation == 1:
            calculation = sett__list[sets_type - 1].union( sett__list[sets_type2 - 1])
            print(f" your union set is {calculation}")
          elif operation == 2:
            calculation = sett__list[sets_type - 1].intersection( sett__list[sets_type2 - 1])
            print(f" your intersect set is {calculation}")
          elif operation == 3:
            calculation = sett__list[sets_type - 1].symmetric_difference( sett__list[sets_type2 - 1])
            print(f" your symmetric difference set is {calculation}")
          elif operation == 4:
            calculation = sett__list[sets_type - 1].isdisjoint( sett__list[sets_type2 - 1])
            print(f" result is {calculation}")
          elif operation == 5:
            calculation = sett__list[sets_type - 1].issubset( sett__list[sets_type2 - 1])
            print(f"result is {calculation}")
          elif operation == 6:
            calculation = sett__list[sets_type - 1].issuperset( sett__list[sets_type2 - 1])
            print(f" result is {calculation}")
        else:
          print("your set cannot be greater than 3")
      else:
        print("your set cannot be same")   
    else:
      print("you are out of range of operation options, try again") 
Set()