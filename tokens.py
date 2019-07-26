"""
Definitions and list of the tokens recognized by ShivC.
"""

from lexer import *

comment_start = Token("comment", "//*")
comment_end = Token("comment", "*//")
plusplus = Token("crement", "++", 100)
minusminus = Token("crement", "--", 100)

equal_comp = Token("eq_compare", "==", 70)
noteq_comp = Token("eq_compare", "!=", 70)
lesseq_comp = Token("compare", "<=", 75)
greateq_comp = Token("compare", ">=", 75)

plusequal = Token("assignment", "+=", 50)  # right-to-left precedence
minusequal = Token("assignment", "-=", 50)
timesequal = Token("assignment", "*=", 50)
divequal = Token("assignment", "/=", 50)
modequal = Token("assignment", "%=", 50)

logic_and = Token("boolean", "&&", 65)
logic_or = Token("boolean", "||", 60)

open_bracket = Token("bracket", ">>")
close_bracket = Token("bracket", "<<")
open_paren = Token("bracket", "(", 100)
close_paren = Token("bracket" , ")")
open_sq_bracket = Token("bracket", "[", 100)
close_sq_bracket = Token("bracket", "]")
equal = Token("assignment", "=", 50) # right-to-left precedence
less_comp = Token("compare", "<", 75)
great_comp = Token("compare", ">", 75)
semicolon = Token("semicolon", ";")
comma = Token("comma", ",")
minus = Token("addop", "-", 85)
plus = Token("addop", "+", 85)
aster = Token("asterisk", "*", 90)
amper = Token("ampersand", "&", 95)
slash = Token("slash", "/", 90)
percent = Token("percent", "%", 90)
logic_not = Token("logicnot", "!", 95)

if_keyword = Token("keyword", "eger")
else_keyword = Token("keyword", "degilse", 210)
break_keyword = Token("keyword", "durdur")
cont_keyword = Token("keyword", "devam")
while_keyword = Token("keyword", "while")
for_keyword = Token("keyword", "icin")

return_command = Token("command", "donus")
print_command = Token("command", "yaz")
int_type = Token("type", "int")

# A list of all the primitives recognized. If adding a primitive, don't forget
# to include it here!
#
# Order the prims from multi-character to single character because the lexer
# searches for tokens in the order specified by prims.
prims = [comment_start,
         comment_end,
         plusplus,
         minusminus,

         plusequal,
         minusequal,
         timesequal,
         divequal,
         modequal,

         logic_and,
         logic_or,

         equal_comp,
         noteq_comp,        
         lesseq_comp,
         greateq_comp,
                  
         open_bracket,
         close_bracket,
         open_paren,
         close_paren,
         open_sq_bracket,
         close_sq_bracket,
         equal,
         less_comp,
         great_comp,
         semicolon,
         comma,
         minus,
         plus,
         aster,
         amper,
         slash,
         percent,
         logic_not,

         if_keyword,
         else_keyword,

         break_keyword,
         cont_keyword,
         
         while_keyword,
         for_keyword,
         
         return_command,
         print_command,
         int_type]

# A list of the primitives of assignment type
assignment_ops = [prim for prim in prims if Token("assignment").match(prim)]

# A list of the text attributes of the primitives
prims_str = [prim.text for prim in prims]

# A dictionary of the primitives and their text attributes
prims_dict = dict(zip(prims_str, prims))
