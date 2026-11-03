---
content_hash: 1e52b526e091ad943ef11158855c86fbf67a59060d77c55d9667ffec9d58d1f9
fetched_at: '2026-06-29T00:09:01.078260+00:00'
page_id: '372541574'
product: rm
source: tdn-rm
title: 1253195 FINANCEIRO01-2053 DT Alteração valores lançamento com cheque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372541574
version: 1
---

# Mensagem que bloqueia alteração de valores em lançamentos com cheque

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Alteração de Lançamentos |
| **Situação/Requisito:** | Ao realizar a alteração de lançamentos o sistema apresenta mensagem de erro relatando que não é possível alterar valores de lançamentos com cheque parcial. |
| **Solução/Implementação:** | Ajuste para que o sistema faça o bloqueio apenas em alterações globais de lançamentos com cheque no campo Conta/Caixa.  Efeito colateral: TVBSCM |
| **Requisito:** | FIN000144 |
