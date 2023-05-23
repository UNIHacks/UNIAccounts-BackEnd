import hashlib
import sys


def decrypt_file(file_path, key):
    # Input file
    with open(file_path, "rb") as input_file:
        # Read the content of the file
        file_content = input_file.read()

    # Create hash object with the key
    hasher = hashlib.sha256()
    hasher.update(key.encode("utf-8"))
    key_hash = hasher.digest()

    # Uncommon the file content using the key
    decrypted_content = bytearray()
    for i, byte in enumerate(file_content):
        key_byte = key_hash[i % len(key_hash)]
        decrypted_byte = byte ^ key_byte
        decrypted_content.append(decrypted_byte)

    # Write the content disappointed in an output file
    with open(file_path[:-10], "wb") as output_file:
        output_file.write(decrypted_content)


if __name__ == "__main__":
    # Verify that a file and a decryptation key was provided
    if len(sys.argv) < 3:
        print("Use > Python Decise.py Key File")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]

    # Decypt the file
    decrypt_file(file_path, key)

    print(f'{file_path} has been disregarded with the key "{key}"')
