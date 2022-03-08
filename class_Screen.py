class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Wrong Type')
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise ValueErrot('Wrong Type')
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height