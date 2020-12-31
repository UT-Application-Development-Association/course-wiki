
from tqdm import tqdm
import os
import argparse
import codecs
import json
import re
import requests
requests.session().keep_alive = False  # 及时释放


def get_info(comments_url, token):
    headers = {'Content-Type': 'application/json',
               'Authorization': 'token %s' % token}
    r = requests.get(comments_url, headers=headers)
    ret = json.loads(r.text)
    if r.status_code > 300:
        print('error %s', r.text)
        return False
    return ret


def generate_header(header_text):
    def partition(beg, end=None):
        if end is None:
            return header_text.partition(beg)[2][1:].strip()
        return header_text.partition(beg)[2].strip().partition(end)[0].strip()[1:].strip()
    title = partition('title', 'subtitle')
    subtitle = partition('subtitle', 'date')
    date = partition('date', 'author')
    author = partition('author', 'tags')
    tags = partition('tags')
    tags = ''.join(list(filter(lambda x:x not in ['\t', '\r', '\n', ' '], tags))).replace('-', '\n    - ')
    mk = f'---\nlayout: post\ntitle: "{title}"\nsubtitle: "{subtitle}"\ndate: {date}\nauthor: "{author}"\ntags:{tags}\n---\n'
    return mk


def to_markdown(page, coms):
    content_body_index = page['body'].index('##')
    content_header = page['body'][:content_body_index]
    mk = generate_header(content_header)
    content_body = page['body'][content_body_index:]
    mk += content_body+'\n'

    for com in coms:
        mk += com['body']+"\n"
    return mk


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', help="github account username")
    parser.add_argument('-r', '--repo', help="github account repo")
    parser.add_argument('-t', '--token', help="github personal access token")
    args = parser.parse_args()

    api_url = f'https://api.github.com/repos/{args.username}/{args.repo}/issues'
    issue_ret = get_info(api_url, args.token)
    for page in tqdm(issue_ret):
        coms = []
        if page['comments'] > 0:
            coms = get_info(page['comments_url'], args.token)
        mk = to_markdown(page, coms)

        # save
        filename = page['created_at'].split('T')[0]+'-'+page['title']+'.md'
        filename = re.sub(r'[/:*?"<>|]', " ", filename)  # check filename
        filename = os.path.join('./_posts', filename)

        with codecs.open(filename, 'w', 'utf-8') as file:
            file.write(mk)