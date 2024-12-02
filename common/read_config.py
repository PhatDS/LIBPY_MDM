import json
from collections import defaultdict

def load_config(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

# Hàm phân chia cleansing thành nhóm theo type
def group_cleansing_by_action(cleansing_list):
    grouped = defaultdict(list)
    
    for cleansing in cleansing_list:
        action = cleansing.get("type")
        grouped[action].append(cleansing)
    
    return dict(grouped)
