---
content_hash: 83c9b838fdef16f4ace73f1889c28b6390cfb4d5db84cda1a72dd06851691ab7
fetched_at: '2026-06-29T00:06:12.106360+00:00'
page_id: '204968706'
product: rm
source: tdn-rm
title: TTJL87_DT_Parametrizador
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJL87_DT_Parametrizador
version: 3
---

# PARAMETRIZADOR - FOLHA DE PAGAMENTO - RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *TOTVS Folha de Pagamento* |
| **Função:** | *Parametrizador - Folha de Pagamento - Rescisão* |
| **Situação/Requisito:** | Ao acessar o parametrizador do Labore e clicar no "nome" da fórmula vinculado ao campo de "Fórmula para evento de saldo salário", é apresentado mensagem de advertência. |
| **Solução/Implementação:** | Alterado a propriedade KeyFields do lookup cFORMULASALDOSALARIOLookup passando o CodSistema. E alterado a propriedade LookupKeyFields passado o APLICACAO. |
| **Chamados relacionados:** | TTJL87 |
| **Versões/Release:** | *11.82.40* |
