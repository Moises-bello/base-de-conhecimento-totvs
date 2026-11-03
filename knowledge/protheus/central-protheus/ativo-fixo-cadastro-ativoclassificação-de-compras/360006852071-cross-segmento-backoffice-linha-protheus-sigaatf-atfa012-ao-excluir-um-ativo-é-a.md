---
article_id: 360006852071
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: de2c0b9f8ff40c2a78235ca4c76d7d324560be024bd0b26116ffc258ab9bb2f5
fetched_at: '2026-06-28T22:41:48.203715+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -  ATFA012 - Ao excluir
  um ativo é apresentado o Help AF010DEL
type: support-article
updated_at: '2021-12-01T18:26:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006852071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Ao-excluir-um-ativo-%C3%A9-apresentado-o-Help-AF010DEL
---

**Ocorrência**Ao excluir ativo é apresenta help: AF010DEL

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus – Ativo Fixo  Versão a partir 11.8

**Causa**Esta validação ocorre quando ao excluir o cadastro do bem é encontrado na tabela SN4 (tabela de movimento do ativo fixo) movimento de implantação e depreciações, impedindo que seja excluído o bem por questão de segurança

**Solução**

Caso exista  movimentações para este bem (Depreciação, baixa, transferência), deve avaliar a possibilidade de:

- Cancelar as movimentações existentes, assim será permitida a exclusão

- Baixar o bem através da rotina **ATFA036**
