---
content_hash: bda30b5b007aab18b042b551896a8d355262f4aef8e842e603ae508518716b7c
fetched_at: '2026-06-29T00:05:52.776417+00:00'
page_id: '1060210314'
product: rm
source: tdn-rm
title: Grupo de Compras Governamentais
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+de+Compras+Governamentais
version: 2
---

# gCompraGov- Grupo de Compras Governamentais

LayoutCampos

| Campo | Grupo Pai | Ocorrência | Ele | Descrição |
| --- | --- | --- | --- | --- |
| **gCompraGov** | **ide** | **0-1** | **Grupo** | O **grupo é gerado** nos seguintes cenários:   * + O campo **Órgão Público** no cadastro de Cliente/Fornecedor estiver diferente de **“Não se aplica”**; |
| tpEnteGov | gCompraGov | 1-1 | Elemento | Tipo de ente governamental:  1=União 2=Estado 3=Distrito Federal 4=Município  Campo Órgão Público configurado na aba **Tributos** do **Cliente/Fornecedor**.   FCFO.ORGAOPUBLICO |
| pRedutor | gCompraGov | 1-1 | Elemento | Percentual de redução de alíquota em compra governamental.  TTRBMOV.PCTREDUTORGOV |
| tpOperGov | gCompraGov | 1-1 | Elemento | Tipo de operação com o ente governamental:  1 – Fornecimento com pagamento posterior; 2 - Recebimento do pagamento com fornecimento já realizado; 3 – Fornecimento com pagamento já realizado; 4 – Recebimento do pagamento com fornecimento posterior;  TMOVFISCAL.TPOPER |
| refDFeAnt | gCompraGov | 0-n | Elemento | Chave de acesso do documento fiscal anterior.  A **tag é gerada** no seguinte cenário:   * + A tag tpOperGov deverá ser 2 ou 3.     - OBS: *a chave de acesso deverá ser de um emitente* *com o mesmo CNPJ base.*   TCHAVEACESSOREF.CHAVEACESSO |

Exemploxml
2
0.1000
3
31230922635197000178551000005214641102230473
31230922635197000178551000005214641102230999
]]>
