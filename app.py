import pandas as pd
import pathlib

def main(password_file_path: str, new_path: str) -> None:
    pass_file = pd.read_csv(password_file_path, index_col=0)
    # TODO: Check whether or not the password file is correct.
    clean_pass_file = pass_file.drop_duplicates() 
    
    clean_pass_file.to_csv(pathlib.Path(new_path, "Cleaned-File.csv"))
    

if __name__ == "__main__":
    print("Enter the path to your passwords file: ", end="")    
    pass_file_path = input().strip()
    print("Enter where you want the new file to be saved (default is here): ", end="")
    new_path = input().strip()
    if new_path == "":
        new_path = "."
        
    main(pass_file_path, new_path)