---
content_hash: 9d0cf9b92ab49ceae76829f9792963ac238e2440b0ca47283163e9273fabc090
fetched_at: '2026-06-29T00:06:21.988878+00:00'
page_id: '223910225'
product: rm
source: tdn-rm
title: TTYB44_DT_TAXA_FAP_POR_ESTABELECIMENTO_PARA_ENCARGOS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTYB44_DT_TAXA_FAP_POR_ESTABELECIMENTO_PARA_ENCARGOS
version: 125
---

# GERAÇÃO DE ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Geração de Encargos |
| **Situação/Requisito:** | De acordo com resolução CNPS nº 1.327 de 24/09/2015 publicada no Diário Oficial de 25/09/2015, o FAP (Fator Acidentário de Prevenção), o qual estabelece que o cálculo da GPS em 2016 deverá ser determinado por Filial.  Como o campo Percentual dos Encargos é um valor Fixo a ser informado, o Cliente não conseguirá efetuar a geração de nenhum Encargo que envolve INSS, Exemplo: Encargo de Férias, Encargo de 13 pois cada Filial poderá ter uma FAP diferente consequentemente um percentual diferente para o Encargo. |
| **Solução/Implementação:** | Foi adicionado uma checkbox na tela de cadastro de encargo para informar se será ou não acrescentado o percentual FAP por estabelecimento no momento da geração do encargo. Caso esteja marcado, no momento da geração do encargo é buscada a alíquota FAP vigente para a filial em questão no período informado. |
| **Chamados relacionados:** | TTYB44, TTYB46, TTXOEL |
| **Versões/Release:** | 11.82.43, 11.83.55, 12.1.9 |

divs
