class compiler:
	class lexer:
		returnvalue = []
		def string(string):
			pass
		def init(code):
			return code.split ('\n')
		def lexer(code):
			readspaces = false
			namesmatter = True
			e = ''
			f = ''
			read = (compiler.lexer.init(code))
			for i in range (0,len(read)):
				for j in range (0,len(read[i]):
					tmp = list(read[i])
					if ((namesmatter == True) and (tmp[j] == '|')):
						compiler.lexer.returnvalue.append('indent')
					elif tmp[j] == '"' :
						for k in range (j,len(read[i]):
							a = 0
							if tmp[k] == '"':
								a = a + 1
							f = f'{f}{tmp[k]}'
							if a == 2:
								compiler.lexer.returnvalue.append(f'str:{f}')
								i = k + 1
								f = ''
								break
						a = compiler.lexer.string(f)
					elif tmp[j] == '`'
						for k in range (j,len(read[i]):
							o = ''
							if tmp[k] not ('`'):
								o = f'{o}{tmp[k]}'
							if tmp[k]== '`' and k != 0:
								i = k + 1
								compiler.lexer.returnvalue.append(f'var:{o}')
								o = ''
								break
					elif tmp[j] == "'":
						for k in range (j+1,len(read[i])):
							if tmp[k] == "'":
								i = k + 1
								break
					
	class parser:
	class executor:
	class memory:
		mem = {}
		def manage(name,rw):
			pass
