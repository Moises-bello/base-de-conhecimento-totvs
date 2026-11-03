---
content_hash: 122630fea82b029f70c9ea88d10501d6d5f66bc1a866619e26efb3cb44d13119
fetched_at: '2026-06-29T00:08:52.563243+00:00'
page_id: '341219514'
product: rm
source: tdn-rm
title: NFE_Rejeição_879_Informado_item_“Produzido_em_Escala_NÃO_Relevante”_e_não_informado_CNPJ_do_Fabricante_[nItem:nnn].
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=341219514
version: 1
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | A partir da 12.1.17 |
| **Ocorrência:** | Rejeição 879 - Informado item “Produzido em Escala NÃO Relevante” e não informado CNPJ do Fabricante [nItem:nnn] |
| **Passo a passo:** | **Causas:**  Essa rejeição é apresentada quando for emitida uma NF-e informando indEscala=”N- não relevante” (id: I05d), e não informado o CNPJ do Fabricante da Mercadoria (id: I05e)  Veja a regra da SEFAZ:      **Verificações para solução:**  Para resolver o problema será necessário informar o CNPJ do Fabricante no cadastro do produto:        Fonte:    NT2016.002 - <http://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=af0MhVeqltw=> |
