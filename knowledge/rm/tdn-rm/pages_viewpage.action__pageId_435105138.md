---
content_hash: 96dceddb320e9a5cd9e994db63c632f10589bb110eddb43942ffbdfec51794e9
fetched_at: '2026-06-29T00:09:48.382755+00:00'
page_id: '435105138'
product: rm
source: tdn-rm
title: Lançamento Financeiro - Cálculo de Deságio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105138
version: 6
---

Com a necessidade de saber a qualquer tempo, o saldo devedor de uma parcela para quitação, em Modelos PRICE e SAC, foi criado um processo de deságio utilizando a integração com o módulo Financeiro. Dessa forma é possível saber o valor correto de uma fatura caso ela for paga de forma adiantada ou até mesmo quitar um contrato antes do vencimento final, assim sabendo o valor de cada parcela com o valor de reajuste monetário e o desconto calculado.

Esse processo é possível de ser executado na versão de revitalização do TIN. O cálculo do desconto será apenas realizado para modelos de cálculo pré-fixados como o PRICE e o SAC.

**Funcionamento** O cálculo para o desconto utilizado é o de Valor Presente Meses (Sendo o mesmo utilizado no aditivo de alteração de vencimento), que verifica se houve mudança de mês entre a data de pagamento (Baixa) e a data de vencimento e assim aplicar o percentual de desconto no cálculo.

Para utilizar o cálculo de Deságio, é necessário habilitar o Reajuste Online, que é um parâmetro do módulo Financeiro. Assim que habilitado, o parâmetro de deságio pode ser ativado no TIN, que criará (Se não existir) um componente do tipo Desconto de Juros de Contrato. O Parâmetro chama-se: Tipo de Deságio no Cálculo de Valor Líquido no Financeiro (Reajuste em Memória).

Ao realizar uma baixa financeira, informando uma data de baixa anterior a data de Vencimento do lançamento, automaticamente o deságio é calculado e é incluído na parcela como Valor de Integração o componente de Desconto de Juros. Se cancelada a baixa, então esse desconto é zerado.  
 No anexo de Lançamentos financeiros da Venda, bem abaixo no rodapé do Anexo, possui o campo Data Líquido. Informando uma data neste campo é possível calcular o valor líquido desta parcela. Caso informar uma data anterior, será calculado o valor presente com o deságio. Caso informada uma data futura, serão calculados os juros de Mora e Multa. Além disso a correção monetária também é calculada por causa do reajuste online.

O cálculo de Valor Presente utilizado no deságio funciona da seguinte forma:  
  
***VP*** *= **VF** / (1 + **i** / 100) ^ **n***  
  
 Sendo que:

* ***VF*** = valor futuro (Valor Total da parcela do TIN).
* ***VP*** = valor presente (Valor descapitalizado da parcela do TIN).
* ***n*** = número de meses.
* ***i*** = taxa de juros (em %).

Para mais informações sobre os parâmetros de deságio, acesse o link
