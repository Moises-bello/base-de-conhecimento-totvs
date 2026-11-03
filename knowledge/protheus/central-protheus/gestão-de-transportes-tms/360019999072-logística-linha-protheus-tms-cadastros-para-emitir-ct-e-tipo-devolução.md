---
article_id: 360019999072
category: Gestão de Transportes (TMS)
content_hash: 0fa9950e1762874be05b8d4cfe94cdeb419da49305943c39cb5a099fe44c8cd9
fetched_at: '2026-06-28T22:45:27.341933+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastros para emitir CT-e Tipo Devolução
type: support-article
updated_at: '2025-03-24T14:35:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019999072-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-para-emitir-CT-e-Tipo-Devolu%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png) Tempo aproximado para leitura: **00:01:20 min  
  
Dúvida**Como gerar um **CT-e - Conhecimento de Transporte Eletrônico** do tipo **Devolução**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Documento gerado a partir de um **CT-e** original que caracteriza a devolução de uma mercadoria ao seu remetente.  
  
**Cadastros necessários:**

* **Configuração de Documentos**Acesse a rotina no menu **Atualizações/Doctos e Regras/Config. Documentos** - **TMSA150**.  
  Realize o cadastro da configuração de documentos com o campo **Docto. Transp. - DUI\_DOCTMS** igual a **6 - CTRC DEVOLUÇÃO**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081437393/mceclip0.png)

Caso utilize uma série diferente do **CT-e** original, é necessário ajustar o parâmetro **MV\_ESPECIE**, conforme exemplo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080376694/mceclip1.png)

* **Regras de Tributação**Acesse a rotina no menu **Atualizações/Doctos e Regras/Regras de Tributação - TMSA410**.  
  Realize o cadastro de uma regra de tributação para o processo de **CT-e** **de Devolução**. Caso não possua uma regra de tributação para gerar este cadastro, é necessário realizar um cadastro na **Tabela Genérica - SX5**, código **MC - Regras de Tributação.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081439393/mceclip2.png)

* **Regras por Cliente:**Acesse a rotina no menu **Atualizações/Doctos e Regras/Regras por Cliente -****TMSA600**.  
  Realize o cadastro de uma regra para o cliente, ou definir a informação para o cliente genérico para o documento do tipo **CT-e de Devolução**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080379334/mceclip3.png)

O campo **DV1\_TIPNFC – Tipo da NFC** deve ser preenchido como **1 – Devolução.**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360081440813/mceclip4.png)
