class __inner__:
	class lexer:
		def init(code):
			output = code.split('\n')
			return (output)
		def tokenizer(segment):
			c = ''
			f = ''
			e = []
			spaces? = True
			f = list(segment)
			for i in range (o,len(f)):
				
	class parser:
		def parse(token):
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
		keywords  =  ['name','state','tapped','untapped','mana','health','hand','i','declare','discrd','draw','play','types','read','it,','stack','if','library','flying','return','enchantment','can','card','reveal','kicker','counterspell','trample','split','Tap','is','has','with','+','-','*','^','/','>','<','<=','>=','=','!=']
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
