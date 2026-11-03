---
article_id: 25979196430871
category: Escrita Fiscal - CIAP
content_hash: 985393913940d7e3376488a0938ae238b9fc7fe113526345577fc89c264c4134
fetched_at: '2026-06-28T22:39:33.909902+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Gerar CIAP sem  vinculo
  com ativo pelo documento de entrada?
type: support-article
updated_at: '2024-08-28T21:22:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25979196430871-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gerar-CIAP-sem-vinculo-com-ativo-pelo-documento-de-entrada
---

**Dúvida**

Como gerar Ciap  sem vinculo com ativo através do Documento de Entrada?  
  
**Ambiente**

Protheus– Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Para que a rotina Manutenção CIAP seja alimentada automaticamente na manutenção ciap, a partir da rotina MATA103 (Documento de Entrada), será necessário configurar a TES, conforme abaixo:

TES ( MATA080)

Credita ICMS = Sim/não

Atualiza Ativo = Não

Desmembra ativo =  Não

Calcula ICMS = Sim

Livro Fiscal de ICMS = Outros

Livro Fiscal CIAP = Sim

Sit trib icm = 90

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25979196407063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25979190177047)

Boletim ciap:

https://tdn.totvs.com/pages/releaseview.action?pageId=708871751
