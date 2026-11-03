---
article_id: 360058737893
category: NFe - Nota Fiscal Eletrônica
content_hash: c244d00ca6c889e51fd0ae48436cba1425cda23586f0138c24fc424c2a580661
fetched_at: '2026-06-28T22:40:01.950159+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição: 402
  XML da área de dados com codificação diferente de UTF-8 ( Caracteres Especiais SEFAZ  MT
  )'
type: support-article
updated_at: '2021-10-11T15:32:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058737893--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-402-XML-da-%C3%A1rea-de-dados-com-codifica%C3%A7%C3%A3o-diferente-de-UTF-8-Caracteres-Especiais-SEFAZ-MT
---

**Dúvida**Como corrigir a rejeição: 402 XML da área de dados com codificação diferente de UTF-8 ( Caracteres Especiais SEFAZ MT )  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A SEFAZ de Mato Grosso (MT) não permite a transmissão com caracteres especiais, sendo que é retornado a *"Rejeição 402: XML da área de dados com codificação diferente de UTF-8".*

Realizado teste para duas SEFAZ com estados diferentes.

Identificará que o conteúdo **§** foi convertido para **Â§**para o mesmo teste.  
Obs.: Em agosto/2017 realizamos um ajuste ao transmitir a NF-e quando houver caractere especial, era substituído por "." (ponto). Com isso, hoje o texto que o Cliente inserir será enviado para a SEFAZ, e a própria SEFAZ que validará se aceita ou não o caractere.

* Ao lado esquerdo (*rcv\_999000031\_caracEsp\_MT\_rejeitada.xml*) - Consta o xml enviado para **SEFAZ - MT**, que tivemos o retorno ***"Rejeição 402: XML da área de dados com codificação diferente de UTF-8".***
* Ao lado direito (*rcv\_999000031\_caracEsp\_MG\_autorizada.xml) -*Consta o xml enviado para **SEFAZ - MG**, que tivemos o retorno ***"Autorizado o uso da NF-e".***

* ***IMPORTANTE:***

Como podem identificar que a **SEFAZ - MT** obtêm uma particularidade com caracteres especiais. Neste caso, orientamos ao clientes que retirem os caracteres especiais de seus cadastros para que a rejeição não ocorra.

Abaixo, temos um print do **Manual de Orientação Contribuinte da NF-e,** aonde condiz o tratamento dos **caracteres especiais:**

![caracteres_especiais.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011902601/caracteres_especiais.JPG)
