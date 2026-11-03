---
article_id: 360042163614
category: NFe - Nota Fiscal Eletrônica
content_hash: 0173c9c8019e81a312a95a7acfcd8bd7a24b644fb8b564038425264546016153
fetched_at: '2026-06-28T22:40:00.411792+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de
  Schema referente as TAGS dhEmi e dhSaiEnt para nota de Entrada'
type: support-article
updated_at: '2021-07-02T20:03:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042163614--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-Schema-referente-as-TAGS-dhEmi-e-dhSaiEnt-para-nota-de-Entrada
---

**Dúvida**Como corrigir a falha de Schema abaixo:

029 : Falha de Schema referente as TAGS dhEmi e dhSaiEnt para nota de Entrada ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe -a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Nas TAGS **dhEmi e dhSaiEnt** é informada a **data, hora e o fuso horário da nota.**

* Conforme o XML de exemplo abaixo **não gerou a hora nas TAGS** do XML.

![](https://totvssuporte.zendesk.com/attachments/token/ivJkl8CzhpES0jMcDrXKLCKTC/?name=inline1116314449.png)​

O campo no Protheus que leva o conteúdo para essas TAGs no XML é o **F1\_HORA.**  
  
Verifique se ao gerar o **Documento de entrada o campo F1\_HORA** foi preenchido, caso não esteja preenchendo o campo na tabela, há o parâmetro:  
  
**Nome Var:** MV\_HORANFE  
**Tipo:** LÓGICO  
**Cont Por:** .T.  
**Descrição:** Utilizado para gravar o campo F1\_HORA no momento  da inclusão do documento de entrada. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057048653/mceclip0.png)

Após habilitar o parâmetro, **exclua a nota e gere novamente.**
