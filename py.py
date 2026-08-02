class __inner__:
	class lexer:
		def init(code):
			output = code.split('\n')
			return (output)
		def tokenizer(segment):
			c = ''
			f = ''
			e = []
			switch = False
			b = list(segment)
			for i in range (0,len(b)):
				if b[i] != ' ':
					if b[i] == '"':
						switch = not switch
					if switch == True:
						f = f'{f}{b[i]}'
					if switch == False and f != '':
						e.append(f)
						f = ''
					if switch == False:
						c = f'{c}{b[i]}'
					if c in __inner__.keywords.keywords:
						e.append(c)
						print (c)
						c=''
					elif c in __inner__.keywords.operators:
						e.append(c)
						print (c)
						c=''
			return(e)
	class parser:
		def parsetoken(token):
			pass
		def strparse(string):
			
	class executor:
		class memory:
			# storage format name:store list:name:stored
			Memory = {}
			def manage(name,rw,value):
				if rw == 'w':
					__inner__.executor.memory.Memory[name] = value
				else:
					return(__inner__.executor.memory.Memory[name])
		def run(segment):
			pass
	class keywords:
		keywords  =  ['cardname','tapped','mana','health','hand','|','flavortext','play','keywords','read.the.card','stack','until.resolved','on.tap:','library','flying']
		operators =['"','(',')','[',']','{','}','kicker','counterspell','trample','split','+','-','is','*','^','/','<','>','<=','>=','=','!=']
print ('please input code and output paths')
print('code path')
code = str(input())
print ('output path')
output = str(input())
with open (code) as file:
	a = file.read()
	a = __inner__.lexer.init(a)
	print (a)
	b=[]
	for i in range (0,len(a)):
		b.append(__inner__.lexer.tokenizer(a[i]))
with open(output) as file:
	pass
