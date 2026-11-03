---
content_hash: af89ba42f162c936ab95e18e75bc4e5655d63dff1ecada987315925278cbf050
fetched_at: '2026-06-29T00:09:28.687423+00:00'
page_id: '423938752'
product: rm
source: tdn-rm
title: Solucionador Financeiro Simples 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938752
version: 9
---

Utilizado como facilitador no preenchimento e cálculo do item de contrato APENAS para o tipo PERIÓDICO. Os cálculos são aplicados de acordo com as funções financeiras de Valor Presente, Valor Futuro, Pagamento e Taxas.  
Abaixo, material extraído do site contendo a memória de cálculo destas funções financeiras:

Memória de Cálculo

* [Função VP](https://support.office.com/pt-br/article/vp-fun%C3%A7%C3%A3o-vp-23879d31-0e02-4321-be01-da16e8168cbd?ui=pt-BR&rs=pt-BR&ad=BR)
* [Função VP](https://support.office.com/pt-br/article/vf-fun%C3%A7%C3%A3o-vf-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3?ui=pt-BR&rs=pt-BR&ad=BR)
* [Função PGTO](https://support.office.com/pt-br/article/pgto-fun%C3%A7%C3%A3o-pgto-0214da64-9a63-4996-bc20-214433fa6441?ui=pt-BR&rs=pt-BR&ad=BR)
* [Função Taxa](https://support.office.com/pt-br/article/pgto-fun%C3%A7%C3%A3o-pgto-0214da64-9a63-4996-bc20-214433fa6441?ui=pt-BR&rs=pt-BR&ad=BR)

\***Sintaxe**: VP(taxa, nper, pgto, \[vf\], \[tipo\])\* A sintaxe da função VP tem os seguintes argumentos:

\***Taxa**: {\*}Necessário. A taxa de juros por período. Por exemplo, se você tiver um empréstimo para um automóvel com taxa de de juros de 10% ano ano e fizer pagamentos mensais, sua taxa de juros mensal será de 10%/12 ou 0,83%. Você deveria inserir 10%/12 ou 0,83%, ou 0,0083, na fórmula como taxa.

\***Nper**: {\*}Necessário. O número total de períodos de pagamento em uma anuidade. Por exemplo, se você conseguir um empréstimo de carro de quatro anos e fizer pagamentos mensais, seu empréstimo terá 4\*12 (ou 48) períodos. Você deveria inserir 48 na fórmula para nper.

\***Pgto**: {\*}Necessário. O pagamento feito em cada período e não pode mudar durante a vigência da anuidade. Geralmente, pgto inclui o principal e os juros e nenhuma outra taxa ou tributo. Por exemplo, os pagamentos mensais de R$ 10.000 de um empréstimo de quatro anos para um carro serão de R$ 263,33. Você deveria inserir -263,33 na fórmula como pgto. Se pgto for omitido, você deverá incluir o argumento vf.

\***Vf**: {\*}Opcional. O valor futuro, ou o saldo, que você deseja obter depois do último pagamento. Se vf for omitido, será considerado 0 (o valor futuro de um empréstimo, por exemplo, é 0). Por exemplo, se você deseja economizar R$ 50.000 para pagar um projeto especial em 18 anos, então o valor futuro será de R$ 50.000. Você poderia então fazer uma estimativa conservadora na taxa de juros e concluir quanto economizaria por mês. Se vf for omitido, você deverá incluir o argumento pgto.

\***Tipo**: {\*}Opcional. O número 0 ou 1 e indica as datas de vencimento.

\***VP** - Valor Presente (Função VP):{\*} VP, uma das funções financeiras, calcula o valor presente de um empréstimo ou investimento com base em uma taxa de juros constante. Você pode usar VP com pagamentos periódicos e constantes (como uma hipoteca ou outro empréstimo) ou um valor futuro que é sua meta de investimento.

\***VF** - Valor Futuro (Função VF): {\*}VF, uma das funções financeiras, calcula o valor futuro de um investimento com base em uma taxa de juros constante. Você pode usar VF com pagamentos periódicos e constantes ou um pagamento de quantia única.   
   
\***PGTO** (Função PGTO): {\*}PMT, uma das funções financeiras, calcula o pagamento de um empréstimo de acordo com pagamentos constantes e com uma taxa de juros constante.   
   
\***TAXA** (Função TAXA): {\*}Retorna a taxa de juros por período de uma anuidade. TAXA é calculado por iteração e pode ter zero ou mais soluções. Se os resultados sucessivos de TAXA não convergirem para 0,0000001 depois de 20 iterações, TAXA retornará o valor de erro #NÚM!.
