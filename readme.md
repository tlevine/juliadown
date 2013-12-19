Given page from Tom's blog, check that only a subset
of HTML is used, and check that all HREFs are URLs.
If this test passes, it is appropriate to send the
markdown file for the given page to Julia for posting
on the DataKind blog.

This is so that we can post them on the DataKind blog.

## How to use
This is what it looks like if it passes.

    $ juliadown http://github.com/tlevine/www.thomaslevine.com/blob/master/content/\!/r-spells-for-data-wizards/index.md
    $ echo $?
    0

This is what it looks like if it fails.

    $ juliadown http://github.com/tlevine/www.thomaslevine.com/blob/master/content/\!/r-spells-for-data-wizards/index.md
    There is a "pre" tag.
    $ echo $?
    1

## Markdown subset
Only the following markdown is allowed. All HTML is valid markdown,
but this stuff must be written in the non-HTML markdown.

* Headers (`#`, `##`, &c.)
* Paragraphs (`\n\n`)
* Strong (`**`)
* Images (`![alt text](url)`)
* Links (`[text](url)`)
