import requests
import os
import sys


def main():
    '''Get argument value'''

    if len(sys.argv) >= 2:
        users_option = sys.argv[1]
        users_number = sys.argv[2]
    else:
        print("Wrong arguments, you need to specify the number of users with option -t <total> or --total <total>")

    if users_option and users_number:
        if users_option in  ["-t", "--total"] and users_number.isdigit():
            return int(users_number)
        else:
            print("Wrong arguments, you need to specify the number of users with option -t <total> or --total <total>")
    return 150
    
    
def get_users(users_number: int):
    url = os.getenv('GITHUB_API_URL')
    return requests.get(url).json()[:users_number]


def populate_database(users_number: int):
    pass


if __name__ == "__main__":
    users_number = main()
    users = get_users(users_number)