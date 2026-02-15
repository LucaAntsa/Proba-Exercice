import unittest
from proba import lancer_piece

class testLancePiece(unittest.TestCase):
    def test_lancier_piece(self):
        #voir si on a 1 ou 0
        for i in range(3):
            resulat = lancer_piece()
            #self assertIn le (output, resultat attendu soit qu je veux)
            self.assertIn(resulat, [1,0])

if __name__ == "__main__":
    unittest.main()