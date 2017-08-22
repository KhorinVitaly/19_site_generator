from jinja2 import Environment, select_autoescape, FileSystemLoader
import json
import markdown
import re
from livereload import Server
from os.path import join, sep


def make_site():
    config_dict = fetch_config()
    topics = config_dict['topics']
    articles = config_dict['articles']

    jinja_env = get_jinja_env()

    for article in articles:
        article_md = load_file(join('articles', article['source']))
        article_html = generate_article_page(article, article_md, jinja_env)
        re_result = re.search(r'\w+.(\w+)', article['source'])
        group_index = 1
        file_name = re_result.group(group_index)
        path_to_html = file_name + '.html'
        write_to_file(article_html, join('site', path_to_html))
        article['html_source'] = path_to_html

    index_page_text = generate_index_page(topics, articles, jinja_env)
    write_to_file(index_page_text, join('site', 'index.html'))


def load_file(filepath):
    with open(filepath, "r", encoding='UTF-8') as current_file:
        return current_file.read()


def fetch_config():
    json_data = load_file('config.json')
    return json.loads(json_data)


def get_jinja_env():
    return Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(
        enabled_extensions=('html', 'xml'),
        default_for_string=True)
    )


def generate_index_page(topics, articles, jinja_env):
    index_template = jinja_env.get_template('index_template.html')
    for topic in topics:
        topic['articles'] = [x for x in articles if x['topic'] == topic['slug']]
    return index_template.render(topics=topics)


def generate_article_page(article, article_md_text, jinja_env):
    article_template = jinja_env.get_template('article_template.html')
    article_text = markdown.markdown(article_md_text, extensions=['codehilite'])
    return article_template.render(acticle_content=article_text, article=article)


def write_to_file(html_data, filepath):
    with open(filepath, "w", encoding='UTF-8') as file_for_write:
        file_for_write.write(html_data)


if __name__ == '__main__':
    make_site()
    server = Server()
    server.watch(join('templates', sep), make_site)
    server.watch(join('articles', sep), make_site)
    server.serve(root=join('site', sep))
