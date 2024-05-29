from sqlite3 import connect

connection = connect('movies.db')
cursor = connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS movies(id INT, ad TEXT, imdb FLOAT)")
    connection.commit()
def insert_data(id, ad, imdb):
    cursor.execute("INSERT INTO movies VALUES(?, ?, ?)", (id, ad, imdb))
    connection.commit()


def get_all_movies():
    cursor.execute("SELECT * FROM movies")
    for row in cursor:
        print(row)


def update_imdb(ad, nimdb):
    cursor.execute("UPDATE movies SET imdb = ? WHERE ad = ?", (nimdb, ad))
    connection.commit()


def delete_data(ad):
    cursor.execute("DELETE FROM movies WHERE ad = ?", (ad))


create_table()

insert_data(1, 'Ada (film, 2005)', 1.0)
insert_data(2, 'Addams ailəsi (film, 1991)', 2.3)
insert_data(3, 'Ağ saray (film, 1990)', 4.5)
insert_data(4, 'Alisa artıq burada yaşamır (film, 1974)', 6.7)
insert_data(5, 'Amerika piroqu (film, 1999)', 9.3)
insert_data(6, 'Ben-Hur (film, 1959)', 8.6)
insert_data(7, 'Bir, iki, üç (film, 1961)', 8.5)
insert_data(8, 'Bleyd (film, 1998)', 8.3)
insert_data(9, 'Böyük diktator (film, 1940)', 5.5)
insert_data(10, 'Boleyn qızı (film, 2008)', 7.4)
insert_data(10, 'Böyük şəhərin işıqları (film, 1931)', 7.3)
update_imdb('Bruklin (film, 2015)', 6.3)
delete_data('Boleyn qızı (film, 2008)')

get_all_movies()

cursor.close()
connection.close()