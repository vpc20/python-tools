import time

for i in range(11):
    # The \r moves the cursor to the start of the line.
    # The end='\r' prevents a newline from being added, keeping the cursor on the same line.
    print(f"Progress: {i*10}%", end='\r')
    time.sleep(0.5)

# Print a final newline character to move to the next line after the loop finishes
print()
