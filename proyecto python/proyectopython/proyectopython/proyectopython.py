import random
def main():
    palabras = ['ESFEROGRAFICO', 'DALTONICOS', 'ESTUDIANTE', 'UNIVERSITARIO', 'FOTOSINTESIS','FABRICANTE',
                'TELEVISION', 'INCOMPETENTE', 'REPRODUCTOR', 'MICROSCOPIO',
            'VENTILADORES', 'NACIMIENTO', 'HOLISTICAMENTE', 'PARACAIDAS', 'BORRADORES',
            'REFRIGERADOR', 'ORNITORRINCO', 'OTORRINOLARINGOLOGO', 'CALEIDOSCOPIO', 'PARALELEPIPEDO',
            'ELECTRODOMESTICO', 'ELECTROCARDIOGRAMA', 'VACACIONES', 'YERBATEROS', 'ASTRONAUTA',
            'FONOGRAFOS', 'INTRANSIGENTE', 'HEDONISMOS', 'DESALENTADO', 'INVEROSIMIL']
    letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    def plrnd():
        palt=random.choice(palabras)
        return palt
    def puestos(nump=4):
        lisr=[]
        while len(lisr)<nump:
            l=random.choice(letras)
            if l in palt:
                if l not in lisr:
                    lisr.append(l)
        return lisr
    def repeticion():
        pit=[]
        for c in palt:
            if c not in pit:
                pit.append(c)
        p=len(pit)
        return p
    def maskcad(li=0):
        palmask=list(palt)
        for reem in lisr:
            for lv in palmask:           
                if lv==reem:
                    while reem in palmask:
                        ubic=palmask.index(lv)
                        palmask[ubic]="*"
        return palmask
    def turnos(t=8):
        ti=0
        score=0
        while ti<t:
            lin=""
            while lin not in letras:
                print("Turno: ",(ti+1))
                print(("".join(palmask)))
                print("Ingrese una letra")
                lin=input()
            if lin in lisr:
                if palt.count(lin)==1:
                    palmask[palt.find(lin)]=lin
                    score+=1
                elif palt.count(lin)>1:
                    i=0
                    while i<len(palmask):
                        if palt[i]==lin:
                            palmask[i]=lin
                            score+=1
                        i+=1
            if "".join(palmask)==palt:
                print("Felicidades, ha ganado")
                print("Su puntaje es: ", score,"\n\n")
                ti=t
            elif ti>=t:
                print("Ha perdido")
                print("Su puntaje es de: ", score,"\n\n")
            ti+=1
    op=0
    while op!=4:
        print("1. Jugar\n2. Ingresar número de turnos\n3. Ingresar número de puestos aleatorios\n4. Salir")
        op=int(input())
        if op==1:
            palt=plrnd()
            lisr=puestos()
            palmask=maskcad()
            turnos()
            print("La palabra es: ",palt,"\n\n")
        elif op==2:
            palt=plrnd()
            lisr=puestos()
            palmask=maskcad()
            print("Ingrese numero de turnos: ")
            trn=int(input())
            turnos(trn)
            print("La palabra es: ",palt,"\n\n")
        elif op==3:
            palt=plrnd()
            print("ingrese numero de puestos que no sea mas grande que %i: "%repeticion())
            p=int(input())
            lisr=puestos(p)
            palmask=maskcad()
            turnos()
            print("La palabra es: ",palt,"\n\n")
        lisr=[]
if __name__=="__main__":
    main()