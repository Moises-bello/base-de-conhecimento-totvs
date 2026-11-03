---
article_id: 34614601965079
category: SIGAACD - Automação e Coleta de Dados
content_hash: 8a1563220853d3b85221d1810028733920280cdc32c2fcea3198a29c76e48b77
fetched_at: '2026-06-28T22:39:12.825869+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Meu Coletor de Dados:
  Separação por Solicitação ao Armazém'
type: support-article
updated_at: '2026-03-05T20:01:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34614601965079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Meu-Coletor-de-Dados-Separa%C3%A7%C3%A3o-por-Solicita%C3%A7%C3%A3o-ao-Armaz%C3%A9m
---

O aplicativo Meu Coletor de Dados permite realizar separações integradas à rotina Ordens de Separação (ACDA100), incluindo uma nova origem chamada Solicitação ao Armazém (CB7\_ORIGEM=4). Para isso, são utilizados os parâmetros MV\_TMCBSA e MV\_MCDCLTE, que habilitam a movimentação interna e a leitura de lote na separação, respectivamente. Mais detalhes estão disponíveis nos links oficiais da TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34614601960343) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como realizar a separação por Solicitação ao Armazém no aplicativo (APP) Meu Coletor de Dados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O App Meu Coletor de Dados tem os seguintes módulos Conferência, Inventário, Separação, Transferência, e Endereçamento.

Esse módulo é integrado com as separações geradas na rotina Ordens de Separação - ACDA100.

Hoje temos as origens: Pedido de Venda, Nota Fiscal de Saída ou Ordem de Produção e foi adicionado uma nova referente a Solicitação ao Armazém (CB7\_ORIGEM = 4), através da qual será possível separar/baixar itens gerados desse solicitação.

Parâmetro validados para essa solução:

[**MV\_TMCBSA**](https://tdn.totvs.com/pages/releaseview.action?pageId=919072787) -> Código de Movimentação - Requisição movimentação interna (SF5), criado pela rotina MATA230.

[**MV\_MCDCLTE**](https://tdn.totvs.com/pages/releaseview.action?pageId=581075184) -> Habilita leitura do lote na separação

Para mais detalhes sobre o processo, acesse:

* [**Meu Coletor de Dados: Separação**](https://tdn.totvs.com/x/I83HNg)

Duvidas: 

1. **O sistema orientará o operador na busca do lote e do endereço para separação?**

   R: Ao configurar os parâmetros [**MV\_MCDCLTE**](https://tdn.totvs.com/pages/releaseview.action?pageId=581075184) e o [**MV\_TMCBSA**](https://tdn.totvs.com/pages/releaseview.action?pageId=919072787)com o tipo do TM de requisição e habilitar o controlo do lote no aplicativo, é informado manualmente pelo cliente o Lote e o Endereço que deseja utilizar na Ordem de Separação por Solicitação ao Armazém.
2. **Quero saber se é usado o mesmo comportamento usado para ordens de separação por OPs e PVs quando temos controle de lote e endereço, o sistema respeita o FIFO e a LOCALIZAÇÃO para indicar a posição do item a ser separado pelo usuário.**

    R: Sim é usado o mesmo comportamento, você manualmente seleciona o Lote e a Localização no Aplicativo.

Saiba mais:

[Configuração do REST Mobile](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043179314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configura%C3%A7%C3%A3o-do-REST-Mobile)  
[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
