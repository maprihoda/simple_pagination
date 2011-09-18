# coding: utf-8

class PageLinks:
    def __init__(self, page, total_items, per_page, url_root, page_field='pg', page_range=9):
        '''
        page:           The current page
        total_items:    The total number of items
        per_page:       The number of items per page
        url_root:       The start of the URL assigned to each page.
        page_field:     The name of the URL parameter to use for pages
        page_range:     The number of pages to show (should be odd)
        '''

        self.page = page

        page_count = total_items / per_page
        if total_items % per_page != 0: page_count += 1

        # page_count: The total number of pages
        self.page_count = page_count
        self.url_root = url_root
        self.page_field = page_field
        self.page_range = page_range


    def get_links(self):
        first_symbol = '&' if self.url_root.count('?') else '?'

        pages = range(1, self.page_count+1)

        if self.page_range < self.page_count:

            middle = self.page_range / 2

            if self.page_range % 2 != 0:
                    middle += 1

            if self.page < 1 + self.page_range:
                pages = range(1, 1 + self.page_range)

            elif self.page > self.page_count - self.page_range:
                pages = range(self.page_count - self.page_range + 1, self.page_count + 1)

            else:
                starting_page = self.page - middle + 1
                pages = range(starting_page, starting_page + self.page_range)


            page_links = []

            for p in pages:
                if p != self.page:
                    page_links.append(u'<a href="%s%s%s=%d">%d</a>' % (self.url_root, first_symbol, self.page_field, p, p))
                else:
                    page_links.append(u'<strong>%d</strong>' % p)

        else:
            page_links = []
            for p in pages:
                if p != self.page:
                    page_links.append(u'<a href="%s%s%s=%d">%d</a>' % (self.url_root, first_symbol, self.page_field, p, p))
                else:
                    page_links.append(u'<strong>%d</strong>' % p)


        if self.page != 1:
            prev_link  = u'<a href="%s%s%s=%d">&lsaquo; Předchozí</a>' % (self.url_root, first_symbol, self.page_field, self.page-1)
            page_links.insert(0, prev_link)

        if self.page != self.page_count:
            next_link = u'<a href="%s%s%s=%d" title="další">Další &rsaquo;</a>' % (self.url_root, first_symbol, self.page_field, self.page+1)
            page_links.append(next_link)


        return page_links

