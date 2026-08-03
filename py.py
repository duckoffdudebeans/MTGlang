class __inner__:
    class lexer:
        def init(code):
            return code.replace('\r', '').splitlines()

        def tokenizer(segment):
            tokens = []
            buf = ''
            quote = None
            i = 0

            while i < len(segment):
                ch = segment[i]

                if quote:
                    buf += ch
                    if ch == quote:
                        tokens.append(buf)
                        buf = ''
                        quote = None
                    i += 1
                    continue

                if ch.isspace() or ch == ',':
                    if buf:
                        tokens.append(buf)
                        buf = ''
                    i += 1
                    continue

                if ch in '"`':
                    if buf:
                        tokens.append(buf)
                        buf = ''
                    quote = ch
                    buf = ch
                    i += 1
                    continue

                if ch in '()[]{}|':
                    if buf:
                        tokens.append(buf)
                        buf = ''
                    tokens.append(ch)
                    i += 1
                    continue

                if ch in '+-*/^<>!=':
                    if buf:
                        tokens.append(buf)
                        buf = ''
                    nxt = segment[i + 1] if i + 1 < len(segment) else ''
                    if ch + nxt in ('<=', '>=', '!=', '=='):
                        tokens.append(ch + nxt)
                        i += 2
                    else:
                        tokens.append(ch)
                        i += 1
                    continue

                buf += ch
                i += 1

            if buf:
                tokens.append(buf)
            return tokens

    class parser:
        @staticmethod
        def parse(tokenlist):
            ast = []
            stack = [ast]

            for tokens in tokenlist:
                if not tokens:
                    continue

                indent = 0
                while indent < len(tokens) and tokens[indent] == '|':
                    indent += 1

                stmt = __inner__.parser.parse_line(tokens[indent:])

                if indent == 0:
                    ast.append(stmt)
                    stack = [ast]
                else:
                    while len(stack) <= indent:
                        parent = stack[-1][-1]
                        parent.setdefault('children', [])
                        stack.append(parent['children'])
                    stack[indent].append(stmt)

            return ast

        @staticmethod
        def parse_line(tokens):
            if not tokens:
                return {'type': 'empty'}

            lower = [t.lower() for t in tokens]

            if lower[:2] == ['read', 'it,']:
                return {
                    'type': 'if',
                    'condition': __inner__.parser.parse_expression(tokens[2:]),
                    'children': []
                }

            if lower[0] == 'until':
                return {
                    'type': 'while',
                    'condition': __inner__.parser.parse_expression(tokens[1:]),
                    'children': []
                }

            if lower[:3] == ['if', 'i', 'play']:
                name = tokens[3] if len(tokens) > 3 else None
                args = []
                if 'with' in lower:
                    with_index = lower.index('with')
                    args = tokens[with_index + 1:]
                return {
                    'type': 'function_def',
                    'name': name,
                    'args': args,
                    'children': []
                }

            if lower[:2] == ['i', 'declare']:
                if 'to' in lower and 'be' in lower:
                    to_i = lower.index('to')
                    be_i = lower.index('be', to_i + 1)
                    name = tokens[2:to_i]
                    expr = tokens[be_i + 1:]
                else:
                    name = tokens[2:3]
                    expr = tokens[3:]
                return {
                    'type': 'declare',
                    'name': name,
                    'expression': __inner__.parser.parse_expression(expr)
                }

            if lower[:2] == ['i', 'reveal']:
                return {
                    'type': 'object',
                    'subject': tokens[2:],
                    'properties': __inner__.parser.parse_expression(tokens[2:])
                }

            if lower[:2] == ['i', 'can']:
                return {
                    'type': 'action',
                    'expression': __inner__.parser.parse_expression(tokens[2:])
                }

            if lower[0] == 'stack':
                return {
                    'type': 'for',
                    'expression': __inner__.parser.parse_expression(tokens[1:]),
                    'children': []
                }

            return __inner__.parser.parse_expression(tokens)

        @staticmethod
        def parse_expression(tokens):
            if not tokens:
                return {'type': 'empty'}

            lower = [t.lower() for t in tokens]

            if 'has' in lower:
                i = lower.index('has')
                return {
                    'type': 'compare',
                    'left': __inner__.parser.parse_expression(tokens[:i]),
                    'op': 'has',
                    'right': __inner__.parser.parse_expression(tokens[i + 1:])
                }

            if 'is' in lower:
                i = lower.index('is')
                return {
                    'type': 'assign',
                    'left': __inner__.parser.parse_expression(tokens[:i]),
                    'right': __inner__.parser.parse_expression(tokens[i + 1:])
                }

            if 'with' in lower:
                i = lower.index('with')
                return {
                    'type': 'with',
                    'left': __inner__.parser.parse_expression(tokens[:i]),
                    'right': __inner__.parser.parse_expression(tokens[i + 1:])
                }

            for op in ['kicker', 'counterspell', 'trample', 'split', '+', '-', '*', '/', '^', '>', '<', '<=', '>=', '=', '!=']:
                if op in lower:
                    i = lower.index(op)
                    return {
                        'type': 'binary',
                        'op': op,
                        'left': __inner__.parser.parse_expression(tokens[:i]),
                        'right': __inner__.parser.parse_expression(tokens[i + 1:])
                    }

            if len(tokens) == 1:
                tok = tokens[0]
                if tok.startswith('`') and tok.endswith('`'):
                    return {'type': 'name', 'value': tok[1:-1]}
                if tok.startswith('"') and tok.endswith('"'):
                    return {'type': 'string', 'value': tok[1:-1]}
                return {'type': 'symbol', 'value': tok}

            return {'type': 'expression', 'tokens': tokens}

        @staticmethod
        def strparse(string):
            fields = []
            idx = 0
            while True:
                start = string.find('{', idx)
                if start == -1:
                    break
                end = string.find('}', start + 1)
                if end == -1:
                    break
                fields.append(string[start + 1:end])
                idx = end + 1
            return {'text': string, 'fields': fields}
    class executor:
        class memory:
            Memory = {}

        function_defs = {}

        @staticmethod
        def execute(ast, out_file=None):
            if out_file is None:
                import sys
                out_file = sys.stdout
            for stmt in ast:
                __inner__.executor.execute_statement(stmt, out_file)

        @staticmethod
        def execute_statement(stmt, out_file):
            stmt_type = stmt.get('type')
            if stmt_type == 'if':
                cond = __inner__.executor.evaluate(stmt.get('condition'))
                if cond:
                    for child in stmt.get('children', []):
                        __inner__.executor.execute_statement(child, out_file)
            elif stmt_type == 'while':
                guard = 0
                while __inner__.executor.evaluate(stmt.get('condition')):
                    if guard > 999:
                        break
                    for child in stmt.get('children', []):
                        __inner__.executor.execute_statement(child, out_file)
                    guard += 1
            elif stmt_type == 'for':
                value = __inner__.executor.evaluate(stmt.get('expression'))
                if isinstance(value, int):
                    for _ in range(value):
                        for child in stmt.get('children', []):
                            __inner__.executor.execute_statement(child, out_file)
                elif isinstance(value, (list, tuple)):
                    for item in value:
                        __inner__.executor.memory.Memory['i'] = item
                        for child in stmt.get('children', []):
                            __inner__.executor.execute_statement(child, out_file)
            elif stmt_type == 'function_def':
                name = stmt.get('name')
                if name:
                    __inner__.executor.function_defs[name] = stmt
            elif stmt_type == 'declare':
                name = __inner__.executor.normalize_name(stmt.get('name'))
                __inner__.executor.memory.Memory[name] = __inner__.executor.evaluate(stmt.get('expression'))
            elif stmt_type == 'object':
                name = __inner__.executor.normalize_name(stmt.get('subject'))
                __inner__.executor.memory.Memory[name] = {
                    'subject': stmt.get('subject'),
                    'properties': __inner__.executor.evaluate(stmt.get('properties'))
                }
            elif stmt_type == 'action':
                val = __inner__.executor.evaluate(stmt.get('expression'))
                if val is not None:
                    text = str(val)
                    out_file.write(text)
                    if not text.endswith('\n'):
                        out_file.write('\n')
            elif stmt_type == 'expression':
                value = __inner__.executor.evaluate(stmt)
                if isinstance(value, str):
                    out_file.write(value)
                    if not value.endswith('\n'):
                        out_file.write('\n')
            else:
                for child in stmt.get('children', []):
                    __inner__.executor.execute_statement(child, out_file)

        @staticmethod
        def normalize_name(name_tokens):
            if not name_tokens:
                return ''
            if isinstance(name_tokens, list):
                return ' '.join(t.strip('`"') for t in name_tokens).strip()
            return str(name_tokens).strip('`"')

        @staticmethod
        def evaluate(expr):
            if expr is None:
                return None
            expr_type = expr.get('type')
            if expr_type == 'empty':
                return None
            if expr_type == 'string':
                return expr['value']
            if expr_type == 'name':
                return __inner__.executor.memory.Memory.get(expr['value'], expr['value'])
            if expr_type == 'symbol':
                tok = expr['value']
                lower = tok.lower()
                if lower == 'true':
                    return True
                if lower == 'false':
                    return False
                if tok.isdigit():
                    return int(tok)
                try:
                    return float(tok)
                except ValueError:
                    pass
                return __inner__.executor.memory.Memory.get(tok, tok)
            if expr_type == 'assign':
                left = expr.get('left')
                right = __inner__.executor.evaluate(expr.get('right'))
                if left and left.get('type') in ('name', 'symbol'):
                    __inner__.executor.memory.Memory[left.get('value')] = right
                return right
            if expr_type == 'compare':
                left = __inner__.executor.evaluate(expr.get('left'))
                right = __inner__.executor.evaluate(expr.get('right'))
                if isinstance(left, dict):
                    props = left.get('properties')
                    if isinstance(props, dict):
                        return right in props.values() or right in props
                return left == right
            if expr_type == 'with':
                return (__inner__.executor.evaluate(expr.get('left')), __inner__.executor.evaluate(expr.get('right')))
            if expr_type == 'binary':
                op = expr.get('op')
                left = __inner__.executor.evaluate(expr.get('left'))
                right = __inner__.executor.evaluate(expr.get('right'))
                if op in ('kicker', 'and'):
                    return bool(left) and bool(right)
                if op in ('trample', 'or'):
                    return bool(left) or bool(right)
                if op in ('split', 'xor'):
                    return bool(left) != bool(right)
                if op in ('counterspell', 'not'):
                    return not bool(right)
                if op in ('=', '=='):
                    return left == right
                if op == '!=':
                    return left != right
                if op == '>':
                    return left > right
                if op == '<':
                    return left < right
                if op == '>=':
                    return left >= right
                if op == '<=':
                    return left <= right
                if op == '+':
                    return left + right
                if op == '-':
                    return left - right
                if op == '*':
                    return left * right
                if op == '/':
                    return left / right
                if op == '^':
                    return left ** right
                return None
            if expr_type == 'expression':
                tokens = expr.get('tokens', [])
                if len(tokens) >= 3 and tokens[1] == '(' and tokens[-1] == ')':
                    name = tokens[0]
                    args = __inner__.executor.parse_call_args(tokens[2:-1])
                    return __inner__.executor.call_function(name, args)
                return ' '.join(str(t) for t in tokens)
            return None

        @staticmethod
        def parse_call_args(tokens):
            args = []
            current = []
            for token in tokens:
                if token == ',':
                    if current:
                        args.append(__inner__.executor.evaluate(__inner__.parser.parse_expression(current)))
                        current = []
                else:
                    current.append(token)
            if current:
                args.append(__inner__.executor.evaluate(__inner__.parser.parse_expression(current)))
            return args

        @staticmethod
        def call_function(name, args):
            key = name.lower()
            if key == 'print':
                return ' '.join(str(x) for x in args)
            if key == 'range':
                try:
                    return list(range(*args))
                except Exception:
                    return []
            if key == 'exec' and args:
                code = args[0]
                if isinstance(code, str):
                    exec(code, {}, __inner__.executor.memory.Memory)
                return None
            if key in __inner__.executor.function_defs:
                return None
            return None

print ('please input code and output paths')
print('code path')
code = str(input())
print ('output path')
output = str(input())
with open(code) as file:
    code = file.read()
    tokens = __inner__.lexer.init(code)
    data = []
    for segment in tokens:
        data.append(__inner__.lexer.tokenizer(segment))
    data = __inner__.parser.parse(data)
with open(output, 'w') as file:
    __inner__.executor.execute(data, file)
