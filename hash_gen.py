import hashlib
import itertools
import sys

def read_input_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def hash_inputs(combined_str):
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()

    sha256_hash.update(combined_str.encode())
    md5_hash.update(combined_str.encode())

    return sha256_hash.hexdigest(), md5_hash.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    lines = read_input_from_file(filename)
    
    if len(lines) < 2:
        print("File should contain at least 2 lines: username and timestamp.")
        sys.exit(1)

    username = lines[0]
    timestamp = lines[1]

    # List of special characters
    special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?", "|"]

    results = []

    # Generate every possible combination for each special character
    for special_char in special_chars:
        combinations = list(itertools.permutations([username, timestamp, special_char], 3))
        for combination in combinations:
            combined_str = ''.join(combination)
            sha256_result, md5_result = hash_inputs(combined_str)
            results.append((combined_str, sha256_result, md5_result))

    # Print all results
    for combined_str, sha256_result, md5_result in results:
        print(f"Combined String: {combined_str}")
        print(f"SHA-256 Hash: {sha256_result}")
        print(f"MD5 Hash: {md5_result}")
        print("-" * 40)
