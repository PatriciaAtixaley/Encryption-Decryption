import sys

def encryptdecrypt(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        data = f.read()
    repass = (password * (len(data) // len(password) + 1))[:len(data)].encode('utf-8')
    endata = bytes([data[i] ^ repass[i] for i in range(len(data))])
    
    with open(output_file, 'wb') as f:
        f.write(endata)

def main():
    if len(sys.argv) != 3:
        print("Usage: python xor1.py <input_file> <password>")
        return

    input_file = sys.argv[1]
    password = sys.argv[2]

    if input_file.endswith('.xor'):
        output_file = input_file[:-4] 
        encryptdecrypt(input_file, output_file, password)
        print("Successfully Decrypted")
    else:
        output_file = input_file + '.xor'
        encryptdecrypt(input_file, output_file, password)
        print("Successfully Encrypted")

if __name__ == "__main__":
    main()
