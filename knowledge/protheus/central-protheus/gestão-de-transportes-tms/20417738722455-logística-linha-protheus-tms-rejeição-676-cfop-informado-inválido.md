---
article_id: 20417738722455
category: Gestão de Transportes (TMS)
content_hash: b917a3040d81e9059e4dc36e14105ab04ac087e62b1b99e180240b4654feadb1
fetched_at: '2026-06-28T22:45:33.275090+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 676 -  CFOP informado inválido
type: support-article
updated_at: '2024-01-09T13:42:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20417738722455-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-676-CFOP-informado-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20417738696855) Tempo aproximado para leitura: **00:01:35 min****Ocorrência**Ao transmitir um **CT-e - Conhecimento de Transporte Eletrônico**no **TOTVS Logística TMS**, ocorre a **Rejeição 676 - CFOP informado inválido.**  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**A rejeição ocorre pois o **CFOP -** **Código Fiscal de Operações e de Prestações** utilizado no **CT-e** não está na relação **Relação de CFOP válidos para autorização de CTe**descrita n **Manual de Orientações do Contribuinte - Visão Geral** do **CT-e.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Avalie com seu Fiscal qual o **CFOP** correto para sua operação de transporte, considerando a relação de **CFOPs** válidos para autorização de **CTe**;
2. Com o **CFOP** definido, acesse a rotina **Atualizações/ Cadastros/ Tipos de Entradas e Saídas - MATA080**, busque sua **TES - Tipos de Entrada e Saída**utilizada no calculo. Caso não saiba qual **TES** foi utilizada no calculo do seu documento, basta verificar no campo **D2\_TES.**
3. Altere o campo **Cod. Fiscal - F4\_CF**, na aba **Impostos,** preenchendo o **CFOP** determinado pelo seu Fiscal.
4. Após realizar o ajuste da **TES**, estorne o calculo do documento e calcule-o novamente. Isso fará com que o Sistema acate o novo **CFOP** definido na **TES** para este documento.

**Saiba mais**Lista de manuais do CT-e, onde é possível encontrar o **Manual de Orientações do Contribuinte - Visão Geral** do **CT-e**: [Manuais do CT-e](https://dfe-portal.svrs.rs.gov.br/Cte/Documentos#)
