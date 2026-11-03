---
article_id: 360049120413
category: Gestão de Transportes (TMS)
content_hash: fa72168a0a8559c70beb3d0beb03c8a29e28c11a483ec3f5e0fc5a10bc3aee17
fetched_at: '2026-06-28T22:45:33.317368+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 719 - IE do Tomador não informada
type: support-article
updated_at: '2023-08-28T11:33:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049120413-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-719-IE-do-Tomador-n%C3%A3o-informada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17081149030039) Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**Na transmissão do **CT-e**ocorre a **Rejeição** **719 -****IE do Tomador não informada**, quando os campos**Inscrição Estadual** ou **Contribuinte** do **Cadastro do Cliente**não estão preenchidos.  **Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
Falta de informação na *tag* **IE** **do Tomador**.  
  
**Solução**Para a **R****ejeição 719 - IE do Tomador não informada**, no **C****adastro do Cliente** os campos**Inscrição Estadual** ou **Contribuinte** deverão estar preenchidos corretamente.   
  
O campo **Contribuinte** não poderá estar em branco, devendo constar preenchido como **1-Sim** ou **2-Não** de acordo com a situação do cliente. Após ajuste estorne o documento, calcule novamente e retransmita para **SEFAZ**.  
  
Todos os clientes da operação **Remetente**, **Destinatário**, **Recebedor** e **Expedidor** precisam estar com a informação para que o **XML** seja criado de forma correta. Com o *layout* do **CT-e** **3.0** a **SEFAZ** passou a validar essas informações.  
  
**Glossário  
CT-e** - Conhecimento de transporte eletrônico **IE** - Inscrição Estadual**SEFAZ**- Secretaria de Estado da Fazenda  
**XML** - Extensible Markup Language
