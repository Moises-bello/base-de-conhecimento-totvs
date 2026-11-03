---
content_hash: 3a92328f71d0c884e42228545fc69db49d8be5490099f44e80080a4fca612edf
fetched_at: '2026-06-29T00:10:53.009945+00:00'
page_id: '574130451'
product: rm
source: tdn-rm
title: DT-  Provisão Férias - Período aquisitivo perdido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574130451
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Geração do Histórico de Provisões |
| **Situação/Requisito:** | Gerar Provisão de férias zerado para funcionário que perderam direito às férias devido ao número de faltas. |
| **Solução/Implementação:** | Criado o parâmetro “Somente férias antecipadas” localizado abaixo dos parâmetros “Permite valores Negativos” e “Permite avos negativos” que considerarão somente as férias antecipadas para permitir avos e valores negativos, ou seja, para perda do período aquisitivo integral por faltas a provisão será zerada caso esse parâmetro esteja marcado.  Os parâmetros só devem ficar habilitados se os parâmetros “Permite valores Negativos” e “Permite avos negativos” estiverem marcados. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-11868](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-11868) |
| **Documento de Referência:** | [Geração do Histórico de Provisões](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719548) |
| **Pacote:** | N/A |
