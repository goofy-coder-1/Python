# =======================================
#     L O O T B O X
# =======================================

# A fun program to find out the details of user

players = {
    "userone" : {
          "name" : "Julius Caesar",
          "survival_time" : "15 minutes",
          "character_ability" : "Philosopher",
          "lootbox" : ("Knife", "arabian_alcohol", "Book of wisdom")
       },
       "usertwo" : {
          "name" : "Alexander",
          "survival_time" : "25 minutes",
          "character_ability" : "Conqueror",
          "lootbox" : ("Divine Sword", "Immortal Poison", "Loyal Servants")
       },
       "userthree" : {
          "name" : "Prithvi Narayan",
          "survival_time" : "9 minutes",
          "character_ability" : "Wrangler",
          "lootbox" : ("Khukuri", "Pride Dhaka", "Fear Factor : +2")
       },
       "userfour" : {
          "name" : "Shakespeare",
          "survival_time" : "7 minutes",
          "character_ability" : "Artist",
          "lootbox" : ("Prime Megan Fox's Portrait", "Big Brush", "something unknown")
       },
       "userfive" : {
          "name" : "Freddie",
          "survival_time" : "5 minutes",
          "character_ability" : "singer",
          "lootbox" : ("Guitar", "arabian_alcohol", "Guild Pass")
       },
       "usersix" : {
          "name" : "Mbappe",
          "survival_time" : "12 minutes",
          "character_ability" : "Dictator",
          "lootbox" : ("Football", "Player Contracts", "Fear Factor: +100")
       }
}

print("Want all player data or for specific person")
operation = input("Enter 'A' for All and 'S' for specific: ")

match operation:

   case 'A':

      #  Loop through the main dictionary
      for username, player_data in players.items():
            print(f"\n=================== {username.upper()} PROFILE ===================")
         
            #  Loop through the inner profile dictionary
            for stat_name, stat_value in player_data.items():
            # Cleanly display the lootbox items if it encounters the tuple
             if stat_name == "lootbox":
                  print(f"Lootbox Items: {', '.join(stat_value)}")
             else:
                  print(f"{stat_name.replace('_', ' ').title()}: {stat_value}")
   
   case 'S':
         
      name = input("Enter name of the player: ")
      found = False

      #  Loop through the main dictionary
      for username, player_data in players.items():
         if name.lower() in player_data['name'].lower():
            found = True
            print(f"\n=================== {username.upper()} PROFILE ===================")
         
            #  Loop through the inner profile dictionary
            for stat_name, stat_value in player_data.items():
            # Cleanly display the lootbox items if it encounters the tuple
             if stat_name == "lootbox":
                  print(f"Lootbox Items: {', '.join(stat_value)}")
             else:
                  print(f"{stat_name.replace('_', ' ').title()}: {stat_value}")
      # if the name of specific person is not found
      if not found:
         print("========= Player Not Found ==============")