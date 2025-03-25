#!/usr/bin/env python3
"""
This script extracts data from the LaTeX project and updates the website HTML.
Run this script whenever you update your LaTeX paper to keep the website in sync.
"""

import re
import os
import shutil
from datetime import datetime

# Paths
LATEX_DIR = "latex"
WEBSITE_DIR = "."
LATEX_MAIN = os.path.join(LATEX_DIR, "main.tex")
WEBSITE_INDEX = os.path.join(WEBSITE_DIR, "index.html")
IMAGES_DIR = os.path.join(WEBSITE_DIR, "images")

def extract_abstract():
    """Extract the abstract from the LaTeX file"""
    with open(LATEX_MAIN, 'r') as f:
        content = f.read()
    
    abstract_pattern = r'\\begin{abstract}(.*?)\\end{abstract}'
    match = re.search(abstract_pattern, content, re.DOTALL)
    
    if match:
        abstract = match.group(1).strip()
        # Replace LaTeX commands with HTML equivalents
        abstract = abstract.replace('\\textbf{', '<strong>')
        abstract = abstract.replace('}', '</strong>')
        abstract = abstract.replace('\\%', '%')
        return abstract
    
    return None

def extract_authors():
    """Extract author information from the LaTeX file"""
    with open(LATEX_MAIN, 'r') as f:
        content = f.read()
    
    author_pattern = r'\\author{(.*?)}\n\n\\begin{document}'
    match = re.search(author_pattern, content, re.DOTALL)
    
    if match:
        author_text = match.group(1).strip()
        # Complex processing would be needed here to parse LaTeX author format
        # This is a simplified version
        return author_text
    
    return None

def extract_results():
    """Extract key results from the LaTeX file"""
    with open(LATEX_MAIN, 'r') as f:
        content = f.read()
    
    results_pattern = r'\\section{Results}(.*?)\\section'
    match = re.search(results_pattern, content, re.DOTALL)
    
    if match:
        results = match.group(1).strip()
        # Extract percentages and key findings
        percentages = re.findall(r'(\d+\.\d+)\\%', results)
        return percentages
    
    return []

def copy_figures():
    """Copy figures from LaTeX to website images directory"""
    latex_figures = os.path.join(LATEX_DIR, "figures")
    
    # Ensure the website images directory exists
    os.makedirs(IMAGES_DIR, exist_ok=True)
    
    # Look for PNG, JPG, and PDF files in the LaTeX figures directory
    if os.path.exists(latex_figures):
        for file in os.listdir(latex_figures):
            if file.endswith(('.png', '.jpg', '.jpeg')):
                src = os.path.join(latex_figures, file)
                dst = os.path.join(IMAGES_DIR, file)
                shutil.copy2(src, dst)
                print(f"Copied {file} to website images directory")

def update_website():
    """Update the website with extracted information"""
    if not os.path.exists(WEBSITE_INDEX):
        print(f"Error: Website index file not found at {WEBSITE_INDEX}")
        return
    
    # Extract information
    abstract = extract_abstract()
    results = extract_results()
    
    # Copy figures
    copy_figures()
    
    # Read the current website HTML
    with open(WEBSITE_INDEX, 'r') as f:
        html = f.read()
    
    # Update the abstract if found
    if abstract:
        abstract_pattern = r'<div class="abstract">\s*<h2>Abstract</h2>\s*<p>(.*?)</p>\s*</div>'
        html = re.sub(abstract_pattern, f'<div class="abstract">\n        <h2>Abstract</h2>\n        <p>\n            {abstract}\n        </p>\n    </div>', html, flags=re.DOTALL)
    
    # Update the results if found
    if results and len(results) >= 4:
        html = html.replace('<span class="highlight">27.4%</span>', f'<span class="highlight">{results[0]}%</span>')
        html = html.replace('<span class="highlight">92.3%</span>', f'<span class="highlight">{results[1]}%</span>')
        html = html.replace('<span class="highlight">18.2%</span>', f'<span class="highlight">{results[2]}%</span>')
        html = html.replace('<span class="highlight">86%</span>', f'<span class="highlight">{results[3]}%</span>')
    
    # Update the last modified date
    today = datetime.now().strftime("%B %Y")
    html = re.sub(r'Website last updated: .*?<', f'Website last updated: {today}<', html)
    
    # Write the updated HTML back to the file
    with open(WEBSITE_INDEX, 'w') as f:
        f.write(html)
    
    print(f"Website updated successfully!")

if __name__ == "__main__":
    update_website()
