
class PadroesAnalisar:

    def __init__(self, arquivo_analisar):
        self._arquivo_analisar = arquivo_analisar
        self._array_com_padroes_analise = []
    
    def ler_arquivo_coloca_no_array(self):
        for linha_com_padraoes in self._arquivo_analisar:
            linha_atual = linha_com_padraoes[0 : 15]
            self._array_com_padroes_analise.append(self.tranforma_cada_padrao_em_float(linha_atual))
        return self._array_com_padroes_analise


    def tranforma_cada_padrao_em_float(self, linha_atual):
        padroes_separados = linha_atual.split(',')
        for cont in range(0, 4):
            padroes_separados[cont] = float(padroes_separados[cont])
        return padroes_separados