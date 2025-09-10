print ("Welcome to Manga Recommender! 👌")
print ("(Action, Horror, Sci-fi)")
sel = input("Please select a genre above 😁: ").lower()

print (" How long would you like it to be? 😊 ")
print ("(Short, Medium, Long) ")
time = input(" Please select on how long would the manga be ⌚ : ").lower()

print ("Which Decade? ")
print ("(2000s, 2010s)")
dec = input("Please select from above ⏳ : ").lower()

#Action
if sel == "action":
   if time == "long":
    if dec == "2000s":
      print ("We recommend: Naruto 🍥 ")

   elif time == "short":
     if dec == "2000s":
       print ("Sorry, we don't have anything available. 😥")

   elif time == "medium":
     if dec == "2000s":
       print ("We recommend: Death Note 📘")

   if sel == "action":
     if time == "short":
       if dec == "2010s":
         print ("We recommend: Assasination Classroom 🔫")
   
     elif time == "medium":
       if dec == "2010s":
         print ("We recommend: Kuroko's Basketball 🏀")

     elif time == "long":
       if dec == "2010s":
         print ("We recommend: Attack on Titan ⚔")

#Horror
if sel == "horror":
   if time == "short":
     if dec == "2000s":
       print (" We recommend: Zashiki Onna 👻")

   elif time == "medium":
     if dec == "2000s":
       print ("Sorry, we don't have anything available. 😥")
   
   elif time == "long":
     if dec == "2000s":
       print ("We recommend: Undead 😈")

if sel == "horror":
   if time == "short":
     if dec == "2010s":
       print ("We recommed: Kakukaku Shikajika 😱")
   
   elif time == "medium":
     if dec == "2010s":
       print ("We recommend: Shibito no Koe o Kiku ga Yoi 💀")
   
   elif time == "long":
     if dec == "2010s":
       print ("Sorry, we don't have anything available. 😥")

#Sci-fi
if sel == "sci-fi":
    if time == "short":
      if dec == "2000s":
        print ("We recommend: Noise 🔊") 

    elif time == "medium":
      if dec == "2000s":
        print ("We recommend: Planetes 🌏")  
   
    elif time == "long":
      if dec == "2000s":
        print ("Sorry, we don't have anything available. 😥")

if sel == "sci-fi":
    if time == "short":
      if dec == "2010s":
        print ("We recommend: Moonlight Mile 🌑🌕")
    
    elif time == "medium":
      if dec == "2010s":
        print ("We recommend: Dragon head 🐉")
   
    elif time == "long":
      if dec == "2010s":
        print ("We recommend: MPD Psycho 😵")