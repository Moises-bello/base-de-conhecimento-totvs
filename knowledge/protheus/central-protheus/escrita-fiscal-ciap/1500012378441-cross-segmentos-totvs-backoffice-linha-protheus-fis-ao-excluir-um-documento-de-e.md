---
article_id: 1500012378441
category: Escrita Fiscal - CIAP
content_hash: 507f0db0e6ee3e853c79b9bfb0a548e92641a4d7c6deb9209c6dfb71da15facc
fetched_at: '2026-06-28T22:39:33.970040+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Ao excluir um Documento
  de Entrada via MATA103 é apresentado o alerta A100CIAPDE
type: support-article
updated_at: '2021-07-28T17:35:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012378441-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Ao-excluir-um-Documento-de-Entrada-via-MATA103-%C3%A9-apresentado-o-alerta-A100CIAPDE
---

**Dúvida**Ao excluir um Documento de Entrada via MATA103 é apresentado o Alerta A100CIAPDE.  
  
**Ambiente**

Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**

Ao excluir a nota fiscal de entrada que realizou a inclusão automática do bem na manutenção CIAP e apresentar o alerta A100CIAPDE, indica que o bem incluído através desta nota fiscal já sofreu apropriações.

Verifique na rotina de **Estorno CIAP (MATA906)**, caso seja necessário a exclusão da nota fiscal e o bem tenha sofrido movimentações, as apropriações devem ser canceladas.

Informações adicionais:

<https://tdn.totvs.com/display/public/PROT/CIAP>
