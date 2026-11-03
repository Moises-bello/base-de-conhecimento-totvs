---
content_hash: e107d80cf4d2d29a4664f05c9e295c5ba337c1b89956e1bdd8eb0b8f65428846
fetched_at: '2026-06-29T00:11:33.399051+00:00'
page_id: '759925190'
product: rm
source: tdn-rm
title: Tags XML Hermes Pardini
type: documentation
url: https://tdn.totvs.com/display/LRM/Tags+XML+Hermes+Pardini
version: 2
---

## **EXPLICAÇÃO E FUNCIONAMENTO**

O XML do resultado do exame recebido na integração com o Hermes Pardini contém diversas tags, cada qual com sua funcionalidade.

Abaixo contém o arquivo XSD com todas as tags e suas respectivas explicações. Espera-se que todas (ou quase todas, de acordo com a demanda do cliente), sejam cobertas pelo sistema:

250

## **INFORMAÇÕES ADICIONAIS**

Recentemente (05/2023) foi feita uma nova análise técnica para cobrir algumas tags que estavam faltando. Foram elas:

### Dentro de <Exame>, tabela SZHPRESULTADOEXAME

* Inclusão do campo CONDAMOSTRA nvarchar(255)
* Inclusão do campo COMENTPATOLOGISTA text
* Inclusão do campo ESTIMULO nvarchar(255)
* Inclusão do campo INTERPRETAÇÃO text

### Dentro de <InfAdicional> → SZHPDINFOADICIONAL

* Inclusão do campo UNIDADE nvarchar(255)

### Dentro de <ItemDeExame> → SZHPDITEMEXAME

* Inclusão do campo INTERPRETACAO text
* Inclusão do campo NOTA text
* Inclusão do campo COMENTPATOLOGISTA text
* Inclusão do campo CONDAMOSTRA nvarchar(255)
* Inclusão do campo ESTIMULO nvarchar(255)

### Dentro de <Resultado> → SZHPDRESULTADOITEMEXAME

* Inclusão do campo UNIDADEMEDIDA nvarchar(255)
