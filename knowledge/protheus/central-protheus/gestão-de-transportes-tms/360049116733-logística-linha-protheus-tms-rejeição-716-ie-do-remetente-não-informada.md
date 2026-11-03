---
article_id: 360049116733
category: Gestão de Transportes (TMS)
content_hash: 953ba6bdb343d581e6076bbf85b6d030e0816a6b9a68ec26fa580dcf00103093
fetched_at: '2026-06-28T22:45:33.296750+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 716 - IE do Remetente não informada
type: support-article
updated_at: '2022-06-15T11:23:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049116733-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-716-IE-do-Remetente-n%C3%A3o-informada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:50 min****Ocorrência**Na transmissão do **CT-e**ocorre a **Rejeição 716 -** **IE do Remetente não informada**, quando os campos**Inscrição Estadual** ou **Contribuinte do Cadastro do Cliente**não estão preenchidos.   
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
Falta de informação na *tag* **IE** **do Remetente**  
  
**Solução**Para a **rejeição 716 - IE do Remetente não informada**, o **cadastro do cliente** precisa ser ajustado nos campos**Inscrição Estadual** ou **Contribuinte** deverão estar preenchidos.  
  
O campo **Contribuinte** não poderá estar em branco, devendo constar preenchido como **1-Sim** ou **2-Não** de acordo com a situação do cliente. Após ajuste estorne o documento, calcule novamente e retransmita para **SEFAZ**.  
  
Todos os clientes da operação Remetente, Destinatário, Recebedor e Expedidor precisam estar com a informação para que o **XML** seja criado de forma correta. Com o  *layout* do **CT-e** 3.0 a **SEFAZ** passou a validar essas informações.  
  
**Glossário  
CT-e**- Conhecimento de transporte eletrônico **IE** - Inscrição Estadual**SEFAZ**- Secretaria de Estado da Fazenda  
**XML** - Extensible Markup Language
