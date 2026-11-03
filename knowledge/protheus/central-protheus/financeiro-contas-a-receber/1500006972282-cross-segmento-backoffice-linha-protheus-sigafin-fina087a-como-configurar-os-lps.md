---
article_id: 1500006972282
category: Financeiro - Contas a Receber
content_hash: f0c999c63157d347f6bbc6e7ee645f5a97de802413613dbcbb82dad8cff8264f
fetched_at: '2026-06-28T22:38:12.800919+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA087A - Como configurar
  os LP´s 575 e 576
type: support-article
updated_at: '2021-04-28T15:16:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006972282-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA087A-Como-configurar-os-LP-s-575-e-576
---

**Dúvida**Como configurar os LP´s 575 e 576?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Na Inclusão/Exclusão de recebimento diverso (**FINA087A**), a tabela que deve ser utilizada para contabilização é a **SEL**, porém a tabela **SE5** estará posicionada para apoio de dados complementares.

**Exemplos:**

## **LP 575**

|  |  |
| --- | --- |
| CT5\_LANPAD | 575 |
| CT5\_SEQUEN | 1 |
| CT5\_DESC | RECIBOS DIVERSOS - INCLUSAO DE UM RECIBO |
| CT5\_DC | 3 |
| CT5\_DEBITO | 1234 |
| CT5\_CREDIT | 1235 |
| CT5\_MOEDAS | 12222 |
| CT5\_VLR01 | IF(SEL->EL\_TIPODOC = 'DC',SEL->EL\_VALOR,0) |
| CT5\_HIST | '575:001 - REC DIV: ' + SE5->('BENEF.: '+E5\_BENEF+' HIST.: '+E5\_HISTOR) |
| CT5\_ORIGEM | '575:001 ' + SEL->('TIPO: '+EL\_TIPO+' RECIBO: '+EL\_RECIBO+' DT EMIS.: '+DTOC(EL\_EMISSAO)) |

|  |  |
| --- | --- |
| CT5\_LANPAD | 575 |
| CT5\_SEQUEN | 2 |
| CT5\_DESC | RECIBOS DIVERSOS - INCLUSAO DE UM RECIBO |
| CT5\_DC | 3 |
| CT5\_DEBITO | 1234 |
| CT5\_CREDIT | 1235 |
| CT5\_MOEDAS | 12222 |
| CT5\_VLR01 | IF(SEL->EL\_TIPODOC = 'TB',SEL->EL\_VALOR,0) |
| CT5\_HIST | '575:001 - REC DIV: ' + SE5->('BENEF.: '+E5\_BENEF+' HIST.: '+E5\_HISTOR) |
| CT5\_ORIGEM | '575:001 ' + SEL->('TIPO: '+EL\_TIPO+' RECIBO: '+EL\_RECIBO+' DT EMIS.: '+DTOC(EL\_EMISSAO)) |

## **LP 576**

|  |  |
| --- | --- |
| CT5\_LANPAD | 576 |
| CT5\_SEQUEN | 1 |
| CT5\_DESC | RECIBOS DIVERSOS - ESTORNO DE UM RECIBO |
| CT5\_DC | 3 |
| CT5\_DEBITO | 1235 |
| CT5\_CREDIT | 1234 |
| CT5\_MOEDAS | 12222 |
| CT5\_VLR01 | IF(SEL->EL\_TIPODOC = 'DC',SEL->EL\_VALOR,0) |
| CT5\_HIST | '576:001 - REC DIV: ' + SE5->('BENEF.: '+E5\_BENEF+' HIST.: '+E5\_HISTOR) |
| CT5\_ORIGEM | '576:001 ' + SEL->('TIPO: '+EL\_TIPO+' RECIBO: '+EL\_RECIBO+' DT EMIS.: '+DTOC(EL\_EMISSAO)) |

|  |  |
| --- | --- |
| CT5\_LANPAD | 576 |
| CT5\_SEQUEN | 2 |
| CT5\_DESC | RECIBOS DIVERSOS - ESTORNO DE UM RECIBO |
| CT5\_DC | 3 |
| CT5\_DEBITO | 1235 |
| CT5\_CREDIT | 1234 |
| CT5\_MOEDAS | 12222 |
| CT5\_VLR01 | IF(SEL->EL\_TIPODOC = 'TB',SEL->EL\_VALOR,0) |
| CT5\_HIST | '576:001 - REC DIV: ' + SE5->('BENEF.: '+E5\_BENEF+' HIST.: '+E5\_HISTOR) |
| CT5\_ORIGEM | '576:001 ' + SEL->('TIPO: '+EL\_TIPO+' RECIBO: '+EL\_RECIBO+' DT EMIS.: '+DTOC(EL\_EMISSAO)) |

**Saiba mais**

<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=557319327>
