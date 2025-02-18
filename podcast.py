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

        for dirpath, _, filenames in os.walk("."):
            if dirpath == ".":
                continue
            elif dirpath.startswith(".\\.git"):
                continue
            dirpath = dirpath[2:]
            for filename in filenames:
                info = pydub.utils.mediainfo(f'{dirpath}/{filename}')
                print(f'<item><title>{dirpath} {filename}</title><pubDate>{_now}</pubDate><enclosure url="{base}/{dirpath}/{filename}" type="audio/mpeg" length="{info["size"]}"/><itunes:duration>{int(float(info["duration"]))}</itunes:duration></item>', file=out)

        print('''</channel>
</rss>''', file=out)


if __name__ == '__main__':
    main()
