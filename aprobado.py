def notas(promedio):
	if promedio>=11:
		resultado="aprobado"
	else:
		resultado="desaprobado"
	return(resultado)


print(notas(21))