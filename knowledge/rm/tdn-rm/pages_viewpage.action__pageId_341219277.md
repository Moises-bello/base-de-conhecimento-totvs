---
content_hash: d26061847a6b26615a41cde72d82c29bf3fb57add1faee575b9be0e97bb7e451
fetched_at: '2026-06-29T00:08:52.560202+00:00'
page_id: '341219277'
product: rm
source: tdn-rm
title: NFE_Rejeição_865_Total_dos_pagamentos_menor_que_o_total_da_nota.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341219277
version: 2
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.17 |
| **Ocorrência:** | Rejeição 865: Total dos pagamentos menor que o total da nota. |
| **Passo a passo:** | **Causas:**  Conforme reportado na Nota Técnica 2016/002 esta rejeição ocorre quando o somatório do valor dos pagamentos (id:YA03, tag:vPag) é menor que o total da nota (id:W16, tag: vNF)  **Exceção 1:** Esta regra não se aplica para nota fiscal de Ajuste, campo finNFe=3 (id:B25) e para nota fiscal de Devolução finNFe=4 (id:B25).      Veja a regra da SEFAZ:      **Verificações para solução:**  Deve-se igualar o valor do pagamento com o valor do movimento.  Manual de Orientação ao Contribuinte - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=af0MhVeqltw=> |
