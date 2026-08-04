class compiler:
	keywords = ['read','name','state','Tapped','Untapped','mana','health','hand','declare','reveal','discard','draw','play','types','read','stack','until','resolves','if','library','flying','return','enchantments','can','kicker','counterspell','trample','split','tap','is','has','with','=','+','-','*','^','/','<','>','<=','>=','!=']
	class lexer:
		retvalue = []
		def string(string):
			pass
		def init(code):
			return code.split ('\n')
		def lexer(code):
			readspaces = false
			e = ''
			f = ''
			read = (compiler.lexer.init(code))
			for i in range (0,len(read)):
				for j in range (0,len(read[i]):
					tmp = list(read[i])
					if   tmp[j] == '|':
						compiler.lexer.retvalue.append('indent:')
					elif tmp[j] == '"':
						for k in range (j,len(read[i]):
							a = 0
							if tmp[k] == '"':
								a = a + 1
							f = f'{f}{tmp[k]}'
							if a == 2:
								compiler.lexer.retvalue.append(f'str:{f}')
								i = k + 1
								f = ''
								break
						a = compiler.lexer.string(f)
					elif tmp[j] == '`':
						for k in range (j,len(read[i]):
							f = ''
							if tmp[k] not ('`'):
								f = f'{o}{tmp[k]}'
							if tmp[k]== '`' and k != 0:
								i = k + 1
								compiler.lexer.retvalue.append(f'var:{o}')
								f = ''
								break
					elif tmp[j] == "'":
						for k in range (j+1,len(read[i])):
							if tmp[k] == "'":
								i = k + 1
								break
					elif tmp[j] == '(':
						compiler.lexer.retvalue.append('parenthesis:')
					elif tmp[j] == '[':
						compiler.lexer.retvalue.append('list:')
					elif tmp[j] == ')':
						compiler.lexer.retvalue.append(':endparenthesis))
					elif tmp[j] == ']':
						compiler.lexer.retvalue.append(':endlist')
					else:#  keywords  #
						if f in compiler.keywords:
							compiler.lexer.retvalue.append(f'keyword: {f}')
							f =''
						else:
							f = f'{f}{tmp[j]}'
				compiler.lexer.retvalue.append('newline:')
			return (compiler.lexer.retvalue)
			compiler.lexer.retvalue = []
	class parser:
	class executor:
	class memory:
		mem = {}
		def manage(name,rw):
			pass
