class Main:
    """Class recalculate index"""
    def __init__(self, list_):
        """Initialisation method"""
        self.list_ = list_

    def __getitem__(self, item):
        """Get item method"""
        try:
            return self.list_[item - 1]
        except IndexError:
            print('Index out of range!')

    def __setitem__(self, key, value):
        """Set item method"""
        try:
            self.list_[key-1] = value
        except IndexError:
            print('Key out of range!')

    def __str__(self):
        """String method"""
        return f'{self.list_}'


