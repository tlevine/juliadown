import markdown2
import lxml.html

def is_juliadown(text):
    html_text = markdown2.markdown(text)
    html = lxml.html.fromstring(html_text)
    for tag in html.iterdescendants():
        if tag.tag not in VALID_TAGS:
            return False, 'There is a %s tag' % tag.tag
    return True, None

def remove_yaml(fp):
    fp.readline() # First line is ---
    for line in fp:
        if re.match(r'^-+$', line):
            # Stop on the second ---
            break
