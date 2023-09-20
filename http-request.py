import requests
import csv
import pprint


# Request Data
base_url = 'https://cse-2023.beekeeper.io/api/2/'
post_url = 'posts'
parameter = '?limit=100'
access_token = 'aea3148c-48ed-4963-86d4-ad0e6eb745f8'
headers = {
    'Authorization': f'Token {access_token}',
    'Accept': 'application/json',
    'Content-type': 'application/json'
}

# Format the Data


def format_data(data):
    total_likes = 0
    total_comments = 0
    for post in data:
        total_likes += post['like_count']
        total_comments += post['comment_count']
    print(len(data))


# Print the Data


def print_data(data):
    posts_file = 'posts.csv'
    fieldnames = data[0].keys()
    with open(posts_file, 'w', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in data:
            writer.writerow(row)

    print(f'Data has been written to {posts_file}')


# Make the Request
response = requests.get(f'{base_url}{post_url}{parameter}', headers=headers)

if response.status_code == 200:
    post_data = response.json()
    pprint.pprint(post_data)
    format_data(post_data)
    # formatted_post_data = format_data(post_data)
    # print_data(formatted_post_data)
else:
    print(f"Failed with status code:{response.status_code}.")
