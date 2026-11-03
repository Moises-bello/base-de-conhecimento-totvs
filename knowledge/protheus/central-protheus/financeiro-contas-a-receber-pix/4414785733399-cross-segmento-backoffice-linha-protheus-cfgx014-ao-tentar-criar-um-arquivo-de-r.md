---
article_id: 4414785733399
category: Financeiro - Contas a Receber - PIX
content_hash: a5561d2298dcc4e0282ff5d8ea19bbbc6d40123cfa512bc292ba57eb8746f0ba
fetched_at: '2026-06-28T22:38:16.490842+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: Cross Segmento Backoffice Linha Protheus - CFGX014 - Ao tentar criar um arquivo
  de retorno CNAB PIX CR o campo conteúdo esta bloqueado
type: support-article
updated_at: '2021-12-02T19:24:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414785733399-Cross-Segmento-Backoffice-Linha-Protheus-CFGX014-Ao-tentar-criar-um-arquivo-de-retorno-CNAB-PIX-CR-o-campo-conte%C3%BAdo-esta-bloqueado
---

**Dúvida**Ao tentar criar um arquivo de retorno CNAB PIX CR o campo conteúdo está bloqueado?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414767812503/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro -  CFGX014- Todas as versões  
  
**Solução**O campo conteúdo é bloqueado, pois somente no **retorno** irá ler as colunas. A configuração está na **remessa**.  
Conforme a documentação oficial do **PIX**  
<https://tdn.totvs.com/pages/viewpage.action?pageId=569478747#Pagamentosinstant%C3%A2neos-PIX-03.CONTASARECEBER>

![](https://p23.zdusercontent.com/attachment/888110/pdQY7KcyCu8rB67fmu0xqKe2b?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..83W-i-HU-0v94W7gE0xvLQ.SlZTiPDUDKqjlD8NSj5-3TGvNxLTxJLQyMM3Ad_Xik95F9y29d6KOiPmYHDZRPDnHv06LHCrbOZt28R2FbFud039MAVTogSQ-z6O1f1cwcMS3mChHbkxM5BDzxrJXlMk9LDy7qRaI0sSh44TnWplMFNXxSwWZFZqKlbsmbgt0Csoiw5z_FKBj_YKg6w3nvOyBdbGjsIRgGnvZtY66Evij2GJXI8OISjbrtZ4QI9Rbo8h11XzkogIcdoI1nbfTAmd8fVWSYmEoYM4Jnu45N-ujWmKjhvEOJbQrunP8gTX_us.6vcqmsN3NrNY7tZM2NF_8A)  
  
O layout é **750 posição**, que no caso internamente é o mesma tratativa do **400 posições.** A configuração é na **remessa** e no **retorno** somente lê as posições**,** por isso este campo é Bloqueado.
