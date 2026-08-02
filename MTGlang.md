# MTGlang docs

## introduction (1)

### what this is(1.1)

MTGlang is a passion project esolang (esoteric language) created in python that aims to read like a game of magic the gathering, with keywords like "I reveal my card" to create objects. it will likely only have one or two versions and once complete will be put on GitHub. being an esolang it does odd some odd characters (being " ` |") it is not designed for speed and will take a while to run. many keywords are used differently based on the context and the code isn't short. for example -

read it, `trained orgg` has a counterspell Tapped, so

|card 1 is "shatter"

|play (1)

if (var == not False):

&#x09;a = "shatter"

&#x09;print (a)

### basic keywords(1.2)

Name

State

Mana

Health

Hand

Play

Types

Read it,

Stack

(Do) until \_\_\_ (resolves/is not true)

If I play

Library

Flying

Draw

Enchantment(s)

I can

(I) Reveal (my) card

## simplified definitions \& python comparisons(2)

### data types(2.1)

#### simple(2.1.1)

##### Name(2.1.1.1)

the name keyword is used during the initiation of a string variable.

##### State(2.1.1.2)

the state keyword is used to initiate a Boolean variable. The 2 sates are;

* untapped (true)
* tapped (false)

##### Mana(2.1.1.3)

mana is the keyword used to initiate a integer variable.

##### Health(2.1.1.4)

health is used to initiate a floating-point number variable.

#### complex(2.1.2)

##### Hand(2.1.2.1)

the hand keyword is used to initiate a list, and has 2 additional operators;

* discard
* draw

those will be gone over in a different section.

##### I declare(2.1.2.2)

the i declare function can be used to create a logical expression variable, these are essentially a tiny function that is made up purely of logical operators, comparisons, and variables. more detail will be given in the full definition.

##### Reveal card(2.1.2.3)

the reveal card function creates an object.

### loops and logic(2.2)

#### set duration(2.2.1)

##### read it(2.2.1.1)

read it is MTGlang's equivalent for an if statement.

##### stack(2.2.1.2)

stack is the for loop in MTGlang.

#### variable duration(2.2.2)

##### until(2.2.2.1)

this is the equivalent of while.

##### if i play(2.2.2.2)

if i play is how you define a function in MTGlang.

### operations(2.3)

#### Boolean(2.3.1)

##### kicker(2.3.1.1)

kicker is MTGlang's and operator.

##### counterspell(2.3.1.2)

counterspell is the same as a not operator.

##### trample(2.3.1.3)

trample is the or command in this language.

##### split(2.3.1.4)

split is the equivalent of XOR in MTGlang.

#### mathematical and comparisons(2.3.2)

MTGlang uses the same mathematical and comparison symbols as python.

EXCEPT:

== is replaced with =

and = is replaced with is

### other(2.4)

#### grouping \& enclosing(2.4.1)

##### operational order(2.4.1.1)

unknown until coding finished.

##### notes(2.4.1.2)

in MTGlang notes can be written by enclosing the text you want to be a note in these ''

##### variable names(2.4.1.3)

in MTGlang there are many keywords, so for consistency all variable names must be enclosed like so; `name`. because of this, you may have spaces in your variable names.

##### other groupings

in MTGlang there are few other groupings

* () used for inputs and operation order
* \[] used for lists
* {} used for string injection using enchantment
* "" used to enclose strings

#### other functions(2.4.2)

### list functions(2.4.2.1)

MTGlang has two list functions

* draw - works like list.append
* discard - works like list.pop

##### misc built-ins(2.4.2.2)

###### i tap (2.4.2.2.1)

used to run a function

###### i can (2.4.2.2.2)

exec

###### library(2.4.2.2.3)

its a class

###### flying(2.4.2.2.4)

its just pass

###### enchantments(2.4.2.2.5)

enchantments is used on a string to inject variables into it. use {x1...} inside a string and after the string use enchantments like python format.

###### types (2.4.2.2.6)

str.split

###### return \_\_\_ to owners hand(2.4.2.2.7)

return

## grammar(3)

this section is about the details of grammar, boring, but important.

### is, has, and with(3.1)

#### has(3.1.1)

has is used whenever a numerical comparison is being made or when it is followed by a logic operator . has is also to be followed by an a/an (unless it is in a stack) for readability, it is not required to function.

|1. yes:  read it, `trained orgg` has a counterspell Tapped, so \\n<br />|2. yes: i declare `b` to be that `trained orgg` has a health above 10.|
|-|-|
|1. no: read it, `trained orgg` has a tapped|2. no: i declare `c` to be that `trained orgg` has a|

#### with(3.1.2)

with is used when assigning one thing to another

examples:

* stack with i in range (0,10)
* if i play boil with (`shatter`) then

|i can "play {x1}" with the enchantment `wild growth`(shatter)

#### is(3.1.3)

'is' is used for directly assigning things, for comparisons see '='.

#### =(3.1.4)

equal is the same as pythons == while 'is' is the same as pythons '='.

### . and ,(3.2)

the comma is unimportant to grammar, however the period is used for cards and libraries.

### the | (3.3)

the | symbol is MTGlangs equivalent to a tab.

### colon equivalents(3.4)

you can use

* so
* then
* \-

## full function definitions(4)

these are sorted alphabetically and by type

glossarry \_\_\[nameofvalue]-value (optional)  a/b-1 of the 2

### builtins(4.1)

#### library function(4.1.1)

##### example code (4.1.1.1)

library plainswalkers-

##### full syntax(4.1.1.2)

library \_\_\_\[library name]-

##### notes(4.1.1.3)

this has no reason to be used

#### if i play function(4.1.2)

##### example code(4.1.2.1)

if i play boil with `shatter` then

| i can "play {x1}" with the enchantment `wild growth`(`shatter`)

##### full syntax (4.1.2.2)

if i play \_\_\[functionname] with (\_\_\[variables]) then

##### notes (4.1.2.3)

this is used to define a function to call back to later.

#### i can function(4.1.3)

##### example code(4.1.3.1)

i can "play {x1}" with the enchantment `wild growth`(shatter) 

##### full syntax (4.1.3.2)

i can "" 

##### notes (4.1.3.3)

useful in if i play







