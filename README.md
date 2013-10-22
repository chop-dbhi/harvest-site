# Harvest Site & Blog


### Layouts

#### Base
These following are the base layouts and are generally not used directly except for custom layouts (like the home page). See the page/article layouts below.

- `base` - The base template that does not contain any containers, rows or columns.
- `container` - Extends `base`. The default template to extend which provides a single container and row. Use this to create single row, column-based layouts.

#### Page/Article

The following layouts are the ones that should be used for creating pages or blog posts.

- `wide` - Extends `container`. Full-width single column.
- `standard` - Extends `container`. 8-point single column. This is the default layout for pages.
- `slim` - Extends `container`. 6-point single column.

The `default` layout is a copy of the default page layout (currently the `standard` layout). This is a simple convenience in case the underlying default layout changes in the future.

### Front-Matter Attributes

The following front-matter attributes are supported:

- `title` - The title of the page/article
- `subtitle` (optional) - The subtitle of the page/article that will be shown inline to the title
- `intro` (optional) - The intro text below the title. Intended to be short and to make a statement.
- `modified` (optional) - The last modified date. This only needs if it's necessary to point out the page has been modified.

A few extra attributes can be used for posts/articles:

- `date` (optional) - Native Jekyll attribute used for sorting articles. This should be supplied for articles.
- `category` (optional) - Native Jekyll attribute used for grouping articles. This is currently not used, but may be in the future.
- `published` (optional) - Native Jekyll attribute for determining if an article should be published for public view.
- `author` (optional) - Should only be used for writing articles. This is a simple identifier to the author's details defined in the `_config.yaml`.

**Example Page**

```markdown
---
layout: default
title: "New Page"
intro: "A swift tagline"
---

Content...
```

**Example Article**

```markdown
---
layout: default
title: "New Article"
author: byron
category: "data"
published: false
---

Content...
```

### Includes

These are the fragments that are used in layouts. Unless new layouts are being created, these do not need to be used directly.

- `page_header.html` - Renders a `.page-header` block. Takes a `title` and optional `subtitle` parameters.
- `author.html` - Renders a span of details for the post's author. This assumes the `author` front-matter variable has been specified and matches one of the authors listed in `_config.yaml`.
- `meta.html` - Renders metadata about a blog post including the author (see above include) and the publish and last update date.
