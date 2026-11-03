---
article_id: 360020130711
category: NFe - Nota Fiscal Eletrônica
content_hash: 6967ac50a08586d6307885390c43d3f5944198ec970a2a65d6798daca39cb96c
fetched_at: '2026-06-28T22:40:03.917504+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 340 Rejeição :
  Não informado o grupo de exportação indireta no item'
type: support-article
updated_at: '2025-06-17T19:17:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020130711-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-340-Rejei%C3%A7%C3%A3o-N%C3%A3o-informado-o-grupo-de-exporta%C3%A7%C3%A3o-indireta-no-item
---

**Dúvida**Como corrigir a 340 Rejeição : Não informado o grupo de exportação indireta no item  ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**  
  
Se gerado a nota com os ***CFOPS 3503 ou 7501*** deve ser informado o grupo de ***TAGS de exportação indireta*** no XML ***TAGS :detExport/exportInd***

 1- Verifique se o CFOP da nota está correto, caso **não seja 3503 ou 7501** altere pela TES da nota no campo **Cod. Fiscal "F4\_CF"**

![CFOP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11547795085975)

2 - Se o CFOP estiver correto na nota de **exportação indireta**  Acesse a rotina **Livros Fiscais** -> **Atualizações** -> **Movimentos** -> **NF manual de Saída** -> **Outras ações** ->**Complementos** -> **Exportação**

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32879197768215)

3- Preencher nos complementos de exportação, **Número do Registro de Exportação CDL\_NRREG , Chave de Acesso da NF-e recebida para exportação CDL\_CHVEXP, Quantidade do item realmente exportado CDL\_QTDEXP,**  os três campos são obrigatórios

Para notas de devolução, conforme ***o NFESEFAZ abaixo, buscará da nota de origem e do campo do documento de entrada a quantidade.***

**<detExport>**

***nRE -*** CDL\_NRREG

***chNFe -*** F2\_CHVNFE

***qExport -*** D1\_QUANT

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14202517796887)

* Parecer da ***Consultoria de Segmentos,*** abaixo:

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=761526948)

* **Validação da Sefaz:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015842072)
