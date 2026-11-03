---
article_id: 10063380995351
category: Faturamento - Integrações
content_hash: 37c5a844219ce8c79ed56a8f59abed5ab4997743821706a537b28c718b4c9ac3
fetched_at: '2026-06-28T22:38:26.599180+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Como
  gerar log de integração no Protheus
type: support-article
updated_at: '2024-03-21T14:51:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10063380995351-Cross-Segmento-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Como-gerar-log-de-integra%C3%A7%C3%A3o-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida** Como gerar log de integração no Protheus?  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões  
  
**Solução**

**1** - Vá em seu **appserver.ini** na chave/bloco que carrega o nome do JOB do WebServices **[JOB\_WS\_XXXX]**

**2 -** Inclua uma linha: **"PROFILE=1"** e depois salve o arquivo **(Atalho: CTRL + S).**

**![](https://tdn.totvs.com/download/attachments/572015644/image2022-8-16_23-5-19.png?version=1&modificationDate=1660701920503&api=v2)**

**3** - Ao integrar/tentar integrar, será gerado um arquivo .txt de log na pasta **protheus > protheus\_data > wsprofiler:**

![https://totvssuporte.zendesk.com/attachments/token/ofIpCXnAnOAlmHpY55saCwGXV/?name=image.png](https://totvssuporte.zendesk.com/attachments/token/ofIpCXnAnOAlmHpY55saCwGXV/?name=image.png)
