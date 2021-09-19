import pprint
cata = {'name': 'Zophie', 'age': 7, 'color': 'gray'}

allCats = []
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})
allCats.append({'name': 'Pooka', 'age': 5, 'color': 'blck'})
allCats.append({'name': 'Fat-Fail', 'age': 5, 'color': 'gray'})
allCats.append({'name': 'Zophie', 'age': 7, 'color': 'gray'})

##################################################################

theBoard = {'top-L': '', 'mid-M': '', 'low-L': '', 'top-M': '',
            'mid-M': '', 'low-M': '', 'top-R': '', 'mid-R': '', 'low-R': ''}
pprint.pprint(theBoard)
theBoard['mid-M'] = 'X'
pprint.pprint(theBoard)
theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('---------------------------------------------------------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('---------------------------------------------------------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


type(42)  # class Int
type('hello')  # class String
type(3.14)  # class Float
type(theBoard)  # class Dict

text = 'That is Alice cars'
text = 'That is Alice`s cars'
print('Hello there!\n How are you? \n I\'m fine.')
print(r'That is Carlos\'s cat')
spam = """ Dear Alice, Eves cat has been arrested for catnapping, cat burglary, and extortion. Sincerely, Bob. """

"""
- Strings can begin and end with double quotes.
- Espace characters let you put quotes and other characters that are hard to type inside strings.
- Raw strings will literally print any backslashes in the string and ignore espace characters.
- Multiline strings being and end with three quotes, and can span multiple lines.
- Indexes, slices, and the in and not in operators all work with strings.
"""
recruiting@nativoplus.com
JVELEZ@VELEZLAWGROUP.COM
