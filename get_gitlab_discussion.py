import requests
import MeCab
from wordcloud import WordCloud

url = "https://api.github.com/repos/hashicorp/terraform/issues/comments?per_page=100&page="
body_str = ''

for i in range(1):
    r = requests.get(url+str(i))
    for node in r.json():
        body_str += node['body']


tagger = MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(body_str)

word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type == '名詞':
        word_list.append(node.surface)
    node = node.next

word_chain = ' '.join(word_list)

W = WordCloud(width=640, height=480, background_color='white', colormap='bone', font_path='/usr/share/fonts/truetype/fonts-japanese-gothic.ttf').generate(word_chain)

W.to_file('W.png')