import string
import re
import subprocess

key_words = {
	"por" : "for",
	"mientras" : "while",
	"en" : "in",
	"si" : "if",
	"si_no" : "elif",
	"sino:" : "else:",
	"Cierto" : "True",
	"Falso" : "False",
	"no" : "not",
	"Y" : "and",
	"O" : "or",
	"imprimir" : "print",
	"romper" : "break",
	"de" : "from",
	"retornar" : "return",
	"importar" : "import",
	"ent" : "int",
	"flotante" : "float",
	"cadena" : "str", # "cadena de caracteres"
	"char" : "car"
}

funs_and_cons = {
	"largo(" : "len(",
	"gama(" : "range(",
	"imprimir(" : "print(",
	"colección(" : "set(",
	"diccionario(" : "dict(",
	"añadir(" : "append(",
	"quitar(" : "remove(",
	"ingresar(" : "input(",
	"ent(" : "int(",
	"flotante(" : "float("
}

piton = open("programa.txt", "r")
program_str = piton.read()

py = open("program.py", "w")

lines = program_str.split("\n")
transition = []
words = []

for line in lines:
	if line.split("(")[0] != "traducir":
		transition = transition + [line, "\n"]
	else:
		parsed = line.split("'")
		funs_and_cons[parsed[1] + "("] = parsed[3] + "("

for trans_line in transition:
	words = words + trans_line.split(" ")

for word in words:
	for key, val in key_words.items():
		if key == re.sub(r'[^a-zA-Z_:]', '', word):
			word = word.replace(key, val)
	for key, val in funs_and_cons.items():
		if key in word:
			word = word.replace(key, val)
	if word == "\n":
		py.write(word)
	else:
		try:
			int(re.sub(r'[^0-9]', '', word))
			if "\"" not in word:
				py.write(word.replace(",", ".") + " ")
			else:
				py.write(word + " ")
		except:
			py.write(word + " ")
			

piton.close()
py.close()

subprocess.call(["python program.py"], shell = True)

