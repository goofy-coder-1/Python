# ==============================================================================
#                  RPG INVENTORY & ENCUMBRANCE MANAGER
# ==============================================================================

# declare lootbox catalogue and also add items
lootbox_catalog = {
    "userone" : {
        "name" : "Dr Driver",
        "Inventory" : {
            "Steering Wheel" : 15,
            "Pliers" : 33,
            "divine accelerator" : 4
        }
    },
    "usertwo" : {
        "name" : "Chef Gordon",
        "Inventory" : {
            "Iron Skillet" : 12,
            "Chef Knife" : 4,
            "Raw Lamb Sauce" : 1
        }
    },
    "userthree" : {
        "name" : "Cyber Hacker",
        "Inventory" : {
            "Overclocked Deck" : 5,
            "Decrypted Drive" : 2,
            "Liquid Nitrogen" : 8
        }
    },
    "userfour" : {
        "name" : "Mountain Guide",
        "Inventory" : {
            "Climbing Rope" : 14,
            "Oxygen Tank" : 20,
            "Khukuri Knife" : 6
        }
    },
    "userfive" : {
        "name" : "The Illusionist",
        "Inventory" : {
            "Smoke Bomb" : 3,
            "Enchanted Deck" : 2,
            "Trick Mirror" : 11
        }
    },
    "usersix" : {
        "name" : "Mechanic Mike",
        "Inventory" : {
            "Hydraulic Jack" : 25,
            "Impact Wrench" : 9,
            "WD-40 Spray" : 2
        }
    },
    "userseven" : {
        "name" : "Time Traveler",
        "Inventory" : {
            "Broken Dial" : 7,
            "Paradox Battery" : 18,
            "Futuristic Relic" : 5
        }
    },
    "usereight" : {
        "name" : "Deep Diver",
        "Inventory" : {
            "Harpoon Gun" : 16,
            "Heavy Helmet" : 22,
            "Glowing Coral" : 3
        }
    },
    "usernine" : {
        "name" : "Street Artist",
        "Inventory" : {
            "Spray Can Set" : 10,
            "Gas Mask" : 4,
            "Masterpiece Sketch" : 1
        }
    },
    "userten" : {
        "name" : "Corporate Baron",
        "Inventory" : {
            "Golden Pen" : 2,
            "Titanium Briefcase" : 15,
            "Bribe Ledger" : 5
        }
    }
}

player_inventory = []
current_weight = 0
max_weight = 50

while True:
    print("\n=====================================")
    print("      HERO INVENTORY MANAGER         ")
    print("=====================================")
    print(f"Weight Load: {current_weight:.1f} / {max_weight:.1f} kg")
    print("-------------------------------------")
    print("[V] View Inventory | [L] Loot New Item")
    print("[D] Drop Carried   | [E] Exit Game")
    print("=====================================")

    choice = input("Enter the operation: ").upper().strip()

    match choice:
        case 'V':
            print("\n--- CARRIED BACKPACK INVENTORY ---")
            if len(player_inventory) == 0:
                print("Your backpack is completely empty.")
            else:
                # Use enumerate to give items a tracking number for dropping later
                for idx, item in enumerate(player_inventory, start=1):
                    print(f"[{idx}] {item['name']} ({item['weight']} kg)")
            print("-------------------------------------")

        case 'L':
            print("\n--- SELECT A CHARACTER ARCHETYPE TO LOOT ---")
            # Create a temporary lookup dictionary to match numbers to user keys
            mapping = {}
            for i, (username, profile) in enumerate(lootbox_catalog.items(), start=1):
                print(f"[{i}] {profile['name']}")
                mapping[i] = username
                
            try:
                char_choice = int(input("\nSelect character index number (1-10): "))
                if char_choice not in mapping:
                    print("[-] Selection Error: Character index out of bounds.")
                    continue
                
                # Extract the selected character's nested profile data
                selected_user_key = mapping[char_choice]
                character = lootbox_catalog[selected_user_key]
                
                print(f"\nItems found inside {character['name']}'s cache:")
                item_options = list(character["Inventory"].items()) # List of tuples: [("item", weight), ...]
                
                for idx, (item_name, weight) in enumerate(item_options, start=1):
                    print(f"  [{idx}] {item_name} ({weight} kg)")
                    
                item_choice = int(input(f"\nSelect item index to loot (1-{len(item_options)}): "))
                if item_choice < 1 or item_choice > len(item_options):
                    print("[-] Selection Error: Item index out of bounds.")
                    continue
                    
                # Target the item name and its weight factor
                target_item_name, target_item_weight = item_options[item_choice - 1]
                
                # CRITICAL ENCUMBRANCE CHECK ENGINE
                if current_weight + target_item_weight > max_weight:
                    print("\n=============================================")
                    print("OVERENCUMBERED! Action refused by engine. ")
                    print(f"Adding this item exceeds maximum limit by {(current_weight + target_item_weight) - max_weight:.1f} kg.")
                    print("=============================================")
                else:
                    # Append item block to backpack list
                    player_inventory.append({"name": target_item_name, "weight": target_item_weight})
                    current_weight += target_item_weight
                    print(f"Success: Stowed '{target_item_name}' into backpack!")
                    
            except ValueError:
                print("[-] Input Error: Enter a raw single digit index.")

        case 'D':
            print("\n--- DROP CARRIED INVENTORY ITEM ---")
            if len(player_inventory) == 0:
                print("Notice: No items inside backpack available to drop.")
                continue
                
            # Reprint inventory block so user sees valid line indexes
            for idx, item in enumerate(player_inventory, start=1):
                print(f"[{idx}] {item['name']} ({item['weight']} kg)")
                
            try:
                drop_idx = int(input(f"\nEnter item number to drop (1-{len(player_inventory)}): "))
                if drop_idx < 1 or drop_idx > len(player_inventory):
                    print("[-] Execution Error: Index key out of range.")
                    continue
                
                # Extract and drop item entirely out of memory array list
                removed_item = player_inventory.pop(drop_idx - 1)
                current_weight -= removed_item["weight"]
                print(f"Success: Abandoned '{removed_item['name']}' on the ground. Freed {removed_item['weight']} kg.")
                
            except ValueError:
                print("[-] Input Error: Enter a raw valid numerical index number.")

        case 'E':
            print("\nShutting down engine matrix loops. Inventory state cleared!")
            break
            
        case _:
            print("[-] Error: Operational option index unrecognized.")