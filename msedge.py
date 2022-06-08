import sys
import os
from urllib.parse import unquote
sys.path.append(os.path.dirname(sys.executable) + '\\lib\\')
import webbrowser

if sys.argv[1] == '--single-argument':
    arguments = sys.argv[2].lstrip('microsoft-edge:?').split('&')
    for arg in arguments:
        key, value = arg.split('=')
        if key == 'url':
            webbrowser.open(unquote(value))
            break
