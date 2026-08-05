# syntax + keywords rework:

\---

## example code:

\---

### 1 - basics

\---

#### 1.1

\---

##### 1.1 MTGlang:


'The' name of "destroy target artifact" is `shatter`
'I' play `shatter`


##### 1.1 python:


shatter = 'destroy target artifact'
print (shatter)


##### 1.1 explanations:

'note', name = string, `Var name`, "string", play = print, is for assignment, of means name is after value.

\---

## ideas

\---

### keywords

\---

True - Untapped #
False - Tapped #
print - play
if - read it,

> - is more than #

>= -is more than or equal to #
< - is less than #

<= -is less than or equal to #
= - is #
!= - is not #
== - =
exec - i can
def - if i play `` /i play ``, on play it (if in an object)
run function - i tap `` (with)
initiate object - i reveal my card ``
tab - |
.append - draw
.pop - discard
.split - types
pass - flying
return - mill #
for - stack
break - destroy #
raise - exile
while - until `` resolves
NOT - counter #
OR - trample #
AND - as well as #
XOR - fight #

const - commander

/with (a) - used to apply variables to functions

/has (a) - can be used in place of '=' to compare things

/control target - open file

/control target \[path] - r

/control target creature with \[path] - r/w

/control target artifact with \[path] - r

/control target enchantment with \[path] - w

/read (creature/artifact/enchantment) - return file contents

/activate (creature/artifact/enchantment) - write to file(works like play)

/sacrifice (creature/artifact/enchantment) - close file

/,- a comma will be ignored(unless in a string).

/on play - used to add a function to an object

/deck new/add \[file] (\[classes = all]) - import custom modules for MTGlang

\---

PREFIXES:

/i - optional line starter, but used in other keywords

/if - optional line starter, but used in other keywords

/the - optional line starter, must be used if using 'of'

\---

SUFFIXES:

/¬ - equivalent of :, anything after it in the same line will be ignored

/for \[x] (of) \[Var name] (mana) - at the end of a line, subtracts \[x] from \[var name] 

/to get \[x] \[var name] (mana) - at the end of a line, adds \[x] to \[var name]

/of - used to give a variables value(s) before its name

/(and) that's 'my turn'/'it for my turn'. - used to add a forceable end to loops.

\---

### grouping

\---

/() - order of operations only

/\[] - list structure, list/dictionary id-ing

/{} - string injection,dictionarys

/`` - variable names

/'' - notes

\---

### data types

\---

list - hand
string - name
object - card
float - health
int - mana
bool - state
dictionary - stats
logic/math expression - i declare `` (to be)

class - battlefield/library

\---

### other

\---

