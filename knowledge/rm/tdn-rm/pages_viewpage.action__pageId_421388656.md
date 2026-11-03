---
content_hash: 59da90d63eb4fc65ab11f25d993ad49e8384d40165cd8072560b19ff778267a9
fetched_at: '2026-06-29T00:09:18.044549+00:00'
page_id: '421388656'
product: rm
source: tdn-rm
title: Valores de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388656
version: 8
---

Os valores de Integração estão disponíveis no produto Totvs Imobiliário - TIN do segmento Construção e Projetos da Linha RM, o Gestão Financeira irá interpretá-los na Baixa, conforme a ação (Acrescentar ou Descontar) definida na origem.   
 Os valores de Integração são cadastrados no  [Componente](http://tdn.totvs.com/x/Ji3vGQ) através do Menu: Cadastros | Itens de Geração do Plano Financiamento | Valores de Integração.

São definidas a ação e a ordem para que os valores sejam considerados na baixa pelo TOTVS Gestão Financeira.  
Exemplo:

|  |  |  |
| --- | --- | --- |
| VALORES DE INTEGRAÇÃO | AÇÃO | ORDEM |
| Sinal | nada | 1 |
| Mensal | nada | 2 |
| Taxa de Juros Após Entrega | Acrescentar | 3 |
| CM após entrega | Acrescentar | 4 |

Considerando esta ordem ao baixar um Lançamento proveniente do Totvs Imobiliário pelo Totvs Gestão Financeira:

1 - Os valores de integração Sinal, Mensal não exercerão nenhuma influência no cálculo do Valor Líquido.

2 - Ao Baixar o Lançamento, os valores serão apropriados segundo uma ordem definida internamente pelo Gestão Financeira, conforme segue:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1º. Retenções | 2º  Ordem dos valores a descontar | 3º.  Ordem dos valores a acrescentar | Valor restante | Observação |
| Considera os valores das retenções  calculadas no item da baixa | * Valor IRRF * Valor INSS * Valor SEST/SENAT * Devoluções * Notas de Crédito * Adiantamentos * Desconto * Valores opcionais a descontar * Valores de integração a descontar (na ordem parametrizada) | * Juros * Multa * Capitalização * Juros Vendor * Valores opcionais a acrescentar * Valores de integração a acrescentar (na ordem parametrizada) * Valor Original | Valor Restante =      Valor Baixado   + Retenções calculadas   + Valores a descontar       Enquanto não chegar a zero:  Valor Restante  =  Valor Restante - Valores a acrescentar  Um valor a acrescentar poderá ser utilizado parcialmente em uma baixa. | No Modo de cálculo por Prioridade, esse tratamento ocorre na **primeira baixa** do Lançamento desde que o valor baixado seja suficiente para absorvê-los.  No modo de cálculo proporcionalização, serão tratados **proporcionalmente ao valor baixado.**Exemplo: Se for baixado 30% do liquido, na baixa serão considerados 30% sobre cada valor que afete o líquido. |

**OBSERVAÇÕES**

1 . Se  um Lançamento for baixado parcialmente utilizando o modo de  Cálculos na Baixa por Prioridade, o restante da baixa será por este modo, mesmo que o parâmetro tenha sido alterado para o modo de Cálculos na Baixa por Proporcionalidade, e vice-versa. Na primeira baixa do lançamento, o campo MODOCALCULOBX será atualizado, sendo:  
 0 = Prioridade

1=  Proporcionalidade - Desejando alterar o modo de cálculo é necessário cancelar todas as baixas do Lançamento.

2. Se forem utilizados vários meios de pagamento na baixa do Lançamento, os valores que afetam o valor líquido serão rateados por meio de pagamento. Os valores de integração serão visualizados somente na edição do item correspondente a baixa do lançamento.

Veja Também

* [Ordem dos Valores de Integração](http://tdn.totvs.com/x/2SvvGQ)
