# ==============================================================================
#                STRUCTURED DATA INTERCHANGE (JSON)
# ==============================================================================
"""
INTRODUCTION TO JSON HANDLING IN PYTHON
--------------------------------------------------------------------------------
JSON (JavaScript Object Notation) is a lightweight, text-based standard format
used universally to store and exchange structured data across web APIs.

Unlike raw text files (.txt) which can only write flat strings, JSON allows 
Python to save complex data topologies—like nested dictionaries and lists—
directly to the system disk without losing their semantic datatype structures.

CORE MECHANICS:
1. SERIALIZATION (Dumping / Writing):
   Converting a live memory-allocated Python object (dict, list) into a flat, 
   system-agnostic text string format using `json.dump()`.

2. DESERIALIZATION (Loading / Reading):
   Parsing a structured JSON text stream from disk back into a live, native, 
   mutable Python data object using `json.load()`.
"""

import json

# ------------------------------------------------------------------------------
# STEP 1: INITIALIZE NATIVE PYTHON COMPONENT MATRIX
# ------------------------------------------------------------------------------
# Creating a complex, multi-layered dictionary representing an entity footprint
user_profile = {
    "username" : "Michael Faraday",
    "age" : 19,
    "location" : "Europa",
    "daily_activities" : {
        "gym" : "2 hours",
        "guitar" : "15 minutes",
        "git commits" : 1,
    },
    "completed_chapters" : ["Chapter_one", "Chapter_two", "Chapter_three"]
}

# ------------------------------------------------------------------------------
# STEP 2: SERIALIZATION (DUMPING OBJECTS TO HARD STORAGE)
# ------------------------------------------------------------------------------
print("--- Step 1: Serializing Data (Dumping Data to File) ---")

# We open a dedicated data file pointer under write mode ('w')
with open("profile_data.json", "w") as json_file:
    # json.dump(object_to_save, file_pointer, indent=number_of_spaces)
    # The 'indent' argument breaks down the raw buffer array into human-readable steps
    json.dump(user_profile, json_file, indent=4)

print("Saved! 'profile_data.json' database footprint generated successfully.\n")

# ------------------------------------------------------------------------------
# STEP 3: DESERIALIZATION (RECONSTRUCTING TEXT STREAM INTO LIVE MEMORY)
# ------------------------------------------------------------------------------
print("--- Step 2: Deserializing Data (Loading into Python) ---")

# Open the physical file channel under explicit read mode ('r')
with open("profile_data.json", "r") as json_file:
    # json.load reads the textual layout and reallocates memory pointers as a dict
    loaded_data = json.load(json_file)

# ------------------------------------------------------------------------------
# STEP 4: DATA VALIDATION & EXTRACTION VERIFICATION
# ------------------------------------------------------------------------------
print(f"Successfully loaded profile for: {loaded_data['username']}")
print(f"Gym Check-in:                     {loaded_data['daily_activities']['gym']}")
print(f"Data type verification:          {type(loaded_data)}")  # Confirms native <class 'dict'>
