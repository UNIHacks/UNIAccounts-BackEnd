import hashlib
import sys


def encrypt_file(file_path, key):
    # Input file
    with open(file_path, "rb") as input_file:
        # Read the content of the file
        file_content = input_file.read()

    # Create hash object with the key
    hasher = hashlib.sha256()
    hasher.update(key.encode("utf-8"))
    key_hash = hasher.digest()

    # Encrypt the content of the file using the key
    encrypted_content = bytearray()
    for i, byte in enumerate(file_content):
        key_byte = key_hash[i % len(key_hash)]
        encrypted_byte = byte ^ key_byte
        encrypted_content.append(encrypted_byte)

    # Write the content encrypted in an output file
    with open(file_path + ".encrypted", "wb") as output_file:
        output_file.write(encrypted_content)


if __name__ == "__main__":
    # Verify that a file and an encryption key was provided
    if len(sys.argv) < 3:
        print("Use > python encrypt.py key file")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2]

    # Encrypt the file
    encrypt_file(file_path, key)

    print(f'{file_path} has been encrypted with the key "{key}"')
