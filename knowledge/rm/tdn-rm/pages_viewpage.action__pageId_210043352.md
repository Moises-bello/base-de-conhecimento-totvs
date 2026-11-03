---
content_hash: f261c815401f844accec5dfc41689c672432fc92f3250d77189990c3bb046cac
fetched_at: '2026-06-29T00:06:14.304481+00:00'
page_id: '210043352'
product: rm
source: tdn-rm
title: TTMQN3_DT_Bolsa_Retroativa_Não_Alterar_Conta_Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=210043352
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
| **Versões/Release:** | *12.1.8* |
