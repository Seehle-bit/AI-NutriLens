print("=======================================")
print("             NUTRILENS")
print("           MEAL ANALYSIS")
print("=======================================")

food_data = {"chicken":{"calories": 165,
                        "protein": 31,
                        "fat": 3.0,
                        "carbs": 0
                        }, 
            "egg": {"calories": 78,
                    "protein": 6.3,
                     "fat": 5.3,
                     "carbs": 0.6
                     },
            "banana":{"calories": 89,
                      "protein": 1.1,
                       "fat": 0.3,
                       "carbs": 22.8
                              },
            "avocado":{"calories": 160,
                       "protein": 2,
                       "fat": 14.7,
                       "carbs": 8.5
                    }
                        }
food = input("what did you consumed?").lower()
amount = float(input("How many grams did you consume? "))

if food in food_data:
    nutrition = food_data[food]
    factor = amount / 100

    calories = nutrition["calories"] * factor
    protein = nutrition["protein"] * factor
    fat = nutrition["fat"] * factor
    carbs = nutrition["carbs"] * factor

    print("==============================================================")
    print("                NUTRITION INFORMATION")
    print("==============================================================")
    print("Calories", calories, "kcal")
    print("Protein:", protein, "g")
    print("Fat:", fat, "g")
    print("Carbohydrates:" ,carbs, "g")


    if  protein >= 20:
       print("Analysis: This portion provides a high amount of protein.")
    else: 
       print("Analysis: This portion provides a lower amount of protein.")
    if fat >= 15:
       print("Fat analysis: This portion contains a high amount of fat.")
    else:
       print("Fat analysis: This portion contains a lower amount of fat")
    if carbs >= 30:
        print("Carbohydrates analysis: This portion contains a high amount of carbohydrates.")
    else:
        print("Carbohydrates analysis: This portion contains a lower amount of carbohydrates.")
    if calories >= 500:
        print("Calorie analysis: This portion contains a high amount of calories.")
    else:
        print("Calorie analysis: This portion contains a lower amount of calories.")

else: 
 print("Sorry, i dont have the nutrition information for that food yet.")

another_food = "yes"
while another_food.lower() == "yes":
  another_food = input("Did you consume another food? yes/no: ")
  if another_food.lower() == "yes":
    current_food = input("What else did you consume? ").lower()
    if current_food in food_data:
       print("Great! I have nutrition information for", current_food)
    current_amount = float(input("How many grams did you consume? "))
    current_nutrition = food_data[current_food]
    current_factor = current_amount / 100

    current_calories = current_nutrition["calories"] * current_factor
    current_protein = current_nutrition["protein"] * current_factor
    current_fat = current_nutrition["fat"] * current_factor
    current_carbs = current_nutrition["carbs"] * current_factor

    total_calories = calories
    total_protein = protein
    total_fat = fat
    total_carbs = carbs
    total_calories = total_calories + current_calories
    total_protein = total_protein + current_protein
    total_fat = total_fat + current_fat
    total_carbs = total_carbs + current_carbs
    print("Second Food Nutrition")
    print("Calories:", current_calories, "kcal")
    print("Protein:", current_protein, "g")
    print("Fat:", current_fat, "g")
    print("Carbohydrates:", current_carbs, "g")



if another_food.lower() == "yes":
   current_food = input("What else did you consume? ").lower()

   if current_food in food_data:
     print("Great! I have a nutrion information for", current_food)
     second_amount = float(input("How many grams did you consume? "))
     current_nutrition = food_data[current_food]
     current_factor = second_amount / 100

     current_calories = current_nutrition["calories"] * current_factor
     current_protein = current_nutrition["protein"] * current_factor
     current_fat = current_nutrition["fat"] * current_factor
     current_carbs = current_nutrition["carbs"] * current_factor

   print("Second food nutrition:")
   print("calories:", current_calories, "kcal")
   print("Protein:",current_protein, "g")
     
   print("Fat:", current_fat, "g")
   print("Carbohydrates:", current_carbs, "g")
   total_calories = calories + current_calories
   total_protein = protein + current_protein
   total_fat = fat + current_fat
   total_carbs = carbs + current_carbs
       
   print("=========================================================================")
   print("                           TOTAL MEAL")
   print("=========================================================================")
    
      
   print("Total calories:", total_calories, "kcal")
   print("Total protein:", total_protein, "g")
     
   print("Total fat:", total_fat, "g")
   print("Total Carbohydrates:", total_carbs, "g")
   print("=========================================================================")
   print("                         MEAL ANALYSIS")
    print("=========================================================================")
      if total_protein >= 40:
       print ("Meal analysis: This meal provides a high amount of protein.")
      else:
        print("Meal analysis: This meal provides lower amount of protein.")
      if total_fat >= 30:
        print("Meal analysis: This meal contains a high amount of fat.")
      else:
        print("Meal Analysis: This meal contains a lower amount of fat.")
      if total_carbs >= 60:
        print("Meal analysis: This meal contains a high amount of carbohydrates.")
      else:
        print("Meal analysis: This meal contains a lower amount of carbohydrates.")
      if total_calories >= 800:
        print("Meal analysis: This meal contains a high amount of calories.")
      else:
        print("Meal analysis: This meal contains a lower amount of colories.")
        print(" ")
        print("=========================================================================")
        print("                      END OF MEAL ANALYSIS")
        print("=========================================================================")
   else:
   print("Sorry, I dont have nutrition for that food yet.")
else:
print("Meal analysis complete.")