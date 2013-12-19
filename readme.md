Given page from Tom's blog, check that only a subset
of HTML is used, and check that all HREFs are URLs.
If this test passes, it is appropriate to send the
markdown file for the given page to Julia for posting
on the DataKind blog.

This is so that we can post them on the DataKind blog.

## How to use
This is what it looks like if it passes.

    $ juliadown http://thomaslevine.com/!/r-spells-for-data-wizards/
    You can send the following file to Julia for posting on the blog.
    http://github.com/tlevine/www.thomaslevine.com/blob/master/content/!/r-spells-for-data-wizards/index.md
    $ echo $?
    0

This is what it looks like if it fails.

    $ juliadown http://thomaslevine.com/!/r-spells-for-data-wizards/
    This page has the following problems.
    * Foo
    * Bar
    $ echo $?
    1

## HTML subset
The following markdown subset is allowed. Juliadown
checks the generated HTML, but 
