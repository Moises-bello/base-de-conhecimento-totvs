---
content_hash: b88aabe055215ce1235324a0a1fef0ad86a58f094fd2083edd1bb9661a7486f0
fetched_at: '2026-06-29T00:08:58.436169+00:00'
page_id: '359477277'
product: rm
source: tdn-rm
title: 2795840 DEDUINTEGRACOES-2394 DT Boleto Bancario - Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/2795840+DEDUINTEGRACOES-2394+DT+Boleto+Bancario+-+Contrato
version: 1
---

# BOLETO BANCÁRIO - CONTRATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Impressão de boletos - Contrato* |
| **Situação/Requisito:** | A geração de relatório realiza uma validação para verificar se a fonte de dados utilizada possua, como tabela master, a tabela FBOLETO. Nessa validação estava sendo realizada considerando a coligada do contexto. Quando o relatório era configurado para ser utilizado de forma global ele não era encontrado, ocasionando erro de referência de objeto. |
| **Solução/Implementação:** | Ajustes para que essa validação leve em consideração a coligada do relatório selecionado, evitando que ele não seja encontrado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
