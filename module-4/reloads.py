import importlib
import file_changes

def changes():
    try:
        importlib.reload(file_changes)
    except:
        pass