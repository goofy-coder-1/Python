# ====================================================
#                A R G S 
# ====================================================

# Using *args (Unlimited Positional Arguments)
# The single asterisk '*' tells Python to grab ALL incoming numbers 
# and pack them neatly into a single Tuple named 'numbers'.

# Example first
def calculateWeights(*weights):
    total = 0
    for weight in weights:
        total += weight

    return f"The total weight is {total} kg"

print(calculateWeights(12, 55, 60))

# Example second

def usersongs(username, *songs):
    print(f"======= {username}'s playlist ========")

    for song in songs:
        print(song)

usersongs("Julius", "Brazilian phonk 101", "Bound 2", "Walking back home")
usersongs("Alexander", "yabadabadoo", "country roads")