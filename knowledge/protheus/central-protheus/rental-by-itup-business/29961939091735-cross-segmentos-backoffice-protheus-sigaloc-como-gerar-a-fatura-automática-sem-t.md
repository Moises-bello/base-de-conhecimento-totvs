---
article_id: 29961939091735
category: Rental by ItUp Business
content_hash: 9dca4ede4130846671901b8f67bbdbbccb89e58dcd8ec36622ee8c751701a004
fetched_at: '2026-06-28T22:36:20.557553+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como gerar a fatura automática
  sem ter a nota fiscal de remessa gerada?
type: support-article
updated_at: '2026-04-09T12:59:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29961939091735-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-gerar-a-fatura-autom%C3%A1tica-sem-ter-a-nota-fiscal-de-remessa-gerada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29961962249239) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar a fatura automática sem ter a nota fiscal de remessa gerada?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - a partir da versão P12.1.2310  
  
**Solução**

Para gerar a fatura automática, é necessário alterar o parâmetro **MV\_LOCX067**. Defina o conteúdo como **".F."** (**F de Falso**), o que permitirá que o faturamento automático seja realizado sem a necessidade de gerar a nota fiscal de remessa.

Dessa forma, ao gerar o contrato, não será necessário gerar a nota fiscal de remessa para emitir a **"Fatura automática"** (**LOCA021**).
