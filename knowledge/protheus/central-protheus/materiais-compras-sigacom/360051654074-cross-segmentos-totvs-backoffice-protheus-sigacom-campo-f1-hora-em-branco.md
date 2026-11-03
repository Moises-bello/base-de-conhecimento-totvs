---
article_id: 360051654074
category: Materiais - Compras (SIGACOM)
content_hash: 53e264f89aa20815dfaedb9738eac81216fb5693bfb5b9ebe0d0777645284d0b
fetched_at: '2026-06-28T22:41:14.311688+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Campo F1_HORA em branco
type: support-article
updated_at: '2024-07-01T12:04:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051654074-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Campo-F1-HORA-em-branco
---

**Dúvida**

Campo F1\_HORA em branco  
  
**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

Foi gerado Documento de Entrada e no momento de transmitir a nota para a Sefaz foi identificado que o campo F1\_HORA consta em branco.

Para o preenchimento automático do campo F1\_HORA verifique preenchimento do parâmetro MV\_HORANFE =  .T. e se o Documento de Entrada consta com formulário próprio = SIM

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081865274)  
  
Para gravar em notas diferentes de normal revise os dois parâmetros a seguir:

* MV\_HORANFE
* MV\_HORARMT

Artigos relacionados:  <https://tdn.totvs.com/pages/viewpage.action?pageId=818456857>

Se houver necessidade de validar com atualização em ambiente de teste, [clique aqui para download do pacote acumulado Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)
