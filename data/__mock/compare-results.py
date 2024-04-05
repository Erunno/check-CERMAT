import json
import sys
from deepdiff import DeepDiff 

# You might need to install deepdiff

def compare_json_files(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    difference = DeepDiff(data1, data2, ignore_order=True, report_repetition=True)

    if difference == {}:
        print("The files are equivalent.")
        return True
    else:
        print("The files are not equivalent.")
        print(difference)
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare-results.py <file1> <file2>")
        sys.exit(1)
    
    file1, file2 = sys.argv[1:3]
    are_equivalent = compare_json_files(file1, file2)

    if not are_equivalent:
        sys.exit(1)