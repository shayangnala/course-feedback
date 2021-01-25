import docx2txt
import argparse

parser = argparse.ArgumentParser(description="Processing the input word file")
parser.add_argument("--inputfile", "-i", help="Path of the input file")
parser.add_argument("--course", "-c", help= "Name of the course")
parser.add_argument("--term", "-t", help="Term of the course")

args = parser.parse_args()

# "/Users/shayangnala/Documents/助教/张晨老师课程反馈整理/【课程反馈】管理学的思与行-2020秋.docx"
my_text = docx2txt.process(args.inputfile)

lines = my_text.split('\n')

lines_cleaned = []

for i in lines:
	if i != "":
		lines_cleaned.append(i)


# write to a txt file with "|" as the delimiter
outputfile_name = "output_" + args.course + "_" + args.term + ".txt"
with open(outputfile_name, "w") as output_file:	
	j = 0
	while j+2 < len(lines_cleaned):
		feedback = lines_cleaned[j]
		keywords_cat = lines_cleaned[j+1].split(":")[1].strip()
		keywords_content = lines_cleaned[j+2].split(":")[1].strip()

		# if len(keywords_cat) == 1:
		# 	print(keywords_cat)

		output_file.write(args.course + "|" + args.term + "|" + feedback + "|" + keywords_cat + "|"+ keywords_content+"\n")
		j = j + 3


# print(lines_cleaned[0+3+3+3])
# print(lines_cleaned[1+3+3].split(":")[1])
# print(lines_cleaned[2+3].split(":")[1])

