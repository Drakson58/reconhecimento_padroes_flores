from scipy.spatial import distance
import json

class CalcularDistanciaPadroes:

    def __init__(self, padroes_exemplos, padroes_analisar, arquivo_padroes):
        self._padroes_exemplos = padroes_exemplos
        self._padroes_analisar = padroes_analisar
        self._arquivo_padroes = arquivo_padroes
        self._resultado_parcial_analise = []
        self._resultado_final_analise = {}


    def distancia_euclidiana(self):
        # De(X, Y) = raizQ (X1 - Y1 )^2 + (X2 - Y2 )^2 + (Xn - Yn )^2 => distance.euclidean([], [])
        for padroes_analise in self._padroes_analisar:
            distancia_minima = distance.euclidean(padroes_analise, self._padroes_exemplos[0])
            for padroes_exemplo in self._padroes_exemplos:
                distancia_euclidiana = distance.euclidean(padroes_analise, padroes_exemplo)
                if distancia_euclidiana < distancia_minima:
                    distancia_minima = distancia_euclidiana
                    self.salva_resultados(padroes_analise, padroes_exemplo, distancia_minima)
        self.salva_no_arquivo_json()
        

    def salva_resultados(self, analisado, vizinho, distancia):
        indice = str(analisado).strip('[]')
        resp_verificacao = self.verifica_existencia_no_array(indice)
        if resp_verificacao:
            self._resultado_parcial_analise.pop(resp_verificacao[1])
            self._resultado_parcial_analise.append(indice)
            self._resultado_final_analise[indice] = {
                'vizinho':vizinho,
                'distancia':distancia,
                'classificao':self.encontra_classificacao_do_padrao(vizinho)
            }
        else:
            self._resultado_parcial_analise.append(indice)
            self._resultado_final_analise[indice] = {
                'vizinho':vizinho,
                'distancia':distancia,
                'classificao':self.encontra_classificacao_do_padrao(vizinho)
            }
        

    def verifica_existencia_no_array(self, analisado):
        if analisado in self._resultado_parcial_analise:
            indice = self._resultado_parcial_analise.index(analisado)
            return [True, indice]
        return False


    def salva_no_arquivo_json(self):
        with open('analise.json', 'w') as json_file:
            json.dump(self._resultado_final_analise, json_file, indent=4)


    def encontra_classificacao_do_padrao(self, vizinho):
        self._arquivo_padroes.seek(0, 0)
        for linha_arquivo in self._arquivo_padroes:
            if linha_arquivo[0:15] == str(vizinho).strip('[]').replace(" ", ""):
                return linha_arquivo[16:]
