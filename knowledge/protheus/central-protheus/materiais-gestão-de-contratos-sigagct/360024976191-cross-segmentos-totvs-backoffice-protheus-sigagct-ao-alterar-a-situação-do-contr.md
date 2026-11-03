---
article_id: 360024976191
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 80c2ca2a90f9197ba66e5bdcde66ec48091143ed0dccba0cb7e3085aa0e9b2b8
fetched_at: '2026-06-28T22:37:19.747976+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT -  Ao alterar a situação
  do contrato para vigente ocorre o Help CNTA100ASS
type: support-article
updated_at: '2025-11-24T16:41:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024976191-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-alterar-a-situa%C3%A7%C3%A3o-do-contrato-para-vigente-ocorre-o-Help-CNTA100ASS
---

**Ocorrência**  
Ao alterar a situação do contrato para Vigente ocorre o Help CNTA100ASS,

Validando que a Data Base de Vigência do Contrato é menor que a Data de Inicio do Contato, ou seja a Data de Inicio do contrato é futura com relação a data que se torna vigente.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5315746028567)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Causa**  
Esse incidente ocorre, ao incluir um contrato com o parâmetro **MV\_CNVLASS " Permite Validar a data da assinatura do contrato?** = **S**e informar uma Data do Início (CN9\_DTINIC) **MAIOR** que a database que está tornando o contrato Vigente (que será gravada no campo "Dt. Sit. Vig" (CN9\_DTASSI)), ao torná-lo vigente, é disparado o Help abaixo CNTA100ASS devido ao parâmetro estar habilitado e assim está validando a data do campo CN9\_DTASSI.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5315325884311)  
  
**Solução**  
Para não apresentar o help ao informar a data de inicio do contrato maior que a data da alteração da situação da vigência do contrato altere o parâmetro **MV\_CNVLASS =** **N.**

***Saiba Mais:***

[MP - SIGAGCT - MV\_CNVLASS - Como validar a Data de Assinatura de um Contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024672492)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
