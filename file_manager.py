import os

def list_files(directory):
    """Lists all files in the specified directory."""
    try:
        files = os.listdir(directory)
        return files
    except Exception as e:
        print(f"Error listing files: {e}")
        return []

def delete_file(file_name):
    """Deletes the specified file."""
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")

def create_new_file(file_name):
    """Creates a new file with the specified name."""
    try:
        with open(file_name, 'w') as file:
            file.write("This is a new file.")
        print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")
