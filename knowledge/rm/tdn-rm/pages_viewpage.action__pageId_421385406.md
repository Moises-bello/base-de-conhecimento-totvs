---
content_hash: 1880a623f9339347256c64200ed06c1e55b35da6d80fe15f3a2e0aabe15a430c
fetched_at: '2026-06-29T00:09:15.537966+00:00'
page_id: '421385406'
product: rm
source: tdn-rm
title: Cálculo do Cronograma de Desembolso Considerando os Contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385406
version: 6
---

O cálculo considerando os contratos do projeto é executado através do processo Calcula Cronograma de Desembolso Considerando Contratos.  Neste caso, para o desembolso de uma tarefa será avaliado primeiramente se ela está associada a um contrato de serviços. Caso esteja, o "Valor Previsto" de cada período do contrato será considerado como o desembolso para a tarefa.

**ATENÇÃO:** Caso a informação Valor Previsto não esteja preenchida nos períodos do contrato de serviço, será considerado que não há desembolso para a tarefa naqueles períodos;  
Caso a totalidade da tarefa não esteja em contratos de serviço, será verificado se existem contratos de fornecimento de material para seus insumos. Caso haja, o valor contratado do insumo será levado em consideração no cálculo do desembolso sobre a quantidade restante da tarefa, ou seja, a quantidade que não foi associada a nenhum contrato de serviços.

**Os valores referentes a contrato só ficarão visíveis no cronograma desembolso agrupados por períodos, e por isso não irão gerar lançamento para o financeiro, por se tratar de várias tarefas e diferentes contratos. Caso deseje visualizar o valor destas tarefas separadamente no cronograma de desembolso e nos lançamentos financeiros, deverá executar o processo sem considerar contrato.**

Se após verificados os contratos de serviço e de fornecimento de material ainda houver quantia remanescente na tarefa para a qual não foi calculado o desembolso, ele então será feito considerando os valores do planejamento da tarefa sobre a quantidade ainda restante.
