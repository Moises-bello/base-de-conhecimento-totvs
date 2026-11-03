---
content_hash: ac3f5f781edf7efab3c6bc3be871e2f08ece45e854ff47aaa1e4173534f2d4d2
fetched_at: '2026-06-29T00:06:02.174433+00:00'
page_id: '198944105'
product: rm
source: tdn-rm
title: TSYBB1_DT_Faturamento_Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYBB1_DT_Faturamento_Movimento
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
| **Versões/Release:** | *12.1.7* |
