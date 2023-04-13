with open("header.txt","r") as f:
   data = f.readlines()
   for item in data:
      one,two = item.split(": ")
      print(f'"{one}":"{two.strip()}",')