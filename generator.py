from jinja2 import Template
import json
import markdown
import re
from livereload import Server


def make_site():
    config_dict = fetch_config()
    topics = config_dict['topics']
    articles = config_dict['articles']
    article_page_template_text = load_file('templates/article_template.html')

    for article in articles:
        article_md_text = load_file('articles/' + article['source'])
        article_page_text = generate_article_page(article, article_md_text, article_page_template_text)
        re_result = re.search(r'\w+.(\w+)', article['source'])
        group_index = 1
        file_name = re_result.group(group_index)
        path_to_html = file_name + '.html'
        write_to_file(article_page_text, 'site/' + path_to_html)
        article['html_source'] = path_to_html

    index_page_template_text = load_file('templates/index_template.html')
    index_page_text = generate_index_page(topics, articles, index_page_template_text)
    write_to_file(index_page_text, 'site/index.html')


def load_file(filepath):
    with open(filepath, "r", encoding='UTF-8') as current_file:
        return current_file.read()


def fetch_config():
    json_data = load_file('config.json')
    return json.loads(json_data)


def generate_index_page(topics, articles, template_text):
    index_template = Template(template_text)
    for topic in topics:
        topic['articles'] = [x for x in articles if x['topic'] == topic['slug']]
    return index_template.render(topics=topics)


def generate_article_page(article, article_md_text, template_text):
    article_template = Template(template_text)
    article_text = markdown.markdown(article_md_text, extensions=['codehilite'])
    return article_template.render(acticle_content=article_text, article=article)


def write_to_file(html_data, filepath):
    with open(filepath, "w", encoding='UTF-8') as file_for_write:
        file_for_write.write(html_data)


if __name__ == '__main__':
    server = Server()
    server.watch('templates/', make_site)
    server.watch('articles/', make_site)
    server.serve(root='site/')
