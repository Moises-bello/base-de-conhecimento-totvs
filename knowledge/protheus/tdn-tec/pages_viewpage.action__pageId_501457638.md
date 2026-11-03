---
content_hash: 3ede4e32b2df1e9dccf48d6bdf5eea75c9fd3d0763fc97fabdd7dfeebce03ee8
fetched_at: '2026-07-02T19:24:25.685271+00:00'
page_id: '501457638'
product: protheus
source: tdn-tec
title: Correção - Update automático sendo feito em toda execução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501457638
version: 1
---

O update automático do SmartClient estava sendo executado em toda execução, mesmo após ter sido atualizado o AppServer indicava que necessitava de uma atualização.

|  |  |
| --- | --- |
| Situação | O update automático do SmartClient acontecia mesmo estando atualizado. |
| Ocorrência | Acontecia por uma divergência de horário/fuso horário entre a estação que estava executando o AppServer e a do SmartClient. |
| Correção | Foi melhorada a checagem por arquivos divergentes entre o SmartClient e o AppServer pra levar em consideração uma medida padrão de tempo. |
| Informações adicionais | * Referente ao chamado: 6213180 * Referente à ocorrência: MTEC-2898 * Disponível em builds superiores a 17.3.0.9 |
