from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the final.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "final.ipynb", "--allow-websocket-origin=*"])

