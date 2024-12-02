usuario='admin'.strip().lower()
contraseña='123'
respuesta_usuario=input('Introduce el usuario')
respuesta_contra=input('Introduce contraseña')
correcta=(respuesta_usuario.strip().lower()==usuario and respuesta_contra==contraseña)
print(f'Se ha validado correctamente?{correcta}')