---
content_hash: 1b6482d2fca8b38ff7d6ac0c70afb283f22dee76805d289efb9e22742fdf11f9
fetched_at: '2026-06-29T00:09:10.605095+00:00'
page_id: '402064071'
product: rm
source: tdn-rm
title: 3575446 FISCAL01-6390 DT NF-e - Devolução de Cupom Fiscal Eletrônico SAT -
  Modelo 59
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=402064071
version: 2
---

# NF-e - Devolução de Cupom Fiscal Eletrônico SAT - Modelo 59

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Emissão de NF-e |
| **Situação/Requisito:** | O cliente necessita realizar a emissão de uma nota fiscal com finalidade de devolução, de uma venda realizada através de um cupom fiscal que possui integração com o Protheus. De acordo com a NT 2015.002 a TAG BA02 refNFe deverá aceitar a referência do modelo 59 Cupom Fiscal e-SAT:  "Aceitar a Chave de Acesso referenciada do documento fiscal “SAT-CF-e”, modelo 59 (RV: BA02-20) ". |
| **Solução/Implementação:** | Foi alterado o processo de montagem do XML da NF-e para gerar a tag refNFe quando se tratar do modelo "59" Cupom Fiscal e-SAT.  A tag será gerada com a chave de acesso preenchida na pasta integrações do movimento referenciado |
