---
content_hash: 232c111727710d540a9b90e0a5d4c49afd1e4f6f2dedd8c8285915167a906043
fetched_at: '2026-06-29T00:09:19.587952+00:00'
page_id: '422545618'
product: rm
source: tdn-rm
title: Informações Complementares NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545618
version: 4
---

**Cadastros** Será necessário cadastrar o [contrato no](http://tdn.totvs.com.br/display/LRM/Contrato)[TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=198948835)[.](http://fwrm-wiki:20658/WikiHelp/EST/EST.ManutencaoContratos)

**Deveram ser criados:**  
 Campo complementar com o nome XPED (Tipo Inteiro) no item do movimento  
 Campo complementar com o nome XNEMP (Tipo Inteiro) no movimento

No tipo de movimento será necessário parametrizar a integração com contrato - Etapa Contratos  
***Observação:***Os Campos Complementares criados deverão ser colocados [visíveis no movimento](http://tdn.totvs.com.br/pages/viewpage.action?pageId=423938849).

Na criação do movimento será necessário o preenchimento do contrato no item.

O número do pedido deverá ser preenchido no campo complementar XPED.  
 O número da nota de empenho deverá ser preenchido campo complementar XNEMP

Na geração do XML da NF-e serão geradas as TAGS no Grupo Compras  
**TAG <<XCONT>> -** Número do contrato vinculado ao movimento  
 **TAG** **<<XNEMP>>** - Informação do campo complementar  
 **TAG** **<<XPED>>** -   Informação do campo complementar

Lembrando que estes campos seguirão as regras de tamanho e quantidade definidos no manual do contribuinte.
