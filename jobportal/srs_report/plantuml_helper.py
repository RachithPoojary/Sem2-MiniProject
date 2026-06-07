#!/usr/bin/env python3
"""
plantuml_helper.py

Usage: python3 plantuml_helper.py <diagrams_dir>

This script finds all .puml files in the provided directory, POSTs each to the PlantUML server,
and saves a PNG for each file next to it.

It uses the public PlantUML server at https://www.plantuml.com/plantuml/png

Note: This requires network access. If the server is unavailable, the script will fail.
"""
import sys
import os
import urllib.request


def render_puml_to_png(puml_path, out_path):
    with open(puml_path, 'rb') as f:
        data = f.read()
    req = urllib.request.Request('https://www.plantuml.com/plantuml/png', data=data, method='POST')
    req.add_header('Content-Type', 'text/plain')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read()
            with open(out_path, 'wb') as out:
                out.write(body)
        print(f"Rendered {puml_path} -> {out_path}")
        return True
    except Exception as e:
        print(f"Failed to render {puml_path}: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 plantuml_helper.py <diagrams_dir>')
        sys.exit(1)
    diagrams_dir = sys.argv[1]
    if not os.path.isdir(diagrams_dir):
        print('Provided path is not a directory')
        sys.exit(1)
    for fname in os.listdir(diagrams_dir):
        if fname.endswith('.puml') or fname.endswith('.plantuml'):
            puml_path = os.path.join(diagrams_dir, fname)
            base = os.path.splitext(puml_path)[0]
            out_path = base + '.png'
            render_puml_to_png(puml_path, out_path)

if __name__ == '__main__':
    main()
