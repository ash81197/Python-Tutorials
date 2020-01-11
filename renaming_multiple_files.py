# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os

# Function to rename multiple files 
def main():

	for i in range(0,10):
		for filename in os.listdir("."):
			if filename.startswith(str(i)):
				os.rename(filename, filename[4:])
	while(filename.startswith(' ')):
		for filename in os.listdir("."):
			if filename.startswith(' '):
				os.rename(filename, filename[1:])
		
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main()
