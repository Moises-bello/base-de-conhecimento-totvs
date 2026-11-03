---
article_id: 360007122832
category: Gestão de Transportes (TMS)
content_hash: 9ec9a8e377d0d6818f5ba2af2df96151a83c99c35c9146248cd47a429ebf944b
fetched_at: '2026-06-28T22:45:29.530228+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Ponto de entrada AT250CPO Alterar campos
  Contrato Clientes
type: support-article
updated_at: '2022-06-20T14:34:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007122832-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-AT250CPO-Alterar-campos-Contrato-Clientes
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** **Tempo aproximado para leitura:** 00:00:30 min **Dúvida**Como implementar o ponto de entrada **AT250CPO** - Alterar campos **Contrato Clientes**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**O ponto de entrada **AT250CPO** é utilizado para indicar campos específicos para permitir alteração destes no **Contrato de Clientes** se possuir **CTRC** gerado.  
  
**Programa** **Fonte**: TECA250.PRW  
  
**Sintaxe**: AT250CPO - Alterar campos Contrato Clientes ( ) --> aRet  
  
**Retorno**:  
  
**aRet**

(array\_of\_record)* Contendo campos específicos para permitir alteração se contrato possuir CTRC gerado.

**Exemplos**:  
  
User Function AT250CPO()

Local aRet := {"DUX\_PESO"}

Return aRet
