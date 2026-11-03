---
article_id: 360047781494
category: Escrita Fiscal - Impostos - ISS
content_hash: 9b59f53130b864d0b63725db4e7e16653b6cde88abbae5db8ff6b48c88d23bfa
fetched_at: '2026-06-28T22:39:35.242267+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Qual o critério para
  utilização dos campos no Relatório modelo 51 (MATR990)?
type: support-article
updated_at: '2021-06-15T12:51:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047781494-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-o-crit%C3%A9rio-para-utiliza%C3%A7%C3%A3o-dos-campos-no-Relat%C3%B3rio-modelo-51-MATR990
---

**Dúvida:**

Qual o critério para utilizar os campos no Registro de Apuração de ISS modelo 51(MATR990)?  
  
**Ambiente:**

Protheus – Livro Fiscal – A partir da versão 12.1.17.  
  
**Solução:**

Para compreender a gravação dos campos no relatório, primeiramente é preciso validar algumas regras no tratamento do impostos ISS:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071260433/mceclip0.png)

Para configurar conforme o exemplo da NF 000032:

**Recolhe ISS (A1\_RECISS) = SIM**

**L. Fiscal ISS** (F4\_LFISS) = **Tributado**

Para configurar conforme o exemplo das notas 000033 e 000032 será necessário deixar o livro fiscal de ISS no TES como outros ou isento.

**L. Fiscal ISS** (F4\_LFISS) = **Outros/ Isento**

Para configurar conforme a NF 000035 (Campo imposto devido e não retido), é necessário que o prestador do serviço seja o responsável pelo recolhimento do ISS:

**Recolhe ISS (A1\_RECISS) = NÃO**

**L. Fiscal ISS** (F4\_LFISS) = **Tributado**
