from durable.lang import *
from coto import *
from metafory import *

with ruleset('Kierunek'):
 
    @when_all((m.matura == 'polski') & (m.hista == 'tak')& (m.zabytki == 'tak'))
    def archeologia(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'archeologia' ,'metafora': metafora_archeologia, 'wyjanienie': coto_archeologia })
        
    @when_all((m.matura == 'polski') & (m.hista == 'nie')& (m.jezyki == 'tak'))
    def stosunki_miedzynarodowe(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'stosunki miedzynarodowe' ,'metafora': metafora_stosunkimiedzynarodowe, 'wyjanienie': coto_stosunkimiedzynarodowe })
        
    @when_all((m.matura == 'polski') & (m.hista == 'tak')& (m.zabytki == 'nie')& (m.prawnicze == 'tak'))
    def prawo(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'prawo' ,'metafora': metafora_prawo, 'wyjanienie': coto_prawo })

    @when_all((m.matura == 'polski') & (m.hista == 'tak')& (m.zabytki == 'nie')& (m.prawnicze == 'nie'))
    def historia(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'historia' ,'metafora': metafora_historia, 'wyjanienie': coto_historia })

    @when_all((m.matura == 'polski') & (m.hista == 'nie')& (m.jezyki == 'nie')& (m.artykuly == 'tak'))
    def dziennikarstwo(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'dziennikarstwo' ,'metafora': metafora_dziennikarstwo, 'wyjanienie': coto_dziennikarstwo })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'tak') & (m.fauna == 'tak')& (m.przyroda == 'tak'))
    def biologia(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'biologia' ,'metafora': metafora_biologia, 'wyjanienie': coto_biologia })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.technologie == 'nie')& (m.finanse == 'tak')& (m.ksiegowy == 'tak'))
    def rachunkowosc(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'rachunkowosc' ,'metafora': metafora_rachunkowosc, 'wyjanienie': coto_rachunkowosc })
        
    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.technologie == 'nie')& (m.finanse == 'tak')& (m.ksiegowy == 'nie'))
    def ekonomia(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'ekonomia' ,'metafora': metafora_ekonomia, 'wyjanienie': coto_ekonomia })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.technologie == 'tak'))
    def informatyka(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'informatyka' ,'metafora': metafora_informatyka, 'wyjanienie': coto_informatyka })

    @when_all((m.matura == 'polski')& (m.hista == 'nie') & (m.jezyki == 'nie')& (m.artykuly == 'nie') & (m.wychowanie == 'tak'))
    def pedagogika(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'pedagogika' ,'metafora': metafora_pedagogika, 'wyjanienie': coto_pedagogika })

    @when_all((m.matura == 'polski')& (m.hista == 'nie') & (m.jezyki == 'nie')& (m.artykuly == 'nie') & (m.wychowanie == 'nie'))
    def psychologia(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'psychologia' ,'metafora': metafora_psychologia, 'wyjanienie': coto_psychologia })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'tak') & (m.chemia == 'tak')& (m.fauna == 'nie') & (m.przyroda == 'tak'))
    def chemia(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'chemia' ,'metafora': metafora_chemia, 'wyjanienie': coto_chemia })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'tak') & (m.chemia == 'nie')& (m.fauna == 'nie') & (m.przyroda == 'tak'))
    def fizyka(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'fizyka' ,'metafora': metafora_fizyka, 'wyjanienie': coto_fizyka })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.przyroda == 'tak')& (m.kreatywnosc == 'tak') & (m.rystech == 'tak'))
    def architektura(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'architektura' ,'metafora': metafora_architektura, 'wyjanienie': coto_architektura })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.przyroda == 'tak')& (m.kreatywnosc == 'nie') & (m.rystech == 'tak'))
    def budownictwo(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'budownictwo' ,'metafora': metafora_budownictwo, 'wyjanienie': coto_budownictwo })

    @when_all((m.matura == 'matematyka')& (m.technologie == 'nie') & (m.finanse == 'nie')& (m.przyroda == 'nie') & (m.transport == 'tak'))
    def logistyka(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'logistyka' ,'metafora': metafora_logistyka, 'wyjanienie': coto_logistyka })

    @when_all((m.matura == 'matematyka')& (m.technologie == 'nie') & (m.finanse == 'nie')& (m.przyroda == 'nie') & (m.transport == 'nie'))
    def matematyka(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'matematyka' ,'metafora': metafora_matematyka, 'wyjanienie': coto_matematyka })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.przyroda == 'tak')& (m.rystech == 'nie') & (m.leczyc == 'tak') & (m.coleczyc == 'ludzi'))
    def medycyna(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'medycyna' ,'metafora': metafora_medycyna, 'wyjanienie': coto_medycyna })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.przyroda == 'tak')& (m.rystech == 'nie') & (m.leczyc == 'tak') & (m.coleczyc == 'zwierzeta'))
    def weterynaria(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'weterynaria' ,'metafora': metafora_weterynaria, 'wyjanienie': coto_weterynaria })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.przyroda == 'tak')& (m.rystech == 'nie') & (m.leczyc == 'nie') & (m.mapy == 'tak'))
    def geografia(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'geografia' ,'metafora': metafora_geografia, 'wyjanienie': coto_geografia })

    @when_all((m.matura == 'matematyka')& (m.laboratorium == 'nie') & (m.przyroda == 'tak')& (m.rystech == 'nie') & (m.leczyc == 'nie') & (m.mapy == 'nie'))
    def rolnictwo(c):
        c.assert_fact({ 'kierunek': c.m.kierunek, 'wynik':'rolnictwo' ,'metafora': metafora_rolnictwo, 'wyjanienie': coto_rolnictwo })
    


 

    @when_all(+m.kierunek)
    def output(c):
        print('Doytyczy: {0} otrzymałeś:{1} metafora:{2} coto:{3} '.format(c.m.kierunek,c.m.wynik,c.m.metafora,c.m.wyjanienie))
        global x
        x=('Doytyczy: {0} otrzymałeś:{1} metafora:{2} coto:{3} '.format(c.m.kierunek,c.m.wynik,c.m.metafora,c.m.wyjanienie))
 
 
post('Kierunek', { 'kierunek': '1', 'matura': 'polski', 'hista': 'tak','zabytki':'tak'})
post('Kierunek', { 'kierunek': '2', 'matura': 'polski', 'hista': 'nie','jezyki':'tak'})
post('Kierunek', { 'kierunek': '3', 'matura': 'polski', 'hista': 'tak','zabytki':'nie','prawnicze':'tak'})
post('Kierunek', { 'kierunek': '4', 'matura': 'polski', 'hista': 'tak','zabytki':'nie','prawnicze':'nie'})
post('Kierunek', { 'kierunek': '5', 'matura': 'polski', 'hista': 'nie','jezyki':'nie','artykuly':'tak'})
post('Kierunek', { 'kierunek': '6', 'matura': 'matematyka', 'laboratorium': 'tak','fauna':'tak','przyroda':'tak'})
post('Kierunek', { 'kierunek': '7', 'matura': 'matematyka', 'laboratorium': 'nie','technologie':'nie','finanse':'tak','ksiegowy':'tak'})
post('Kierunek', { 'kierunek': '8', 'matura': 'matematyka', 'laboratorium': 'nie','technologie':'nie','finanse':'tak','ksiegowy':'nie'})
post('Kierunek', { 'kierunek': '9', 'matura': 'matematyka', 'laboratorium': 'nie','technologie':'tak'})
post('Kierunek', { 'kierunek': '10', 'matura': 'polski', 'hista': 'nie','jezyki':'nie','artykuly':'nie','wychowanie':'tak'})
post('Kierunek', { 'kierunek': '11', 'matura': 'polski', 'hista': 'nie','jezyki':'nie','artykuly':'nie','wychowanie':'nie'})
post('Kierunek', { 'kierunek': '12', 'matura': 'matematyka', 'laboratorium': 'tak','chemia':'tak','fauna':'nie','przyroda':'tak'})
post('Kierunek', { 'kierunek': '13', 'matura': 'matematyka', 'laboratorium': 'tak','chemia':'nie','fauna':'nie','przyroda':'tak'})
post('Kierunek', { 'kierunek': '14', 'matura': 'matematyka', 'laboratorium': 'nie','kreatywnosc':'tak','rystech':'tak','przyroda':'tak'})
post('Kierunek', { 'kierunek': '15', 'matura': 'matematyka', 'laboratorium': 'nie','kreatywnosc':'nie','rystech':'tak','przyroda':'tak'})
post('Kierunek', { 'kierunek': '16', 'matura': 'matematyka', 'technologie': 'nie','finanse':'nie','przyroda':'nie','transport':'tak'})
post('Kierunek', { 'kierunek': '17', 'matura': 'matematyka', 'technologie': 'nie','finanse':'nie','przyroda':'nie','transport':'nie'})
post('Kierunek', { 'kierunek': '18', 'matura': 'matematyka', 'laboratorium': 'nie','przyroda':'tak','rystech':'nie','leczyc':'tak','coleczyc':'ludzi'})
post('Kierunek', { 'kierunek': '19', 'matura': 'matematyka', 'laboratorium': 'nie','przyroda':'tak','rystech':'nie','leczyc':'tak','coleczyc':'zwierzeta'})
post('Kierunek', { 'kierunek': '20', 'matura': 'matematyka', 'laboratorium': 'nie','przyroda':'tak','rystech':'nie','leczyc':'nie','mapy':'nie'})
post('Kierunek', { 'kierunek': '21', 'matura': 'matematyka', 'laboratorium': 'nie','przyroda':'tak','rystech':'nie','leczyc':'nie','mapy':'tak'})
 
# print (x)

