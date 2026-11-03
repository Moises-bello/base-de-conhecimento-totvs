---
article_id: 360013486372
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 72960fda5dccfd3d725d6d05bb830f3a5c764526d3a4184880a4ea206a9fcaff
fetched_at: '2026-06-28T22:38:30.099160+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- Validação de origem
  na exclusão da nota
type: support-article
updated_at: '2024-10-16T14:50:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013486372-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Valida%C3%A7%C3%A3o-de-origem-na-exclus%C3%A3o-da-nota
---

**Dúvida**

Ao excluir a nota, gera a mensagem: Atenção: Esta nota fiscal não pode ser excluída , pois foi gerada no módulo Fiscal, Loja ou Venda Direta.  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- a partir da versão 11.80.  
  
**Solução**

Para  solucionar, verifique a origem da nota de saída gerada através do campo **D2\_ORIGLAN**, para poder saber a rotina pela qual poderá excluir a nota.

O campo **D2\_ORIGLAN** pode receber as seguintes informações:

**LF - Livros fiscais**

**LO - Loja**

**VD- Venda Direta**

Para mais detalhes, acesse:**[Validação de origem na exclusão da Nota](http://tdn.totvs.com/pages/viewpage.action?pageId=392502936)**
