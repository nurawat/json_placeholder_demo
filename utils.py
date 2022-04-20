import requests
import logging

logger = logging.getLogger(__name__)
api_url = "http://jsonplaceholder.typicode.com"
all_users = []

def request_users_list():
    try:
        user_url = f"{api_url}/users"
        response = requests.get(user_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def request_user_todos(userID):
    try:
        user_todo_url = f"{api_url}/users/{userID}/todos"
        response = requests.get(user_todo_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def request_user_posts(userID):
    try:
        user_post_url = f"{api_url}/users/{userID}/posts"
        response = requests.get(user_post_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def request_user_posts(userID):
    try:
        user_post_url = f"{api_url}/users/{userID}/posts"
        response = requests.get(user_post_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def get_comments_on_user_post(postID):
    try:
        user_post_url = f"{api_url}/posts/{postID}/comments"
        response = requests.get(user_post_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

def get_comments_on_post(userID):
    comments = 0
    get_all_posts = request_user_posts(userID)
    for user_posts in get_all_posts:
        comments += len(get_comments_on_user_post(user_posts["id"]))
    return comments
  
def get_posts_by_user(userID):
    return len(request_user_posts(userID))

def get_todos_by_user(userID):
    return len(request_user_todos(userID))

def get_all_users():
    for elements in request_users_list():
        all_users.append((
        elements["id"],
        elements["name"],
        elements["username"],
        elements["email"]
    ))
    return all_users
