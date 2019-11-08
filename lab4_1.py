def is_even():
   
   user_data = int(input("Please give me an integer. "))
   out = None
   #Set to true or false instead of print
   if user_data%2 == 0:
      out = True	   
   else:
      out = False

   return out
     
#Reorganized so the conditions execute in correct order
def multi_condition():
   
   user_data = int(input("Please give me an integer. "))

   if user_data < 0:
      print("Negative Nelly!")
   elif user_data == 0:
      print("Don't be such a zero!")
   elif user_data % 2 == 0:
      print("Even Steven!")
   else:
      print("Positively odd!")		  	   	  		  
   
   return None

def is_underage():
   
   user_age = int(input("How old are you?"))
   
   if user_age >= 21:
      print("You may drink, smoke, and drive if you wish!")
    #Got rid of extra code
   elif user_age >= 18:
      print("You may smoke and drive!")
   #Got rid of extra code
   elif user_age >= 16:
      print("You may drive!")
   else:
      print("Enjoy you bike, kid!")
  
   return None

#Replaced original with while loop to make it easier
def countdown():
   
   count = 10
   while count > 0:
      print(count)
      count = count - 1
	   
   return None

def guessing_game(num):
#Added a while loop instead of for loop  
   count = 0
   while count < 10:   
      user_input = int(input("Guess a number between 1 and 20"))
    #Got rid of extra prompt at end 
      if user_input = 'q':
         print("Goodbye, quitter!")
         return None	
	#Added input here to catch integer guesses 	 	  
      user_input = int(user_input):
      if user_input == num:
         print("You win!")
	 win = True 	
      elif user_input > num:
         print("Too high!")
      elif user_input < num: 
         print("Too low!")
      else:
         print("You lose!")   
         win = False
    #Not sure if this should go here, but added to keep track of guesses	  
      count += 1
   
   return None
