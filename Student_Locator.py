import json

# Program that makes a specific serch for individuals that
# have a high average final grade from high school. In this case
# I practiced searching for males wiht a certain final avarage.
# Copyright (C) 2020  David Josué Marcial Quero

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA  02110-1301, USA.
# Also available at https://www.gnu.org/licenses/old-licenses/gpl-2.0.html


selection = []
lowest_year = 1995
actual_period = "2016"
# Oaxaca, Nuevo León, Mexico City
close_states = ('OC', 'NL', 'DF')
grade_limit = 9.9

#To reduce the ammount of 
def isMale(curp):
    try:
        sex = curp[10]
    except IndexError:
        print(f"Curp is too short, {curp}")
        return False

    return sex == 'H'
    # return True


def isSameAge(curp):
    try:
        two_year = int(curp[4:6])
    except ValueError:
        print(f"Wrong year, {curp}")
        return False

    year = 1900 + two_year
    if two_year < 20:
        year = 2000 + two_year
    return year > lowest_year


def isClose(curp):
    state = curp[11:13]

    return state in close_states


def thisGeneration(period):
    generation = period[:4] == actual_period
    return generation


def hasAverage(grade):
    num_grade = float(grade)
    return num_grade >= grade_limit


for i in range(1, 201):
    name = f"certificate_data_{i:03}.json"

    with open(name, "r") as json_part:
        json_data = json.load(json_part)
    # CURP is no longer available in the High School certificate
    # therefore, I can no longer obtain the name, age and location
        for person in json_data['people_list']:
            curp = person['curp']
            grade = person['promedio']
            period = person['periodo']
            if (isMale(curp) and isSameAge(curp) and isClose(curp) and
                    hasAverage(grade) and thisGeneration(period)):

                selection.append(person)

with open('the_list.txt', 'w') as list_text:
    list_text.write(f"THE ANSWER TO LIFE, THE UNIVERSE, AND EVERYTHING\n\n")
    for person in selection:
        curp = person['curp']
        list_text.write(f"{person['nombre']}, {curp[11:13]}\n")
        list_text.write(f"{curp[8:10]}/{curp[6:8]}/{curp[4:6]}\n")
        list_text.write(f"{person['plantel']}\n")
        list_text.write(f"Promedio: {person['promedio']}\n\n")

    list_text.write(f"-------------------------------------\n\n")
    list_text.write(f"Total obtained: {len(selection)}")

print(f"Total obtained: {len(selection)}")
