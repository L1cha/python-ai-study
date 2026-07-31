'''
读写json
'''

import json

def save_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

config = {
    "title": "OpenGL Demo",
    "width": 1280,
    "height": 720,
    "fullscreen": False
}

save_json("config.json", config)
config = load_json("config.json")
print(f'窗口标题：{config["title"]}')
print(f'窗口宽度：{config["width"]}')