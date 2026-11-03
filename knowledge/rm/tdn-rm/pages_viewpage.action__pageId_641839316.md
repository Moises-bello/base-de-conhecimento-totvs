---
content_hash: ec7c0528da1cc2582c74d4c39f361d98eb7d1954f3b077684b0d2057aae39e69
fetched_at: '2026-06-29T00:11:10.174414+00:00'
page_id: '641839316'
product: rm
source: tdn-rm
title: FISCAL01-16575 - DT DMA-BA - QUADROS 40 a 92 - Implementação dos Registros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=641839316
version: 5
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DMA-BA |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16575 |

## **02. SITUAÇÃO/REQUISITO**

Implementar dos QUADROS 40 a 92

## **03. SOLUÇÃO**

Gerados de Acordo com Lançamentos Fiscais com determinadas Regras:

Regras:

Dentro do Estado:  
Entrada:

Naturezas Sintéticas: 1949 ou >= 1553 e <= 1555 ou >= 1905 e <= 1914 ou >= 1917 e <= 1926 e Tipo Op. Não Especifica:

Não Incidência - 1  
Industria - 2  
Demonstração - 3  
Amostra - 4  
Suspensão ICMS - 5  
Deposito - 7  
Embalagens - 8  
Brindes - 9  
Não Dedutíveis - 10

Naturezas Sintéticas: 1901,1902 e Tipo Op .Não Especifica: Industria - 2  
Naturezas Sintéticas: 1904,1414,1415 - 6

Saídas:

Naturezas Sintéticas: 5554,5555,5929,5932,5949 ou >= 5905 e <= 5914 >= 5916 e <= 5926 e Tipo Op. Não Especifica:

Não Incidência - 27  
Industria - 28  
Demonstração - 29  
Amostra - 30  
Suspensão ICMS - 31  
Deposito - 33  
Embalagens - 34  
Brindes - 35  
Não Dedutíveis - 36

Naturezas Sintéticas: 5412,5413,5551,5552,5553,5557,5556 - 26  
Naturezas Sintéticas: 5901,5902,5903 e Tipo Op. Não Especifica: Industria - 28  
Naturezas Sintéticas: 5904,5414,5415 - 32

Fora do Estado:  
Entrada:

Naturezas Sintéticas: 2949 ou >= 2553 e <= 2555 ou >= 2905 e <= 2914 ou >= 2917 e <= 2925 e Tipo Op. Não Especifica:

Não Incidência - 11  
Industria - 12  
Demonstração - 13  
Amostra - 14  
Suspensão ICMS - 15  
Deposito - 17  
Embalagens - 18  
Brindes - 19  
Não Dedutíveis - 20

Naturezas Sintéticas: 2901,2902 e Tipo Op. Não Especifica: Industria - 12  
Naturezas Sintéticas: 2904,2414,2415 - 16

Saídas:

Naturezas Sintéticas: 6412,6413,6551,6552,6553,6557,6556: - 37  
Naturezas Sintéticas: 6554,6555,6929,6932,6949 ou >= 6905 e <= 6914 ou >= 6917 e <= 6925 e Tipo Op. Não Especifica:

Não Incidência - 38  
Industria - 39  
Demonstração - 40  
Amostra - 41  
Suspensão ICMS - 42  
Deposito - 44  
Embalagens - 45  
Brindes - 46  
Não Dedutíveis - 47

Naturezas Sintéticas: 6551,6552,6557,6555,6556 - 37  
Naturezas Sintéticas: 6901,6902,6903 e Tipo Op. Não Especifica = Industria - 28  
Naturezas Sintéticas: 6904,6414,6415 - 43

Exterior:

Naturezas Sintéticas: 3553,3930,3949 e Tipo Op. Não Especifica  
Não Incidência - 21  
Industria - 22  
Suspensão ICMS - 23  
Amostra - 24  
Não Dedutíveis - 25

Naturezas Sintéticas: 7930,7949 e Tipo Op. Não Especifica  
Não Incidência - 49  
Industria - 50  
Suspensão ICMS - 51  
Amostra - 52  
Não Dedutíveis - 53

Registro:  
TipoReg                  Fixo 40 a 92  
Ano                        Ano de Referência   
Mes                        Ano de Referência  
Inscrição Estadual Inscrição Estadual  
VlrBaseCalculo      BASEREDICMS  
VlrIsentas              IsentoICMS  
VlrOutras              OutrosICMS
