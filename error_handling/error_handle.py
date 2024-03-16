# Open the file 'youtube.txt' in write mode. If the file does not exist, it will be created.
file = open('youtube.txt', 'w')

try:
    # Write the string 'Chai aur code' to the file.
    file.write('Chai aur code')
finally:
    # Ensure the file is closed properly even if an error occurs.
    file.close()

# Open the file 'youtube.txt' in write mode using the 'with' statement. 
# The 'with' statement ensures that the file is properly closed after it is no longer needed.
with open('youtube.txt', 'w') as file:
    # Write the string 'Chai aur python' to the file.
    file.write('Chai aur python')
