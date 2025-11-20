import json
import os
from jinja2 import Environment, FileSystemLoader

# Setup: Define paths relative to the script location
current_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize Jinja2 environment (The Templating Engine)
file_loader = FileSystemLoader(current_dir)
env = Environment(loader=file_loader)

try:
    print("🔨 Fetching data and building CV...")
    
    # 1. Load the data layer (JSON)
    with open(os.path.join(current_dir, 'cv_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Load the presentation layer (HTML Template)
    template = env.get_template('template.html')

    # 3. Render: Merge data + template
    output = template.render(data)

    # 4. Export to static HTML
    output_file = os.path.join(current_dir, 'index.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)
        
    print(f"✅ Success! CV generated at: {output_file}")

except Exception as e:
    print(f"❌ Build failed: {e}")