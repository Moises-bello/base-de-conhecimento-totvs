---
article_id: 4422771990807
category: TAF - REINF
content_hash: 54491cacfa3a8a62b87c7d6d121684aa7bb0d8227150fa9551af3ce76b437755
fetched_at: '2026-06-28T22:41:33.363775+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - TAF - REINF - O valor 'XX' informado
  na coluna 'X' para o campo Id. Natureza BC Credito ( C30_NATBCC ) não existe na
  base de dados
type: support-article
updated_at: '2023-03-31T17:19:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422771990807-Cross-Segmento-Backoffice-Linha-Protheus-TAF-REINF-O-valor-XX-informado-na-coluna-X-para-o-campo-Id-Natureza-BC-Credito-C30-NATBCC-n%C3%A3o-existe-na-base-de-dados
---

**Dúvida**

O valor 'XX' informado na coluna 'X' para o campo Id. Natureza BC Credito ( C30\_NATBCC ) não existe na base de dados.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF - a partir da versão 12  
  
**Solução**

O erro de integração ocorre devido ao código de Base de calculo do credito informado no cadastro do TES, não corresponder aos códigos de Base de Calculo de Credito na tabela dinâmica **C11 - Base Cálculo de Credito**.

Este campo **( C30\_NATBCC )** é relacionado ao TES campo **Cod. BC. Cred. (F4\_CODBCC)**  
  
O código é gravado no campo **(FT\_CODBCC)** esse campo é alimentado pelo TES campo **(F4\_CODBCC)**.

***Campo Cod. BC. Cred. F4\_CODBCC localizado no Cadastro do TES***

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422772344343/mceclip3.png)

***Tabela Dinâmica C11, que pode ser consultada em Consulta // Tabelas dinâmicas e visualizada na opção Abrir Browse***

***![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422777622807/mceclip2.png)***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422771822103/mceclip1.png)

Configure o TES corretamente, Reprocesse a Nota Fiscal através da rotina (MATA930) Reprocessamento e efetue a integração apenas da Nota Fiscal em qual ocorreu erro de integração via Extrator Fiscal (EXTFISXTAF).
