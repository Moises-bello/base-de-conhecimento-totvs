---
article_id: 16779444671895
category: Financeiro - Reinf
content_hash: ad0b4c77b0777f48c5e859150a740543071f3456733b6c66f8c56b0bab18508a
fetched_at: '2026-06-28T22:37:51.845873+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - O campo Natur.
  Rend. FKF_NATREN não habilita preenchimento
type: support-article
updated_at: '2024-01-17T18:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16779444671895-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-O-campo-Natur-Rend-FKF-NATREN-n%C3%A3o-habilita-preenchimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16779435776535) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**O campo Natur. Rend. FKF\_NATREN não habilita preenchimento  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**Quando a origem do titulo é pelo modulo de **Compras** a **naturezas de rendimento** deve ser informado no modulo de origem.  
  
No modulo de **Compras**, ao posicionar no produto clique em**Outras Ações**, selecione a opção **"Nat. Rendimento".**  
![](https://tdn.totvs.com/download/attachments/738246820/imgREINF-2-1.png?version=1&modificationDate=1676034528103&api=v2)  
   
   
No módulo Financeiro o campo **FKF\_NATREN** fica bloqueado quando o título vem do módulo de Compras. Isso acontece porque a natureza de rendimento deve ser associada a um produto específico, e essa informação é salva na tabela **DHR**.  
   
Por outro lado, se o título é gerado diretamente no **módulo Financeiro**, o campo fica disponível para ser preenchido. Isso ocorre porque, a natureza de rendimento é associada a um título sendo preenchido no campo (**FKF\_NATREN**).  
   
**Saiba mais:**  
Facilitador de preenchimento - Natureza de Rendimento X Natureza Financeira  
<https://tdn.totvs.com/pages/releaseview.action?pageId=743696864>
