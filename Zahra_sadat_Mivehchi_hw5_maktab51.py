class Book:

    def __init__(self, title, author, publish_year, pages, language, price, media_type):
        """

        :param title: presents title of the book
        :param author:presents author of the book
        :param publish_year: presents publish year of the book
        :param pages: presents number of book pages
        :param language: presents language of the book
        :param price: presents price of the book
        :param media_type: present type of media 
        :param read_pages: presents read pages of the book
        :param percent: present progress that frist = 0
        """
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.media_type = media_type
        self.percent = 0

    def Read(self):
        """
        This function take the number of read and left pages of book
        :param pages: presents the read pages by user
        """
        self.read = int(input('Enter the number of pages you read: '))
        while self.read > self.pages:
            self.read = int(input('The number of pages read is more than the number of pages in the book, please re-enter: '))
            
        return self.read

    def Get_status(self):
        """
        This function show whether the book is in read,unread or reading state
        :return:
        """
        if self.read == 0:
            self.status = 'unread'
        elif self.read < self.pages:
            self.status = 'reading'
        elif self.read == self.pages:
            self.status = 'finished'
        
        return self.status

    def __str__(self):
        return f'\nBook information:\n    name:{self.title}\n    aouthor:{self.author}\n    media type:{self.media_type}\
                \n    publish year:{self.publish_year}\n    pages:{self.pages}\n    media type:{self.media_type}\
                \n    language:{self.language}\n    price:{self.price}\
                \n    read:{self.read}\n    status:{self.status}'


class Magazine(Book):

    def __init__(self, title, issue, author, publish_year, pages, language, price, media_type):
        self.issue = issue
        Book.__init__(self, title, author, publish_year, pages, language, price, media_type)

    def Read(self):
        #just call parent Read function
        Book.Read(self)
    
    def Get_status(self):
        #just call parent Get_status function
        Book.Get_status(self)

    def __str__(self):
        #override and call parent __str__ function
        return Book.__str__(self)+f'\n    issue:{self.issue}'
        

class Podcast(Book):
    """
    In this class is child of Book and parent of Audiobook and present podcast episode.
    """
    def __init__(self, title, speaker, publish_year, time, price, language, default_val, default_val1, media_type):
        self.speaker = speaker
        self.time = time
        Book.__init__(self, title, default_val1, publish_year, default_val, language, price, media_type)
        
    def Listen(self):
        """
        This function take the number of listen and left time of podcast
        :param listen: presents the listen minuets by user
        """
        self.listen = int(input('Please enter the amount of time you listened to the podcast(In minutes): '))
        while self.listen > self.time:
            self.listen = int(input('The minutes of time is more than the number of minutes in the podcast, please re-enter'))
            
        return self.listen

    def Get_status(self):
        #override function
        if self.listen == 0:
            self.status = 'not listen'
        elif self.listen < self.time:
            self.status = 'listenning'
        elif self.listen == self.time:
            self.status = 'finished'
        

        return self.status

    def __str__(self):
        #override function
        return f'\nPodcast information:\n    name:{self.title}\n    speaker:{self.speaker}\n    media type:{self.media_type}\
                \n    publish year:{self.publish_year}\n    time:{self.time}\
                \n    language:{self.language}\n    price:{self.price}\
                \n    listen:{self.listen}\n    status:{self.status}'


class AudioBook(Podcast):

    def __init__(self, title, speaker, publish_year, time, price, author, pages, media_type, book_language, audio_language, default_val):
        self.book_language = book_language
        self.audio_language = audio_language
        Podcast.__init__(self, title, speaker, publish_year, time, price, default_val, author, pages, media_type)

    def Listen(self):
        Podcast.Listen(self)

    def Get_status(self):
        Podcast.Get_status(self)
    
    def __str__(self):
         return f'\naudiobook information:\n    name:{self.title}\n    author:{self.author}\n    publish year:{self.publish_year}\
                    \n    pages:{self.pages}\n    book language:{self.book_language}\n    audio language:{self.audio_language}\
                        \n    price:{self.price}\n    listen:{self.listen}\n    speaker:{self.speaker}\n    status:{self.status}\
                            \n    time:{self.time}\n    media type:{self.media_type}'


def get_data():
    """
    This Function get data from user
    """
    if check_point == 1:
        title = input('Enter title: ')
        author = input('Enter author: ')
        publish_year = input('Enter publish year: ')
        pages = int(input('Enter pages: '))
        language = input('enter language: ')
        price = input('Enter price: ')
        media_type = 'book'

        return title, author, publish_year, pages, language, price, media_type
    
    if check_point == 5:
        title = input('Enter title: ')
        author = input('Enter author: ')
        publish_year = input('Enter publish year: ')
        pages = int(input('Enter pages: '))
        language = input('Enter language: ')
        price = input('Enter price: ')
        issue = input('Enter issue: ')
        media_type = 'magazine'
      
        return title, issue, author, publish_year, pages, language, price, media_type
    
    if check_point == 6:
        title = input('Enter title: ')
        speaker = input('enter speaker: ')
        publish_year = input('Enter publish year: ')
        time = int(input('enter time: '))
        language = input('enter language: ')
        price = input('Enter price: ')
        media_type = 'podcast'
    
        return title, speaker, publish_year, time, price, language, media_type
    
    if check_point == 7:
        title = input('Enter title: ')
        author = input('Enter author: ')
        publish_year = input('Enter publish year: ')
        pages = int(input('Enter pages: '))
        price = input('Enter price: ')
        speaker = input('Enter speaker: ')
        time = int(input('enter time: '))
        book_language = input('enter book language: ')
        audio_language = input('enter audio language: ')
        media_type = 'audiobook'
    
        return title, speaker, publish_year, time, price, author, pages, media_type, book_language, audio_language


def Progress():
    """
        This function calculate progress in reading or listening media
        :return: progress in percentage
        """
    title = input('\nEnter media name for computing its percent: ')
    for obj in shelf:
        if title == obj.title:
            if obj.media_type == 'book' or obj.media_type == 'magazine':#becouse book and magazine have read attr
                obj.percent = (obj.read/obj.pages)*100
                break
            elif obj.media_type == 'podcast' or obj.media_type == 'audiobook':#becouse podcast and audiobook have listen attr
                obj.percent = (obj.listen/obj.time)*100
                break
            else:
                pass
    return f'\n{obj.title} {obj.media_type} progress is {obj.percent}%'

shelf = [] # keeps all media types in a list(objs of different classes:Book,Magazine,Podcast,AudioBook)
while True:
    '''
        show menu and choice an item...
    '''
    check_point = int(input('\n1-Add book to bookshelf\n2-Update read pages\n3-Get status\n4-show my Collection\n5-Add magazin to magazinshelf\
                                \n6-Add podcast to podcast library\n7-Add audiobook in audiobook library\n8-cempute progress\
                                    \n9-See sorted shelf based on progress\n10-See (media type-title-percent)\
                                        \n0-exit\nchoice a item from menu(just a number): '))

    if check_point == 0:
        break

    elif check_point == 1:
        #for add book
        my_title, my_author, my_publish_year, my_pages, my_language, my_price, my_media_type = get_data()
        book = Book(my_title, my_author, my_publish_year, my_pages, my_language, my_price, my_media_type)
        book.Read()
        book.Get_status()
        shelf.append(book)
        print('-------otput------\n',book)
        print('\n>>>>>>>>>!!one book add in bookshelf sucsessful!!\n')
    
    elif check_point == 2:
        #for update read pages
        which_book = input('Enter the name of the book you want to update the pages you read: ')
        for book in shelf:
            if book.title == which_book:
                book.Read()
                book.Get_status()
                print('\n>>>>>>>>>!!read pages up to date successfully!!\n')

    elif check_point == 3:
        #for show status
        which_book = input('Enter the name of the book you want see its status: ')
        for book in shelf:
            if book.title == which_book:
                print(f'\n>>>>>>>>>!!This book is in {book.status} status!!\n')
    
    elif check_point == 4:
        #for show all shelf
        for item in shelf:
            print(item.__str__())

    elif check_point == 5:
        #for add magazine
        my_title, my_issue, my_author, my_publish_year, my_pages, my_language, my_price, my_media_type = get_data()
        magazine = Magazine(my_title, my_issue, my_author, my_publish_year, my_pages, my_language, my_price, my_media_type)
        magazine.Read()
        magazine.Get_status()
        shelf.append(magazine)
        print('-------otput------\n')
        print(magazine.__str__())
        print('\n>>>>>>>>>!!one magazine add in magazineshelf sucsessful!!\n')

    elif check_point == 6:
        #for add podcast
        my_title, my_speaker, my_publish_year, my_time, my_price, my_language, my_media_type = get_data()
        default_val = None
        default_val1 = None
        podcast = Podcast(my_title, my_speaker, my_publish_year, my_time, my_price, my_language, default_val, default_val1, my_media_type)
        podcast.Listen()
        podcast.Get_status()
        shelf.append(podcast)
        print('-------otput------\n')
        print(podcast.__str__())
        print('\n>>>>>>>>>!!one podcast add in podcastlibrary sucsessful!!\n')

    elif check_point == 7:
        #for add audiobook
        my_title, my_speaker, my_publish_year, my_time, my_price, my_author, my_pages, my_media_type, my_book_language, my_audio_language = get_data()
        default_val = None
        audiobook = AudioBook(my_title, my_speaker, my_publish_year, my_time,my_price, my_author, my_pages, my_media_type\
                                , my_book_language, my_audio_language, default_val)
        audiobook.Listen()
        audiobook.Get_status()
        shelf.append(audiobook)
        print('-------otput------\n')
        print(audiobook.__str__())
        print('\n>>>>>>>>>!!one audiobook add in audiolibrary sucsessful!!\n')

    elif check_point == 8:
        #for show percent of media
        print(Progress())

    elif check_point == 9:
        #for show sorted shelf with all attr
        for item in shelf:
            Progress()
        newlist = sorted(shelf, key=lambda x: x.percent, reverse=True)
        for item in newlist:
            print(item.__str__()+f'\n    persent:{item.percent}')
    
    elif check_point == 10:
        #for show sorted shelf with 3 attr :media type, title, percent
        for item in shelf:
            Progress()
        newlist = sorted(shelf, key=lambda x: x.percent, reverse=True)
        for item in shelf:
            print(item.media_type+'...'+item.title+'...'+item.percent)