import re

# Definimos los patrones de tokens
TOKEN_PATTERNS = [
    ("Comment", r"//.*|/\*[\s\S]*?\*/"),
    ("Data Type", r"\b(int|float|double|boolean|char|string|String)\b"),
    ("Conditional", r"\b(if|else)\b"),
    ("Loop", r"\b(for|while)\b"),
    ("Exception", r"\b(try|catch|throw)\b"),
    ("Access Modifier", r"\b(public|private|protected)\b"),
    ("Data Structure", r"\b(array|list|set)\b"),
    ("Print", r"\b(System.out.print|System.out.println|System.out.printf)\b"),
    ("String Literal", r'"([^"\\]*(\\.[^"\\]*)*)"'),
    ("Number", r"\b\d+(\.\d+)?\b"),
    ("Reserved Word", r"\b(class|public|private|protected|static|void|if|else|while|for|return|try|catch|throw)\b"),
    ("Identifier", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("Arithmetic Operator", r"[+\-*/%]"),
    ("Assignment Operator", r"="),
    ("Compound Operator", r"(\+=|-=|\*=|/=)"),
    ("Logical Operator", r"(&&|\|\||!)"),
    ("Relational Operator", r"(==|!=|<|>|<=|>=)"),
    ("Delimiter", r"[;{}(),]"),
    ("Opening Bracket", r"\["),
    ("Closing Bracket", r"\]"),
    ("Newline", r"\n"),
    ("WHITESPACE", r"[ \t]+"),
    ("ERROR", r".")  # Matches any unexpected character
]

TOKEN_REGEX = [(name, re.compile(pattern)) for name, pattern in TOKEN_PATTERNS] #Se compilan las expresiones regulares una sola vez antes del bucle

# Lista de palabras reservadas en Java
PALABRAS_RESERVADAS = [
    'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char',
    'class', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
    'extends', 'final', 'finally', 'float', 'for', 'goto', 'if', 'implements',
    'import', 'instanceof', 'int', 'interface', 'long', 'native', 'new', 'null',
    'package', 'private', 'protected', 'public', 'return', 'short', 'static',
    'strictfp', 'super', 'switch', 'synchronized', 'this', 'throw', 'throws',
    'transient', 'try', 'void', 'volatile', 'while'
]

# Función para analizar las palabras reservadas en el código
def analizar_palabras_reservadas(texto_entrada):
    palabras = re.findall(r'\b\w+\b', texto_entrada)

    # Devolver las palabras que son reservadas en Java
    return [palabra for palabra in palabras if palabra in PALABRAS_RESERVADAS]

# Función para análisis del código
def lexer(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None
        for token_type, regex in TOKEN_REGEX:
            match = regex.match(code, position)

            if match:
                value = match.group(0)
                if token_type != "WHITESPACE":  # Ignorar espacios
                    tokens.append((token_type, value))
                position = match.end()
                break

        if not match:
            raise SyntaxError(f"Unexpected character {position}: {code[position]}")

    # Ahora analizamos las palabras reservadas en el código
    palabras_reservadas = analizar_palabras_reservadas(code)
    print("Palabras reservadas en el código:", palabras_reservadas)
    
    return tokens