---
article_id: 9684194575767
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: fd5d6d9d659f43d484d998d82560740c7929f7db7e4e17ccc910b78ee44ad2d8
fetched_at: '2026-06-28T22:38:23.966859+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Desconexão
  Automática/ Time Out no PGV
type: support-article
updated_at: '2023-10-06T20:19:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9684194575767-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Desconex%C3%A3o-Autom%C3%A1tica-Time-Out-no-PGV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Existe alguma forma de desconexão automática por time out, semelhante ao que existe no SmartClient, no Portal Gestão de Vendas?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Portal Gestão de Vendas - Todas as versões  
  
**Solução**

No Portal Gestão de Vendas não existe esse controle de timeout.

Porém, as licenças do REST são liberadas automaticamente pelo próprio Framework caso a thread fique inativa por muito tempo no caso do usuário PGV, o Token de acesso com validade de cerca de 8 horas.   
  
Caso o usuário esteja inativo por este período o próprio Mingle desconecta o usuário.
