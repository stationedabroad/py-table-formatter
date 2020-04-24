class Holdings:

    def __init__(self, name, price, _class):
        self.name = name
        self.price = price
        self._class = _class



columns = ['name', 'price', '_class']

portfolio = []
a = Holdings('CAT', 66.99, 'Auto')
b = Holdings('MSFT', 102.98, 'Tech')
c = Holdings('IBM', 100.22, 'Tech')
d = Holdings('GE', 234.99, 'Util')

portfolio.append(a)
portfolio.append(b)
portfolio.append(c)
portfolio.append(d)