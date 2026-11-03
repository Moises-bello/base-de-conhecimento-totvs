---
article_id: 1500005086241
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 0df198e83d91cc5c89cca7e02a0c7489d9254e33bfa6c4c877626ab53a5b1121
fetched_at: '2026-06-28T22:38:53.910080+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como alterar o tipo
  de controle de rastreabilidade de Lote para Sub-lote?
type: support-article
updated_at: '2025-12-15T18:08:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005086241-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-alterar-o-tipo-de-controle-de-rastreabilidade-de-Lote-para-Sub-lote
---

O ajuste para alterar o controle de rastreabilidade de Lote para Sublote no Protheus pode ser feito copiando o código do produto para um novo código com controle por Sublote ativado. Se não for possível, é necessário zerar o saldo em todos os lotes via Inventário, realizar o Fechamento de Estoque (MATA280) e depois alterar o campo B1\_RASTRO na rotina MATA010.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37035865500439)****Tempo aproximado para leitura:****00:01:45 min**

**Dúvida**

Possuo produtos com controle de rastreabilidade (B1\_RASTRO) por Lote, porém preciso alterar para controlar Sublote. Como fazer este ajuste no Protheus?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

**Observações importantes:**Para esse cenário o mais adequado, para manter a integridade dos registros de movimentações existentes é efetuar a **C****ópia do Código do Produto** para um **Novo Código de Produto** definindo que esse **Novo Código inicie controlando Sublote (B1\_RASTRO=S)**, dessa forma o produto inicia com o conceito de rastreabilidade por Sublote.

**Caso não possa efetuar o procedimento acima**, realize os seguintes passos para a mudança de controle de Lote para Sublote:

**- 1 -** Zerar o saldo do produto em todos os Lotes existentes (normalmente feito por meio do [**Inventário**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049739614-MP-SIGAEST-MATA340-Processo-padr%C3%A3o-para-Inventariar-produtos-no-Estoque#:~:text=MP%20%2D%20SIGAEST%20%2D%20MATA340%20%2D%20Processo%20padr%C3%A3o%20para%20Inventariar%20produtos%20no%20Estoque,-Atualizado%20em%3A&text=O%20Invent%C3%A1rio%20%C3%A9%20a%20forma,os%20saldos%20fornecidos%20pelo%20sistema.));

**- 2 -** Efetuar o processo de Fechamento de Estoque (MATA038);

**- 3 -** Logo após o Fechamento, acessar à rotina MATA010 e alterar o produto desejado no campo **B1\_RASTRO** de **Lote** para **Sublote**.

A partir dos próximos movimentos que serão considerados os registros com Controle por Sublote.

**Saiba mais:**

[MP - SIGAEST - MATA010 - Erro ao alterar o tipo de controle de Rastreabilidade de Lote para Sub-lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005178162)

[SIGAEST - Como ativar o controle de Lote/Rastro para produtos com saldo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020672612-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-ativar-o-controle-de-Lote-Rastro-para-produtos-com-saldo)

[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
