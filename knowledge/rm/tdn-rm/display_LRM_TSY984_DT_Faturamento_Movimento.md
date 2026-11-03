---
content_hash: 6b4bb1891030a2aea65fbb8c2a9cbfe2627ac6157c970456c014f97c68ff80f2
fetched_at: '2026-06-29T00:06:02.136833+00:00'
page_id: '198943899'
product: rm
source: tdn-rm
title: TSY984_DT_Faturamento_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSY984_DT_Faturamento_Movimento
version: 1
---

# Faturamento de Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Faturamento de Movimento* |
| **Situação/Requisito:** | Durante o processo de faturamento, após salvar o movimento gerado, o sistema demora alguns segundos para fechar a tela de conclusão do processo. |
| **Solução/Implementação:** | Foram realizadas melhorias de performance no processo responsável pelo faturamento manual de movimento. Após salvar o registro, a tela do assistente de faturamento demorava alguns segundos para fechar, identificamos uma solicitação de processamento ao servidor de Jobs desnecessária, ao remover tal solicitação tivemos um ganho em performance. |
| **Conversores e Parâmetros:** | *Não se Aplica.* |
| **Chamados relacionados:** | *Não se Aplica.* |
| **Requisito (ISSUE):** | *Não se Aplica.* |
| **Versões/Release:** | *11.82.40* |
