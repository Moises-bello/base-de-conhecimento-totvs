---
content_hash: f8163eec5b53a8c876674b16b5a7d011d424afd9591f033de74b169b0ac39e5b
fetched_at: '2026-06-29T00:06:12.143952+00:00'
page_id: '204968817'
product: rm
source: tdn-rm
title: TTJYGH_DT_Parametrizador
type: documentation
url: https://tdn.totvs.com/display/LRM/TTJYGH_DT_Parametrizador
version: 3
---

# PARAMETRIZADOR - FOLHA DE PAGAMENTO - RESCISÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Parametrizador - Folha de Pagamento - Rescisão* |
| **Situação/Requisito:** | Ao acessar o parametrizador do Labore e clicar no "nome" da fórmula vinculado ao campo de "Fórmula para evento de saldo salário", é apresentado mensagem de advertência. |
| **Solução/Implementação:** | Alterado a propriedade KeyFields do lookup cFORMULASALDOSALARIOLookup passando o CodSistema. E alterado a propriedade LookupKeyFields passado o APLICACAO. |
| **Chamados relacionados:** | TTJYGH |
| **Versões/Release:** | *12.1.8* |
