import os
def rename_files():
    #(1) get file names from a directory
    file_list=os.listdir(r"./prank")
    #print file_list

    #(2) for each file, rename filename
    for file_name in file_list:
        print "Old name : ",file_name
        print "New name : ",file_name.translate(None,'0123456789')
        os.rename(r"./prank/"+file_name,r"./prank/"+file_name.translate(None,'0123456789'))

rename_files()  #keys are in the closet. behind the shoe box 

#https://www.youtube.com/watch?v=rDzq5zr5r98&feature=share
#https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
#https://docs.python.org/2/library/os.html
#http://www.tutorialspoint.com/python/string_translate.htm
#https://docs.python.org/3/library/stdtypes.html?highlight=maketrans#str.translate



#an other way

# import os
# def rename_files():
#     #(1) get file names from a directory
#     file_list=os.listdir(r"./prank")
#     #print file_list
#     saved_path=os.getcwd()
#     os.chdir(r"./prank")
#     #(2) for each file, rename filename
#     for file_name in file_list:
#         os.rename(file_name,file_name.translate(None,'0123456789'))
#     os.chdir(saved_path)
# rename_files()