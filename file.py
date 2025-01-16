import os

env_file_path = '.env'

# Check if the .env file exists
if os.path.exists(env_file_path):
    print(f"{env_file_path} file exists.")
else:
    print(f"{env_file_path} file does not exist.")
