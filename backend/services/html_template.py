# template.py

def get_html(data):
    file_links = ""
    for file in data['files']:
        anchor = file['name'].replace('.', '-')
        file_links += f'<a href="#{anchor}">{file["name"]}</a>\n'

    files_html = ""
    for file in data['files']:
        anchor = file['name'].replace('.', '-')
        functions = "".join([f"<li>{f}</li>" for f in file['functions']]) or "<li>None</li>"
        deps = "".join([f"<li>{d}</li>" for d in file['dependencies']]) or "<li>None</li>"

        files_html += f"""
        <div id="{anchor}">
            <h3>{file['name']}</h3>
            <p>{file['purpose']}</p>
            <h4>Functions</h4>
            <ul>{functions}</ul>
            <h4>Dependencies</h4>
            <ul>{deps}</ul>
            <hr>
        </div>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{data['project_name']}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: Georgia, serif; background: #fff; color: #222; display: flex; }}
  #sidebar {{ width: 220px; position: fixed; top: 0; left: 0; bottom: 0; padding: 32px 20px; border-right: 1px solid #ddd; overflow-y: auto; }}
  #sidebar h2 {{ font-size: 13px; font-weight: bold; margin-bottom: 16px; text-transform: uppercase; letter-spacing: 1px; color: #222; }}
  #sidebar a {{ display: block; font-size: 13px; color: #0000EE; text-decoration: underline; margin-bottom: 8px; font-family: monospace; }}
  #sidebar a:hover {{ color: #551A8B; }}
  #main {{ margin-left: 220px; padding: 40px 60px; max-width: 820px; }}
  h1 {{ font-size: 24px; margin-bottom: 32px; }}
  h3 {{ font-size: 16px; font-family: monospace; margin: 24px 0 8px; }}
  h4 {{ font-size: 13px; margin: 12px 0 6px; color: #444; }}
  p  {{ font-size: 14px; color: #444; line-height: 1.6; }}
  ul {{ padding-left: 20px; margin-bottom: 8px; }}
  li {{ font-size: 13px; color: #444; line-height: 1.8; }}
  hr {{ border: none; border-top: 1px solid #eee; margin: 24px 0; }}
  input {{ width: 100%; padding: 6px 8px; font-size: 12px; border: 1px solid #ddd; margin-bottom: 16px; }}
</style>
</head>
<body>
<div id="sidebar">
  <h2>Files</h2>
  <input placeholder="Search..." oninput="filterFiles(this.value)">
  {file_links}
</div>
<div id="main">
  <h1>{data['project_name']}</h1>
  {files_html}
</div>
<script>
  function filterFiles(query) {{
    document.querySelectorAll('#sidebar a').forEach(link => {{
      link.style.display = link.textContent.toLowerCase().includes(query.toLowerCase()) ? 'block' : 'none';
    }});
  }}
</script>
</body>
</html>"""