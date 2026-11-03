---
article_id: 360048365274
category: Gestão de Transportes (TMS)
content_hash: 80662697328d8479e2266978a37243b48d06cc5d23386ed432d05528402271c2
fetched_at: '2026-06-28T22:45:33.310267+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: 'Logística - Linha Protheus - TMS - Rejeição 718 - IE do Recebedor não informada '
type: support-article
updated_at: '2023-01-18T14:22:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048365274-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-718-IE-do-Recebedor-n%C3%A3o-informada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:00:50 min** **Ocorrência**Na transmissão do **CT-e**ocorre a **Rejeição** **718 -****IE do Recebedor não informada**, quando os campos**Inscrição Estadual** ou **Contribuinte** do **Cadastro do Cliente**não estão preenchidos.   
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
Falta de informação na *tag* **IE** **do Recebedor**  
  
**Solução**Para a **rejeição 718 - IE do Recebedor não informada**, o **C****adastro do Cliente**precisa ser ajustado nos campos**Inscrição Estadual** ou **Contribuinte** deverão estar preenchidos.  
  
O campo **Contribuinte** não poderá estar em branco, devendo constar preenchido como **1- Sim** ou **2** **-Não** de acordo com a situação do cliente. Após ajuste estorne o documento, calcule novamente e retransmita para **SEFAZ**.  
  
Todos os clientes da operação Remetente, Destinatário, Recebedor e Expedidor precisam estar com a informação para que o **XML** seja criado de forma correta. Com o *layout* do **CT-e** 3.0, a **SEFAZ** passou a validar essas informações.  
  
**Glossário  
CT-e**- Conhecimento de transporte eletrônico **IE** - Inscrição Estadual **SEFAZ**- Secretaria de Estado da Fazenda  
**XML** - Extensible Markup Language
