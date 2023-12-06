import json
class Item:
    def __init__(self,title,creator,year):
        self.title=title
        self.creator=creator
        self.year=year
    def display_info(self):
        pass

class Book(Item):
    def __init__(self,title,creator,year,genre,isbn):
        super().__init__(title,creator,year)
        self.genre=genre
        self.isbn=isbn
    def display_info(self):
        print(f'Title: {self.title}')
        print(f'Creator: {self.creator}')
        print(f'Year: {self.year}')
        print(f'Genre: {self.genre}')
        print(f'ISBN: {self.isbn}\n')
        
class Movie(Item):
    def __init__(self,title,creator,year,genre,duration):
        super().__init__(title,creator,year)
        self.genre=genre
        self.duration=duration
    def display_info(self):
        print(f'Title: {self.title}')
        print(f'Creator: {self.creator}')
        print(f'Year: {self.year}')
        print(f'Genre: {self.genre}')
        print(f'Duration: {self.duration} minutes\n')
        
        
class Library:
    def __init__(self):
        self.items=[]
        
    def add_item(self,item):
        self.items.append(item)
        
    def display_items(self):
        for item in self.items:
            item.display_info()
            
    def save_to_file(self,file_name):
        with open(file_name, 'w') as file:
            for item in self.items:
                file.write(str(item.__dict__))
                file.write('\n')
    
    def load_from_file(self,file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                d = json.loads(line.replace("'","\""))
                if 'isbn' in d.keys():
                    b = Book(d['title'],d['creator'],d['year'],d['genre'],d['isbn'])
                    self.items.append(b)
                else:
                    m = Movie(d['title'],d['creator'],d['year'],d['genre'],d['duration'])
                    self.items.append(m)
                    
    def recommend(self,movie):
        for item in self.items:
            if(isinstance(item,Movie) and item.genre==movie.genre and item.title!=movie.title):
                item.display_info()
    
    
    
library = Library()

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", "978-3-16-148410-0")
movie = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148)

library.add_item(book)
library.add_item(movie)

# Wyświetl informacje o przedmiotach w bibliotece
library.display_items()

# OUT:
# Title: The Great Gatsby
# Creator: F. Scott Fitzgerald
# Year: 1925
# Genre: Classic
# ISBN: 978-3-16-148410-0

# Title: Inception
# Creator: Christopher Nolan
# Year: 2010
# Genre: Sci-Fi
# Duration: 148 minutes

# # Zapisz informacje do pliku i wczytaj z powrotem
library.save_to_file("library_data.json")

new_library = Library()
new_library.load_from_file("library_data.json")

# # Wyświetl informacje o przedmiotach w nowej bibliotece
new_library.display_items()

# # Zawartosć pliku:
# Title: The Great Gatsby
# Creator: F. Scott Fitzgerald
# Year: 1925
# Genre: Classic
# ISBN: 978-3-16-148410-0

# Title: Inception
# Creator: Christopher Nolan
# Year: 2010
# Genre: Sci-Fi
# Duration: 148 minutes


movie2 = Movie("Interstellar", "Christopher Nolan", 2014, "Sci-Fi", 169)
movie3 = Movie("Shutter Island", "Martin Scorsese", 2010, "Mystery", 138)
movie4 = Movie("Star Wars - New Hope", "George Lucas", 1977, "Sci-Fi", 121)

new_library.add_item(movie2)
new_library.add_item(movie3)
new_library.add_item(movie4)

print("Rekomendacje dla Inception:\n")
new_library.recommend(movie)

