---
article_id: 360049116573
category: Gestão de Transportes (TMS)
content_hash: 8e97f6a852eb539e37d3ea35cc65b2f427b3d10d03f2d18fc20adc65c1ca7dce
fetched_at: '2026-06-28T22:45:32.555740+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Rejeição 232 - IE do Destinatário não informada
type: support-article
updated_at: '2022-06-15T11:45:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049116573-Log%C3%ADstica-Linha-Protheus-TMS-Rejei%C3%A7%C3%A3o-232-IE-do-Destinat%C3%A1rio-n%C3%A3o-informada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min**  
**Ocorrência****Rejeição 232 -****IE** **do Destinatário não informada**,na transmissão do **CT-e**.  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Causa**  
Falta de informação na *tag* **IE** do destinatário  
  
**Solução  
Para a rejeição 232 - IE do Destinatário não informada,** o **cadastro do cliente** precisa ser ajustado nos campos **Inscrição Estadual**ou **Contribuinte** deverão estar preenchidos.  
O campo **Contribuinte** não poderá estar em branco, devendo constar preenchido como **1 - Sim** ou **2 -Não** de acordo com a situação do cliente. Após ajuste estorne o documento, calcule novamente e retransmita para **SEFAZ**.  
  
Todos os clientes da operação **Remetente**, **Destinatário**, **Recebedor** e **Expedidor** precisam estar com a informação para que o **XML** seja criado de forma correta. Com o *layout* do **CT-e** 3.0 a **SEFAZ** passou a validar essas informações.  
  
**Glossário  
CT-e**- Conhecimento de Transporte eletrônico **IE** - Inscrição Estadual**SEFAZ**- Secretaria de Estado da Fazenda  
**XML** - Extensible Markup Language
