---
article_id: 360021105771
category: NFe - Nota Fiscal Eletrônica
content_hash: 2d9cd3b3c30b5ed4622518111d570da2a98327bba4b22384c400f6c0e6dfc31d
fetched_at: '2026-06-28T22:40:06.778888+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como imprimir uma
  DANFE com bloqueio de movimento
type: support-article
updated_at: '2025-06-18T14:34:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021105771-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-imprimir-uma-DANFE-com-bloqueio-de-movimento
---

**Dúvida**Como imprimir uma DANFE com bloqueio de movimento?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

 1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar MV\_IMPDIR = .T.

**Nome da variável**  
MV\_IMPDIR

**Tipo**           
Lógico

**Descrição**Indica a opção de acessar diretamente o WebService na impressão do  
DANFE, sem verificar os Livros Fiscais (SF3)

**Conteúdo**.T.
