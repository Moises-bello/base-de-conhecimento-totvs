---
content_hash: 211a182b449555b5c6908eb60ca821ec1f14e1a190889339e770ad3661527e2c
fetched_at: '2026-06-29T00:12:10.748875+00:00'
page_id: '953003691'
product: rm
source: tdn-rm
title: Grupo W02 – Total da NF-e / Retenção de Tributos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003691
version: 1
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo W02 – Total da NF-e / Retenção de Tributos** | | | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 348 | W23 | retTrib | Grupo Retenções de Tributos | G | W01 | - | 0-1 | - | Exemplos de atos normativos que definem obrigatoriedade da retenção de contribuições: a) IRPJ/CSLL/PIS/COFINS - Fonte - Recebimentos de Órgão Público Federal, Lei nº 9.430, de 27 de dezembro de 1996, art. 64, Lei nº 10.833/2003, art. 34, como normas infralegais, temos como exemplo: IN SRF 480/2004 e IN 539, de 25/04/05. b) Retenção do Imposto de Renda pelas Fontes Pagadoras, REMUNERAÇÃO DE SERVIÇOS PROFISSIONAIS PRESTADOS POR PESSOA JURÍDICA, Lei nº 7.450/85, art. 52 |  |  | Serão selecionados somentes tributos do movimento com os tipo PISRF, COFINSRF, CSLLRF, IRRFPJ, IRRF ou INSS. |
| 349 | W24 | vRetPIS | Valor Retido de PIS | E | W23 | N | 0-1 | 13v2 | TTRBMOV.VALOR |  |  |
| 350 | W25 | vRetCOFINS | Valor Retido de COFINS | E | W23 | N | 0-1 | 13v2 | TTRBMOV.VALOR |  |  |
| 351 | W26 | vRetCSLL | Valor Retido de CSLL | E | W23 | N | 0-1 | 13v2 | TTRBMOV.VALOR |  | Será selecionado a codificação do municipio conforme os dados do municipio de prestação preenchidos no movimento (TMOV.CODETDMUNSERV TMOV.CODMUNSERVICO) e a classificação IBGE utilizada nos parametros (DPARAMETROS.IDCLASSIFMUNICIBGE). |
| 352 | W27 | vBCIRRF | Base de Cálculo do IRRF | E | W23 | N | 0-1 | 13v2 | TTRBMOV.BASEDECALCULO |  |  |
| 353 | W28 | vIRRF | Valor Retido do IRRF | E | W23 | N | 0-1 | 13v2 | TTRBMOV.VALOR |  |  |
| 354 | W29 | vBCRetPrev | Base de Cálculo da Retenção da Previdência Social | E | W23 | N | 0-1 | 13v2 | TTRBMOV.BASEDECALCULO |  | A geração das tags **vBCRetPrev** e **vRetPrev**, referente ao imposto retido do **Funrural** e **INSS**. Passa a ser considerado a seguinte regra, para geração das tags:   ● Existir tributo principal (deve existir tributo Funrural ou INSS com tipo de recolhimento “Retido na Fonte”)   Será seguido a seguinte regra para totalizar as tags: ● Os outros tributos devem ser do mesmo tipo do tributo principal( exemplo, para o INSS15, INSS20 e INSS25 o tipo de tributo deve ser INSS)   Quando o tipo de recolhimento for “Retido na fonte” as tags **serão** geradas no XML da NF-e Tipo de recolhimento for diferente de "Retido na Fonte" as demais tags  **não serão** geradas. |
| 355 | W30 | vRetPrev | Valor da Retenção da Previdência Social | E | W23 | N | 0-1 | 13v2 | TTRBMOV.VALOR |  |
