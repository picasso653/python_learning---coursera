class MyFirstClass():
    print("Who wrote this book?")
    index = "Author-Book"
    def hand_list(self,philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + ' wrote the book ' + book)

whodunnit = MyFirstClass()

print(whodunnit.hand_list('Sun Tzu', 'The Art of War'))