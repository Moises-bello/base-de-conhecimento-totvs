---
content_hash: 0f0b9a8ad743aa5bc455c3d09bf56674f71d5874a8a118620347bf9a43667ab6
fetched_at: '2026-06-29T00:09:55.004445+00:00'
page_id: '445673604'
product: rm
source: tdn-rm
title: 4475047 FISCAL01-7297 DT - NF-e - CEP do emitente sendo gerado errado no Danfe
type: documentation
url: https://tdn.totvs.com/display/LRM/4475047+FISCAL01-7297+DT+-+NF-e+-+CEP+do+emitente+sendo+gerado+errado+no+Danfe
version: 1
---

# NF-e - CEP do emitente sendo gerado errado no Danfe

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Impressão de DANFE |
| **Situação/Requisito:** | Ao imprimir a DANFE, caso o CEP da Filial inicie com 0 (zero) este caracter não é apresentado e o CEP não é formatado. |
| **Solução/Implementação:** | Alterado o provider para formatar corretamente o conteúdo do CEP. |
