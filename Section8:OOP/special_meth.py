# Dunder methods/Special methods

class Book():
    def __init__(self, title, author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    # __str__ allows the class to return a string representation of an instance of itself as opposed to returning an object with its location in memory
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book has been deleted')

bookOne = Book('Sherlock Holmes', 'Arthur Conan Doyle', 900)
print(bookOne)
print(len(bookOne))
del bookOne
# print(bookOne) error checking


    
