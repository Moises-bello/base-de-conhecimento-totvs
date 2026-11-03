---
content_hash: 013b12fd82c2a4689da302a2c1cdb2f35ab233372ad7518c2e77c8c5b1913039
fetched_at: '2026-06-29T00:08:28.113100+00:00'
page_id: '271659797'
product: rm
source: tdn-rm
title: 387471 MRH-6523 DT Geração de Encargos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271659797
version: 111
---

# GERAÇÃO DE ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração de Encargos* |
| **Situação/Requisito:** | Ao gerar o encargo de provisão do tipo 8 - Provisão de FGTS de 13o. salário com os parâmetros de provisão acumulada e Abate Adiantamento de 13º marcada, para um funcionário que teve adiantamento da primeira parcela de décimo terceiro salário o sistema não abate o valor da parcela, gera o encargo sem o acumulado, isso no mês de Dezembro, no mês de Novembro o abatimento é realizado corretamente. |
| **Solução/Implementação:** | Ajuste no processo de geração de encargos quando a opção de  provisão acumulada e Abate Adiantamento de 13º quando estiver marcada nos parâmetros, pois se já tiver valor para o código de cálculo 35 não deve buscar o valor do código de cálculo 9. |
| **Tickets relacionados:** | * [387471](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%22387471%22 "387471") |

divs
