---
article_id: 1500002070661
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8a53c16b1acde62a020a7a0a2b0ab6bece3613822712ae4e468b46f335b80e0e
fetched_at: '2026-06-28T22:38:38.540763+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help: REGNOIS
  ao Preencher o campo Cond.Pagto no Pedido de Venda'
type: support-article
updated_at: '2023-04-20T13:10:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002070661-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-REGNOIS-ao-Preencher-o-campo-Cond-Pagto-no-Pedido-de-Venda
---

**Ocorrência**No módulo Faturamento, ao realizar a inclusão de um Pedido de Venda e preencher o campo Cond.Pagto o sistema apresenta a mensagem:

**"Help: REGNOIS - Problema: Não existe registro relacionado a este código."**  
"**Help: REGNOIS - Problema: Não existe registro relacionado a chave informada no alias SE4, ordenação 1.**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

Esse incidente ocorre, pois foi realizada a inclusão da Condição de Pagamento e Tabela de Preço no Cadastro do Cliente, e na inclusão do Pedido de Venda está sendo informado outro código de Cond.Pagto.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103033413/mceclip0.png)![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100869214/mceclip1.png)  
  
**Solução**Para ajustar essa ocorrência, realize os seguintes passos:  
1. Caso seja mesma estas informações, manter a Cond.Pagto e Tabela de Preço que está cadastrado no Cliente;  
2. Caso queria alterar a condição e tabela para o pedido de venda, teria que acessar o cadastro deste Cliente, e alterar estas informações ou retirar elas do cadastro do Cliente, para que possa selecionar qualquer dado no Pedido de Venda;

Documentação Complementar:

[Explicativo sobre os tipos de condições de pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=240310845)

[Tabelas de Preços (OMSA010 - SIGAFAT)](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=357601934)
