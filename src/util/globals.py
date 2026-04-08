# globals.py — patched to remove dependency on globals.yml

data = {
    "device": "cuda",
    "dtype": "float32"
}

def get(key, default=None):
    return data.get(key, default)
