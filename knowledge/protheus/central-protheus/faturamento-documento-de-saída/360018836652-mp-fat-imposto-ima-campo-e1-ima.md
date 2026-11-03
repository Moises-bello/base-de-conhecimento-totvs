---
article_id: 360018836652
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 3aa6eb582ee64a8cd7c873bfe4b5a8014e382d5f63b792c71b4fae7442168408
fetched_at: '2026-06-28T22:38:45.182773+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP - FAT - IMPOSTO IMA CAMPO E1_IMA
type: support-article
updated_at: '2021-04-28T15:13:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018836652-MP-FAT-IMPOSTO-IMA-CAMPO-E1-IMA
---

**Dúvida**

IMPOSTO IMA CAMPO E1\_IMA.

**Ambiente**

Microsiga Protheus - Versão 12.

**Causa**

Ao realizar uma nota de saída para um cliente Pessoa Jurídica, o sistema está calculando o imposto **IMA** mas não está gerando título no contas a receber para que possa ser realizado o abatimento sobre o título principal no momento da baixa. E também ao excluir documento de saída que apresenta error.log informando falta do campo **E1\_IMA**.

**Errorlog**:  *invalid field name in Alias MACANDELNF->E1\_IMA on FACANDELCR(FINXAPI.PRX)*

Ambas as situações ocorrem por falta do campo **E1\_IMA**

**Solução**

Foi realizado o ajuste da rotina do **Documento Fiscal de Saída**para atualizar o conteúdo do campo **E1\_IMA**do título financeiro, que é referente ao **ICMS-MT - Cálculo do IMA-MT** - Instituto Mato-grossense do Algodão.

Para solução é necessário que exista o campo **E1\_IMA** para isso atualizar o **sdfbra** a partir de 26/10/2018 conforme documento abaixo.

**Saiba mais:**

**[DSERFAT-8309 DT Documento Fiscal de Saída - Gravação do Imposto IMA (E1\_IMA)](http://tdn.totvs.com/pages/releaseview.action?pageId=425457570)**

**[96724 DSERFINR-3105 DT Abatimento de imposto IMA/MT](96724%20DSERFINR-3105%20DT%20Abatimento%20de%20imposto%20IMA/MT)**
