2

print('''
                 ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----.....___
           \               ""/
      ~^~^~^~^~^`~^~^`^~^~^`^~^~^
       ~^~^~`~~^~^`~^~^~`~~^~^~
''')
print ("Welcome to this weird game. You are on a small sailboat.")
print ("Your mission is to finish the game. Unlock all 7 of the multiple endings because why not?\n\n")
print ("You find yourself on a boat in the middle of the ocean. There's a steady tailwind pushing you along. What would you like to do?")
print ("\t1. Chop down the mast.\n\t2. Keep sailing.")
print ("(Choose '1' or '2')")
choice = input()
if choice == '1':
  print ("You chose: '1. Chop down the mast.'")
  print ("\nYou chop down the boat's mast and get a small bonfire going. In a short while, it will turn into a raging blaze that will render the flammable wooden boat incapable of floating. What would you like to do?")
  print ("\t1. Beat your chest and scream at the top of your lungs.\n\t2. Dive into the sea to escape the fire.'")
  print ("(Choose '1' or '2')")
  choice = input()
  if choice == '1':
    print ("You chose: \'1. Beat your chest and scream at the top of your lungs.'")
    print ("\nYou make a ruckus by grabbing and throwing around anything you can get your hands on. As the boat slowly tilts to one side and starts to fill with seawater, you stand at the edge of the bow and scream to the point of being hoarse, \"LIFE IS SO UNFAIR!! WHY IS LIFE SO DIFFICULT!!??\"\n\nWith a loud snap, one of the wooden plank snaps, and a little piece of wood flies directly into your gaping mouth. As you choke on the piece of wood and sink to the bottom of the sea, the glimmering sun slowly fades from the water surface as gradually as your consciousness does.\n\nGame Over, GENIUS.")
  elif choice == '2':
    print ("You chose: '2. Dive into the sea to escape the fire.'")
    print ("\nYou come to your senses and jump into the sea to escape the raging fire. You wade in the water watching your charred boat disappear under the waves. You hold on as long as you could trying to stay afloat in the middle of the blue wet wilderness. Alas, humans were not meant to live perpetually submerged in liquid. Fresh or saltwater. You try your best but even an experienced athlete could not fight the painful involuntary contraction of muscles that characterize muscle cramps. \n\nAs memories flash by your eyes, you have the most powerful insight you ever had: it's the brain that requires the most exercise, because obviously you have not had enough growing up.\n\nGame Over, Bubble Brain.")
  else:
    print ("You chose: Neither 1 nor 2.")
    print ("\nYou freeze in shock as if your brain stopped functioning. The now tilting boat makes your body lose balance and it falls into the fire you made. Your non-sentient vessel becomes fuel for the fire and as the cells are destroyed, your vision goes black like a screen turned abruptly off.\n\nYour consciousness wanders endlessly in the void of nothingness. Intuitively, you just know that the afterlife simply cannot accept substandard intelligences like yourself. Which is a funny thing if you think about it, since you wouldn't show up on any intelligence scale at all.\n\nGame Over, you blip-blop.")
elif choice == '2':
  print ("You chose: '2. Keep sailing.'")
  print ("\nYou man the sails to keep the boat steadily going in one general direction. Nothing eventful happens as you keep going. Finally, on the horizon, what appears to be a coastal town is within sight. You steer the boat towards it and you finally are within the whole view of the town of 'Maybaybay' (By the Bay). An up and coming trading town. Its strategic placement as a busy port makes it home to many skillful artisans and scholars. You can choose to moor the boat in one of the many available piers of the harbor. You can go to a few other places after that. Where would you want to go next?")
  print ("\t- Town Hall\n\t- Home\n\t- Tavern")
  print ("(Type any of the destinations. Careful with typos.)")
  choice = input().lower()

  if choice == 'town hall':
    print (f"You chose: 'Town Hall'")
    print("\nYou make the decision to visit the Town Hall. For some reason, you figured that confronting the mayor is a good idea. Just thinking about him and his round pudgy face, balding with hairs on the side of the head, the round spectacles and the bushy moustache makes you furious. You feel like getting up there and giving him a piece of your mind.\n\nYou trudged up the hill that leads to the center of town. It's a high and tiring climb. No wonder the people who live up here win the annual race competitions. They get great exercise everyday going up and down the hill to go to school, the market, or the harbor and then back home. As you cross the gates of the Town Hall, you are no longer in a good mood. You are hungry, tired, and sticky from all that salty air. How fortunate, the mayor is by the entrance of the public park, it seems they are conducting an opening ceremony for the park this late in the afternoon. While the public works councilor delivers a speech, you push past the crowd to get closer to the front. \"Ouch!\" \"Excuse me!\" \"What the-\" Many people complain as you push them all aside to get through. You finally reach the front, the kind mayor 10 meters away from you. In a huge burst of energy, you make a powerful dash towards the mayor, and with a running leap throw your whole body into him. You both fall into the ground, the mayor's glasses fly to who knows where. You scream, \"HAAIIYAAAA!!\" as you bite down hard into his balding head, leaving a mark. The whole crowd comes upon you to pull you off the old man. Chaos ensues as everyone tries to enact vengeance for the mayor. As order is restored by the police sergeant, the mayor comes up to you with a band-aid on his head, saying, \"We have no idea what just came to you, but I suppose we'll have to detain you until we figure out what's wrong.\"\n\nYou spend the night in prison muttering things like, \"I hate your bald head\" or \"I'll burn that silly moustache\" You would never again recover from this strange insanity.\n\nGame Over, weirdo.")
  elif choice == 'home':
    print (f"You chose: 'Home'")
    print ("\nYou walk on familiar roads and cut routes on memorized paths. Even without the moon's soft glow illuminating the town, your feet can carry you home by memory. A turn into a quiet street leads you a few hundred meters from your house. Dogs can be heard barking in the distance. Two cats chasing each other cross the street in front of you. They dive into the bushes by the road and as you pass by, you see two pairs of glowing gems watching you. One of them pounces the other and they begin to tussle again. Laughter and the tinkling of utensils on plates can be heard from the open-windowed houses. As you enter your front yard, the smell of flowers greets you, followed by the smell of cured beef floating from the open front door. Smells like tapsilog (beef with egg) is for dinner. Home. Home sweet home.\n\nGame Over! You Win! Or something! Whatever!")
    print("\n")
  elif choice == 'tavern':
    print ("You chose: 'Tavern'")
    print("\nAh... The Tavern. The perfect place to visit for any adventurous traveller. You visit the most famous tavern in Maybaybay, 'Ang Galising Kuting' (The Mangy Kitten). You order a flagon of their finest drink. And another. And yet another. Soon you must have had been able to drink enough for three people. The inn keeper confronts you if you even had the coin to pay for all that luxurious imported wine. Your response of vomiting onto the good innkeeper educated everyone how he earned the moniker Makalangit (Heavenly). It was not because he was a religious man but because he sent people to heaven early. Seems like heaven has a new applicant.\n\nGame Over, buddy.")
  else:
    print (f"You chose: '{choice}', or none of the three available options.")
    print ("\nYou freeze as if your brain stopped functioning. You hold onto the sails and leave the boat moving forward onto a collision course with one of the larger trading ships. The watchwoman on the boat warns you from faraway to correct your course as the larger ship cannot make sharp turns as your small boat can. Her requests, commands and soon shouts catch the attention of her other crewmates. In unison, they all begin to gesture frantically with their hands for you to correct your course. Some of them are waving their hands and some are even cursing your deaf ears. Seconds before you ram into their prow, someone shouts in anticipation, \"Impact!\" A cacophony of splintering and cracking wood can be heard as the trade ship drives right into your tiny boat. \"Gods above!\" A sailor shouts as your pretty little boat was turned into flotsam in an instant. They helplessly watch the bits and pieces brush the side of their boat.\nYour non-sentient body is still clutching hard onto the sail's steering stick which is still attached to half of the boat's mast. The wood parts are floating on the water, only your body's hand is visible from the surface. Your critically injured body floats just below. Did I say critically injured? Sorry, I meant lifeless body.\n\nGame Over, you ding dong.")
  
else:
    print (f"You chose: '{choice}', or none of the two available options.")
    print ("\nYou just stand there on the boat with a blank, dead stare on the horizon. The boat aimlessly drives towards wherever the wind steers the sail. You stand eerily without moving for hours. As the time goes by, a titanic figure passes around 50 meters to port. Its size was so gigantic that the wake was easily taller than your boat. As the wave from the passing of the creature comes closer, you still reactionlessly stand on the deck of your little boat. Even the danger of being tipped over does not wake you from your strange behavior. In one quick moment, you were thrown overboard and into the sea. Fortunately, you landed in just the correct position to still float on the surface. Floating aimlessly like you were a mannequin. As you stare into the now darkening sky, the sound of some huge sea vessel can be heard coming closer. As the sound comes closer and closer to just beside you, it seems it was a huge cave that was making the noise. The water around you gets sucked into it and darkness engulfs you. You were supposed to come home for dinner, but it seems you ended up as someone else's dinner in their home.\n\nGame Over, you ding-a-ling.")