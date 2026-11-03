---
article_id: 360021998271
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e29bb19ec427b5320c37d9bf08e4e97a52ae2e2b8e49dcc0863604b5ee34c1e5
fetched_at: '2026-06-28T22:38:42.372730+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help A410TEMOP
  ao alterar um Pedido de Vendas (MATA410)
type: support-article
updated_at: '2023-02-23T17:16:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021998271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A410TEMOP-ao-alterar-um-Pedido-de-Vendas-MATA410
---

**Ocorrência**

No módulo Faturamento, ao alterar um Pedido de Vendas, o sistema apresenta a mensagem **"A410TEMOP: Este item não pode ser alterado, pois já foi gerada Ordem de Produção"**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

Essa mensagem de validação ocorre porque existe uma Ordem de Produção vinculada ao Pedido de Vendas ([Ordem de Produção x Pedido de Vendas](https://tdn.totvs.com/x/YW52Hw)), porém, o sistema está configurado para não permitir a alteração de um Pedido de Vendas que tenha Ordem de Produção gerada.  
  
**Solução**

Para solucionar essa ocorrência, de forma que o Help não seja mais apresentado, realize os seguintes passos:

1. Acesse o Configurador (SIGACFG) do sistema;  
2. Acesse a área de Parâmetros (CFGX017);  
3. Configure o parâmetro MV\_ALTPVOP com o valor S.

Saiba mais: [**Ordem de Produção x Pedido de Vendas**](https://tdn.totvs.com/x/YW52Hw)
