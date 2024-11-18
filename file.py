import sys

def main():

    if len(sys.argv) != 2:
        print("Error: No filename provided.")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as infile:

            line_number = 1
            for line in infile:
        
                line = line.strip()
                values = line.split()

                if len(values) != 2:
                    print(f"Error on line {line_number}: Line does not contain exactly two values.")
                else:
                    try:
     
                        num1 = float(values[0])
                        num2 = float(values[1])
                        print(f"Sum of line {line_number}: {num1 + num2}")
                    except ValueError:

                        print(f"Error on line {line_number}: Invalid data, could not convert to float.")

                line_number += 1

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        sys.exit(1)


if __name__ == "__main__":
    main()
