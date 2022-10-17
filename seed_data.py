from desafio.models import Familiar

Familiar(nombre="Santiago", direccion="Manuel Castro 2950", numero_dni=3878445).save()
Familiar(nombre="Ariel", direccion="Javier Pie 214", numero_dni=22824785).save()
Familiar(nombre="Delfina", direccion="Lucerna 164", numero_dni=34825541).save()
Familiar(nombre="Felipe", direccion="Lucerna 164 depo 3", numero_dni=56478854).save()

print("Se cargo con éxito los usuarios de pruebas")