---
article_id: 360018691951
category: Call Center - Telecobrança
content_hash: 9bfa5eec9f502b4aa81d017550687b40ef1c94f7276f992a763cfc6239381e86
fetched_at: '2026-06-28T22:41:28.674799+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Schedule na Baixa
  de Cobrança até a release 12.1.17
type: support-article
updated_at: '2022-06-22T17:33:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018691951-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Schedule-na-Baixa-de-Cobran%C3%A7a-at%C3%A9-a-release-12-1-17
---

**Dúvida**

Não consigo criar o **Schedule** da rotina Baixa de cobrança **TMKA290**.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- até a release 12.1.17.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Crie o agente scheduler:;  
2. Crie a rotina a ser schedulada;  
3. Configure a rotina ser schedulada, informando a condição, exemplo: **TMKA290**('01','01',' ','ZZ','2');  
4. Configure o server.ini para uso do schedule.

Obs: após a versão 12, release 12.1.23, o processo de schedule de baixa de cobrança mudou, acesse a documentação: **[MP-TMK-Como Configurar Schedule na baixa de cobrança](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007696541-MP-TMK-Como-Configurar-Schedule-na-baixa-de-cobran%C3%A7a)**
