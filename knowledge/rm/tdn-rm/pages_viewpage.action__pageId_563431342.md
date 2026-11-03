---
content_hash: 3c781fa191a02a32efa939012974e46978b5b3c692050ef6440d70fbe338742e
fetched_at: '2026-06-29T00:10:50.812908+00:00'
page_id: '563431342'
product: rm
source: tdn-rm
title: Lançamentos do Diário (Ernst & Young)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=563431342
version: 13
---

Através desse layout é possível extrair dados dos lançamentos contábeis diários que irão apoiar as auditorias das demonstrações financeiras realizadas pela Ernst & Young. 

| ID | Formato | Tamanho | Dec | Descrição | Origem dos Dados | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Alfanumérico | 100 |  | Número do Lançamento Contábil | Identificador do lançamento contábil. | O lançamento contábil pode ser composto por uma ou mais partidas. |
| 2 | Alfanumérico | 100 |  | Número da linha do Lançamento | Identificador da partida contábil. | Concatenar o identificador da partida com 0 se for conta a débito e 1 se for conta a crédito.  Exemplo: Se na partida 123 a conta utilizada for a débito o número da linha no lançamento será 123\_0, porém se a conta for a crédito será 123\_1. |
| 3 | Alfanumérico | 100 |  | Código da Conta Contábil | Código da conta a débito ou a crédito. |  |
| 4 | Alfanumérico | 25 |  | Unidade de Negócios | Código da coligada que deu origem ao lançamento. | Empresa do lançamento. |
| 5 | Decimal |  | 2 | Valor da partida na moeda funcional | Valor informado na partida contábil. |  |
| 6 | Alfanumérico | 25 |  | Código da Moeda Funcional | Moeda corrente existente nos parâmetros do módulo contábil. |  |
| 7 | Decimal |  | 2 | Valor da partida na moeda de apresentação | Segundo valor informado na partida contábil. | Esse campo só será preenchido se o valor da moeda de apresentação for superior a zero. |
| 8 | Alfanumérico | 25 |  | Moeda de Apresentação | Moeda do segundo valor existente nos parâmetros do modulo contábil. | Esse campo só será preenchido se o valor da moeda de apresentação for superior a zero e o sistema estiver parametrizado para trabalhar com segundo valor. |
| 9 | Alfanumérico | 25 |  | Ano Fiscal | Ano da partida contábil. |  |
| 10 | Alfanumérico | 25 |  | Período Fiscal | Mês da partida contábil. |  |
| 11 | Data |  |  | Data efetiva de Lançamento | Data da partida contábil. |  |
| 12 | Data |  |  | Data da última atualização do Lançamento | Data em que ocorreu a inclusão ou a última alteração da partida contábil. |  |
| 13 | Alfanumérico | 25 |  | Usuário da última atualização | Código do usuário que incluiu ou atualizou a partida pela última vez. |  |
| 14 | Alfanumérico | 25 |  | Módulo do Lançamento | Módulo de origem do lançamento. |  |
| 15 | Alfanumérico | 250 |  | Descrição do Lançamento | Descrição do lançamento contábil. |  |
| 16 | Alfanumérico | 250 |  | Descrição da Linha do Lançamento | Descrição da partida contábil. | Campo formado pela concatenação da descrição do histórico padrão  com o complemento existente na partida. |
