---
content_hash: fe59e4c0785783f90f8561142d6069c5eb354e47c242fc2b2ab3fe9d1e95c45d
fetched_at: '2026-06-29T00:05:53.150928+00:00'
page_id: '1068171435'
product: rm
source: tdn-rm
title: Quadro Comparativo - ANTIGO (NAO PUBLICAR)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068171435
version: 1
---

Após o registro de Orçamento, é preciso clicar na opção "Calcular Quadro Comparativo" para que o sistema realize os cálculos e defina quem foi o vencedor da cotação.  
O quadro comparativo possui as seguintes opções:

|  |  |  |  |
| --- | --- | --- | --- |
|  | **FORNECEDOR** | | |
| Seq: 1 Produto: PRODUTO Quant.Req.: X Quant.Ped.: Y | Quantidade Efetivada | Valor Unitário |  |
| Valor Desconto | Valor Calculado\*\* | Valor IPI |
| Valor Total Negociado | Valor Negociado | Diferença ICMS |
| Valor Desconto Negociado | Valor Calculado | Valor IPI |
| Eficiência Oferta |  | 100 |
| Eficiência Negociada | Valor Homogenizado | 100 |
| **Valor Total Negociado** |  |  | 100 |
| **Valor Total Melhor Oferta** |  |  |  |
| **Valor Total Equalizado** |  |  |  |

**Quantidade Efetivada**: Quantidade efetivada do produto na ordem de compras.

**Valor Unitário**:  Valor unitário do produto.

**Valor Desconto**:  Desconto do produto.

**Valor Calculado**: Preço Cotado com desconto e IPI.

**Valor IPI**: Cálculo do IPI = (( Tabela TCITMORCAMENTO -- Campo VALTRB) /100) \*Valor Negociado ou Valor Cotado com o desconto e despesa calculada.

**Valor Total Negociado**: Valor Desconto Negociado \* Quantidade

**Valor Negociado**: Valor negociado informado pelo processo de registrar negociação.

**Valor Calculado**: Preço Negociado com desconto e IPI.

**Diferença ICMS**:

* Calcula a diferença do valor de ICMS em relação ao ICMS interna ao Estado que estamos.
* Caso a cotação esteja informado para Creditar ICMS (TCCOTACAO - CreditarICMS) o percentual da alíquota é diminuída do valor Homogeneizado. Caso contrário é somado.
* Se o parâmetro USAICMSITMORC da cotação estiver marcado a diferença é calculada através do valor informado em TCITMORCAMENTO - PERCICMSITMORC, caso contrário será usado o valor informado em TCORCAMENTO - VALTRB.

**Valor Desconto Negociado**:  Valor do desconto negociado pelo fornecedor

**Valor IPI**:  Cálculo do IPI = (( Tabela TCITMORCAMENTO -- Campo VALTRB) /100) \*Valor Negociado ou Valor Cotado com o desconto e despesa calculada.

**Eficiência Oferta**:  ((((Último preço cotado \* quantidade requisitada) - (Vl.Unit. c/ IPI \* quantidade requisitada)) / (Último preço cotado \* quantidade requisitada)) \* 100)

**Eficiência Negociada**:

Total da compra = Preço negociado \* Quantidade requisitada  
Total com base no último preço cotado = Total última compra \* Quantidade requisitada

Se "Total com base no último preço cotado" for menor que "Total da compra" então  
(((Total com base no último preço cotado) - (Total da compra)) / (Total com base no último preço cotado)) \* 100  
Se não  
(((Total com base no último preço cotado) / (Total da compra)) - 1) \* 100

**Valor Homogenizado**: Valor que define quem foi o vencedor da Cotação

* Se foi informado na cotação para Creditar IPI o valor do IPI é diminuído do valor homogeneizado, caso contrário será somado.
* Se a cotação usar valor frete (USAVALORFRETE), o cálculo do Valor Homogeneizado é:

((Valor Equalizado +/- IPI) + (Frete Rateado) + (Despesa Rateada) - (Desconto Rateado)) \* Diferença ICMS \* Diferença ICMSST   
Senão:  
((Valor Equalizado +/- IPI) + (Valor Equalizado \* (VALFRETE /100) )+(Despesa Rateada) - (DescontoRateado)) \* Diferença ICMS \*Diferença ICMSST  
  
***Obsevação***: O valor do campo VALFRETE é buscado da tabela FCFO caso esteja nulo é buscado da TCParametros.

* O frete rateado é calculado somente se o parâmetro USAVALORFRETE estiver marcado. Frete Rateado = (Valor Equalizado / Valor Total CFO) \* ValorFrete
* O desconto rateado é calculado somente se o parâmetro USADESCORC estiver marcado.

Se o desconto for por Porcentagem (PERCVALORDESCORC = true): Desconto Rateado = (Valor Equalizado) \* (Desconto Percentual / 100)   
Senão

* Desconto Rateado = (Valor Equalizado / Valor Total CFO) \* Desconto
* Despesa Rateada = (Valor Equalizado / Valor Total CFO) \* Despesa

**Valor Equalizado**: Calcula o valor Negociado ou Cotado considerando o custo Financeiro e a condição de pagamento. É usada uma função matemática chamada Valor Presente Líquido, onde é passado o Fluxo de Caixa e o custo financeiro. O fluxo de caixa é preenchido de acordo com a condição de pagamento.

* Calcula a diferença do valor de ICMSST em relação ao ICMS interna ao Estado que estamos. O percentual da alíquota é somado do valor Homogeneizado. Se o parâmetro USAICMSITMORC da cotação estiver marcado a diferença é calculada através do valor informado em TCITMORCAMENTO - VALICMSST, caso contrário será usado o valor informado em TCORCAMENTO - VALICMSST.

**Valor total CFO** : É a soma do Valor Equalizado \* Quantidade de todos os itens de um determinado CFO.

100 = Indicador de Melhor Oferta  
100 = Indicador de Melhor Negociação  
100 = Indicador de Fornecedor com melhor oferta

**Marca Negociada**: Se a cotação estiver parametrizada para Usar Marca de Produto, será exibida a Marca Negociada do produto. Ao utilizar a opção CTRL + clique, será apresentada a tela de Itens Detalhados onde serão exibidas a Marca Solicitada e a Marca Negociada na pasta Identificação. Na pasta Últimas Compras será exibida a marca das movimentações do tipo 1.2.XX.
