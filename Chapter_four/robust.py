# ==============================================================================
#                ADVANCED DEFENSIVE LOOPS & CLEANUP
# ==============================================================================

print("--- Step 1: The Infinite Validation Loop ---")

while True:
    try:
        # Ask for gym weights (must be an integer)
        bench_press = int(input("Enter your Max Bench Press weight (kg): "))
        
        # If the conversion succeeds, we break out of the infinite loop!
        print(f" Lift locked in at: {bench_press} kg\n")
        break
        
    except ValueError:
        # If they type 'abc' or strings, the loop triggers again instead of crashing!
        print("Invalid input! Please type a clean, raw number (e.g., 60, 75). Try again.\n")


print("--- Step 2: The 'finally' Resource Safeguard ---")

try:
    print("Opening active data channel stream...")
    # Simulating data operations
    data_stream = open("runtime_log.txt", "w")
    
    # Intentionally trigger a crash inside the stream to test the safeguard
    division_test = 10 / 0 
    
    data_stream.write("This line will never execute due to the crash.")

except ZeroDivisionError:
    print(" Caught a math exception mid-stream!")

finally:
    # This block ALWAYS runs, regardless of whether a crash occurred or not!
    # Essential for cleaning up system memory and saving open file channels.
    data_stream.close()
    print("File system resources safely closed and flushed via 'finally' block.")

print("\nChapter 5 Finalized: Your code is now fully armored.")