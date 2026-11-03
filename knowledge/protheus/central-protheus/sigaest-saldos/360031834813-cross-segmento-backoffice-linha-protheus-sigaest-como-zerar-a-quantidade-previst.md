---
article_id: 360031834813
category: SIGAEST - SALDOS
content_hash: 8e011158dea007e1938aef2b8b85578a4c358686ea62a2bfef2053a3b4167370
fetched_at: '2026-06-28T22:39:14.815833+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como zerar a Quantidade
  Prevista de um produto (B2_SALPEDI)?
type: support-article
updated_at: '2022-08-11T14:31:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031834813-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-zerar-a-Quantidade-Prevista-de-um-produto-B2-SALPEDI
---

**Dúvida**  
Como zerar a quantidade prevista de um determinado produto (B2\_SALPEDI) no *Protheus*?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todos os Módulos - Todas as versões  
  
  
**Solução**  
Para zerar o campo **B2\_SALPEDI** - que se refere à **Entrada Prevista**  - deverá inicialmente verificar os movimentos existentes no ambiente para o respectivo produto.  
  
Os movimentos que geram esta entrada prevista são: **Ordem de Produção** em aberto, **Solicitação de Compras** em aberto e **Pedido de compras** em aberto.  
  
Desta forma, após verificações descritas acima, é necessário:

- Para a Ordem de Produção: apontar a mesma ou excluir a Ordem de Produção;

- Para o Pedido de Compras: vincular em uma pré-nota ou diretamente no Documento de Entrada (MATA103) ou excluir o Pedido de Compras;

- Para a Solicitação de Compras: vincular em uma cotação fazendo todo o processo de analise, geração do Pedido de Compras e vinculo deste pedido no Documento de Entrada ou pré-nota ou poderá simplesmente excluir a Solicitação de Compras.

Caso não tenha movimentos pendentes, mas identifique que o campo B2\_SALPEDI possui quantidades, é necessário executar a rotina **R****efaz Acumulados** -**MATA215**, que fará a checagem dos movimentos e limpará o campo caso não haja movimentos de entrada prevista.

**Saiba mais:**

*[Clique aqui para mais artigos sobre Saldos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)*
