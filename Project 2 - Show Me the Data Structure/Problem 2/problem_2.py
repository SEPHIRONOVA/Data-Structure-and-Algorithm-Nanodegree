# Problem 2 - File Recursion
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    # Check if the path is file
    if os.path.isfile(path):
        file = path
        if file.endswith('.' + suffix):
            return [file]
        return ''

    # Check if path is a directory
    elif os.path.isdir(path):

        fileList = os.listdir(path)
        filePathList = []

        for file in fileList:
            filePath = os.path.join(path + "\\" + file)

            # Check if filePath is a folder
            if os.path.isdir(filePath):
                # If it is a folder, recursively call the function on folder
                filePathList += find_files(suffix, filePath)
            else:
                # If it is a file, append the filePath to the filePathList
                if file.endswith('.' + suffix):
                    filePathList.append(filePath)

    # File not exists
    else:
        print("File not exist")
        return ''

    return filePathList

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Working Directory Structure
###################################################################################################
#################################### os.getcwd() ##################################################
################################### / ######### \ #################################################
################################## / ########### \ ################################################
####################### Test Folder 1 ##########       Test Folder 2        #######################
############################ / ################## / ####### | ########## \ ########################
########################### / ################## / ######## | ########### \ #######################
###################### abc.txt ###### Test Folder 2-1 ## Test Folder 2-1 ### def.txt ##############
####################################### / #########################################################
###################################### / ##########################################################
################################## ghi.xlsx #######################################################
###################################################################################################


# Test Case 1
# Empty Folder
# Returned Empty, and print File not Exists
print(find_files('txt', os.getcwd() + "/Test Folder 2/Test Folder 2-2"))

# Test Case 2
# No such file exists
# Returned Empty, and print File not Exists
print(find_files('txt', os.getcwd() + "/Test Folder 2/abc.txt"))

# Test Case 3
# Filename correct but different suffix (it is actually ghi.xlsx)
# Returned Empty, and print File not Exists
print(find_files('txt', os.getcwd() + "/Test Folder 2/Test Folder 2-1/ghi.txt"))

# Test Case 4
# A file Path - Should print out file path directly
# Should print out correct path directly
print(find_files('txt', os.getcwd() + "/Test Folder 1/abc.txt"))

# Test Case 5
# A directory path
print(find_files('txt', os.getcwd() + "/Test Folder 2"))
