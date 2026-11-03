---
article_id: 16282199530775
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: f09312c7ea74237509e995cd234753c4c496d2aeea6035b9950d540363f902f1
fetched_at: '2026-06-28T22:39:58.511795+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Schema Inválido.
  Element ''{http://www.abrasf.org.br/nfse.xsd}ItemListaServico'': [facet ''enumeration'']
  The value ''XXXX'' is not an element of the set'
type: support-article
updated_at: '2024-03-22T18:46:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16282199530775-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Schema-Inv%C3%A1lido-Element-http-www-abrasf-org-br-nfse-xsd-ItemListaServico-facet-enumeration-The-value-XXXX-is-not-an-element-of-the-set
---

**Ocorrência**Ao realizar a transmissão de um RPS, apresenta: "Schema Inválido. The value 'XXXX' is not an element of the set".  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - À partir da versão 12.1.33.  
  
**Causa**Esse incidente ocorre pelo fato de estar sendo utilizado o Código de Serviço em um formato incorreto e/ou o conteúdo não ser permitido pela prefeitura.  
  
**Solução**Para correção deverá ser utilizado uma das opções disponíveis mostrada na própria falha de schema ao clicar em 'Schema->OK'.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16282181481367)  
  
**Exemplo**: Foi utilizado 1405, porém a prefeitura trabalha com formato de cinco dígitos (XX.XX), ou seja, deverá ser utilizado 14.05 (com ponto).  
  
**IMPORTANTE**!  
Lembrando que o Código de Serviço pode variar o local de onde será extraído:  
- [Clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061751034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Possibilidades-de-montagem-de-C%C3%B3digo-de-Servi%C3%A7o-C%C3%B3digo-de-Tributa%C3%A7%C3%A3o-e-CNAE-NFSEXMLENV?source=search)  
  
Após isso refazer o documento de saída da nota.
