---
article_id: 11017114752023
category: PMS - Projetos
content_hash: 83418baf27cf0723c6cafd349ce0e9d628b476efd6d22aa906fb63a99c7cace3
fetched_at: '2026-06-28T22:37:15.984198+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Help: NOCPOSX3
  referenciando os campos AFG_ALI_WT e AFG_REC_WT'
type: support-article
updated_at: '2024-03-11T19:51:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11017114752023-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Help-NOCPOSX3-referenciando-os-campos-AFG-ALI-WT-e-AFG-REC-WT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao realizar movimentações no módulo SIGAPMS, o sistema apresenta o Help: NOCPOSX3 referenciando os campos AFG\_ALI\_WT e AFG\_REC\_WT.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Todas as versões  
  
**Causa**Esse incidente ocorre quando os campos AFG\_ALI\_WT e AFG\_REC\_WT estão no dicionário (SX3) ou no banco de dados do ambiente.

Esses campos (ALI\_WT e REC\_WT) são manipulados através do *aHeader*, no qual são criados em tempo de execução pelos processos internos de framework.

Não são campos existentes no dicionário de dados ou Banco de Dados, portanto os campos não devem existir no ambiente.  
  
**Solução**Verifique com sua área de TI, caso os campos existam em seu ambiente, pois eles devem ser retirados do dicionário e do banco de dados.

Lembrando que os campos são de uso interno da camada de Framework do Protheus e, por esse motivo,  não podem ser utilizados em customizações/personalizações.
