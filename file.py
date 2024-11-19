def open_file():
    try:
        file = input("Enter a file you wish to open:")
        file_contents = open(file, "r")
        for line in file_contents:
            try:
                line = line.rstrip("\n")
                line_list = line.split ("")
                sum = round(float(line_list[0]) + float(line_list[1]),2)
                print(sum)
            except:
                print("failed to add this line")
    except IOError as e:
        print("Error:", e)
open_file()
