#-------------------------------------------------------------------------------
# Credit card verification program
# Criteria: 
#	1. First number must be 4, 5 or 6
#	2. Must contain exactly 16 digits 
#	3. May have characyers but not other than "-" and seperated by 4 numbers
#	4. Consecutive 4 numbers must not be same 
#-------------------------------------------------------------------------------

#--function to calculate consecutive 4 identical--
def Identical4(number):
    for i in range(0,len(number)-3): 
        if number[i]==number[i+1]:
           if number[i+1]==number[i+2]:
              if number[i+2]==number[i+3]:
                 return 0
    return 1


#--function to varify the card-- 
def Varify(card_number):
 #--condition 1--                 
 if card_number[0]!='4' and card_number[0]!='5' and card_number[0]!='6':
   print(card_number+": invalid1")
 #--check for the digit--
 elif card_number.isdigit()==False:                    #--if number contains characters-
   if card_number.find("-")>0:                         #--only '-' is allowed 
      if card_number.count('-')==3:                    #--check for number of occurances
         if card_number[4]=='-' and card_number[9]=='-' and card_number[14]=='-': 
            card_number = card_number.replace("-","")  #--remove the '-' character from the card number 
            if Identical4(card_number)==0:             #--check for the consecutive 4 occurances
               print(card_number+": invalid2").         
            else:
               print(card_number+": valid1") 
         else:
            print(card_number+": invalid3")
      else:
         print(card_number+": invalid4")
   else:
      print(card_number+": invalid5")
 else:                                                 #--card first number is 4/5/6
   if len(card_number)!=16:                            #--check the card number lenght
      print(card_number+": invalid6")
   elif Identical4(card_number)==0:                    #--check for the consecutive 4 occurances
      print(card_number+": invalid7")
   else: 
      print(card_number+": valid2")


#--Sample input--
Varify("4123456789123456")
Varify("5123-4567-8912-3456")
Varify("61234-567-8912-3456")
Varify("4123356789123456")
Varify("5133-3367-8912-3456")
Varify("5123 - 3567 - 8912 - 3456")
