#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PadroesExemplos import PadroesExemplos
from PadroesAnalisar import PadroesAnalisar
from CalcularDistanciaPadroes import CalcularDistanciaPadroes

arquivo_analise = sys.argv[1]
arquivo_padroes_exemplos = sys.argv[2]
 
arquivo = open(arquivo_padroes_exemplos, 'r')
padroes_exemplos = PadroesExemplos(arquivo)
tabela_exemplos_padroes = padroes_exemplos.ler_arquivo_coloca_no_array()

arquivo_analise = open(arquivo_analise, 'r')
padroes_analise = PadroesAnalisar(arquivo_analise)
tabela_analise = padroes_analise.ler_arquivo_coloca_no_array()

distancia = CalcularDistanciaPadroes(tabela_exemplos_padroes, tabela_analise, arquivo)
distancia.distancia_euclidiana()