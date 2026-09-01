# '\r' '\n' -> CRLF -> Windows
# '\n' -> LF -> Unix. MacOs, Linux...
print(12, 34, sep='-') # sep='' serve para alterar o separador padrão substituindo pelo que quiser.
print(56, 78, sep="/") # Ele pode ter aspas simples e aspas duplas.
print(9, 10, end=' fim') # adiciona o que quiser no fim dos argumentos na função print