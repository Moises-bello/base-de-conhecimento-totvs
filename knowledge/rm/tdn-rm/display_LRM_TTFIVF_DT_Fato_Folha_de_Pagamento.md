---
content_hash: 03ba5248f4fcd74f5402bc898afd63d1daf7756cf694a175e4264e9fd1dcc85b
fetched_at: '2026-06-29T00:06:08.060299+00:00'
page_id: '201743498'
product: rm
source: tdn-rm
title: TTFIVF_DT_Fato_Folha_de_Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTFIVF_DT_Fato_Folha_de_Pagamento
version: 2
---

# CONCEITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Framework |
| **Módulo:** | *Integração* |
| **Função:** | *Conceito - Fato Folha de Pagamento* |
| **Situação/Requisito:** | *A consulta do dataserver RHFolhaPagamentoData gerava timeout em bancos com muitos registros em PFUNC, devido à quantidade de JOINs* |
| **Solução/Implementação:** | *Foi alterada a função para gerar a consulta por coligada e por funcionário, para evitar o problema de timeout.* |
| **Chamados relacionados:** | TTFIVF |
| **Versões/Release:** | *12.1.8* |
