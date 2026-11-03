---
article_id: 360022576132
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d331ed4d29e978f026ac8d6919c92ea200a8d60423a66eb69ddf39a0276c696f
fetched_at: '2026-06-28T22:37:20.138277+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os campos a serem
  considerados no ajuste de casas decimais das tabelas do Gestão de Contratos ?
type: support-article
updated_at: '2026-06-02T11:04:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022576132-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-os-campos-a-serem-considerados-no-ajuste-de-casas-decimais-das-tabelas-do-Gest%C3%A3o-de-Contratos
---

**Dúvida**

Quais os campos a serem considerados no ajuste de casas decimais das tabelas do Gestão de Contratos ?

**Ambiente**

Microsiga Protheus – Gestão de Contratos – A partir da versão 11.80

**Solução**

Quando considera-se a alteração de casas decimais no módulo de Gestão de Contratos, é preciso prever todos os campos a serem ajustados, afim de evitar-se problemas futuros.

Abaixo, segue links de documentação onde os campos são listados:

* [Alteração de Casas Decimais para maior precisão nos Cálculos de Contratos - Quantidade](http://tdn.totvs.com/display/public/PROT/GCT0016_Quantidade_Casas+Decimais_Contrato_GCT)
* [Alteração de Casas Decimais para maior precisão nos Cálculos de Contratos - Valor](http://tdn.totvs.com/display/public/PROT/GCT0017_Valor_Casas+Decimais_Contrato_GCT)

***Obs:***

O parâmetro **MV\_ARREFAT** influencia o arredondamento de casas decimais não apenas nos processos de Faturamento, mas também na geração de Pedidos de Compras e Vendas, assim como nos Títulos a Pagar e a Receber.

Portanto, no caso da utilização de mais casas decimais nos processos da empresa, é aconselhável habilitar o parâmetro **MV\_ARREFAT** (**defini-lo como 'S'**).

***Obs2:***

No uso de mais casas decimais para geração de Pedido de Compras, recomenda-se também a avaliação interna e, se necessário, a utitilzação do parâmetro "**MV\_ARRPEDC = ROUND**".

***Saiba Mais:***

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)

[FAT0068 Aumento de Casas Decimais no ambiente Faturamento (SIGAFAT)](https://tdn.totvs.com/x/twEmDg)
