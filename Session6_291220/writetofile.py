file_string = str(input("Enter Text here:"))

def write_to_file(text):
    file_object = open("testfile.txt","w")
    file_object.write(text)
    file_object.close()

write_to_file(file_string)
