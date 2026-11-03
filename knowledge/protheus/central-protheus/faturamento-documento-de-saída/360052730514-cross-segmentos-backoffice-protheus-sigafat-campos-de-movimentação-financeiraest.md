---
article_id: 360052730514
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 0986527ce258117efbbc574bdadd3b89df7612cac9053c8f20e2b6e59a7d50cd
fetched_at: '2026-06-28T22:38:44.008167+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Campos de movimentação financeira/estoque
  na NF
type: support-article
updated_at: '2024-11-05T18:46:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052730514-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Campos-de-movimenta%C3%A7%C3%A3o-financeira-estoque-na-NF
---

**Dúvida**Além do campo D2\_TES, existe algum outro campo, seja no cabeçalho ou nos itens da nota fiscal de saída (SF2 ou SD2), que informe se o documento gerou duplicata e/ou movimentou o estoque?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**No caso da tabela SF2, é possível verificar a geração de títulos por meio do campo F2\_DUPL. Se o título foi gerado, esse campo exibirá o número do título associado à nota.

Na tabela SD2, existem os seguintes campos relevantes ao ESTOQUE:

* **D2\_NUMSEQ**: numeração sequencial dos movimentos de estoque, gerada automaticamente pelo sistema, para efeitos de recálculo do custo médio e que abrange os arquivos SD1, SD2 e SD3.
* **D2\_ESTOQUE**: indica se a TES (Tipo de Entrada e Saída - SF4) utilizada na criação da nota movimenta o estoque (sim ou não).  
  Esses campos permitem identificar de maneira clara se o documento gerou uma duplicata e/ou movimentou o estoque. Uma vez gerado o documento de saída, o conteúdo registrado permanecerá o mesmo nas tabelas independente de alterações da TES cadastrada.
