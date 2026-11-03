---
content_hash: 1e680e0ccb6fcad16beb41f03a7db24a3d80cb7fb4fa610a7e201904e57cf692
fetched_at: '2026-06-29T00:06:14.300762+00:00'
page_id: '210043346'
product: rm
source: tdn-rm
title: TTLKMT_DT_Bolsa_Retroativa_Não_Alterar_Conta_Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210043346
version: 1
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão**Educacional* |
| **Função:** | *Bolsa Retroativa* |
| **Situação/Requisito:** | *Nos processos de inclusão/exclusão de bolsa retroativa,  o sistema sempre gravava os valores default da conta caixa, parametrizados nos parâmetros Educacionais de Integração Financeira. Quando um lançamento tinha sua conta caixa alterada manualmente para outra diferente deste default, esta alteração estava sendo sobreposta com os valores default da parametrização.* |
| **Solução/Implementação:** | *Alterado processo de inclusão/exclusão de bolsa retroativa para não mudar a conta caixa e nem o convênio do lançamento para os valores default, quando estas informações forem alteradas após a geração do lançamento.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.41* |
