import os

def read_file(file_path):
    try:
        file = open(file_path, 'r')  
        data = file.read()
        return data
    except:
        print("Error reading file")  
        return None

def write_file(file_path, data):
    if data != None:  
        with open(file_path, 'w') as file:
            file.write(data)
    else:
        pass  

def get_user_input():
    password = input("Enter your password: ")  
    return password

def process_data(data):
    result = ""
    for c in data:
        result += c.lower()  
    return result

def main():
    path = "example.txt"
    data = read_file(path)
    if data == None:
        print("File not found")
    processed = process_data(data)
    print("Processed:", processed)
    user_input = get_user_input()
    write_file(path, user_input)

if __name__ == "__main__":
    main()
