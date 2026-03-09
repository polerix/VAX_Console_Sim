import re

with open('index.html', 'r') as f:
    index = f.read()

with open('ka670_diagnostic.html', 'r') as f:
    diag = f.read()

# Extract CSS from index.html
css_match = re.search(r'<style>(.*?)</style>', index, re.DOTALL)
css = css_match.group(1)

# Modify body CSS to .boot-overlay
css = re.sub(r'body\s*{([^}]+)}', r'.boot-overlay {\1 transition: opacity 1s ease-out; position: fixed; top: 0; left: 0; right: 0; bottom: 0; z-index: 9999;}\n.boot-overlay.hidden { opacity: 0; pointer-events: none; }', css)

# Extract HTML from index.html
html_match = re.search(r'<body>(.*?)<script>', index, re.DOTALL)
html_content = html_match.group(1).strip()
html = f'<div id="bootOverlay" class="boot-overlay">\n{html_content}\n</div>'

# Extract JS from index.html
js_match = re.search(r'<script>(.*?)</script>', index, re.DOTALL)
js = js_match.group(1).strip()

# Modify bootSystem in JS
js = re.sub(
    r'setTimeout\(\(\) => \{\s*window\.location\.href = \'ka670_diagnostic\.html\';\s*\}, 4000\);',
    r"setTimeout(() => {\n                    const overlay = document.getElementById('bootOverlay');\n                    overlay.classList.add('hidden');\n                    setTimeout(() => overlay.style.display = 'none', 1000);\n                }, 4000);",
    js
)

# In diag, we need to remove the existing AudioEngine and the window.addEventListener('load') logic
diag_js_remove_pattern = r'const AudioEngine = \(\(\) => \{.*?\n      return \{ startFan, stopFan \};\n    \}\)\(\);\n'
diag = re.sub(diag_js_remove_pattern, '', diag, flags=re.DOTALL)

# Remove the window load event that starts the fan in diag
diag_load_pattern = r'// Continue fan noise from index page.*?window\.addEventListener\(\'load\', \(\) => \{.+?\}\);\n'
diag = re.sub(diag_load_pattern, '', diag, flags=re.DOTALL)

# Inject CSS
if '</style>' in diag:
    diag = diag.replace('</style>', f'{css}\n</style>')
else:
    diag = diag.replace('</head>', f'<style>\n{css}\n</style>\n</head>')

# Inject HTML
diag = diag.replace('<body>', f'<body>\n{html}')

# Inject JS
# Diag has a large script section. We will prepend the new AudioEngine and bootSystem to the beginning of the script section.
diag = diag.replace('<script>', f'<script>\n{js}\n')

with open('index.html', 'w') as f:
    f.write(diag)

print("Merged successfully.")
