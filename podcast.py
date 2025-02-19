#!/usr/bin/env python3

import os
import datetime
import pydub

def main():
    base = "https://wctang-data.github.io/happythreekingdoms"
    name = "歡樂三國志"
    _now = datetime.datetime.now()
    with open("feed.xml", "w", encoding="utf-8", newline='\n') as out:
        print(f'''<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" version="2.0">
<channel>
<title>{name}</title>
<description>{name}</description>
<itunes:image href="{base}/logo.jpg"/>
<link>{base}/</link>
<language/>
<pubDate>{_now}</pubDate>
<author>wctang-data</author>''', file=out)

        idx = 0
        items = []
        for dirpath, _, filenames in os.walk("."):
            if dirpath == ".":
                continue
            elif dirpath.startswith(".\\.git"):
                continue
            dirpath = dirpath[2:]
            for filename in filenames:
                info = pydub.utils.mediainfo(f'{dirpath}/{filename}')
                items.append((f'{dirpath} {filename[:-4]}', f'{dirpath}/{filename}', info["size"], info["duration"]))

        for idx, item in enumerate(items):
            print(f'<item><title>{item[0]}</title><pubDate>{_now+datetime.timedelta(days=-len(items)+idx)}</pubDate><enclosure url="{base}/{item[1]}" type="audio/mpeg" length="{item[2]}"/><itunes:duration>{int(float(item[3]))}</itunes:duration></item>', file=out)

        print('''</channel>
</rss>''', file=out)


if __name__ == '__main__':
    main()
