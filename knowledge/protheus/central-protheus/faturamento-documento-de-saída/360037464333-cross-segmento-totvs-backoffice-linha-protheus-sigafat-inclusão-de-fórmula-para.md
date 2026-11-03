---
article_id: 360037464333
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 5f4475af8527b0602a3d411fb01f8b7b7f27cc5c7774c9ea558c8602c3cc45af
fetched_at: '2026-06-28T22:38:43.826839+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  Inclusão de
  Fórmula para exibir na Mensagem na Nota Fiscal de Saída
type: support-article
updated_at: '2025-11-19T20:57:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037464333-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Inclus%C3%A3o-de-F%C3%B3rmula-para-exibir-na-Mensagem-na-Nota-Fiscal-de-Sa%C3%ADda
---

**Dúvida**

 Como incluir uma Fórmula para Mensagem na Nota Fiscal de saída?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**Para solucionar essa dúvida, cadastre uma fórmula com a informação desejada para ir automaticamente para a nota fiscal.

1. Atualizações > Cadastros > Formulas;  
2. Inserir ou Alterar;  
3. Em caso de inclusão a formula deve ser cadastrada entre aspas no campo Formula.

![formula.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049245653/formula.gif)

4. Em pedido de vendas, incluir a fórmula no campo C5\_MENPAD.

5 .Após faturar, o sistema levará a informação para Danfe, desde que o XML esteja configurado para a receber a informação do campo C5\_MENPAD.

**Obs..O atendimento a dúvidas do cadastro de fórmula e de reponsabilidade da equipe que atende a tabela  qual a fórmula estiver se relacionando.**

Exemplo: Se formula se relacionar com a tabela SC5- Pedido de Vendas, a equipe de atendimento será Faturamento e CRM, caso a tabela  seja SF4- TES, a equipe de atendimento será Escrita Fiscal, e assim sucessivamente.

**Outros assunto relacionados a Cadastro de Fórmulas:** [Fórmulas - CFGX019](https://tdn.totvs.com/pages/viewpage.action?pageId=344478428)
