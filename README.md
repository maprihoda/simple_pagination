# Simple Pagination

A utility class, a pager method and a jinja2 macro for paging query results and generating page links. Can be used with Google App Engine (GAE).

The utility class is the PageLinks class found in the page_links.py file. The class's initialization method accepts the following parameters:

    page:           The current page
    total_items:    The total number of items
    per_page:       The number of items per page
    url_root:       The start of the URL assigned to each page.
    page_field:     The name of the URL parameter to use for pages
    page_range:     The number of pages to show (should be odd)


## Example Usage (GAE specific)

Simply copy the page_links.py file into your GAE project root.
In your project's base handler (base controller) class, create a pager method:

    form page_links import PageLinks

    class BaseHandler(webapp.RequestHandler):

        # ...other code...

        def pager(self, query, page, total_items, per_page, url_root, page_field='pg', page_range= 9):
            try:
                page = int(page)
            except ValueError:
                page = 1

            entities = query.fetch(per_page, (page - 1) * per_page)

            pagination_links = PageLinks(
                page,
                total_items,
                per_page,
                url_root,
                page_field,
                page_range
            )

            pagination_links = pagination_links.get_links()
            return entities, pagination_links


Then, in your handlers, you can use the pager method as follows:

    class Recruiters(BaseHandler):
        per_page = 20

        def get(self):
            # ...other code...

            page = self.request.get('pg')
            query = company.recruiters

            recruiters, pagination_links = self.pager(
                query,
                page,
                query.count(),
                self.per_page,
                '/a/recruiters',
            )


You can also use the following Jinja2 macro in your templates:

    {% macro pagelinks(pagination_links) %}
    <div id="pagelinks">
    {% for link in pagination_links %}
       {{ link }}
    {% endfor %}
    </div>
    {% endmacro %}


You can see Simple Pagination in action on [Aktuální nabídky práce](http://www.aktualninabidkyprace.cz/). It's a simple job board built on [Google App Engine](http://code.google.com/appengine/).


## Credits

The PageLinks class is an adapted version of a utility class from the he3-appengine-lib project (http://code.google.com/p/he3-appengine-lib/wiki/PageLinks)

