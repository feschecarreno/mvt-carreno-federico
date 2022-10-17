from desafio.models import Familiar

Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_dni=123123).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_dni=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_dni=345345).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_dni=567567).save()

print("Se cargo con éxito los usuarios de pruebas")