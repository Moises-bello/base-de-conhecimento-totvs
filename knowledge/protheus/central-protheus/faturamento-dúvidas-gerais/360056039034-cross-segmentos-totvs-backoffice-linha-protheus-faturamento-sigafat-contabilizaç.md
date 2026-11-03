---
article_id: 360056039034
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: c8c6731033e167addc553c2aacded27fdddfa262a629d7a6e048bdad5125fed6
fetched_at: '2026-06-28T22:38:29.903008+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT)
  - Contabilização no Modulo Faturamento Protheus
type: support-article
updated_at: '2024-12-26T17:57:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056039034-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Contabiliza%C3%A7%C3%A3o-no-Modulo-Faturamento-Protheus
---

**Dúvida**

Como configurar (efetuar) a contabilização no módulo Faturamento Protheus?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - todas as versões  
  
**Solução**

A contabilização no módulo faturamento pode ser efetuada:

* **Pedido de Vendas** - para contabilizar valores relacionado ao cabeçalho do pedido (SC5) ou ao item do pedido (SC6);
* **Nota Fiscal de Saída** -  podendo contabilizar no momento da geração da nota (contabilização on line) ou posteriormente (contabilização off line) em miscelâneas, fechamento, contabilização off line de documento de saída.

A contabilização requer um lançamento específico para cada situação, no pedido podem ser utilizados os seguintes Lp´s: ***611, 612, 613, 614, 621, 632 e 636.***

O Lp´s  para contabilização da nota de saída podem ser utilizados: ***610, 620 ,630 e 635***.

Para tratar custo na saída, compartilhamos o mesmo lançamento do estoque para custo médio, ***LP678***.

Atenção: Para que o custo na saída seja contabilizado, o campo **D2\_CUSTO**(1 a 5) precisa conter informações, se a nota não tiver movimentação de estoque , o que é determinado pelo TES de saída, não haverá informações de custo no campo em questão.

Nesse caso, se há necessidade contabilizar custo na saída e este não é gerado por que não há movimentação de Estoque, avalie a documentação: **[MP - FAT - Atualização do campo D2\_CUSTO1 ao utilizar TES que não atualiza estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021429372-MP-FAT-Atualiza%C3%A7%C3%A3o-do-campo-D2-CUSTO1-ao-utilizar-TES-que-n%C3%A3o-atualiza-estoque)**

Obs: **O cadastro de Lançamento Padrão é desenvolvido pelo departamento contábil de sua empresa juntamente com um analista programador em campo, o suporte não auxilia por tratar de regras específicas de cada empresa.**

Para as configurações do módulo Contábil e  exemplos dos LP´s, acesse a documentação completa:

**[Integração Faturamento X SigaCtb (SIGAFAT)](https://tdn.totvs.com/x/W2nXIQ)  
[Como incluir ou alterar linhas na contabilização no Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007173901-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-incluir-ou-alterar-linhas-na-contabiliza%C3%A7%C3%A3o-no-Faturamento)**
