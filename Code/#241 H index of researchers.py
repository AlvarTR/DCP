"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""
import time, unittest

def hIndexOfPapersQuadratic( listOfCitations ):
    """ Time = O(n^2), Space = O(1) """
    EH = 0
    for e in listOfCitations:
        try:
            aux = int(e)
            if aux < 0:
                return EH
        except ValueError:
            return EH

    #print()
    #print()
    #print("New citation list:", listOfCitations)
    hIndex = 0
    for citations in listOfCitations:
        if citations <= hIndex:
            continue

        moreCitatedPapers = 0
        #print()
        for number in listOfCitations:
            #print("Citation:", citations, "; Compare to:", number)
            if number >= citations:
                moreCitatedPapers += 1
            #print("Papers with at least", citations, "citations:", moreCitatedPapers)
            if moreCitatedPapers >= citations:
                hIndex = citations
                break

    #print("H Index =", hIndex)
    return hIndex

def hIndexOfPapersLogLineal( listOfCitations ):
    #Error Handling
    #Ordena los elementos de mayor a menor
    #Para todo numero distinto
        #Escoge la posicion mas a la dcha de las repeticiones de ese numero
        #Cuenta los elementos que hay a su izda + si mismo
        #Si cuenta >= numero
            #Devuelve hIndex = numero
    pass

def hIndexOfPapersLineal( listOfCitations ):
    """ Time = O(n), Space = O(n) """

    #Error Handling
    hIndexDict = {0:0}
    for citations in listOfCitations:
        if citations not in hIndexDict:
            hIndexDict[citations] = 0

        for registeredCitations in [n for n in range(citations+1) if n in hIndexDict]:
            hIndexDict[registeredCitations] += 1

    hIndex = 0
    for key in hIndexDict:
        if hIndex >= key:
            continue

        if hIndexDict[key] >= key:
            hIndex = key

    return hIndex


class Prueba(unittest.TestCase):
    ITERACIONES = 500

    def testCheckearCuadratico(self):
        chrono = time.time()
        for i in range(1, self.ITERACIONES):
            hIndex = hIndexOfPapersQuadratic( list(range(i)) )
            self.assertEqual( hIndex, int(i/2.0) )
        print("Cuadratico:", time.time() - chrono)

    def testCheckearLineal(self):
        chrono = time.time()
        for i in range(1, self.ITERACIONES):
            hIndex = hIndexOfPapersLineal( list(range(i)) )
            self.assertEqual( hIndex, int(i/2.0) )
        print("Lineal:", time.time() - chrono)

if __name__ == "__main__":
    unittest.main()
