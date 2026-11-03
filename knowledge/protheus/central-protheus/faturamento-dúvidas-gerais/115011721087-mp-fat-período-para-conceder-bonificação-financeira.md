---
article_id: 115011721087
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: e8946e5f231fc0d22dada37b137cfc90b560409bdee48beb5d477396280a5960
fetched_at: '2026-06-28T22:38:31.097233+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - Período para conceder  Bonificação Financeira
type: support-article
updated_at: '2021-04-28T15:56:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011721087-MP-FAT-Per%C3%ADodo-para-conceder-Bonifica%C3%A7%C3%A3o-Financeira
---

**Dúvida**

Tem como especificar um período que o sistema deva considerar para conceder a Bonificação Financeira ao cliente? Exemplo: se eu determinar a bonificação por trimestre,ao encerrar o ciclo , os valores não serão acumulados para os cálculos de bonificação do trimestre seguinte?

**Ambiente**

Microsiga Protheus - a partir da versão 11.80

**Solução**

Na própria rotina de Bonificação Financeira, na opção **Processar** dentro do ações relacionadas, há os parâmetros para informar (Data de/até), onde será considerado o período que deseja para a geração da bonificação.  
Baseado no exemplo citado, utilizado vendas de dois meses, desta forma, foi fechado o período de 26.06.17 a 26.07.17, onde há 2 pedidos que somados chegam a R$2.000,00, um terceiro pedido de R$ 2.000,00 do período de 26.07.17 e  mais um novo pedido de R$ 2.000,00, também datado de 26.07.18, totalizando R$ 6.000,00, onde a regra de bonificação é para ser validada sobre o valor de r$ 2.000,00.  
Na rotina de bonificação, processar, parametrizando com o período desejado de 26.06.17 a 26.07.17, o sistema gera um único título de 5% do total de R$ 6.000,00.  
Se tentar processar a rotina novamente, será gerado um título substituindo o anterior porém, com o mesmo valor de apuração relacionado aos R$ 6.000,00 do período, não duplicando o valor de bonificação e tratando apenas o período fechado.
