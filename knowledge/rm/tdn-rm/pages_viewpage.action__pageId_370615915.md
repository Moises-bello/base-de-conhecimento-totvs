---
content_hash: ca79ddd7b6a91f7c30a52a4b726cb39522e1d185150f0f33922100e7c4faefe6
fetched_at: '2026-06-29T00:09:00.978165+00:00'
page_id: '370615915'
product: rm
source: tdn-rm
title: 2732588 FINANCEIRO01-7408 DT Alteração dados pagamento do Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370615915
version: 1
---

# Ao alterar meio de pagamento do movimento é apresentado erro ao cancelar lançamentos.

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Alterar forma de pagamento Movimento - Cancela Lançamentos |
| **Situação/Requisito:** | Ao realizar a alteração do meio de pagamento do movimento o sistema cancela os lançamentos provenientes do movimento para gerar novas parcelas.  Nesse momento o sistema apresenta uma mensagem relatando que não é último gerador de INSS.  "O Lançamento 'X não pode ser cancelado, pois existem valores de INSS pendentes posteriores a esse lançamento. O Lançamento com INSS pendente é 'Y'."  Porém ambos os lançamentos estão dentro do mesmo movimento. |
| **Solução/Implementação:** | Agora o sistema não considera mais lançamentos dentro da mesma lista do processo de cancelamento. |
| **Tickets relacionados:** | 2732588 |
| **Requisito:** | FIN000073 |
