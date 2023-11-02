import random
def quiz_namen(naam):
    namen1 = ['danny', 'sean', 'thomas', 'marc', 'thijmen', 'maurits', 'bram', 'dean', 'soufyan', 'conrad', 'stef', 'ross', 'sylvie', 'mathieu', 'steven', 'sebastiaan', 'kaj', 'michelle']
    namen2 = ['thijmen', 'maureen', 'owen', 'demi', 'imran', 'jabir', 'casper', 'stijn', 'niels', 'norma', 'jayden', 'ahsen', 'adil', 'jesse', 'isis', 'garon', 'thijmen']
    docent = ['thomas', 'martijn', 'lukas', 'jan']
    studenten = namen1 + namen2 
    if naam in studenten:
        print('Found student')
    if naam in docent:
        print("Found docent")



player1 = input("player1 name:")
quiz_namen(player1)
print(f'hallo {player1}')
def antwoorden_goed_of_fout(antwoord, getal):
        antwoorden = {
        'goed': [f'ja goed gedaan {player1}', f'zeer goed {player1}', f'{player1} jij hebt 100 procent google gerbuikt',f'goed bezig{player1}', f'jajajajajjaja {player1}', f'universiteit niveuuaw jij {player1}' ],
        'fout': [f'nee jammer dit {player1}', f'dit heb je goed....  nee grapje', f'een kind zou dit zelfs weten hoe jij niet {player1}?', f'foutfoutfout {player1}', f'beetje dom {player1} maar geeft niet']
        }

        print(antwoorden[antwoord][getal])
#antwoorden_goed_of_fout('fout',(random.randint(0,5)) )
#antwoorden_goed_of_fout('goed',(random.randint(0,6)) )



print('\n\n\njajajaja dit is algemene kennis quiz 10 vragen en als je alles goed hebt krijg je niks')

antwoord=input('Ben je klaar om de Quiz te spelen? (ja/nee) :')
punten=0
aantal_vragen=10

if antwoord.lower()=='ja':

    print('\n\nMooi, je gaat toch niks goed hebben dusja')
    
    antwoord=input('Vraag 1:  Op het embleem van welk luxueus Italiaans automerk staat een chargerende stier?=')
    if antwoord.lower()=='lamborghini' or antwoord.lower()=='lambo':
        punten += 1
        #print('geluk.')
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) ), quiz_namen(player1)
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) ),quiz_namen(player1)


    antwoord=input('Vraag 2: Welke stripfiguur is als kind in een ketel toverdrank gevallen en werd daardoor supersterk?=')
    if     antwoord.lower()=='obelix' or antwoord.lower()=='obelix':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) )

    antwoord=input('Vraag 3: Hoe heet in de psychologie het gevoel dat men een huidige situatie al eens eerder heeft meegemaakt?=')
    if antwoord.lower()=='deja vu' or antwoord.lower()=='déjà vu':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) )
        
    antwoord=input('Vraag 4: Welke kleur krijg je als je magenta mengt met cyaan?= ')
    if antwoord.lower()=='paars' or antwoord.lower()=='paars':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) )

    antwoord=input('Vraag 5:  In welk land ligt het befaamde stadje Tsjernobyl?=')
    if antwoord.lower()=='Oekraïne' or antwoord.lower()=='oekraine':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
       antwoorden_goed_of_fout('fout',(random.randint(0,5)) )

    antwoord=input('Vraag 6: Waar ben je bang voor als je cryofobie hebt= ')
    if antwoord.lower()=='bang voor kou' or antwoord.lower()=='bang voor ijs' or antwoord.lower()=='bang voor kou en ijs':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) )

    antwoord=input('Vraag 7: Wat zijn de klinkers?=')
    if antwoord.lower()=='a,e,i,o,u' or antwoord.lower()=='a,e,i,o,u':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) )

    antwoord=input('Vraag 8: Hoe noemen we het moment waarop het heelal ontstond?=')
    if antwoord.lower()=='big bang' or antwoord.lower()=='oerknal':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) )

    antwoord=input('Vraag 9: Waarvoor staat de term E.H.B.O.?=')
    if antwoord.lower()=='Eerste Hulp Bij Ongevallen' or antwoord.lower()=='eerste hulp bij ongevallen':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) )

    antwoord=input('Vraag 10: Welke winkel heeft als slogan Steeds verrassend, altijd voordelig?')
    if antwoord.lower()=='Kruidvat' or antwoord.lower()=='kruidvat':
        punten += 1
        antwoorden_goed_of_fout('goed',(random.randint(0,6)) )
    else:
        antwoorden_goed_of_fout('fout',(random.randint(0,5)) )
        
        
    print('\n\nyesyes je bent klaar, je hebt '+str(punten)+' van de '+str(aantal_vragen)+' vragen goed!')
    cijfer = round(float(10/aantal_vragen*punten), 1)
    print('Je eindcijfer is '+str(cijfer)+'.')
    if punten >= 7: print('goed gedaan maar kan altijd beter!')
    else:           print('ik stuur je wel terug naar een basisschool https://www.junioreinstein.nl/. \n\n')

elif antwoord.lower()=='nee':
    print('Kom maar terug wanneer je alles hebt gegoogled\nDOEIDOEI')
else:
    print('Dit antwoord ken ik niet!')
    

    
   







