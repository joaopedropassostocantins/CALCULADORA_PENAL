from bs4 import BeautifulSoup
from pathlib import Path

html_path = Path('/home/ubuntu/browser_html/planalto_gov_br_l11340.htm_1786999058141.html')
soup = BeautifulSoup(html_path.read_text(errors='replace'), 'html.parser')
text = soup.get_text('\n')
lines = [line.strip() for line in text.splitlines() if line.strip()]
for i, line in enumerate(lines):
    if 'Art. 24-A' in line or 'Pena' in line and i > 0:
        if i > 0 and ('Art. 24-A' in line or any('Art. 24-A' in prev for prev in lines[max(0, i-8):i])):
            print('\n'.join(lines[max(0, i-8):min(len(lines), i+12)]))
            print('---')
