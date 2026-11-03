---
content_hash: 9f69e701e8416e28a7d9f46f67c682c7fc4f1fb7aa0a33dc45544e5c14b2b9bf
fetched_at: '2026-06-29T00:09:01.708080+00:00'
page_id: '376668300'
product: rm
source: tdn-rm
title: 3223991 DT Erro ao gerar lançamento em lote com bolsa 100%
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=376668300
version: 2
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Geração de Lançamento em Lote |
| **Situação/Requisito:** | Ao gerar lançamento em lote no cenário que ocorre algum erro ao baixar o lançamento com 100% de bolsa, o demais lançamentos não estavam sendo gerados e o sistema estava apresentando uma mensagem de não conformidade “Sintaxe incorreta”. |
| **Solução/Implementação:** | Implementado ajuste no processo de geração em lote para que os lançamentos que não estão com não conformidade sejam gerados com sucesso e seja apresentado no LOG somente os lançamentos que não estejam atendendo a regra de negócio. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |
| **Documento de Referência:** |  |
| **Pacote:** | Informe o [linkdopacote] |
