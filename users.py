from utils import *


class Users(object):
    def __init__(self, id: int, name: str, username: str, email: str):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def get_todo_count_by_user(self, id: int):
        return get_todos_by_user(self.id)

    def get_posts_count_by_user(self, id: int):
        return get_posts_by_user(self.id)

    def get_comments_on_post(self, id: int):
        return get_comments_on_post(self.id)

    def __repr__(self):
        return f'{self.id},{self.name},{self.username},{self.email}'
