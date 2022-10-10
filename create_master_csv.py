import csv
import os
from glob import glob

with open("SUMMARY.csv", 'w', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)

    # create header
    writer.writerow(['post_url', 'price', 'location', 'post_title', 'source'])
    for filename in glob(f"{path}/*.csv"):
        with open(filename, 'r', encoding='utf-8') as input_file:
            value = "FAIL"
            reader = csv.reader(input_file)
            for lineno, line in enumerate(reader, 1):
                if lineno != 2:
                    continue
                if line[1] != "":
                    value = "PASS"
                break
        writer.writerow([os.path.basename(filename).split(".")[0], value])



    
# with open('Users.csv', 'rt') as f:
#      reader = csv.reader(f, delimiter=',')
#      for row in reader:
#           if username == row[2]: # if the username shall be on column 3 (-> index 2)
#               print "is in file"

#               import glob

# write_header = True
# output_csv = 'new york.csv'     # assume this is not already used

# with open(output_csv, 'w', newline='') as f_output:
#     csv_output = csv.writer(f_output)

#     for csv_filename in glob.glob('*.csv'):
#         if csv_filename != output_csv:
#             with open(csv_filename) as f_input:
#                 csv_input = csv.reader(f_input)
#                 header = next(csv_input)

#                 if write_header:
#                     csv_output.writerow(header)
#                     write_header = False

#                 for row in csv_input:
#                     if "new york" in row[1].lower():
#                         csv_output.writerow(row)




# print("We found this: " + craigslist)


# craigl.get_craigslist_search_results(craigslist_base_url)