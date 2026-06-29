import re

def remove_comments(html):
    return re.sub(r'<!--[\s\S]*?-->', '', html)


def remove_calibre_classes(html):
    return re.sub(r'\sclass="calibre[^"]*"', '', html)


def remove_inline_styles(html):
    return re.sub(r'\sstyle="[^"]*"', '', html)


def remove_empty_spans(html):
    return re.sub(
        r'<span\b[^>]*>\s*</span>',
        '',
        html,
        flags=re.I
    )


def clean_basic(html):
    html = remove_comments(html)
    html = remove_calibre_classes(html)
    html = remove_inline_styles(html)
    html = remove_empty_spans(html)
    return html
