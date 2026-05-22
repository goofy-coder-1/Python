# ==================================
#     F I L E  H A N D L I N G
# ==================================

# writing data (overwrites existing contents)
print("------ Writing Files --------")

with open("user_log.txt", "w") as file:
    file.write("User: John Cena\n")
    file.write("Status: Not seen\n")

print("File 'user_log.txt' created and to successfully")

# Reading Data
print("\n--- Reading File ---")

with open("user_log.txt", "r") as file:
    content = file.read()
    print("Contents of user_log.txt: ")
    print(content)

# Append Mode
# This allows you to add new data on file without overwriting previous datas

print("\n-------Appending Data----------\n")

with open("user_log.txt", "a") as file:
    file.write("User: Tony Adams\n")
    file.write("Status: Seen\n")

print("New logs appended safely!")

print("\n--- Final File Check ---")
with open("user_log.txt", "r") as file:
    print(file.read())