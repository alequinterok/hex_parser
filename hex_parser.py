import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input.txt> <output.bin>")
        sys.exit(1)

    in_fname = sys.argv[1]
    out_fname = sys.argv[2]

    try:
        with open(in_fname, 'r') as fin, open(out_fname, 'wb') as fout:
            byte_list = []

            for line in fin:
                for d in line.split():
                    if len(d) == 1:
                        d = "0" + d
                    try:
                        byte_list.append(bytes.fromhex(d))
                    except ValueError:
                        print(f"[-] Warning: skipping invalid hex value '{d}'")

            fout.write(b''.join(byte_list))
            print(f"[+] The script has finished successfully!")

    except FileNotFoundError:
        print(f"[-] Error: could not find file '{in_fname}'")
        sys.exit(1)
    except IOError as e:
        print(f"[-] I/O Error: {e}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()