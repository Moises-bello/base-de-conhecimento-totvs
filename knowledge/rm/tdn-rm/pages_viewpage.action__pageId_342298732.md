---
content_hash: 702671a085faf8c836e96128f28987a1716d5e4ec2933705253b3afe3953970d
fetched_at: '2026-06-29T00:08:52.666957+00:00'
page_id: '342298732'
product: rm
source: tdn-rm
title: 'FISCAL01-2715 DT NF-e - Layout Sefaz - Rejeição: Total do Valor Aproximado
  dos Tributos difere do somatório dos itens.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=342298732
version: 1
---

# NFC-e 4.00

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio NF-e no Layout SEFAZ 3.10 e 4.0 |
| **Situação/Requisito:** | Após realizar a conversão da base de dados para 12.1.18, podemos verificar que a tag <vTotTrib> do totalizador do ICMS não está realizando a soma dos valores das tags <vTotTrib> dos itens, gerando a seguinte rejeição:  "**Rejeicao: Total do Valor Aproximado dos Tributos difere do somatório dos itens**". |
| **Solução/Implementação:** | Implementado o preenchimento da tag vTotTrib da tag de totalizadores da NF-e também para serviços. |
