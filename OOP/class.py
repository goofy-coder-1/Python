# ==============================================================================
#                          C L A S S E S  &  O B J E C T S
# ==============================================================================

# A class is a blueprint (template) for creating objects.
# An object is a real-world instance built from that blueprint.
# Inside a class, we use '__init__' (the constructor) to initialize data fields,
# and functions inside a class are called 'methods'.

# 1. Defining the Blueprint (The Class Structure)
class Character:
    # The Constructor: Automatically runs when a new object is created.
    # 'self' refers to the specific object we are creating right now.
    def __init__(self, name, character_type, health_points):
        self.name = name                 # Object Attribute (Data)
        self.type = character_type       # Object Attribute (Data)
        self.hp = int(health_points)     # Object Attribute (Data)

    # A Method: A function belonging to the object that performs an action.
    def display_status(self):
        print(f"\n--- Matrix Telemetry: {self.name} ---")
        print(f"Class Type: {self.type}")
        print(f"Health Pool: {self.hp} HP")
        if self.hp > 50:
            print("Status: Combat Ready")
        else:
            print("Status: Warning - Critical Vitals")


# 2. Instantiating Objects (Creating instances from the blueprint)
print("--- Creating Objects from the Class Blueprint ---")

# create two distinct objects using the same single template
player_one = Character("Zoro", "Swordsman", 100)
player_two = Character("Luffy", "Captain", 45)


# 3. Executing Object Methods (Invoking actions)
# Each object carries its own unique data bundle independent of the other.
player_one.display_status()
player_two.display_status()


# 4. Dynamic Object Generation (Using interactive user input)
print("\n--- Generate Your Own Custom Class Object ---")
user_name = input("Enter character name: ")
user_type = input("Enter character class type (e.g., Mage, Rogue): ")
user_hp = input("Enter starting health points: ")

# Building the object using the user's terminal arguments
custom_player = Character(user_name, user_type, user_hp)

# Running the status check on your custom entity
custom_player.display_status()