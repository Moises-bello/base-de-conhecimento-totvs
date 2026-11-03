---
content_hash: fc7fd17f373fc0a22c1c3837368d0f4895cb47e5c26e254fb3464a51e670ce85
fetched_at: '2026-06-29T00:06:05.563680+00:00'
page_id: '201724594'
product: rm
source: tdn-rm
title: TTBV10_DT_Historico_Funcao_Transferencia_Entre_Colidadas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBV10_DT_Historico_Funcao_Transferencia_Entre_Colidadas
version: 2
---

# RESCISÃO POR TRANSFERÊNCIA TIPO 5

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão por Transferência* |
| **Situação/Requisito:** | *Quando ocorre rescisão por transferência para outra Coligada, e não é marcada a opção de transferir históricos, não está sendo criado o novo registro no histórico de função.*  *Nos outros históricos cria corretamente.* |
| **Solução/Implementação:** | *Existe uma consistência de só criar um novo registro no histórico de funções se houve mudança de função. Se o código se manteve o mesmo, o novo registro não é criado.*  *É necessário tratar nesta consistência para deixar de criar o novo registro, somente se os históricos anteriores forem copiados.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTBV10* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
