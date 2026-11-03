---
article_id: 360019088611
category: Gestão de Transportes (TMS)
content_hash: 4ad9bcfafb0c1a32c9d90ec444acbfe7620544ddffd1664c6205e51f9040d99d
fetched_at: '2026-06-28T22:45:33.330001+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 756 -  Data de emissão do CT-e
  deve ser igual a data de emissão da EPEC
type: support-article
updated_at: '2022-06-14T20:12:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019088611-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-756-Data-de-emiss%C3%A3o-do-CT-e-deve-ser-igual-a-data-de-emiss%C3%A3o-da-EPEC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:00:30 min  
  
Ocorrência**Ao gerar um **CTE - Conhecimento de Transporte Eletrônico** e tentar transmitir em **EPEC - Evento Prévio de Emissão em Contingência** apresenta a rejeição **756 :** **Data de emissão do CT-e deve ser igual a data de emissão da EPEC.** **Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Causa**Essa falha é apresentada quando encontra divergência entre a data e hora do servidor onde é gerado o **XML** com a data e hora da **SEFAZ - Secretaria de Estado da Fazenda**.  
  
**Solução**A data e hora usadas para a **EPEC** são geradas ao trocar o tipo de **CT-e** na tela de monitoramento do mesmo, onde é digitado uma observação. Neste momento são gravadas a data e hora que serão utilizadas para a transmissão do **CT-e**.  
  
O usuário não tem acesso para alteração das datas supracitadas.  
  
Verificar as data e hora no servidor em que foi gerado o **XML**, pois podem estar divergentes com a **SEFAZ**.
