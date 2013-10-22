# Contributing/Guidelines

## Tickets

For new blog posts, documentation additions, and spelling or grammar fixes no separate ticket needs to be created since the pull request (see below) provides that facility. For more significant changes such as reorganization of documentation or addition of new sections, open a ticket first to ensure everyone is in agreement to the changes.

## Pull Requests

If you _do_ have write permissions to the repository, create a branch off of `gh-pages` with the new or updated content and send a pull request.

If you _do not_ have write permissions to the repository, you can:

- Create or edit the file on the site (it will automatically create a fork and pull request for you)
- Fork it and create a branch off of `gh-pages`

## Conventions

### Markdown Everywhere

HTML can be embedded in markdown files, so always use Markdown.

### Prefixed Links

Prefix site URLs with `{{ site.baseurl }}` to ensure the absolute paths relative to the domain. Always assume the `baseurl` has a trailing slash `/`.

**Example**

```
{{ site.baseurl }}demo/
```

### Page URLs

To create site pages, create a new directory with an `index.md` file so URLs are _pretty_, i.e. they do not contain an `.html` suffix.

```
demo/
    index.md
download/
    index.md
```

One exception is `articles/index.html` which must be an HTML page [for Jekyll pagination to work](http://jekyllrb.com/docs/pagination/).