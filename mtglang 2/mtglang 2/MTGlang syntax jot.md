#### MTGlang syntax jot

##### format--, <> - optional, \[] - type, / - one or the other

###### keywords

permanent - const

spell = auto

card - object

library - class

mana - int

life - float

state - bool

name - string

type - char

hand - list/array

battlefield - tuple/nested list/ named nested list

token - dictionary

turn - logical expression

tap \[function] <with> \[function vars] - run function

until \[logic] resolves - while

read the card <it says<that>> \[logic] <is \[true/false]> - if

on my turn i play <a> \[var type] \[name] <for> (<\[var type] \[var name],...>) - function

i reveal my card \[name] <it has/it is a> - create object

loop - for C++ style

deck - include

play - print

read - input

exile - void

graveyard - return

###### symbols

<> - type

{} - indentations

\[] - arrays

() - order of operations/logic

"" - string/char

¬¬/↑↑ - user defined

!@ \[line] \[col] - error

\# one line note (can be in code)#

<##>

multi

line

note

<##>

; - end line

###### operations

trample - or

with - and

graveyard - not

^^ - xor

is/has - = - assignment

= - == - comparison

&#x20;\* - multiplication

&#x20;/ - division

&#x20;+ - addition

&#x20;- - subtraction

&#x20;\*^ - exponent

tapped - false

untapped - true

###### string format

/>/ - newline

:#: tab

:@: double quote

:/\[number]/: - used for variable insertion

:/%\[var name]/: - used for variable insertion

/%\[text]%|\[hex]/ - text hex value

/%\[text]%|^/ - bolds text

/%\[text]%|\&/ - italicizes text

/%\[text]%|--/ - strikethrough

/%\[text]%|^|\&/ - this is okay

\[text]/++/\[text] - connects two string into one

/\[text]|->\[splitter]<-|/ - splits text

\[text/array]/{\[id]}/ - reads location id of text or array

\~\~@>{text}<@\~\~ - ignores other text formatting

