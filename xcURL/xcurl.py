import click as c
from pywebcopy import save_website as save

@c.command()
@c.option('--url', '-u', help="The URL to download", required=True)
@c.option('--folder', '-f', help="The Folder to download the website into", required=True)
def url(url, folder):
    save(
        url=url,
        project_folder=folder,
        bypass_robots=True,
        debug=True,
        open_in_browser=True,
        delay=None,
        threaded=False,
    )