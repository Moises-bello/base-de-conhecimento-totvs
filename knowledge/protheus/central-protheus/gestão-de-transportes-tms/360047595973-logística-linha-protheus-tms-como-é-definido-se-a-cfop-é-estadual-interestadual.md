---
article_id: 360047595973
category: Gestão de Transportes (TMS)
content_hash: 6724e5bcbd04642cf6b235b1406d6ff2b68830df4a8ab74ccd5e02ffec2c74d0
fetched_at: '2026-06-28T22:45:27.414374+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como é definido se a CFOP é Estadual, Interestadual
  ou Exterior
type: support-article
updated_at: '2024-06-06T18:25:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047595973-Log%C3%ADstica-Linha-Protheus-TMS-Como-%C3%A9-definido-se-a-CFOP-%C3%A9-Estadual-Interestadual-ou-Exterior
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:40 min**  
**Dúvida**Como é definido se a **CFOP é Estadual, Interestadual ou Exterior** no **SIGATMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**A definição da **UF de Origem** e **Destino** para identificar se o **transporte é Estadual, Interestadual ou Exterior** está relacionado à **UF** registrada na tabela **DUY - Grupo de Regiões** referente aos campos **DTC\_CDRORI** e **DTC\_CDRCAL**.  
  
Com isso no **SIGATMS**  será verificado as **UFs** dos campos **DTC\_CDRORI** e **DTC\_CDRCAL** e aplicado as seguintes regras:  
  
**UF Inicio** igual a **UF Fim**, resultado será **CFOP Inicio 5  
UF Inicio** diferente a **UF Fim**, resultado será **CFOP Inicio 6  
UF Fim** igual a **EX**, resultado será **CFOP Iniciado com 7**A verificação do digito inicial do **CFOP** é realizado pelo **Módulo Fiscal** de acordo com as regras descritas acima.  
  
**Glossário****SIGATMS -**Gestão de Transportes  
**UF -** Unidade da Federação  
**CFOP -**Código Fiscal de Operações e Prestações
