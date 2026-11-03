---
article_id: 360034058473
category: NFe - Nota Fiscal Eletrônica
content_hash: 7c29acc81dab858c26bfeabc21d10d2ffec5e3839c30bfda87fa633c92c92c02
fetched_at: '2026-06-28T22:40:00.466281+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 228 Rejeição -
  Data de Emissão muito atrasada '
type: support-article
updated_at: '2021-08-25T14:12:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034058473--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-228-Rejei%C3%A7%C3%A3o-Data-de-Emiss%C3%A3o-muito-atrasada
---

**Dúvida**228 Rejeição -  Data de emissão muito atrasada  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Quando for emitida uma NF-e com data de emissão **com atraso maior que 30 dias (ou limite de dias, a critério da Sefaz)**, contando a partir da data atual, será retornado a rejeição "228 - Data de Emissão muito atrasada".

**Regra de Validação:**

NF-e com Tipo de Emissão = 1-Normal **(ou 6-SVC-AN, 7-SVC-RS)** (NT2012.003): – Data de Emissão ocorrida há mais de 30 dias **(ou outro limite definido pela SEFAZ)**   
  
**Observação:**

A critério da SEFAZ, podem ser aceitas as NF-e com Data de Emissão muito atrasadas, desde que tenham sido emitidas em contingência (tpEmis=2, 4, 5). Nestes casos, a autorização da SEFAZ será com o cStat=”150- Autorizado Uso da NF-e, autorização fora de prazo” (NT 2012.003).   
  
  
  
É necessário que consulte a legislação vigente em seu Estado, ou entrar em contato com a Sefaz para saber o prazo máximo permitido.

* Para **a correção:**

1- **Exclua** a nota;

2- Verifique a **data base ao se logar no Protheus;**

3- Inclua a nota **novamente e transmita;**

* **Validação da Sefaz:**

**![228_rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405946667799/228_rejei__o.JPG)**

```
 
```
