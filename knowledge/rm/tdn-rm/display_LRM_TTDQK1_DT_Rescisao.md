---
content_hash: 441e4bd3f7aaf765239727b355cfbc9c36935a3761bb1bd6027aadc76b037359
fetched_at: '2026-06-29T00:06:06.761657+00:00'
page_id: '201731734'
product: rm
source: tdn-rm
title: TTDQK1_DT_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDQK1_DT_Rescisao
version: 1
---

# Rescisão

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *Construção e projetos.* |
| **Módulo:** | *Folha de pagamento.* |
| **Função:** | *Rescisão.* |
| **Situação/Requisito:** | Ao salvar uma rescisão pela tela "Aviso Prévio" não preenchendo o campo "Motivo da Mudança" a seguinte mensagem é apresentada:      "ORA-01400: cannot insert NULL into ("RM"."PFHSTSIT"."MOTIVO")"  *.* |
| **Solução/Implementação:** | Otimizada tela de rescisão, acerto na validação do motivo da mudança no histórico de situação  *.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTDQK1 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
