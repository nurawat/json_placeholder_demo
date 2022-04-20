import click
from user_summary import UserStatsSummary

@click.command()
@click.option('--output', '-o', type=click.Choice(["csv", "table"]),
                help='Sets default output format for configuration files')
def callAPI(output):
  user_stats = UserStatsSummary()
  user_stats.fetch()
  user_stats.display_data(output)
 
if __name__ == "__main__":
    callAPI()
