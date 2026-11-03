---
content_hash: afa908a867956f949540ac02431b88b348ce02dfe9c2e98a1269d0cb426b054b
fetched_at: '2026-06-29T00:09:23.879492+00:00'
page_id: '422546148'
product: rm
source: tdn-rm
title: Tributação 60 - ICMS Cobrado Anteriormente por Substituição Tributária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546148
version: 3
---

Para produtos que tem como tipo de ICMS igual 60 em movimento de saída, será realizado o calculo do valor unitário da Base de calculo e do Valor do Imposto do ICMS-ST referente a o último movimento de entrada que tenha ICMS ST e que controle saldo de estoque.  
    
 **1. Abaixo exemplo quando a unidade de entrada é diferente da de saída**

**Entrada**

|  |  |
| --- | --- |
| Unidade | Caixa (com 12 unidades) |
| Quantidade de compra | 50 |
| Valor unitário | 6,00 |
| Base do ICMS ST entrada | 300,00 (6,00² \* 50¹) |
| Valor do ICMS ST entrada | 15,00 (300³ \* 5%) |
| Base do ICMS ST unitária | 6,00 (300³ / 50¹) |
| Valor do ICMS ST unitário | 0,30 (15⁴ /50¹) |

**Onde:**

¹Quantidade de compra  
²Valor unitário  
³Base do ICMS ST entrada  
 ⁴Valor do ICMS ST entrada

**Saída**

|  |  |
| --- | --- |
| Unidade | Unidade |
| Fator de Conversão | 12 |
| Quantidade de saída | 4 |
| Base ICMS ST unitária da saída | 0,5 (6¹ / 12²) |
| Valor ICMS ST unitário da saída | 0,025 (0,3³ / 12²) |
| Base ICMS ST da saída | 2,00 (4⁴ \* 0,5⁵) |
| Valor ICMS ST da saída | 0,1 (4⁴ \* 0,025⁶) |

**Onde:**

¹Base do ICMS ST unitária   
²Fator de Conversão  
³Valor ICMS ST unitário  
 ⁴Quantidade de Saída  
 ⁵Base ICMS ST unitária da saída  
 ⁶Valor ICMS ST unitário da saída**.**

**2. Comportamento da saída quando a unidade é a mesma da entrada**  
 Considerando o mesmo exemplo de entrada acima sem fator de conversão, os valores da saída serão os seguintes:  
**Saída**

|  |  |
| --- | --- |
| Unidade | Unidade |
| Quantidade de saída | 4 |
| Valor unitário | 6,00 |
| Base ICMS ST da saída | 24,00 (4¹ \* 6²) |
| Valor ICMS ST da saída | 1,2 (0,3³ \* 4¹) |

**Onde:**  
 ¹Quantidade de saída  
²Valor unitário  
³Valor ICMS ST unitário da entrada

***Importante:*** O TOTVS Gestão de Compras e Faturamento somente irá realizar esse recálculo se a base de calculo se o tributo ICMS-ST **não for editado**.

É obrigatório que na tributação do Item seja incluído o tributo ICMS e o ICMS-ST onde deve ser informando somente a base de calculo do ICMS com sua alíquota e valor com **valores igual a 0**, conforme legislação vigente da NF-e.  
 Ao realizar esse processo, será incluído na tag de Informações Complementares de interesse do Contribuinte (infCpl) as informações referentes ao ICMS 60. Conforme exemplo abaixo:  
 <infCpl>  
 Informacoes da saida ST 60 (Produto - Base ICMS ST - Valor ICMS ST) : 02.04- 520 - 62,40|02.05- 3900 -  468|02.06- 260 - 31,20|  
 </infCpl>

***Observação*:**Não existe vinculo entre os Movimentos e não é realizado o controle de estoque por Substituição Tributária.  
 Ao escriturar o movimento os lançamentos não podem ser recalculados para que os valores não sejam alterados.
