print("actividad 9 clase humano")
print("Johana Moras Mat:22308051280458")
# zona de clases 
class humano_0458:
    #zona de atributos dentro de la clase
    edad=17
    genero="femenino"
    peso=56 
    ojos="cafe oscuro"
    estatura=1.60
    #zona de funciones dentro de la clase
    def correr_0458(self,n):
        print(f"{n} esta corriendo jiiji...")
    def escucharmusica_0458(self,n):
        print(f"{n} esta escuchando musica")
    def dormir_0458(self,n):
        print(f"{n} duerme sus 8 horitas")
    def bailar_0458(self,n):
        print(f"{n} esta bailando canciones de lady gaga")
    def comer_0458(self,n):
        print(f"{n} esta comiendo pizza")
    #zona de creacion de objetos
johana=humano_0458()
alecita=humano_0458()
    #zona de uso de objetos
print("--resultados para johana--")
johana.edad=17
print(f"edad: {johana.edad}")
print(f"genero: {johana.genero}")
print(f"peso: {johana.peso} kilos")
print(f"ojos color: {johana.ojos}")
print(f"estatura: {johana.estatura} cm")
print("----------------------------------")
johana.correr_0458("johana")
johana.escucharmusica_0458("johana")
johana.dormir_0458("johana")
johana.bailar_0458("johana")
johana.comer_0458("johana")
print("----------------------------------")
print("--resultados para alecita--")
alecita.edad=18
print(f"edad: {alecita.edad}")
print(f"genero: {alecita.genero}")
alecita.peso=40
print(f"peso: {alecita.peso} kilos")
print(f"ojos color: {alecita.ojos}")
alecita.estatura=1.70
print(f"estatura: {alecita.estatura} cm")
print("----------------------------------")
alecita.correr_0458("alecita")
alecita.escucharmusica_0458("alecita")
alecita.dormir_0458("alecita")
alecita.bailar_0458("alecita")
alecita.comer_0458("alecita")

