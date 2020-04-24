import sys

class TableFormatter:

    def __init__(self, outfile=None):
        self.outfile = outfile
        if not self.outfile:
            self.outfile = sys.stdout

    def headings(self, headers):
        raise NotImplementedError

    def entry_row(self, data):
        raise NotImplementedError


class TextTableFormatter(TableFormatter):

    def __init__(self, outfile=None, width=10):
        super().__init__(outfile)
        self.width = width

    def headings(self, headers):
        for header in headers:
            print('{0:>{1}s}'.format(header, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)

    def entry_row(self, data):
        for row in data:
            print('{0:>{1}s}'.format(row, self.width), end=' ', file=self.outfile)
        print(file=self.outfile)


class CVTableFormatter(TextTableFormatter):

    def headings(self, headers):
        print(','.join(headers))

    def entry_row(self, data):
        print(','.join(data)) 
        

class QuotedMixin(object):
    def entry_row(self, data):
        quoted = ['"{}"'.format(d) for d in data]
        super().entry_row(quoted)

class CustomFormatter(TextTableFormatter, QuotedMixin):
    pass        

def print_table(objects, columns, formatter):
    formatter.headings(columns)
    for obj in objects:
        row_data = [str(getattr(obj, col)) for col in columns]
        formatter.entry_row(row_data)