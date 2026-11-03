---
content_hash: cf89c55403723a52dacdcc07d9364a6f8bb863c135cca8a759ce6f267e250cfe
fetched_at: '2026-06-29T00:10:56.840361+00:00'
page_id: '593244359'
product: rm
source: tdn-rm
title: Lançamento Fiscal 1/7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=593244359
version: 6
---

Permite Nota Fiscal repetidaPermite Nota Fiscal repetida

Identificação de Regras de Apuração | ICMS | Lançamento Fiscal 1/7

De forma geral o Módulo Fiscal considera que um Lançamento Fiscal esta repetido verificando os campos chave do Lançamento:

* Tipo do Lançamento (Entrada/Saída)
* Código da Filial
* Série do Documento
* Tipo de Documento
* Doc. Inicial
* Cliente Fornecedor ou Filial (Destinatário / Remetente / Emitente)

O parâmetro **Permite Nota Fiscal repetida**altera a consistência do Lançamento para possibilitar a inclusão de Lançamento Fiscais com os campos chave repetidos.

Data do Lançamento

Mesmo com o parâmetro **Permite Nota Fiscal repetida**habilitado, o Fiscal não permitirá inclusão de Lançamentos repetidos com data iguais.
