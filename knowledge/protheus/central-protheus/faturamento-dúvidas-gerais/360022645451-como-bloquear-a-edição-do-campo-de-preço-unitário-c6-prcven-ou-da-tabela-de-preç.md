---
article_id: 360022645451
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 55e0cac313260c37b72563474a722266a151b2c395b05701752ba437736a6475
fetched_at: '2026-06-28T22:38:32.709191+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Como bloquear a edição do campo de Preço Unitário (C6_PRCVEN) ou da Tabela
  de Preço (C5_TABELA) no Pedido de Venda?
type: support-article
updated_at: '2025-12-31T11:13:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022645451-Como-bloquear-a-edi%C3%A7%C3%A3o-do-campo-de-Pre%C3%A7o-Unit%C3%A1rio-C6-PRCVEN-ou-da-Tabela-de-Pre%C3%A7o-C5-TABELA-no-Pedido-de-Venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37361257512087)** **Tempo aproximado para leitura:****00:03:00 min**

**Dúvida**

Como bloquear a edição do campo de Preço Unitário (C6\_PRCVEN) ou da Tabela de Preço (C5\_TABELA) no Pedido de Venda?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
  
**Solução**

Existem algumas formas de realizar bloqueio de campos, dependendo da necessidade da sua operação, mas a principal e mais indicada é o **Bloqueio definitivo via Dicionário de Dados (Configurador).**

Este procedimento torna o campo apenas para visualização para todos os usuários:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Base de Dados > Dicionário > Bases de Dados > Dicionário de Dados**;
3. Pesquise a tabela correspondente, exemplo:

   * **SC6** (Itens do Pedido) para o campo `C6_PRCVEN` (Preço Unitário).
   * **SC5** (Cabeçalho do Pedido) para o campo `C5_TABELA` (Tabela de Preço).
4. Clique em **Editar** (ícone do lápis);
5. Localize o campo desejado e clique no ícone de edição;
6. Na aba **Campo**, localize o tópico **Propriedade** e altere para **Visualizar**;
7. Clique em **Confirmar** e salve a alteração;
8. Lembre-se de atualizar o Dicionário de Dados clicando no ícone do disquete (necessário ambiente exclusivo).

Caso a necessidade seja um Bloqueio condicional específico é necessário customizar, o mais indicado para o Pedido de Vendas seria o ponto de entrada, como por exemplo:

[M410LIOK - Validação de linha de pedido](https://tdn.totvs.com/x/lYRn)

[MT410TOK - Validar confirmação da operação](https://tdn.totvs.com/x/YYVn)

[A410TAB - Tabela de preços](https://tdn.totvs.com/x/JYRn)

Demais pontos de entrada da rotina Pedido de Vendas MATA410:

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Pontos de Entrada na rotina "Pedidos de Venda (MATA410)"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7381576110871-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pontos-de-Entrada-na-rotina-Pedidos-de-Venda-MATA410)
