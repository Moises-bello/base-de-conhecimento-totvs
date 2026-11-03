---
article_id: 360047220274
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: ad188e67c49e5d916e17f5c690af370af9ff8e524babaafe1a45790811d7f43b
fetched_at: '2026-06-28T22:42:43.364009+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Help: MATA712'
type: support-article
updated_at: '2022-11-14T11:26:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047220274-Manufatura-Linha-Protheus-SIGAPCP-Help-MATA712
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura:**00:01:00 min****Ocorrência**No módulo de **PCP - Planejamento e Controle da Produção** ao tentar executar o **MATA712 - MRP** é apresentado o *help* **MATA712**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068768014/mceclip1.png)

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Esse help é apresentado pois o **PCPA107 - MRP Multi-Empresa** já foi executado alguma vez e há registros na tabela **SOQ - Objetos do MRP**.  
  
**Solução**O **MATA712** valida o conteúdo da tabela **SOQ** para determinar se o **MRP Multi Empresas** já foi executado. Portanto, para voltar a poder utilizar o **MATA712**, é necessário que a tabela **SOQ** não tenha registros vinculados com a filial em questão.  
  
Para isso tem duas opções:

1. Se tiver empresa centralizadora cadastrada no **PCAP106 - Empresa Centralizadora**, selecione a **Empresa > Outras Ações > Limpar tabelas MRP**;
2. Caso não tenha nenhum empresa centralizadora cadastrada, através do **APSDU** apague os registros da tabela **SOQ.**
