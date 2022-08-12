import click as c
from pywebcopy import save_website, save_webpage

@c.group()
def url():
    pass

@c.command(name="website")
@c.option('--url', '-u', help="The URL to download", required=True)
@c.option('--folder', '-f', help="The Folder to download the website into", required=True)
def save_all_website(url, folder):
    save_website(
        url=url,
        project_folder=folder,
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )

@c.command(name="webpage")
@c.option('--url', '-u', help="The URL to download", required=True)
@c.option('--folder', '-f', help="The Folder to download the website into", required=True)
def save_only_webpage(url, folder):
    save_webpage(
        url=url,
        project_folder=folder,
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )

url.add_command(save_only_webpage)
url.add_command(save_all_website)