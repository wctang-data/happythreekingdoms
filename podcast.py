#!/usr/bin/env python3

import os

def main():
    base = "https://wctang-data.github.io/happythreekingdoms"
    with open("feed.xml", "w", encoding="utf-8") as out:
        print(f'''<!DOCTYPE html>
<html>
<head>
<title>歡樂三國志</title>
</head>
<body>
<h1>歡樂三國志</h1>
<img src="{base}/logo.jpg" />
<p>歡樂三國志</p>
<a href="{base}/feed.xml">feed</a>
<ul>''', file=out)

        for dirpath, _, filenames in os.walk("."):
            if dirpath == ".":
                continue
            elif dirpath.startswith(".\\.git"):
                continue
            dirpath = dirpath[2:]
            for filename in filenames:
                print(f'<li><a href="{base}/{dirpath}/{filename}">{dirpath} {filename}</a></li>', file=out)

        print('''</ul>
</body>
</html>''', file=out)


if __name__ == '__main__':
    main()
