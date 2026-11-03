---
content_hash: f396073731a1f036590a8e340a5b49a2fa0457e209248dd18662d7a75c62e0af
fetched_at: '2026-06-29T00:10:08.645662+00:00'
page_id: '452719552'
product: rm
source: tdn-rm
title: Layout da Ficha Financeira
type: documentation
url: https://tdn.totvs.com/display/LRM/Layout+da+Ficha+Financeira
version: 1
---

**Layout da Ficha Financeira**   
Para que a importação do movimento da Ficha Financeira seja realizado corretamente, é necessário que o arquivo siga o seguinte layout:

|  |  |  |  |
| --- | --- | --- | --- |
| **DESCRIÇÃO** | **TIPO** | **TAMANHO** | **CAMPO** |
| Chapa do Funcionário | String | 16 | 1 |
| Ano de Competência | Inteiro | 4 | 2 |
| Mês de Competência | Inteiro | 2 | 3 |
| Nº do Período | Inteiro | 2 | 4 |
| Código do Evento | String | 4 | 5 |
| Data de Pagamento | Data | 8 | 6 |
| Hora (Formato HHH:MM) | String | 6 | 7 |
| Referência (Formato 999,99 | Real | 6 | 8 |
| Valor (Formato 999999999999,99) | Real | 15 | 9 |
| Valor Original (Formato 999999999999,99) | Real | 15 | 10 |
