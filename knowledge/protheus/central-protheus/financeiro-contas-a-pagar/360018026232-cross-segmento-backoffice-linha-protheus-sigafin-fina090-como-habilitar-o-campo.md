---
article_id: 360018026232
category: Financeiro - Contas a Pagar
content_hash: 733eeecec57ad13da4667f1608bebc7479b1d2d1d65be7a64d9385f3a4074e66
fetched_at: '2026-06-28T22:38:08.272983+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA090 – Como habilitar
  o campo cheque nas rotinas de baixa automática
type: support-article
updated_at: '2023-06-30T02:25:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018026232-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA090-Como-habilitar-o-campo-cheque-nas-rotinas-de-baixa-autom%C3%A1tica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**Como habilitar o campo cheque na rotina de baixa automática **(FINA090 e FINA091)**?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - A partir da versão 12.1.17

**Solução**Para habilitar o campo cheque na rotina de **baixa de automática**, é preciso ajustar o parâmetro da rotina**(F12)**.

* Acesse a rotina **FINA090/FINA091**
* Altere os parâmetros **(F12)** da rotina:

De: **Gera Cheque Autom. ? = Não**

Para: **Gera Cheque Autom. ? = Sim**

* Execute a rotina.

**Importante:**   
Verifique também se o Banco utilizado está configurado nos parâmetros **MV\_CXFIN** e **MV\_CARTEIR**.  
Os bancos informados nos parâmetros anteriores são considerados como bancos internos da empresa, e que, por consequência **não poderão emitir cheque**.  
  
**Saiba mais:**http://tdn.totvs.com/pages/releaseview.action?pageId=172300136
