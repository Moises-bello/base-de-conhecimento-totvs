---
content_hash: dca21720d49e69ab28dd7197e1b3308465e879f412514ea559d019710abb8da9
fetched_at: '2026-06-29T00:10:19.272680+00:00'
page_id: '4813188'
product: rm
source: tdn-rm
title: A Filial de Saída e Local de Saída não são apresentados na inclusão do movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813188
version: 4
---

BLOCK

A Filial de Saída e Local de Saída não são apresentados na inclusão do movimento

FAQ: **A Filial de Saída e Local de Saída não são apresentados na inclusão do movimento**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Sintoma

* **Sintoma**

A Filial de Saída e Local de Saída não são apresentados na inclusão do movimento

Causa

* **Causas**

1- Nos parâmetros do tipo de movimento etapa Emitente/Destinatário, o campo emitente e destinatário esta diferente de “Empresa” e a edição do local de destino esta como “Não Edita”.

2- O Tipo de Movimento esta parametrizado para “Gerar Escrituração” e ao mesmo tem o tributo INSS parametrizado.

Solução

* **Solução**

1- O Tipo de movimento deverá estar parametrizado para que o campo emitente e destinatário seja “Empresa” e a edição do local de destino **diferente** de “Não Edita”.

2- O Tipo de movimento não pode ter a combinação de “Gera Escrituração” e ao mesmo tempo ter o tributo INSS parametrizado. Isto porque quando um tipo de movimento é parametrizado com esta combinação a inclusão da movimentação será pelo campo CEI do Cliente/Fornecedor, não apresentando assim o código da filial e local de destino.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/dica-filial-de-saida-e-local-de-saida.html>
