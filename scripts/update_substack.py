"""Refresh the 'Latest on Substack' list in index.html from the RSS feed."""
import html, re, urllib.request, xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
FEED = "https://www.americanmuckrakers.com/feed"
req = urllib.request.Request(FEED, headers={"User-Agent": "wheelernc-site/1.0"})
root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
rows = []
for item in list(root.iter("item"))[:3]:
    t = html.escape(item.findtext("title").strip())
    link = html.escape(item.findtext("link").strip())
    d = parsedate_to_datetime(item.findtext("pubDate"))
    date = f"{d.strftime('%b')} {d.day}, {d.year}"
    rows.append(f'      <li><a href="{link}" rel="noopener" target="_blank"><span class="outlet">Substack</span><span class="headline">{t}</span><span class="date">{date}</span></a></li>')
p = "index.html"
s = open(p, encoding="utf-8").read()
new = re.sub(r"(<!-- SUBSTACK:START -->\n).*?(\n\s*<!-- SUBSTACK:END -->)", lambda m: m.group(1) + "\n".join(rows) + m.group(2), s, flags=re.S)
if new != s:
    open(p, "w", encoding="utf-8").write(new)
    print("updated")
else:
    print("no change")
