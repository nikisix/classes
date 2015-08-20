import argparse
# [[ CLI_EXCERCISE ]]
#     Design a simple program that accepts command line arguements for a file to read in, which lines to print 
#     and whether or not to add line numbers to the front of it.
discription_message = """This program allows us to choose the line numbers of a file to print """
parser = argparse.ArgumentParser(description=discription_message)
parser.add_argument("-f", "--file", required=True, dest="input_file", help="file to import")
parser.add_argument("-n", "--number_lines", dest="number_lines", action="store_true", default=False, help="whether or not to number the lines")
parser.add_argument("-k", "--keep_rows", dest="keep_rows", help="A comma separated list of the rows to keep")
args = parser.parse_args()
if args.keep_rows:
    keep_rows = args.keep_rows.split(',')
    keep_rows = [int(i) for i in keep_rows]
i = 0

with open(args.input_file,'r') as f:
    for line in f.readlines():
        i+=1
        print 'i: '+str(i)
        if i > max(keep_rows): break
        if i in keep_rows:
            if args.number_lines:
                print str(i)+'\t'+line.rstrip('\n')
            else:
                print line.rstrip('\n')
        else:
            continue
