import re

# Definimos los patrones de tokens
PATRONES_TOKEN = [
    ("Comentario", r"//.*|/\*[\s\S]*?\*/"),
    ("Tipo de Dato", r"\b(int|float|double|boolean|char|string|String)\b"),
    ("Condicional", r"\b(if|else)\b"),
    ("Bucle", r"\b(for|while)\b"),
    ("Excepción", r"\b(try|catch|throw)\b"),
    ("Modificador de Acceso", r"\b(public|private|protected)\b"),
    ("Estructura de Datos", r"\b(array|list|set)\b"),
    ("Impresión", r"\b(System.out.print|System.out.println|System.out.printf)\b"),
    ("Literal de Cadena", r'"([^"\\]*(\\.[^"\\]*)*)"'),
    ("Número", r"\b\d+(\.\d+)?\b"),
    ("Palabra Reservada", r"\b(class|public|private|protected|static|void|if|else|while|for|return|try|catch|throw)\b"),
    ("Identificador", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    ("Operador Aritmético", r"[+\-*/%]"),
    ("Operador de Asignación", r"="),
    ("Operador Combinado", r"(\+=|-=|\*=|/=)"),
    ("Operador Lógico", r"(&&|\|\||!)"),
    ("Operador Relacional", r"(==|!=|<|>|<=|>=)"),
    ("Delimitador", r"[;{}(),]"),
    ("Corchete de Apertura", r"\["),
    ("Corchete de Cierre", r"\]"),
    ("Salto de Línea", r"\n"),
    ("ESPACIO EN BLANCO", r"[ \t]+"),
    ("ERROR", r".")  # Coincide con cualquier carácter inesperado
]

# Compilamos las expresiones regulares una sola vez antes del bucle
REGEX_TOKENS = [(nombre, re.compile(patron)) for nombre, patron in PATRONES_TOKEN]

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
def lexer(codigo):
    tokens = []
    posicion = 0

    while posicion < len(codigo):
        coincidencia = None
        for tipo_token, regex in REGEX_TOKENS:
            coincidencia = regex.match(codigo, posicion)

            if coincidencia:
                valor = coincidencia.group(0)
                if tipo_token != "ESPACIO EN BLANCO":  # Ignorar espacios
                    inicio_pos = posicion
                    fin_pos = coincidencia.end()
                    tokens.append((tipo_token, valor, f"{inicio_pos}-{fin_pos}"))
                posicion = coincidencia.end()
                break

        if not coincidencia:
            raise SyntaxError(f"Carácter inesperado {posicion}: {codigo[posicion]}")

    # Ahora analizamos las palabras reservadas en el código
    palabras_reservadas = analizar_palabras_reservadas(codigo)
    print("Palabras reservadas en el código:", palabras_reservadas)
    
    return tokens