---
article_id: 360016471032
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0c191502ed4273a61a59d863b215a0cba5b771499c50868ef9a6df4cae76c3ce
fetched_at: '2026-06-28T22:38:38.666572+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Como utilizar
  as formas de pagamento no faturamento
type: support-article
updated_at: '2023-02-22T16:02:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016471032-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-utilizar-as-formas-de-pagamento-no-faturamento
---

**Dúvida**

Como utilizar as formas de pagamento no faturamento?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

O uso da funcionalidade Formas de Pagamento no Pedido de Vendas, se faz da seguinte forma:

A Tabela **SCV** armazena os registros de relacionamento **Pedidos X Formas de Pagamento**. No módulo **Faturamento** > **Pedido de Venda** > **Incluir/Alterar** > **Ações Relacionadas** > **Formas**

Informe, por exemplo, 50% Boleto e 50% Cheque. No campo **CV\_FORMAPG** registrar a forma desejada e em **CV\_RATFOR** o percentual a ser pago por meio desta Forma de Pagamento (que deverá ser "100" caso seja incluída apenas uma Forma). Se precisar amarrar mais de uma Forma ao mesmo Pedido; após selecionar a primeira forma de pagamento, tecla na "seta para baixo" em seu teclado e registre as demais formas, registrando o percentual rateado até completar 100%

**O que o sistema considera para a geração de títulos é a Condição de Pagamento (C5\_CONDPAG).**

**Importante: Uma vez que a forma de pagamento é tratado como um histórico no pedido de venda e não é levado na geração da nota para o título, caso precise desta informação no Título a receber, deve ser utilizado ponto de entrada para isso, podendo ser utilizado o [M460FIM](https://tdn.totvs.com/x/tIRn)**

Saiba mais:**[FAT0105 - Formas de Pagamento no Faturamento](http://tdn.totvs.com/display/public/PROT/FAT0105_Formas+de+Pagamento+no+Faturamento)**
