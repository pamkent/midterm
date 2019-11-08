#Changed to return true or false
def divisible_by_7(num):
   if num %7 == 0:
      return True 

   return False  

def compare_it(x, y):
#Changed "and" to "or"
   if not isinstance(x, int) or not isinstance(y, int):
      return False
   if x != y:
      return False 
   if x < 0 and y < 0:
      return False
  #Took away else  
   return True

def keyword_counter(word_list, logic, test):
#Replaced "data" with "text" 
   text = test
   if not logic:
      with open(test, "r") as f:
         text = f.read().replace("\n", " ")
   results = {}
   for word in word_list:
      results[word] = text.count(word)
   
   return results

