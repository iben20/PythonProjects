# insecure_deserialization_vuln.py
import pickle

def load_data(serialized_data):
    # Insecure deserialization
    return pickle.loads(serialized_data)

if __name__ == "__main__":
    data = input("Enter serialized object: ")
    obj = load_data(data.encode())
    print(obj)
