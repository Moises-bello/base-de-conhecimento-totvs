---
content_hash: 17e24e9dfa18e1565e2bae82ca40115b7e593bf7b48c57416f5a289c049e8c2e
fetched_at: '2026-06-29T00:06:25.756321+00:00'
page_id: '224445114'
product: rm
source: tdn-rm
title: TUDEK2_DT_Geracao_Encargos
type: documentation
url: https://tdn.totvs.com/display/LRM/TUDEK2_DT_Geracao_Encargos
version: 120
---

# GERAÇÃO DE ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Geração de encargos* |
| **Situação/Requisito:** | Referente ao mês de janeiro, temos a seguinte situação.  O calculo do encargo INSS 13o SAL - DEDUCAO SAL MATERNIDADE (calculado pelo tipo de encargo G - Dedução 13o ref. a lic. maternidade), esta sendo calculado utilizando o ano 2016.  Já na geração da guia, o calculo remete ao ano 2015, ficando com valores diferentes. |
| **Solução/Implementação:** | Otimizado geração de encargos para encargo de dedução de salário maternidade, de forma que o sistema busque no envelope do funcionário o valor do evento de diferença de 13 de licença maternidade e o inclua no cálculo do encargo |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUDEK2 TUFTJY |
| **Requisito (ISSUE):** |  |

divs
