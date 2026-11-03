---
content_hash: b9762b0a42bef309a76fe095569f509085fc1671cd21b37fca35fd69e97c3520
fetched_at: '2026-06-29T00:05:53.194560+00:00'
page_id: '1068188772'
product: rm
source: tdn-rm
title: NFTS - WebService - Tipo de Documento
type: documentation
url: https://tdn.totvs.com/display/LRM/NFTS+-+WebService+-+Tipo+de+Documento
version: 2
---

CardsleftParâmetro

**Configuração de tipo de documento.**

Para o preenchimento da tag "tipodocumento" é necessário preencher o "Modelo ISS" associado ao Tipo de Documento (Espécie) nos parâmetros do TOTVS Gestão Fiscal (Processo 03.02.03 – Apur. ISS por Filial, Etapa 1 – Modelo ISS).

Comportamento na geração da tag "tipodocumento"

**Visualização do tipo documento na NFTS**

O sistema irá considerar preferencialmente o valor informado no campo "Modelo ISS", para o preenchimento da tag "tipodocumento".  
Se não existir registro no parâmetro de modelo ISS ou caso o campo esteja vazio, o sistema irá considerar o comportamento anterior.

**Comportamento anterior.**  
Caso o município do prestador seja diferente do tomador, a tag "tipodocumento" será preenchida valor fixo: 01 – *Documento fiscal emitido por outro município*, caso contrário a tag não é gerada no XML.
