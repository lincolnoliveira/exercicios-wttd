import unittest
from poker import valorCarta, rank, comparaMaos, straight, flush, gruposCartas, rankFullHouse, rank2pares


class TestValorCarta(unittest.TestCase):

    def test2vale2(self):
        self.assertEqual(valorCarta('2h'),2)

    def testKvale13(self):
        self.assertEqual(valorCarta('Kd'), 13)

    def test10vale10(self):
        self.assertEqual(valorCarta('10s'), 10)


class TestRank(unittest.TestCase):

    def test_5cartasNumericas(self):
        self.assertEqual(rank(['2h', '5c', '10c', '9h', '7d']), 1009070502)

    def test_3cartasComRepeticaoMaior(self):
        self.assertEqual(rank(['5d', 'Jc', 'Jh']), 111105)

    def test_4cartasComRepeticaoMenor(self):
        self.assertEqual(rank(['5d', 'As', '5h', '10d']), 14100505)

class TestRankFullHouse(unittest.TestCase):

    def test_semFullHouse(self):
        self.assertEqual(rankFullHouse({'Quadra':0, 'Trinca':0, 'Par1':4, 'Par2':0}),0)

    def test_FullHouse305(self):
        self.assertEqual(rankFullHouse({'Quadra':0, 'Trinca':3, 'Par1':5, 'Par2':0}),305)


class TestRank2pares(unittest.TestCase):

    def test_sem2Pares(self):
        self.assertEqual(rank2pares({'Quadra':0, 'Trinca':0, 'Par1':4, 'Par2':0}),0)

    def test_2ParesAsRei(self):
        self.assertEqual(rank2pares({'Quadra':0, 'Trinca':0, 'Par1':14, 'Par2':13}),1413)


class TestStraight(unittest.TestCase):

    def test_semSequencia(self):
        self.assertEqual(straight(['2h', '5c', '10c', '9h', '7d']),0)


    def test_sequenciaForaDeOrdem(self):
        self.assertEqual(straight(['2h', '5c', '4c', '6h', '3d']), 6)

    def test_repeticaoQuaseSequencia(self):
        self.assertEqual(straight(['2h', '5c', '4c', '5h', '3d']), 0)

    def test_sequenciaAltaOrdenada(self):
        self.assertEqual(straight(['10h', 'Jc', 'Qs', 'Kh', 'Ad']), 14)

class TestFlush(unittest.TestCase):

    def test_semFlush(self):
        self.assertEqual(flush(['10h', 'Jc', 'Qs', 'Kh', 'Ad']),0)


    def test_comFlush2Cartas(self):
        self.assertEqual(flush(['3h', 'Ah']), 1403)

    def test_comFlush5Cartas(self):
        self.assertEqual(flush(['3s', 'As', '5s', '10s', 'Js']), 1411100503)


class TestGruposCartas(unittest.TestCase):

    def testSemNada(self):
        self.assertEqual(gruposCartas(['3s', 'As', '5s', '10s', 'Js'])['Quadra'],0)
        self.assertEqual(gruposCartas(['3s', 'As', '5s', '10s', 'Js'])['Trinca'],0)
        self.assertEqual(gruposCartas(['3s', 'As', '5s', '10s', 'Js'])['Par1'],0)
        self.assertEqual(gruposCartas(['3s', 'As', '5s', '10s', 'Js'])['Par2'],0)

    def testComQuadra(self):
        self.assertEqual(gruposCartas(['5s', 'As', '5s', '5h', '5c'])['Quadra'],5)
        self.assertEqual(gruposCartas(['5s', 'As', '5s', '5h', '5c'])['Trinca'],0)
        self.assertEqual(gruposCartas(['5s', 'As', '5s', '5h', '5c'])['Par1'],0)
        self.assertEqual(gruposCartas(['5s', 'As', '5s', '5h', '5c'])['Par2'],0)

    def testComTrinca(self):
        self.assertEqual(gruposCartas(['3s', '3h', '3c', '10s', 'Js'])['Quadra'],0)
        self.assertEqual(gruposCartas(['3s', '3h', '3c', '10s', 'Js'])['Trinca'],3)
        self.assertEqual(gruposCartas(['3s', '3h', '3c', '10s', 'Js'])['Par1'],0)
        self.assertEqual(gruposCartas(['3s', '3h', '3c', '10s', 'Js'])['Par2'],0)

    def testCom1Par(self):
        self.assertEqual(gruposCartas(['3s', '7h', '7c', '10s', 'Js'])['Quadra'],0)
        self.assertEqual(gruposCartas(['3s', '7h', '7c', '10s', 'Js'])['Trinca'],0)
        self.assertEqual(gruposCartas(['3s', '7h', '7c', '10s', 'Js'])['Par1'],7)
        self.assertEqual(gruposCartas(['3s', '7h', '7c', '10s', 'Js'])['Par2'],0)

    def testCom2Pares(self):
        self.assertEqual(gruposCartas(['9d', '7h', '7c', '10s', '9d'])['Quadra'],0)
        self.assertEqual(gruposCartas(['9d', '7h', '7c', '10s', '9d'])['Trinca'],0)
        self.assertEqual(gruposCartas(['9d', '7h', '7c', '10s', '9d'])['Par1'],9)
        self.assertEqual(gruposCartas(['9d', '7h', '7c', '10s', '9d'])['Par2'],7)

    def testComFullHouse(self):
        self.assertEqual(gruposCartas(['9d', '7h', '7c', '9s', '9c'])['Quadra'],0)
        self.assertEqual(gruposCartas(['9d', '7h', '7c', '9s', '9c'])['Trinca'],9)
        self.assertEqual(gruposCartas(['9d', '7h', '7c', '9s', '9c'])['Par1'],7)
        self.assertEqual(gruposCartas(['9d', '7h', '7c', '9s', '9c'])['Par2'],0)


class TestComparaMaos(unittest.TestCase):

    def test_cartaMaisAlta1a(self):
        self.assertEqual(comparaMaos(['2h', '5c', '10c', '9h', 'Kd'],['3h', '9c', '10h', 'Qh', '7d']),1)

    def test_empateCartaMaisAlta(self):
        self.assertEqual(comparaMaos(['2h', '5c', '10c', '9h', 'Kd'],['2h', '5c', '10c', '9h', 'Kd']),0)

    def test_cartaMaisAlta3a(self):
        self.assertEqual(comparaMaos(['2h', '5c', '10c', '7h', 'Kd'],['2s', '5h', '10d', '9d', 'Kc']),2)


    def test_parXalta(self):
        self.assertEqual(comparaMaos(['2h', '2c', '3c', '5h', '4d'],['3h', '9c', '10h', 'Qh', '7d']),1)

    def test_parXpar(self):
        self.assertEqual(comparaMaos(['2h', '2c', '6c', '3h', '4d'],['Jh', 'Jc', '10h', 'Qh', '3d']),2)


    def test_2paresXalta(self):
        self.assertEqual(comparaMaos(['2h', '2c', '3c', '3h', '4d'],['3h', '9c', '10h', 'Qh', '7d']),1)

    def test_2paresX2pares(self):
        self.assertEqual(comparaMaos(['2h', '2c', '6c', '3h', '3d'],['Jh', 'Jc', '10h', 'Qh', 'Qd']),2)


    def test_trincaXalta(self):
        self.assertEqual(comparaMaos(['2h', '2c', '2c', '3h', '4d'],['3h', '9c', '10h', 'Qh', '7d']),1)

    def test_trincaX2pares(self):
        self.assertEqual(comparaMaos(['2h', '2c', '6c', '3h', '2d'],['Jh', 'Jc', '10h', 'Qh', 'Qd']),1)

    def test_trincaXtrinca(self):
        self.assertEqual(comparaMaos(['2h', '2c', '6c', '3h', '2d'],['Jh', 'Jc', '10h', 'Qh', 'Jd']),2)


    def test_straightXsemStraight(self):
        self.assertEqual(comparaMaos(['2h', '5c', '6c', '3h', '4d'],['3h', '9c', '10h', 'Qh', '7d']),1)

    def test_straightX2pares(self):
        self.assertEqual(comparaMaos(['2h', '5c', '6c', '3h', '4d'],['9h', '9c', '10h', '8h', '8d']),1)

    def test_straightXtrinca(self):
        self.assertEqual(comparaMaos(['2h', '5c', '6c', '3h', '4d'],['9h', '9c', '10h', '9h', '8d']),1)

    def test_straightMaisAlto(self):
        self.assertEqual(comparaMaos(['2h', '5c', '6c', '3h', '4d'],['Jh', '9c', '10h', 'Qh', '8d']),2)


    def test_flushXalta(self):
        self.assertEqual(comparaMaos(['2c', '5c', '6c', '3c', '10c'],['Jh', '9c', '10h', 'Qh', '8d']),1)

    def test_flushX2pares(self):
        self.assertEqual(comparaMaos(['2c', '9c', '6c', 'Ac', '4c'],['9h', '10c', '10h', '9h', '8d']),1)

    def test_flushXtrinca(self):
        self.assertEqual(comparaMaos(['2c', '9c', '6c', 'Ac', '4c'],['9h', '9c', '10h', '9h', '8d']),1)

    def test_flushXstraight(self):
        self.assertEqual(comparaMaos(['2c', '9c', '6c', '3c', '10c'],['2h', '5c', '6c', '3h', '4d']),1)

    def test_flushMaisAlto4aCarta(self):
        self.assertEqual(comparaMaos(['Jc', '6c', '4c', '2c', '5c'],['2h', '5h', '6h', '3h', 'Jh']),1)


    def test_fullXalta(self):
        self.assertEqual(comparaMaos(['7h', '7s', '4h', '7d', '4c'],['2h', '5s', '6s', '3d', 'Jh']),1)

    def test_fullX2pares(self):
        self.assertEqual(comparaMaos(['9h', '9s', '4c', '3h', '4d'],['7h', '2s', '2h', '7d', '7c']),2)

    def test_fullXtrinca(self):
        self.assertEqual(comparaMaos(['9h', '9s', '9c', '3h', '4d'],['7h', '2s', '2h', '7d', '7c']),2)

    def test_fullXstraightMaisAlto(self):
        self.assertEqual(comparaMaos(['7h', '5s', '6h', '3h', '4d'],['7h', 'As', 'Ah', '7d', '7c']),2)

    def test_fullXflushMaisAlto(self):
        self.assertEqual(comparaMaos(['7h', '5h', 'Ah', 'Jh', '4h'],['7h', 'As', 'Ah', '7d', '7c']),2)

    def test_fullXfull(self):
        self.assertEqual(comparaMaos(['7h', '7s', 'Ah', 'Ad', '7c'],['3c', '3c', 'Jh', 'Js', 'Jd']),2)


    def test_quadraXalta(self):
        self.assertEqual(comparaMaos(['7h', '7s', '4h', '7d', '7c'],['2h', '5s', '6s', '3d', 'Jh']),1)

    def test_quadraX2pares(self):
        self.assertEqual(comparaMaos(['9h', '9s', '4c', '3h', '4d'],['7h', '2s', '2h', '2d', '2c']),2)

    def test_quadraXtrinca(self):
        self.assertEqual(comparaMaos(['9h', '9s', '9c', '3h', '4d'],['7h', '2s', '2h', '2d', '2c']),2)

    def test_quadraXstraightMaisAlto(self):
        self.assertEqual(comparaMaos(['7h', '5s', '6h', '3h', '4d'],['7h', '7s', 'Ah', '7d', '7c']),2)

    def test_quadraXflushMaisAlto(self):
        self.assertEqual(comparaMaos(['7h', '5h', 'Ah', 'Jh', '4h'],['7h', '7s', 'Ah', '7d', '7c']),2)

    def test_quadraXfull(self):
        self.assertEqual(comparaMaos(['7h', '7s', 'Ah', '7d', '7c'],['3c', 'Jc', 'Jh', '3s', '3d']),1)

    def test_2quadras(self):
        self.assertEqual(comparaMaos(['7h', '7s', 'Ah', '7d', '7c'],['3c', 'Jc', 'Jh', 'Js', 'Jd']),2)


    def test_straightFlushXalta(self):
        self.assertEqual(comparaMaos(['3c', '6c', '4c', '2c', '5c'],['2h', '5s', '6h', '3h', 'Jh']),1)

    def test_sraightFlushX2pares(self):
        self.assertEqual(comparaMaos(['9h', '9s', '4c', '3h', '4d'],['3c', '6c', '4c', '2c', '5c']),2)

    def test_sraightFlushXtrinca(self):
        self.assertEqual(comparaMaos(['9h', '9s', '9c', '3h', '4d'],['3c', '6c', '4c', '2c', '5c']),2)

    def test_straightFlushXstraightMaisAlto(self):
        self.assertEqual(comparaMaos(['7h', '5s', '6h', '3h', '4h'],['3c', '6c', '4c', '2c', '5c']),2)

    def test_straightFlushXflushMaisAlto(self):
        self.assertEqual(comparaMaos(['7h', '5h', 'Ah', 'Jh', '4h'],['3c', '6c', '4c', '2c', '5c']),2)

    def test_straightFlushXfull(self):
        self.assertEqual(comparaMaos(['2c', '3c', '4c', '5c', '6c'],['3c', 'Jc', 'Jh', '3s', '3d']),1)

    def test_straightFlushXquadra(self):
        self.assertEqual(comparaMaos(['7h', '7s', 'Ah', '7d', '7c'],['3c', '6c', '4c', '2c', '5c']),2)

    def test_2straightFlush(self):
        self.assertEqual(comparaMaos(['7h', '5h', '6h', '8h', '4h'],['3c', '6c', '4c', '2c', '5c']),1)

    def test_2straightFlushIguais(self):
        self.assertEqual(comparaMaos(['7h', '5h', '6h', '8h', '4h'],['7d', '5d', '6d', '8d', '4d']),0)
