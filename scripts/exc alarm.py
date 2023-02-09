import time

# Define a counter and set to five
seconds = 5

# As long as counter is not zero:
while seconds > 0:

    print("tiiiiick")

	# Decrement counter
    seconds = seconds - 1

	# Sleep for one second
    time.sleep(1)


# Make beep sound
print("Beeeeep")
print('\a')







import time

# Define a counter and set to five
counter = 5

# As long as counter is not zero:
while counter != 0:

    print("Tick")
	
	# Decrement counter
    counter = counter - 1

    # Sleep for one second
    time.sleep(1)


# Make beep sound
print("Beep")
print('\a')