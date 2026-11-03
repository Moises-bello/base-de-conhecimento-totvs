---
article_id: 360028521952
category: RH - Folha de Pagamento
content_hash: 8e4a9a81270693296679c0a63696454ecd9dc59c7b976eef85b316d886f7ae9f
fetched_at: '2026-06-28T22:44:12.026785+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de  INSS patronal para MEI
type: support-article
updated_at: '2025-04-15T13:03:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028521952-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-INSS-patronal-para-MEI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26282150865047)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como calcular 20% de INSS Patronal para autônomo MEI?  
   
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**É considerado **MEI o contribuinte individual quando o campo RA\_AUTMEI estiver com SIM**. Assim a verba de pagamento da prestação de serviço com ID 0218 será substituída pela verba com ID 1413 (Autônomo MEI sem INSS).

Para que seja gerada somente os **20% Patronal** deve-se seguir a configuração abaixo:

- Deverá deixar o campo **Calc. INSS = Não** no cadastro do autônomo

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029469171)

A verba com **ID 1413** o campo **INSS** tem que ficar = **SIM**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029469431)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029469731)

Exemplo do cálculo da folha:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029471392)  
  
**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como cadastrar um Autônomo MEI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035241534-RH-Linha-Protheus-GPE-Como-cadastrar-um-Aut%C3%B4nomo-MEI)

[RH - Linha Protheus - GPE - eSocial - S-1200 - Qual a tratativa do eSocial para MEI - Microempreendedor Individual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026394631-RH-Linha-Protheus-GPE-eSocial-S-1200-Qual-a-tratativa-do-eSocial-para-MEI-Microempreendedor-Individual)
