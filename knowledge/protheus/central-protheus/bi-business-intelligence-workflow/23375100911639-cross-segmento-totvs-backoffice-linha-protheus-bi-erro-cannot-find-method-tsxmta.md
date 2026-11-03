---
article_id: 23375100911639
category: BI - Business- Intelligence - Workflow
content_hash: 37287ba68dfd248df42423fd14984dc0e19738080cee03bb92ffbc1b7ef593ee
fetched_at: '2026-06-28T22:37:03.079815+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - BI- Erro: Cannot find method
  TSXMTABLE:GRVSXMTSKMAIL on TWFPROCESS:EXEC(WFPROCESS.PRW)'
type: support-article
updated_at: '2024-08-19T11:37:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23375100911639-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Erro-Cannot-find-method-TSXMTABLE-GRVSXMTSKMAIL-on-TWFPROCESS-EXEC-WFPROCESS-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23375111226519)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Ao utilizar a função TWFProcess é gerado o erro: Cannot find method TSXMTABLE:GRVSXMTSKMAIL on TWFPROCESS:EXEC(WFPROCESS.PRW)   
   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.33

**Solução**

Esse falha ocorre, pois o Fonte WFTSXM.PRW com data anterior a 24/04/2024, não possui o novo método TSXMTABLE, segue abaixo patch com a atualização.

Pacotes:

[12.1.2210](https://suporte.totvs.com/portal/p/10098/download?e=1144971)  
[12.1.2310](https://suporte.totvs.com/portal/p/10098/download?e=1144972)  
[12.1.33](https://suporte.totvs.com/portal/p/10098/download?e=1144973)

**Saiba Mais**

**[TWFProcess](https://tdn.totvs.com/display/public/PROT/TWFProcess)**
