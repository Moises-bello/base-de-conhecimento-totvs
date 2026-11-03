---
article_id: 360018482071
category: Ativo-Fixo - Error log
content_hash: 29db1be97bb540e39c34238c0f660f9cba41a66e0dc21537f4fdff885d19da4a
fetched_at: '2026-06-28T22:41:54.821073+00:00'
product: protheus
section_id: 1500001547442
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 erro no parâmetroFWFormGridModel:
  Id N3_TXDEPR01 inválido on FWFORMGRIDMODEL:GETVALUE(FWFORMGRIDMODEL.PRX)'
type: support-article
updated_at: '2023-11-30T19:33:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018482071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-erro-no-par%C3%A2metroFWFormGridModel-Id-N3-TXDEPR01-inv%C3%A1lido-on-FWFORMGRIDMODEL-GETVALUE-FWFORMGRIDMODEL-PRX
---

**Ocorrência**

Error log

erro no parâmetroFWFormGridModel: Id N3\_TXDEPR01 inválido on FWFORMGRIDMODEL:GETVALUE(FWFORMGRIDMODEL.PRX) 24/08/2018 15:13:38 line : 2575   
  
**Ambiente**  
Protheus – Ativo Fixo – A partir da versão P12  
  
**Causa**

Erro ocasionado pois o campo no padrão é N3\_TXDEPR1 e não N3\_TXDEPR01  
  
**Solução**

Verifique o cadastro do campos N3\_TXDEPR1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013779672)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013779832)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013779952)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013779872)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013791771)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013780232)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013791931)

**Importante**

Para evitar que erros como esse ocorram e de extrema importância que o dicionario de dados seja atualizado, SDF.BRA na pasta systemload e a execução do UPDDISTR.

[MP - SIGACTB - Ambiente desatualizado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000043507-MP-SIGACTB-Ambiente-desatualizado?source=search)

Veja também :

[MV\_CENT](http://tdn.totvs.com/pages/viewpage.action?pageId=286729887)

[MP - SIGAATF Impressão de relatório em Disco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018487051-MP-SIGAATF-Impress%C3%A3o-de-relat%C3%B3rio-em-Disco?source=search&auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjo4ODgxMTAsInVzZXJfaWQiOjY2MjU2NjQ5ODgsInRpY2tldF9pZCI6NDE5NjI4MywiY2hhbm5lbF9pZCI6NjMsInR5cGUiOiJTRUFSQ0giLCJleHAiOjE1NDI1NzI1OTJ9.p8k9LUilTolzPggAY40oEikNRxlWwibIAElEA4yJf94)
