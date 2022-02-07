from durable.lang import *

with ruleset('kierunek'):

    @when_all((m.matura=='polski') & (m.hista=='tak') & (m.zabytki=='tak'))
    def archeologia(c):
        c.assert_fact({'wybor':c.m.wybor,'wynik':'archeologia', 'metafora': 'tresc metafory','wyjasnienie':'cotowyjasnienie'})

    @when_all((m.matura=='polski') & (m.hista=='nie') & (m.jezyki=='tak'))
    def stosunki_miedzynarodowe(c):
        c.assert_fact({'wybor':c.m.wybor,'wynik':'archeologia', 'metafora': 'tresc metafory','wyjasnienie':'cotowyjasnienie'})

    @when_all(+m.zamowienie)
    def output(c):
        print('nr wyniku: {0} nazwa: {1} metafora: {2}: coto: {3}' .format(c.m.zamowienie, c.m.wynik, c.m.metafora, c.m.wyjasnienie))

