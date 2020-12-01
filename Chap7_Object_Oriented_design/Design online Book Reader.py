
Question : Design the data structures for an online book reader system. 

- Book(name, pages)
- Shelf(size)
    *placing_a_book 
    * Removing_a_book


- BookReader():
        *read(publcation year, author, title )


class BST:
    def __init__(self,count,book):
        self.number_of_books = count
        self.book = book 
        self.left = None
        self.right = None

    def insert(self, buch):
        if not self: 
            self.book = buch
        elif self < buch:
            if not self.left:
                self.left = buch
            else:
                self.left.insert(buch)

        else:
            if not self.right:
                self.right = buch
            else:
                self.right.insert(buch)

    def get_a_book(self, buch):
        if self == buch:
            return buch 
        elif self < buch:
            self.left.get_a_book(buch)
        else:
            self.right.get_a_book(buch)
        return None 


    def remove(self, buch):
        if self == buch:
            self = None
        elif self < buch:
            self.left.remove(buch)
        else:
            self.right.remove(buch)



class Book: 
    def __init__(self, name, page,year,author):
        self.book_name = name 
        self.bookpage = page 
        self.year = year
        self.author = author
        self.key = year + author + name

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.key < other.key
    
    def __gt__(self, other):
        if isinstance(other, Book):
            return self.key > other.key

    

class Shelf:
    def __init__(self, size):
        self.size = size
        self.container = BST()

class BookReader:
    def __init__(self, book):
