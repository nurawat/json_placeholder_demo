import requests
import json
import sys
import csv
from prettytable import PrettyTable
from users import Users
from userstats import UserStats
from utils import get_all_users

class UserStatsSummary:
    def __init__(self):
        self.all_user_stats = []
        
    def fetch(self):
      
        for user_id, name, username, email in get_all_users():
            stats = UserStats(Users(user_id, name, username, email))
            self.all_user_stats.append(stats)

    def display_data(self, format):
      headers = ["User-ID",
                "Name",
                "User-Name",
                "Email",
                "TODO-Count",
                "Post-Count",
                "Comment-Count"]
      
      if format == "csv":
        print(",".join(headers))
        for user_info in self.all_user_stats:
          print(",".join([str(user_info.user.id),
                          str(user_info.user.name),
                          str(user_info.user.username),
                          str(user_info.user.email),
                          str(user_info.todo_count),
                          str(user_info.post_count),
                          str(user_info.comment_count)
                          ]))
      else:
        user_table = PrettyTable()
        user_table.field_names = headers
        for user_info in self.all_user_stats:
            user_table.add_row([
                user_info.user.id,
                user_info.user.name,
                user_info.user.username,
                user_info.user.email,
                user_info.todo_count,
                user_info.post_count,
                user_info.comment_count]
            )
        print(user_table)

            
    def __repr__(self):
        return f'{self.all_user_stats}'
