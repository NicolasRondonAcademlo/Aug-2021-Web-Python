class Article:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return  self.title



a = Article("Hola como van")
print(a.title)
class Article:
    def __init__(self,title):
        self.title = title

    @property
    def title(self):
        return  self.title
