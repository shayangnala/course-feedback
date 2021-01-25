import csv
import argparse

# This file transforms the entries in the input file to generate and output new entries
# that each contains (one keyword, course, term, feedback)

# IMPORTANT: The input csv file should contain comman deliminited columns in the following order:
# [0] 课程
# [1] 学期
# [2] 全文
# [3] 种类关键词
# [4] 内容关键词


parser = argparse.ArgumentParser(description="Transform the feedback entries from the input file and write the result to two different keyword files")
parser.add_argument("--inputfile", "-i", help="Path of the input file")
args = parser.parse_args()

# The list containing all transformed cat keywords entries
cat_keywords_list = []

# The list containing all transformed content keywords entries
content_keywords_list = []

# open the input file and perform the transformation
with open(args.inputfile) as INPUT_FILE:
	reader = csv.reader(INPUT_FILE)
	header_row = next(reader)

	for row in reader:
		course = row[0].strip()
		term = row[1].strip()
		feedback = row[2].strip().replace('\n', '')
		keywords_cat = row[3].strip()
		keywords_content = row[4].strip()

		# split keywords_cat by space
		keywords_cat_array = keywords_cat.split()

		# iterate through the keywords_cat_array and 
		# store each (keyword, course, term, feedback) entry in a tuple,
		# then put the tuple in a list 
		for cat_k in keywords_cat_array:
			t = (cat_k, course, term, feedback)
			cat_keywords_list.append(t)

		# split keywords_content by space
		keywords_content_array = keywords_content.split()

		# iterate through the keywords_content_array and 
		# store each (keyword, course, term, feedback) entry in a tuple,
		# then put the tuple in a list 
		for content_k in keywords_content_array:
			t = (content_k, course, term, feedback)
			content_keywords_list.append(t)


# write the transformed category keywords results to a file
output_cat_keywords_file = "output_cat_keywords.csv"
with open(output_cat_keywords_file, "w") as output_file:
	writer = csv.writer(output_file)

	# iterate through the cat_keywords_list
	# and write each entry into the output file

	# write the header
	writer.writerow(["关键词", "课程", "学期", "全文"])

	for t in cat_keywords_list:
		writer.writerow([t[0], t[1], t[2], t[3]])


# write the transformed content keywords results to a file
output_content_keywords_file = "output_content_keywords.csv"
with open(output_content_keywords_file, "w") as output_file:
	writer = csv.writer(output_file)

	# iterate through the content_keywords_list
	# and write each entry into the output file

	# write the header
	writer.writerow(["关键词", "课程", "学期", "全文"])

	for t in content_keywords_list:
		writer.writerow([t[0], t[1], t[2], t[3]])

