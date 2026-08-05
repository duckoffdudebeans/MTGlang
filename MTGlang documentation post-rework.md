# MTGlang documentation
---
## introduction `1`
MTGlang is a programming language that aims to read like a game of *Magic: The Gathering*. it is also an esolang[^1]: which is a programming langage designed to be difficult to code in.

[^1]: MTGlang is not explicitly designed to be difficult to code in, but it is also not designed to actually be coded in.

---
## keywords, grammar, and syntax: simplified. `2`
---
### table of simple keywords`2.1`

|MTGlang keyword|python eqivalent|full definition|can use either|
|:---:           |:---:      |:---:   |:---:   |
|Untapped        |True       ||yes     |
|Tapped          |False      ||yes     |
|play            |print      ||no      |
|read it         |if         ||no      |
|i can           |exec       ||no      |
|if i play       |def        ||no      |
|i tap           |none       ||no      |
|i reveal my card|none       ||no      |
|vertical bar    |tab        ||no      |
|draw            |var.append ||no      |
|discard         |var.pop    ||no      |
|types           |var.split  ||no      |
|flying          |pass       ||yes     |
|mill            |return     ||yes     |
|stack           |for        ||no      |
|destroy         |break      ||yes     |
|exile           |raise      ||no      |
|until           |while      ||no      |
|counter(spell)  |NOT        ||yes     |
|trample         |OR         ||yes     |
|as well as      |AND        ||yes     |
|fight           |XOR        ||yes     |
|commander       |Const      ||no      |
|control target  |open       ||no      |
|read            |file.read  ||no      |
|activate        |file.write |[full](#activate-`string`)|no      |
|sacrifice       |close(file)||no      |
|on play (it)    |none       ||no      |
|deck            |import     ||yes     |
|raw PY          |none       ||no      |
|hand            |list       ||yes     |
|name            |str        ||no      |
|card            |object     ||no      |
|health          |float      ||yes     |
|mana            |int        ||yes     |
|state           |bool       ||yes     |
|stat            |dictionary ||no      |
|i declare       |none       ||no      |
|battlefeild     |class      ||no      |
|enchantments    |format     ||no      |
---
### table of non keywords`2.2`
|words                   |symbol|Full |
|:---:                   |:---: |:---:|
|is more than            |>     |     |
|is less than            |<     |     |
|is more than or equal to|>=    |     |
|is less than or equal to|<=    |     |
|is                      |none  |     |
|does not have           |!=    |     |
|has                     |=     |     |
|none                    |()    |     |
|none                    |{}    |     |
|none                    |[]    |     |
|none                    |""    |     |
|none                    |''    |     |
|none                    |``    |     |
---
### prefix and suffix table`2.3`
|PREFIX/SUFFIX|KEYWORD    |FULLDEF|WHERE TO USE              |
|:---:        |:---:      |:---:  |:---:                     |
|suffix       |creaature  |       |after 'control target'    |
|↑            |artifact   |       |↑                         |
|↑            |enchantment|       |↑                         |
|prefix       |i,if,the   |       |start of line             |
|suffix       |¬          |       |end of line before indent |
|↑            |for        |       |end of line               |
|↑            |to get     |       |↑                         |
|↑            |of         |       |after var type when adding|
|↑            |and thats  |       |in loop; ends all layers  |
---
## full keyword definitions `3`

### full list of keywords `3.1`
1. builtins
> 1. play
> 2. read it
> 3. i can
> 4. if i play
> 5. i tap
> 6. i reveal my card
> 7. draw
> 8. discard
> 9. types
> 10. flying
> 11. mill
> 12. return
> 13. stack
> 14. destroy
> 15. break
> 16. exile
> 17. until
> 18. counter
> 19. not
> 20. trample
> 21. or
> 22. as well as
> 23. and
> 24. fight
> 25. xor
> 26. commander
> 27. control target
> 28. read
> 29. activate
> 30. sacrifice
> 31. on play
> 32. deck
> 33. import
> 34. raw PY
> 35. enchantments
2. data
> 1. hand
> 2. list
> 3. name
> 4. card
> 5. health
> 6. float
> 7. mana
> 8. int
> 9. state
> 10. bool
> 11. stat
> 12. i declare
> 13. battlefeild
> 14. library
> 15. tapped
> 16. untapped
3. comparisons
> 1. is more than
> 2. '>
> 3. is less than
> 4. <
> 5. is more than or equal to
> 6. '>=
> 7. is less than or equal to
> 8. <=
> 9. is
> 10. does not have
> 11. !=
> 12. has
> 13. =
4. affixes
> 1. creature
> 2. artifact
> 3. enchantment
> 4. ¬
> 5. for
> 6. to get
> 7. of
> 8. and thats
5. grouping
> 1. ()
> 2. {}
> 3. []
> 4. ''
> 5. ""
> 6. ``
---
### per keyword rules `3.2`
#### glossary of symbols in this section `3.2.1`
1. `type` - variable of type boxed in
2. a/b - one or the other
3. () - text or variables inside parenthesis is optional
4. {} - notes
5. '' - other keyword
6. "" for parts with spaces
7. --codetype-- is used to show a required type of code after 
#### builtin functions `3.2.2`
- **A:**
##### activate `string`
###### `3.2.2.1`
activate is used to write to a file and works like 'play'.
###### requirements
to use activate, you must currently have a file open in either write or read and write mode. the string must only consist of plaintext charachters as MTGlang only supports .txt {and technically markdown because it only uses plaintext charachters} files.
##### `logic` and/"as well as" `logic`
###### `3.2.2.2`
and/"as well as" is used to see if two logical values or expressions are both true.
###### requirements
must be part of a logical expression variable,{or any logical branching statement's logic}, requires both logic inputs to not be NULL {empty} and, also to be either a logical expression or a boolean variable
- **B:**
##### break/destroy
###### `3.2.2.3`
break/destroy is used to escape 1 layer of looping.
###### requirements
this keyword requires that it be inside of an 'until','"if i play"' or 'stack' loop, no matter the relative indented depth. if it is, it breaks all indented layers up to and icluding the stated loop.
- **C:**
##### commander --declarevar--
###### `3.2.2.4`
commander is used to create a constant variable.
###### requirements
commander requires a variable decalration after it[^2]. the variable it makes cannot be changed after it is created.
[^2]: in some cases this is not the case, them being '"i reveal my card `name`"' and '"i declare"'; for '"i reveal my {1} card `name` '" in this scenario, commander would be placed at {1}, and '"i declare `name` to be"' would become '"i declare commander `name` to be"'.



---
## full syntax definitions `4`
---

---
## full grammar specifications`5`
---

---
## full semantic specifications`6`
---