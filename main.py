from langdetect import detect
from sys import argv
from sys import stdin

low = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

poss_languages = ["en", "de"]

# overview of script usage
def usage():
	print("Usage: python3 %s options \"text\"\n" % argv[0])
	print("Options:\n-s <int>\tShift the supplied text by given offset.")
	print("-r <int>\tRevert shift by given offset.")
	print("-f <filename>\tLoad text from file.")
	print("-d\t\tDetect offset of shifted text using word detection.")
	print("-i\t\tRead text from STDIN.")
	print("-l <en,de,fr>\t\tSupply possible languages of original.")
	exit()

# shift characters in string by offset
def shift(msg: str, offset: int):
	result = ""
	for c in msg:
		if low.__contains__(c):
			list = low
		elif up.__contains__(c):
			list = up
		else:
			result += c
			continue
		i = list.index(c) + offset
		while i > 25:
			i -= 26
		while i < -26:
			i += 26
		result += list[i]

	return result


# like shift, but negated offset
def unshift(msg, offset):
	return shift(msg, offset*-1)


def getOffset2(data):
	for i in range(8):
		print(i, unshift(data, i)[:50])


def getOffset(data: str, langs):
	print(langs)
	og = data
	poss_offset = (0, 0) # offset and detected words
	for i in range(1, 26):
		data = unshift(og, i)
		dic = {}
		for sen in data.split("."):
			for word in sen.replace(",", "").replace("\n", "").split(" "):
				if len(word) > 1:	
					try:
						lan = detect(word)
						dic[lan] += 1
					except KeyError:
						dic[lan] = 1
					except Exception as e:
						pass

		for k in dic:
			if langs.__contains__(k) and poss_offset[1] < dic[k]:
				poss_offset = (i, dic[k])
				print("Possible offset of %i with %i words detected in %s." % (i, dic[k], k))
			else:
				continue

	print(unshift(og, poss_offset[0]))
			

	# print(unshift(og, poss_offset[0]))


def main():

	if argv.__contains__("-l"):
		new_langs = argv[argv.index("-l") + 1]
		poss_languages = new_langs.split(",")

	if argv.__contains__("-f"):
		try:
			data = open(argv[argv.index("-f")+1], "r").read()
		except FileNotFoundError:
			usage()
	elif argv.__contains__("-i"):
		data = stdin.readline()
	else:
		data = argv[-1]

	try:
		if argv.__contains__("-d"):
			getOffset(data, poss_languages)
		elif argv.__contains__("-s"):	
			print(shift(data, int(argv[argv.index("-s")+1])))
		elif argv.__contains__("-r"):
			print(unshift(data, int(argv[argv.index("-r")+1])))
		else:
			usage()
	except Exception as e:
		print(e)
		usage()

main()
