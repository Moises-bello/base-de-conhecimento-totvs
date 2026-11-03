---
content_hash: 52fdb64db76e35b7fe6be8aff97243a5f097343d9e88cd9301d3a89956838e98
fetched_at: '2026-06-29T00:09:22.070229+00:00'
page_id: '422545959'
product: rm
source: tdn-rm
title: Cancelar Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Cancelar+Faturamento
version: 3
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **XML**: Cancelar Fatura (Cancelar Faturamento)  **Padrão de Nomeclatura dos arquivo CF**: FAT + CANC + Código Coligada + Código Filial + Id. Laf. Agrup + Data + Hora  **Formato**: XML  **Observação**: Para montagem do CF Cancelado serão considerados Lançamentos Fiscais de Saída cancelado | | | | |
| **Campo** | **Descrição** | **Origem dos Dados** | **Obrigatório** | **Observação** |
| ID Fatura Empresa | Informar o número identificador do faturamento da empresa que fará o mapeamento com o registro de fatura | **DLAF.CODCOLIGADA  + DLAF.CODFILIAL + DLAF.IDLAFAGRUP** | Obrigatório |  |
