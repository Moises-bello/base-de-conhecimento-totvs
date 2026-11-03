---
article_id: 360048828513
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f989cb070d8698d26ca34eb293db23f2e63b6ebd36b6955f12d95020c6c1c50e
fetched_at: '2026-06-28T22:38:38.512181+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Edição de campos
  customizados na Liberação de pedidos (MATA440)
type: support-article
updated_at: '2024-01-02T12:59:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048828513-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Edi%C3%A7%C3%A3o-de-campos-customizados-na-Libera%C3%A7%C3%A3o-de-pedidos-MATA440
---

**Dúvida**

Por que alguuns campos customizados na rotina de Liberação de Pedidos (MATA440) ficam como visualização não permitindo editar?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Há campos customizados que, mesmo configurados no SIGACFG como disponíveis para edição, ficam bloqueados em algumas rotinas (disponíveis unicamente para visualização)**.**

Isso ocorre pois determinadas rotinas são exclusivas para processamento de dados, ou seja, não possuem formulário para inserir/alterar dados.  
  
Essas rotinas são preparadas, de modo particular para processamento, portanto somente alguns campos tratados diretamente no fonte da rotina podem ser disponibilizados pra edição, como por exemplo:

Na rotina MATA440 Liberação do Pedido de Venda, somente alguns campos estão disponíveis para alteração e os demais devem ser alterados no próprio Pedido de Venda MATA410.

Uma forma de tratar os campos customizados para edição nessas rotinas é utilizar os Pontos de Entrada:

* [**MTA440AC - Inclusão de campos na liberação do pedido de venda**](https://tdn.totvs.com/x/jYVn)
* [**MTA440C5 - Informar campos a ser alterados**](https://tdn.totvs.com/x/joVn)
