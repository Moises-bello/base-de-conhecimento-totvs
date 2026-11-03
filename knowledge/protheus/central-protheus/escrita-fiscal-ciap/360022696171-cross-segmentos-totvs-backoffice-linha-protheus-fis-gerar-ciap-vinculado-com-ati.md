---
article_id: 360022696171
category: Escrita Fiscal - CIAP
content_hash: 8dbe14804653c5a80e421a4c130a139a5a5200285771f12f22ddf3192a86dd32
fetched_at: '2026-06-28T22:39:33.912600+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Gerar CIAP vinculado
  com ativo pelo documento de entrada?
type: support-article
updated_at: '2024-08-28T20:44:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022696171-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gerar-CIAP-vinculado-com-ativo-pelo-documento-de-entrada
---

**Dúvida**

Como gerar Ciap  vinculado ao ativo através do Documento de Entrada?  
  
**Ambiente**

Protheus– Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para que a rotina Manutenção CIAP seja alimentada automaticamente com ativo e manutenção ciap, a partir da rotina MATA103 (Documento de Entrada), será necessário configurar a TES, conforme abaixo:

TES ( MATA080)

Credita ICMS = Sim

Atualiza Ativo = Sim

Desmembra ativo = Sim ou Não

Calcula ICMS = Sim

Livro Fiscal de ICMS = Outros

Livro Fiscal CIAP = Sim

Sit trib icm = 90

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25978505218071)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25978483161495)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25978483165079)

Boletim Ciap

<https://tdn.totvs.com/pages/releaseview.action?pageId=708871751>
