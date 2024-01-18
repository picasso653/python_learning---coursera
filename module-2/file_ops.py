def read_file(file_name):
    
    with open(file_name, 'r') as File:
        data = File.read()
        print(data)
        return data
        
    
    raise NotImplementedError()

def read_file_into_list(file_name):
   
    with open(file_name, 'r') as file:
        return file.readlines()

    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    
    first_line = file_contents.split('\n')
    with open(output_filename, 'w') as new_file:
        new_file.write(first_line[0]+'\n')
    return

    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        return [lines[i] for i in range(1, len(lines), 2)]

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    with open(file_name) as file:
        order = file.readlines()
        order.reverse()
        print(order)
        return order

    raise NotImplementedError()

def main():
    file_contents = read_file("sampletext.txt")
    # print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()

print(main)

# I have no idea what I'm doing to
    
"""
Okay so I'm out data and I can't continue my lessons as of now 
Let's ust make this look like we dey do something
 """