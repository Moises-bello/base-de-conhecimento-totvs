---
article_id: 11992171036055
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 876366ee86c7da20f97dc36fe943af494bb56020020a5ccf88cc2e09d6949136
fetched_at: '2026-06-28T22:38:45.269070+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M460PROC
type: support-article
updated_at: '2023-01-27T20:18:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11992171036055-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M460PROC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M460PROC**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

**Após executar** a função **INDREGUA na tabela SC9.** Este Ponto de Entrada é chamado **logo após** efetuar a **seleção dos registros da tabela SC9** - Pedidos Liberados.  
  
**Exemplo**

```
#INCLUDE 'TOTVS.CH'  
  
User Function M460PROC()  
  
    Alert("Passou pelo PE M460PROC")  
  
Return
```

**Saiba Mais**

**[Ponto de Entrada M460PROC](https://tdn.totvs.com/x/xIRn)**
