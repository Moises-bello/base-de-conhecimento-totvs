---
content_hash: ea59449cd94f21b10658fa4136eb46a9de9381b0a5200490230fd94641428c56
fetched_at: '2026-06-29T00:09:58.051848+00:00'
page_id: '450158956'
product: rm
source: tdn-rm
title: 4550014 FISCAL01-7450 DT NF-e Brasília - Duplicação do grupo de ISS.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450158956
version: 6
---

# ISS (Retido Fonte - Retido Fonte Deduzido - Devido)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | ISS (Retido Fonte - Retido Fonte Deduzido - Devido) |
| **Situação/Requisito:** | O cliente possui uma particularidade legal no qual o mesmo precisa realizar a redução da alíquota em 1% no ISS Retido Fonte para a emissão das notas fiscais para Brasília/DF. Segue o entendimento legal da Consultoria Tributária:  Ao enviar uma nota fiscal com um tributo ISS Devido e um Retido no item de movimento o sistema está duplicando o grupo do ISS. |
| **Solução/Implementação:** | Alterado a geração da tag vISS:  Quando existirem dois Tributos ISS (cada um com um tipo de recolhimento: (Retido Fonte ou Retido Fonte Deduzido) e Devido). A tag vISS será preenchida com o valor do ISS Devido e a tag vISSRet será preenchida com o ISS Retido.  Quando existir apenas o retido,será preenchido o valor nas duas tags (vISS e vISSRet).  Quando houver apenas o devido deve será preenchido apenas a tag vISS. |
