# === Stage 14: Add file load support with fallback demo data ===
# Project: MentorBoard
def load_data(path=None):
    if path and os.path.exists(path):
        with open(path) as f:
            data = []
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split('|||')
                if len(parts) == 6:
                    entry = {
                        'goal': parts[0],
                        'question': parts[1],
                        'resource': parts[2],
                        'feedback': parts[3],
                        'progress': int(parts[4]),
                        'date': parts[5]
                    }
                    data.append(entry)
            if data:
                return data
    else:
        import json
        with open('mentorboard_demo.json') as f:
            demo = json.load(f)
            for item in demo['sessions']:
                entry = {
                    'goal': item.get('goals', {}).get(item, ''),
                    'question': item.get('questions', {}).get(item, ''),
                    'resource': item.get('resources', {}).get(item, ''),
                    'feedback': item.get('feedback', {}).get(item, ''),
                    'progress': int(item.get('progress', 0)),
                    'date': item.get('date', '')
                }
                data.append(entry)
    return data if data else [
        {'goal': 'Learn Python basics', 'question': 'What is a function?', 'resource': '', 'feedback': 'Good start!', 'progress': 5, 'date': '2024-01-15'},
        {'goal': 'Build a simple app', 'question': 'How to handle errors?', 'resource': 'Python docs', 'feedback': 'Keep going!', 'progress': 7, 'date': '2024-01-20'},
        {'goal': 'Master data structures', 'question': 'List vs tuple?', 'resource': '', 'feedback': 'Understood!', 'progress': 8, 'date': '2024-02-01'}
    ]
