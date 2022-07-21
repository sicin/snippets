import os
import mammoth
import re
from docx_to_html_variables import block_1, block_2, block_2_no_button

docx_dir_path = "../"
html_dir_path = "../"
a_style = 'style="color: #98FB98;"'


def get_button_text(content):
    button_text = re.search(
        r'<table><tr><td><p>.+</p></td></tr></table>', content)
    button_text = button_text.group(0)
    button_text = re.sub(
        r'<table><tr><td><p>(.+)</p></td></tr></table>', '\g<1>', button_text)
    return button_text


def get_bellow_button_text(content):
    below_button_text = re.search(
        r'</td></tr></table>(.+|)</div>', content)
    below_button_text = below_button_text.group(0)
    below_button_text = re.sub(
        r'</td></tr></table>(.+|)</div>', '\g<1>', below_button_text)
    return below_button_text


def get_content(below_button_text, button_text, content):
    content = re.sub(
        r'(</td></tr></table>).+(</div>)', '\g<1>\g<2>', content)
    content = content.replace(
        'PLACEHOLDER2', below_button_text)
    content = re.sub(
        r'<table><tr><td><p>.+</p></td></tr></table>', '', content)
    content = content.replace('PLACEHOLDER1', button_text)
    return content


def get_base_content(content):
    content = re.sub(
        r'FNAME', '<span th:utext="${firstName}"></span>', content, flags=re.I)
    content = re.sub(r'<a\W+href', f'<a {a_style} href', content)
    content = re.sub(
        r'<p>.+Subject:.+<\/p>(<p>.*<span th:)', '\g<1>', content)
    return content


def process_buttons(content, messages, new_file_name):
    below_button_text = get_bellow_button_text(content)
    button_text = get_button_text(content)
    content = get_content(below_button_text, button_text, content)
    print(
        f"File = {new_file_name}\nButton = {button_text}\nBelow button = {below_button_text}\nErrors = {messages}\n\n")
    return content


def build_full_html(html_text, is_button_html):
    return (block_1 + html_text + block_2) if is_button_html else (block_1 + html_text + block_2_no_button)


def process_raw_html_file(result):
    messages = result.messages
    html_text = re.sub(" +", " ", result.value)
    is_button_html = bool(re.search('<table><tr><td><p>', html_text))
    full_html = build_full_html(html_text, is_button_html)
    new_file_name = html_dir_path + file[:-5] + ".html"
    with open(new_file_name, "w", encoding="utf-8") as html_file:
        html_file.write(full_html)
    with open(new_file_name, "r") as f:
        content = get_base_content(f.read())
        if is_button_html:
            content = process_buttons(content, messages, new_file_name)
        else:
            print(
                f"File = {new_file_name}\nNO BUTTON\nErrors = {messages}\n\n")
    print(content, file=open(new_file_name, "w"))


for file in os.listdir(docx_dir_path):
    if file.endswith(".docx"):
        with open(os.path.join(docx_dir_path, file), "rb") as docx_file:
            process_raw_html_file(mammoth.convert_to_html(docx_file))
