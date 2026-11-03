---
content_hash: 3c09c8868f93bdd89d59db0ac5429dfa6f20d63f7f8556cdd7d7150314e6c69d
fetched_at: '2026-06-29T00:08:49.599659+00:00'
page_id: '331847440'
product: rm
source: tdn-rm
title: 99476 FINANCEIRO01-1360 DT Baixa com cheque emitido
type: documentation
url: https://tdn.totvs.com/display/LRM/99476+FINANCEIRO01-1360+DT+Baixa+com+cheque+emitido
version: 2
---

# Baixa com cheque emitido

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Baixa com cheque emitido. |
| **Situação/Requisito:** | Ao selecionar para baixa um lançamento (sem retenção) que está agrupado com outro registro (com retenção de tributo) através de um cheque, sistema apresenta a mensagem abaixo no fim da execução da baixa:  Dados adicionais de tributo não encontrado: IdLan: [ XXXXXX ], CodTrb: [RET.CS] |
| **Solução/Implementação:** | Ajustado processo de baixa de cheque emitidos, para poder baixar os cheques que agrupam lançamento com tributos e sem tributos, ao selecionar o lançamento sem tributo para poder executar o processo. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | FINTRF000196 |
| **Documento de Referência:** | N/A. |
