import re, os
#Appending to tag file so that it plays nicely with other tag file generators you may have
#may be necessary to delete your tagfile in between runs
#remove these after testing
toc_file_name = './Table_of_Contents.txt'
tag_file_name = './tags'
if os.path.isfile(tag_file_name):   os.remove(tag_file_name)
if os.path.isfile(toc_file_name):   os.remove(toc_file_name)
source_file_names = ['./unix_class.txt', './vi_class.txt', './python_class.txt', './git_class.txt']
generate_TOC = False

toc_file = file(toc_file_name,'a')
tag_file = file(tag_file_name,'a') 


def extract_tags_from_file(filename):
    tags = []
    headers = []
    for line in source_file.readlines():
        tag_header = ''
        try:
            tag_pattern = re.search('\[\[ (.*) \]\]',line).group(0)
            tag_header = re.search('\[\[ (.*) \]\]',line).group(1)
            tags.append(tag_header.split(' ')[0]+'\t'+source_file.name+'\t/'+tag_pattern)
            headers.append(tag_header)
        except (AttributeError, IndexError):
            continue
    tags.sort()
    headers.sort()
    return (headers, tags)

for source_file_name in source_file_names:
    source_file = file(source_file_name,'r')
    toc_file.write(source_file_name+'\n')
    (headers, tags) = extract_tags_from_file(source_file)
    tag_file.write('\n'.join(tags)+'\n\n')
    toc_file.write('\n'.join(headers)+'\n\n')
    source_file.close()

toc_file.close()
tag_file.close()

# dropped the table of contents at the top of the file from which the tags were
#being extracted. removed in favor of a table of contents file
# if generate_TOC:
#     #prepend the table of contents onto the source file
#     source_file_str = ''
#     with open(source_file_name,'r') as source_file:
#         source_file_str = source_file.read()
#     with open(source_file_name,'w') as source_file:
#         source_file.write('Table of Contents')
#         source_file.write('\n*'+'\n*'.join(headers)+'\n\n')
#         source_file.write(source_file_str)
