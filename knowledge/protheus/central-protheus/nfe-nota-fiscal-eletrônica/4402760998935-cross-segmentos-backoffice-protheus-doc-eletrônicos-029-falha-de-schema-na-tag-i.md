---
article_id: 4402760998935
category: NFe - Nota Fiscal Eletrônica
content_hash: 12cb185fd80a2624658685a1178a915db8100c5f90b376f18717f50176f623c3
fetched_at: '2026-06-28T22:40:00.386938+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  schema na Tag indpres'
type: support-article
updated_at: '2023-10-27T19:04:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402760998935--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-indpres
---

**Dúvida**Como solucionar a falha de Schema referente a TAG indPres ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - Ao gerar falha de Schema **referente ao indPres** verifique se o seu XML gerou conforme o **exemplo abaixo:**

![indpres_1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402760918935/indpres_1.JPG)

2- O conteúdo dessa TAG é obrigatório ***indPres*** A TAGpode ter os conteúdos abaixo:

**0=**Não se aplica (por exemplo, Nota Fiscal complementar ou de ajuste);   
**1=**Operação presencial;   
**2=**Operação não presencial, pela Internet;   
**3=**Operação não presencial, Teleatendimento;   
**4=**NFC-e em operação com entrega a domicílio;   
**5=**Operação presencial, fora do estabelecimento;   
**9=**Operação não presencial, outros. 

1- No pedido de vendas preencher o campo **Presença Com "C5\_INDPRES " :**

**![venda_presencial_fora.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103876013/venda_presencial_fora.gif)**

2- No documento de entrada deve ser preenchido o campo **Indicador de Presença "F1\_INDPRES" :**

3- Após isso, **exclua a nota e gere novamente.**

* **Importante:**

Se o campo não for preenchido, caso seja nota do tipo normal, **conforme o fonte do NFESEFAZ** abaixo, será levado como **9- Operação Presencial.**

Caso seja **nota de devolução, conforme o fonte do NFESEFAZ abaixo:**

![indpres_fonte.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4402754697623/indpres_fonte.JPG)

1- Para nota de devolução  preencher o campo do TES **"Venda Pres."** **F4\_VENPRES=1** na montagem da tag **indPres=1 – Operação Presencial**.

![venda_presencial_TES.gif](https://totvssuporte.zendesk.com/hc/article_attachments/1500002491502/venda_presencial_TES.gif)

2- Após isso, **exclua a nota e gere novamente.**

* **Saiba mais:**

Caso gere  a **rejeição 434,** há documentação do link abaixo:

[Cross Segmentos - Backoffice Protheus - 434 Rejeição: NF-e sem indicativo do intermediador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062802333)
