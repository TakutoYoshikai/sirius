from lina import lina
import os
import argparse

def encode(secret_filepath, key_filepath, output_filepath):
    if os.path.getsize(secret_filepath) > os.path.getsize(key_filepath):
        print("size over")
        return
    secret_file = open(secret_filepath, "rb")
    key_file = open(key_filepath, "rb")
    secret_data = secret_file.read()
    key_data = key_file.read()
    secret_file.close()
    key_file.close()
    secret_binary = "".join(lina.message_to_binary(secret_data))
    key_binary = "".join(lina.message_to_binary(key_data))
    result_binary = ""
    for i in range(len(secret_binary)):
        s_bit, k_bit = secret_binary[i], key_binary[i]
        r_bit = "0"
        if (s_bit == "1" and k_bit == "0") or (s_bit == "0" and k_bit == "1"):
            r_bit = "1"
        result_binary += r_bit
    result = lina.split(result_binary)
    result_file = open(output_filepath, "wb")
    result_file.write(result)

def decode(data_filepath, key_filepath, output_filepath):
    encode(data_filepath, key_filepath, output_filepath)


def main():
    parser = argparse.ArgumentParser(description="sirius is an encoder/decoder of data")
    parser.add_argument("mode", help="encode or decode")
    parser.add_argument("-s", "--secret")
    parser.add_argument("-k", "--key")
    parser.add_argument("-d", "--data")
    parser.add_argument("-o", "--output")
    args = parser.parse_args()
    if args.mode == "encode":
        if args.secret == None or args.key == None or args.output == None:
            parser.print_help()
            return
        encode(args.secret, args.key, args.output)
    elif args.mode == "decode":
        if args.data == None or args.key == None or args.output == None:
            parser.print_help()
            return
        decode(args.data, args.key, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

