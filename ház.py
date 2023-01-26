def balvjobb(valto):
    if valto%2 ==0:
        return True
    elif valto%2 !=0:
        return False
        
utcanev=None        
while utcanev !='':
    utcanev=input('Kérem adja meg az utca nevét. ')
    if utcanev !='':
        hazszam=int(input('Kérem adja meg a házszámát. '))
    if balvjobb(hazszam) == True:
        print(f'A(z) {utcanev} {hazszam} jobb oldalt van.')

    elif balvjobb(hazszam) == False:
        print('A(z)',utcanev, hazszam,'bal oldalt van.')
