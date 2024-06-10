

us_books = [["ISBN1234", "The Solar System", "Hardcover", "Science", 15.00, 5],
         ["ISBN9876", "Types of Animal Species", "Paperback", "Science", 10.00, 8],
         ["ISBN1290", "Second World War", "Hardcover", "History", 12.50, 1]]

us_magazines = [["01", "History of Cricket", "color", "Sports", 5.00, 7],
             ["02", "Evolution of the Computer", "black&white", "Technology", 3.00, 21]]

edu_dvds = [["10", "Birth of the Solar System", "Astronomy", 2.50, 10],
        ["11", "Pythagoras Theorem", "Math", 1.00, 50]]

lec_cds = [["21", "Basics of Western Music", "Music", "1.50", "11"],
       ["22", "Japanese Language", "Foreign Languages", "2.00", "3"],
       ["32", "english Language", "Foreign Languages", "4.00", "0"]]

print("\nAdding resources - 'add' \n Remove resources - 'remove' \n View currently available resources - 'vca'\nView currently unavailable resources 'vcua'\nView all resources (any type) filtered by subject 'vas' \nchooce subject write name eg-'maths' \n")

operation = input("what do you want to do ? ").lower()


class add_books:
    def __init__(self, isbn, title, format, subject, rental_price, num_copies):
        self.isbn = isbn
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price = rental_price
        self.num_copies = num_copies
        book = [isbn, title, format, subject, rental_price, num_copies]
        us_books.append(book)
        print(f"Added book: {book}")


class add_magazine :
    def __init__(self, magazine, number, title, color_or_black_and_white_print, rental_price_per_day, number_of_copies):
        self.magazine = magazine
        self.number = number
        self.title = title
        self.color_or_black_and_white_print = color_or_black_and_white_print
        self.rental_price_per_day = rental_price_per_day
        self.number_of_copies = number_of_copies
        magazine = [magazine, number, title, color_or_black_and_white_print, rental_price_per_day, number_of_copies]
        magazines.append(magazine)
        print(f"Added magazine: {magazine}")


class add_dvds:
    def __init__(self, DVD_number, title, subject, rental_price_per_day, number_of_copies):
        self.DVD_number = DVD_number
        self.title = title
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.number_of_copies = number_of_copies
        dvd = [DVD_number, title, subject, rental_price_per_day, number_of_copies]
        dvds.append(dvd)
        print(f"Added dvd: {dvd}")

class add_Lecture_CD:
    def __init__(self, CD_number, title, subject, rental_price_per_day, number_of_copies):
        self.CD_number = CD_number
        self.title = title
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.number_of_copies = number_of_copies
        cd = [CD_number, title, subject, rental_price_per_day, number_of_copies]
        cds.append(cd)
        print(f"Added cd: {cd}")
    

# remove resources
class remove_books:
    def __init__(self, isbn):
        for book in books:
            if book[0] == isbn:
                books.remove(book)
                print(f"Removed book with ISBN {isbn}")
                return
        print(f"Book with ISBN {isbn} not found")
    
class remove_magazine :
    def __init__(self, magazine):
        for mag in magazines:
            if mag[0] == magazine:
                magazines.remove(mag)
                print(f"Removed magazine with code {magazine}")
                return
        print(f"Magazine with code {magazine} not found")
    
class remove_dvds:
    def __init__(self, DVD_number):
        for dvd in dvds:
            if dvd[0] == DVD_number:
                dvds.remove(dvd)
                print(f"Removed DVD with number {DVD_number}")
                return
        print(f"DVD with number {DVD_number} not found")
    
class remove_Lecture_CD:
    def __init__(self, CD_number):
        for cd in cds:
            if cd[0] == CD_number:
                cds.remove(cd)
                print(f"Removed CD with number {CD_number}")
                return
        print(f"CD with number {CD_number} not found")



# Lend a resource
class lend_resource:
    def __init__(self, resource_type, resource_code):
        if resource_type == "books":
            for book in books:
                if book[0] == resource_code:
                    if book[5] > 0:
                        book[5] -= 1
                        print(f"Borrowed book with ISBN {resource_code}")
                        return
                    else:
                        print(f"Sorry, all copies of book with ISBN {resource_code} are currently unavailable.")
                        return
            print(f"Book with ISBN {resource_code} not found")
        elif resource_type == "magazines":
            for mag in magazines:
                if mag[0] == resource_code:
                    if mag[5] > 0:
                        mag[5] -= 1
                        print(f"Borrowed magazine with code {resource_code}")
                        return
                    else:
                        print(f"Sorry, all copies of magazine with code {resource_code} are currently unavailable.")
                        return
            print(f"Magazine with code {resource_code} not found")
        elif resource_type == "dvds":
            for dvd in dvds:
                if dvd[0] == resource_code:
                    if dvd[4] > 0:
                        dvd[4] -= 1
                        print(f"Borrowed DVD with number {resource_code}")
                        return
                    else:
                        print(f"Sorry, all copies of DVD with number {resource_code} are currently unavailable.")
                        return
            print(f"DVD with number {resource_code} not found")
        elif resource_type == "cds":
            for cd in cds:
                if cd[0] == resource_code:
                    if cd[4] > 0:
                        cd[4] -= 1
                        print(f"Borrowed CD with number {resource_code}")
                        return
                    else:
                        print(f"Sorry, all copies of CD with number {resource_code} are currently unavailable.")
                        return
            print(f"CD with number {resource_code} not found")
        else:
            print("Invalid resource type")



# view all resources filtered by subject
if operation == "vas":
    resources = input("What resource do you want to see 'BOOKS', 'MAGAZINES', 'DVDS', 'CDS', or 'ALL'? ").lower()
    subject = input("What subject are you interested in? ")
    if resources == "books" or resources == "all":
        for book in books:
            if book[-1] > 0 and book[3] == subject:
                print(book)
    if resources == "magazines" or resources == "all":
        for magazine in magazines:
            if magazine[-1] > 0 and magazine[3] == subject:
                print(magazine)
    if resources == "dvds" or resources == "all":
        for dvd in dvds:
            if dvd[-1] > 0 and dvd[2] == subject:
                print(dvd)
    if resources == "cds" or resources == "all":
        for cd in cds:
            if int(cd[-1]) > 0 and cd[2] == subject:
                print(cd)
    if resources != "books" and resources != "magazines" and resources != "dvds" and resources != "cds" and resources != "all":
        print("Invalid resource type.")


# currently available resources
if operation == "vca":
    resources = input("\nwhat resource do you want to see 'BOOKS', 'magazines', 'dvds', 'cds' or 'ALL' ?").lower()
    if resources == "all":
        for book in books:
            if book[-1] > 0:
                print("\n", book, "\n")

        for magazine in magazines:
            if magazine[-1] > 0:
                print(magazine, "\n")

        for cd in cds:
            if int(cd[-1]) > 0:
                print(cd, "\n")

        for dvd in dvds:
            if dvd[-1] > 0:
                print(dvd, "\n")

    elif resources == "books":
        for book in books:
            if book[-1] > 0:
                print(book)

    elif resources == "magazines":
        for magazine in magazines:
            if magazine[-1] > 0:
                print(magazine)

    elif resources == "cds":
        for cd in cds:
            if int(cds[-1]) > 0:
                print(cd)

    elif resources == "dvds":
        for dvd in dvds:
            if dvd[-1] > 0:
                print(dvd)



# currenly unavaleble resources
if operation == "vcua":
    resources = input("\nwhat resource do you want to see 'BOOKS', 'magazines', 'dvds', 'cds' or 'ALL' ?").lower()

    if resources == "all":

        for book in books:
            if book[-1]==0:
                print("\n", book, "\n")

        for magazine in magazines:
            if magazine[-1]==0:
                print(magazine, "\n")

        for cd in cds:
            if int(cd[-1])==0:
                print(cd, "\n")

        for dvd in dvds:
            if dvd[-1]==0:
                print(dvd, "\n")

        

    elif resources == "books":
        for book in books:
            if book[-1]==0:
                print(book)
            else:
                print("books are avelable")

    elif resources == "m":
        for magazine in magazines:
            if magazine[-1]==0:
                print(magazine)
            else:
                print("magazine are avelable")

    elif resources == "cds":
        for cd in cds:
            if int(cd[-1])==0:
                print(cd)
            else:
                print("CDS are avelable")

    elif resources == "dvds":
        for dvd in dvds:
            if dvd[-1]==0:
                print(dvd)
            else:
                print("DVDs are avelable")
#update_resource
class update_resource:
    def __init__(self, resource_list, resource_id):
        for resource in resource_list:
            if resource[0] == resource_id:
                resource[5] += 1 # Increase the number of copies available by 1
                print(f"Updated resource with ID {resource_id}")
                return
        print(f"Resource with ID {resource_id} not found")

#-------------------------------------------------------------------------------

# #-------------------------------------------------------------------------------


if operation == "add":
    r_type = input("what type of resources do you want to add eg - 'books', 'magazines', 'dvds', or 'cds'?").lower()

    if r_type =="dvds":

        dn = input("DVD N:")
        t = input("title: ")
        s = input("subject: ")
        rppd = input("rental_price_per_day: ")
        noc = input("number_of_copies:")

        add_dvds(dn, t, s, rppd, noc)

    elif r_type == "cds":

        cn = input("CD_number: ")
        t = input("title: ")
        s = input("subject: ")
        rppd = input("rental_price_per_day: ")
        noc = input("number_of_copies: ")

        add_Lecture_CD(cn, t, s, rppd, noc)


    elif r_type == "books":
        
        n = input("enter isbn: ")
        t = input("enter title: ")
        f = input("enter format: ")
        s = input("enter subject: ")
        rp = input("rental_price: ")
        nc = input("num_copies: ")

        add_books(n, t, f ,s ,rp ,nc)

    elif r_type == "m":
        
        m = input("Enter your magazine: ")
        n = input("Enter your number: ")
        t = input("ENter ypu title: ")
        c = input("color_or_black_and_white_print: ")
        r = input("rental_price_per_day: ")
        nfc = input("number_of_copies: ")

        add_magazine(m, n, t, c, r, nfc)
        


# if code for remove resources
if operation == "remove":
    resource_type = input("What resource do you want to remove 'books', 'magazines', 'dvds', or 'cds'? ").lower()
    if resource_type == "books":
        isbn = input("Enter the ISBN of the book to remove: ")
        remove_books(isbn)
    elif resource_type == "magazines":
        code = input("Enter the code of the magazine to remove: ")
        remove_magazine(code)
    elif resource_type == "dvds":
        number = input("Enter the number of the DVD to remove: ")
        remove_dvds(number)
    elif resource_type == "cds":
        number = input("Enter the number of the CD to remove: ")
        remove_Lecture_CD(number)
    else:
        print("Invalid resource type.")

# calling funtion Lend a resource
if operation == "lend":
    resource_type = input("\nwhat type of resource do you want to lend? 'books', 'magazines', 'dvds', or 'cds': ").lower()
    resource_code = input(f"\nwhat is the code of the {resource_type} you want to lend? ")
    lend_resource(resource_type, resource_code)

#update_resource
if operation == "update":
    resource_id = input("Enter the ID of the resource that was returned: ")
    if resources == "books":
        update_resource(books, resource_id)
    elif resources == "magazines":
        update_resource(magazines, resource_id)
    elif resources == "dvds":
        update_resource(dvds, resource_id)
    elif resources == "cds":
        update_resource(cds, resource_id)
    elif resources == "all":
        update_resource(books, resource_id)
        update_resource(magazines, resource_id)
        update_resource(dvds, resource_id)
        update_resource(cds, resource_id)
    else:
        print("Invalid input")
