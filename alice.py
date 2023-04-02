filename = 'alice.txt'
file_path = '/Users/abrun/Documents/python_work/text_files/' + filename

try:
	with open(file_path, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.")
else:
	# Count the approximate number of words in the file.
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words.")