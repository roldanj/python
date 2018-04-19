collectionOfBooks = ["The Alchemist", "How to win friends and influence people", "the seven habits of highly effective people"]
print("Enter the name of the book: ")
bookToBeChecked = input()
for book in collectionOfBooks:
    if book == bookToBeChecked:
        print("Yes I do have that book!")
        break
    else:
        print("No, I do not have that book!")