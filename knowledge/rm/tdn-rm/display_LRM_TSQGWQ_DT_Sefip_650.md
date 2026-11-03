---
content_hash: 6f63366eb0e42505dd1a28770ed5d63e55a55a9cc3c0a510d16c8467141a719e
fetched_at: '2026-06-29T00:06:00.974688+00:00'
page_id: '196813726'
product: rm
source: tdn-rm
title: TSQGWQ_DT_Sefip_650
type: documentation
url: https://tdn.totvs.com/display/LRM/TSQGWQ_DT_Sefip_650
version: 2
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | Funcionário era levado no arquivo do Sefip sem valores de base a serem informados.   Situação ocorria para código de recolhimento 650 (Recolhimento ao FGTS e informações à Previdência Social relativos a dissídio coletivo, reclamatória trabalhista ou conciliação perante as Comissões de Conciliação Prévia) |
| **Solução/Implementação:** | Otimizada geração do Sefip, com verificação para que funcionários sem valores de base a serem informados não sejam levados para o arquivo quando o código de recolhimento for 650 (Recolhimento ao FGTS e informações à Previdência Social relativos a dissídio coletivo, reclamatória trabalhista ou conciliação perante as Comissões de Conciliação Prévia) |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSQGWQ* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.40* |
