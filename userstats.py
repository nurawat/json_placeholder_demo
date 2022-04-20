from users import Users
import concurrent.futures

class UserStats:
    def __init__(self, user: Users):
        self.user = user
        self.todo_count = user.get_todo_count_by_user(user.id)
        self.post_count = user.get_posts_count_by_user(user.id)
        self.comment_count = user.get_comments_on_post(user.id)


    def process(self):
      with concurrent.futures.ThreadPoolExecutor() as executor:
          futures = []
          futures.append(executor.submit(self.user.get_todo_count_by_user, self.user.id))
          futures.append(executor.submit(self.user.get_posts_count_by_user, self.user.id))
          futures.append(executor.submit(self.user.get_comments_on_post, self.user.id))
          for future in concurrent.futures.as_completed(futures):
              print(future.result())
  
    def __repr__(self):
        return f"user={self.user}, todo_count={self.todo_count}, post_count={self.post_count}, comment_count={self.comment_count}"
