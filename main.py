import json
import xml.etree.ElementTree as ET


def get_long_words(s):
    words = []
    for w in s.split():
        if len(w) > 6:
            words.append(w)
    return words


def get_top_words(words, top_count=10):
    words_count ={}
    words.sort()
    for i in words:
        if i in words_count.keys():
            words_count[i] +=1
        else:
            words_count[i] = 1
    top_words_with_count = dict(sorted(words_count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[:top_count])
    return list(top_words_with_count.keys())


def newsreader_top_json(filename):
    with open(filename, encoding="utf8") as f:
        news = json.load(f)
        all_words = []
        for i in news['rss']['channel']['items']:
            all_words += get_long_words(i['description'])
    return get_top_words(all_words)


def newsreader_top_xml(filename):
    all_words = []
    tree = ET.parse(filename)
    for item in tree.findall('channel/item'):
        all_words += get_long_words(item.find('description').text)
    return get_top_words(all_words)


print(f"Top 10 from json: {newsreader_top_json('news_source/newsafr.json')}")
print(f"Top 10 from xml: {newsreader_top_xml('news_source/newsafr.xml')}")
