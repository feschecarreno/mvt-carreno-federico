from desafio.models import Familiar

Familiar(nombre="Santiago", direccion="Manuel Castro 2950", numero_dni=3878445, fecha_de_nacimiento="1994-08-19").save()
Familiar(nombre="Ariel", direccion="Javier Pie 214", numero_dni=22824785, fecha_de_nacimiento="1969-12-04").save()
Familiar(nombre="Delfina", direccion="Lucerna 164", numero_dni=34825541, fecha_de_nacimiento="1991-06-25").save()
Familiar(nombre="Felipe", direccion="Lucerna 164 depo 3", numero_dni=56478854, fecha_de_nacimiento="2017-10-30").save()

print("Se cargo con éxito los usuarios de pruebas")