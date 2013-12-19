import markdown2
import lxml.html
import urllib2

VALID_TAGS = {
    'strong',
    'h1', 'h2', 'h3', 'h4',
    'p',
    'img',
}

def is_juliadown(text):
    '''
    >>> is_juliadown('# Foo nbar**baz**huhu')
    (True, None)

    >>> is_juliadown('# italics are *not* allowed.')
    (False, 'There is a "em" tag.')
    '''
    html_text = markdown2.markdown(text)
    html = lxml.html.fromstring(html_text)
    for tag in html.iterdescendants():
        if tag.tag not in VALID_TAGS:
            return False, 'There is a "%s" tag.' % tag.tag
    return True, None

def remove_yaml(fp):
    fp.readline() # First line is ---
    for line in fp:
        if re.match(r'^-+$', line):
            # Stop on the second ---
            break

def download(raw_url):
    exclamation_url = raw_url.split('/!/')[1]
    url = 'https://raw.github.com/tlevine/www.thomaslevine.com/master/content/!/' + exclamation_url
    fp = urllib2.urlopen(url)
    return fp

def main():
    import sys
    url = sys.argv[1]
    fp = download(url)
    remove_yaml(fp)
    result, message = is_juliadown(fp.read())
    if result:
        exit(0)
    else:
        print(message)
        exit(1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # main()
