---
content_hash: 0dc1d6cd25956edd16e443ebec9c494cdc59bbecfe936ddcd22561561effac24
fetched_at: '2026-06-29T00:10:37.118271+00:00'
page_id: '535857577'
product: rm
source: tdn-rm
title: Código de Cálculo 433 - BASE TRIBUTADA DE INSS 13º SEGUNDA FAIXA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535857577
version: 9
---

Evento tipo base, valor.  
Este evento é calculado caso o sistema esta com o parâmetro 'Calcula INSS conforme eSocial' estiver marcado em Configuração | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral.  
   
Quando o funcionário utiliza o cálculo de INSS conforme o eSocial,  e é calculada a base de INSS de 13º salário, pode ser lançado o evento de código de calculo 433 com o valor da base que foi usada para fazer o cálculo de INSS de 13ºsalário. 

 **Exemplo:**

 Coligada 1:  R$1200,00

 Coligada 2:  R$1000,00

 **Tabela de INSS:**

Até  R$1045,00 - 7,5%

Até  R$2089 ,60 - 9%

Até  R$3134,40 - 12% 

Até  R$6101,06 - 14% 

O cálculo ocorrerá da seguinte forma:

Ao lançar o movimento para a **coligada 1**, será lançado o evento de código de calculo 432 no valor de R$1045,00 que será a base para o cálculo do evento de INSS 13 salario código de calculo 103 aplicando a alíquota de 7,5 % encontrando o valor de R$78,37.No código de calculo 432 foi tributado R$1045,00, restando R$155,00( R$1200,00- R$1045,00)  que será lançado no código de calculo 433 para ser tributado na segunda faixa aplicando uma alíquota de 9% encontrando um valor de R$13,95.

Sendo descontado no código de calculo 103 as somas dos valores encontrado após o desconto progressivo  R$78,37+ R$13,95=92,32.  
 

Ao lançar o movimento para **coligada 2**, será lançado o evento de código de calculo 433 com o valor de R$889,60 que é R$1044,60 - R$155,00 ( Valor já tributado na coligada 1).Neste valor será aplicado o percentual de 9% =R$80,06. Será lançado também o evento código de calculo 434 Base Tributada de 13º salario terceira faixa, neste evento será lançado o restante a ser tributado na terceira faixa. O sistema considera o total da base dos dois vínculos =R$2200,00, deste valor retiramos o que já foi tributado na primeira e segunda faixa ( R$2200,00-  R$1045,00 - R$1044,60)= R$110,40 e aplicamos a alíquota de 12%= R$13,24

Sendo descontado no código de calculo 103 as somas dos valores encontrado após o desconto progressivo  R$80,06 + R$13,24= R$93,30  
 

FIQUE ATENTO!

Para que a folha de pagamento realize o cálculo corretamente dos descontos de INSS de múltiplos vínculos em coligadas diferentes, é imprescindível respeitar a ordem para o cálculo. **Exemplo:** Empregador 1 deverá realizar o lançamento e calcular todos os valores referentes ao pagamento do seu vínculo para aquela competência, apenas após esse processo, o Empregador 2 poderá dar o início aos seus lançamentos e cálculos. Caso seja necessário realizar alterações no Empregador 1, sugerimos que seja feito o cancelamento dos lançamentos e feitos novamente na ordem que deseja enviar as informações ao governo.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
