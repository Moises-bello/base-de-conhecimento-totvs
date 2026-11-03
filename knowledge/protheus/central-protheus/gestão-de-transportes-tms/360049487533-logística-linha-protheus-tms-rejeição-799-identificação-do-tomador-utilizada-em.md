---
article_id: 360049487533
category: Gestão de Transportes (TMS)
content_hash: 5ad9e0b4f0d8b5661a0f0e3a0d18789cdb8fc87eb342d09fb8fc5fcdaea45daf
fetched_at: '2026-06-28T22:45:32.547634+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição  799 - Identificação do tomador
  utilizada em outro papel no CT-e, CNPJ, CPF ou IE
type: support-article
updated_at: '2021-08-23T19:32:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049487533-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-799-Identifica%C3%A7%C3%A3o-do-tomador-utilizada-em-outro-papel-no-CT-e-CNPJ-CPF-ou-IE
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Na transmissão do **CT-e** ocorre a **Rejeição 799** - **Identificação do tomador utilizada em outro papel no** **CT-e - CNPJ, CPF ou IE,**quando o tomador do frete está também declarado em outro papel no **CT-e**.  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
Esta rejeição ocorre quando a *tag* **TOMA4** possui o mesmo **CNPJ** ou **IE** declarados nas informações de **Remetente, Destinatário, Recebedor ou Expedidor.**  
  
**Solução**Esta rejeição é apresentada porque na digitação do lote o usuário informou:  
**Remetente**, **Destinatário**, **Recebedor** ou **Expedidor** como consignatário e definiu que o **devedor do frete também será o consignatário.**  
  
Quando definimos que o devedor do frete é o consignatário, o **XML** é gerado com a *tag***TOMA4.** A **SEFAZ** valida se **CNPJ, CPF e IE** são diferentes dos grupos **Remetente**, **Destinatário**, **Recebedor**, **Expedidor**. Se forem iguais haverá rejeição.  
  
Sendo assim quando o devedor for o **Consignatário**, este não poderá ser o **Remetente, Destinatário, Recebedor** ou **Expedidor**.  
  
Caso seja um deles não há necessidade de informar o **Consignatário**, basta defini-los como **Devedor** do frete.  
  
**Glossário****CT-e**- Conhecimento de Transporte Eletrônico  
**CNPJ** - Cadastro Nacional da Pessoa Jurídica  
**CPF** - Cadastro de Pessoas Físicas  
**IE** - Inscrição Estatual   
**XML**- Extensible Markup Language
