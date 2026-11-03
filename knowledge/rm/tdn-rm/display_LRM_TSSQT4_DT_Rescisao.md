---
content_hash: 7eb6f838f4ee0d941067ffb5fcf083c612501522c70211045b29937dbca5e8f0
fetched_at: '2026-06-29T00:06:06.491948+00:00'
page_id: '201731450'
product: rm
source: tdn-rm
title: TSSQT4_DT_Rescisao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSSQT4_DT_Rescisao
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
| **Chamados relacionados:** | TSSQT4 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
