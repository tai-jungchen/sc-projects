"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: carry out the boggle game
	"""
	########################################
	word_dic = read_dictionary()    # read dictionary

	# read inputs
	matrix = []
	illegal = False
	for i in range(4):
		row = input(f'{i + 1} row of letters: ').lower()
		matrix.append(row.split(" "))

		# Illegal inputs - more than 4 characters are input
		if len(matrix[i]) != 4:
			print("Illegal input")
			break
		# Illegal inputs - length of character is not 1 or input is not alpha
		for ch in matrix[i]:
			if len(ch) != 1 or not ch.isalpha():
				print("Illegal input")
				illegal = True
				break
		if illegal:
			break
	# boggle!
	ans = []    # a list to collect answers
	start = time.time()
	if not illegal:
		for i in range(4):
			for j in range(4):
				boggle(matrix[i][j], i, j, i, j, matrix, word_dic, ans)
				# print('---------- end of grid search ----------')

		print(f'There are {len(ans)} words in total.')
		# print(ans)
	########################################
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(word, cur_row_idx, cur_col_idx, last_row_idx, last_col_idx, matrix, word_dic, ans):
	"""
	This recursive function search for words using DFS
	:param word: (str) the word to be concatenated
	:param cur_row_idx: (int) the row index of the current stack frame
	:param cur_col_idx: (int) the row index of the current stack frame
	:param last_row_idx: (int) the row index of the last stack frame
	:param last_col_idx: (int) the column index of the last stack frame
	:param matrix: (list) a 2-dim list that contains the inputs
	:param word_dic: (list) the dictionary that contains the valid words
	:param ans: (list) the list to carry the answer found by boggle function
	:return: none
	"""
	# found words (not actually base case)
	if word in word_dic and word not in ans:
		print(f'Found \"{word}\"')
		ans.append(word)
		# for roomy
		boggle(word, cur_row_idx, cur_col_idx, last_row_idx, last_col_idx, matrix, word_dic, ans)
		return

	# recursive step
	for i in range(-1, 2):
		for j in range(-1, 2):
			next_row_idx = cur_row_idx + i
			next_col_idx = cur_col_idx + j
			if (0 <= next_row_idx <= 3) and (0 <= next_col_idx <= 3) and (i != 0 or j != 0) and \
				(next_row_idx != last_row_idx or next_col_idx != last_col_idx):

				next_ch = matrix[next_row_idx][next_col_idx]
				# print(word + next_ch, has_prefix(word + next_ch, word_dic))

				# check if base case occur
				if has_prefix(word + next_ch, word_dic):
					boggle(word + next_ch, next_row_idx, next_col_idx, cur_row_idx, cur_col_idx, matrix, word_dic, ans)
				# base case


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list

	:return (list) A list that contains all the valid words
	"""
	word_dic = []
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= 4:    # read only words that are longer or equal to 4
				word_dic.append(line.strip())
	return word_dic


def has_prefix(sub_s, word_dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param word_dic: (list) A list containing all the valid words
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for words in word_dic:
		if words.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
