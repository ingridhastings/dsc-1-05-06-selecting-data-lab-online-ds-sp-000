import sqlite3
connection = sqlite3.connect('planets.db')
cursor = connection.cursor()
    
def select_all_columns_and_rows():
    cursor.execute('''"SELECT * FROM planets"''')
    
def select_name_and_color_of_all_planets():
    cursor.execute(''''''"SELECT name, color FROM planets"'''''').fetchall()
    
def select_all_planets_with_mass_greater_than_one():
    cursor.execute('''"SELECT name FROM planets WHERE mass > 1"''').fetchall()
    
def select_name_and_mass_of_planets_with_mass_less_than_equal_to_one():
    cursor.execute('''"SELECT (name, mass) FROM planets WHERE mass <= 1"''').fetchall()

def select_name_and_color_of_planets_with_more_than_10_moons():
    cursor.execute('''"SELECT (name, color) FROM planets WHERE num_of_moons > 10"''').fetchall()    
    
def select_all_planets_with_moons_and_mass_less_than_one():
    cursor.execute('''"SELECT name FROM planets WHERE num_of_moons  < 1 AND mass < 1"''').fetchall()   

def select_name_and_color_of_all_blue_planets():
    cursor.execute('''"SELECT (name, color) FROM planets WHERE color = 'blue'"''').fetchall()
