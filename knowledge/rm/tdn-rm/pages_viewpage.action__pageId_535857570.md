---
content_hash: ebe3860e522389ff3d9919d9dd63dfe33ac8ec2ef3e264c331f8e2acb6c30c90
fetched_at: '2026-06-29T00:10:37.112929+00:00'
page_id: '535857570'
product: rm
source: tdn-rm
title: Código de Cálculo 432 - BASE TRIBUTADA DE INSS 13º PRIMEIRA FAIXA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535857570
version: 7
---

Evento tipo base, valor.  
Este evento é calculado caso o sistema esta com o parâmetro 'Calcula INSS conforme eSocial' estiver marcado em Configuração | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral.  
   
Quando o funcionário utiliza o cálculo de INSS conforme o eSocial,  e é calculada a base de INSS de 13º salário pode ser lançado o evento de código de calculo 432  com o valor da base que foi usada para fazer o cálculo de INSS de 13º salário. 

**Exemplo:**

 Coligada 1:  R$1000,00 

 Coligada 2:  R$1000,00 

 **Tabela de INSS:**

Até  R$1045,00 - 7,5%

Até  R$2089 ,60 - 9%

Até  R$3134,40 - 12% 

Até  R$6101,06 - 14% 

O cálculo ocorrerá da seguinte forma:

Ao lançar o evento de 13º salário para a **coligada 1**, será lançado o evento de código de calculo 432 que será a base para o cálculo do evento de INSS 13º salário código de calculo 103 aplicando a alíquota de 7,5 % encontrando o valor de R$75,00.

Ao lançar o movimento para **coligada 2**, será lançado o evento de código de calculo 432 com o valor de R$45,00 que é (R$1045,00 - R$1000,00) que será a primeira base para o cálculo do evento de INSS 13º código de calculo 103 aplicando a alíquota de 7,5 % = R$3.37. Será lançado também o evento código de calculo 433 Base Tributada de INSS 13º salario segunda faixa, neste evento será lançado o restante a ser tributado na segunda faixa. O sistema considera o total da base dos dois vínculos = R$2000,00, deste valor retiramos o que já foi tributado na primeira faixa, ( R$2000,00-  R$1045,00)= R$955,00 e aplicamos a alíquota de 9%= R$85,95

Sendo descontado na **coligada 2** o valor de INSS 13º salário de R$3,37+ R$85,95= R$89,32

FIQUE ATENTO!

Para que a folha de pagamento realize o cálculo corretamente dos descontos de INSS de múltiplos vínculos em coligadas diferentes, é imprescindível respeitar a ordem para o cálculo. **Exemplo:** Empregador 1 deverá realizar o lançamento e calcular todos os valores referentes ao pagamento do seu vínculo para aquela competência, apenas após esse processo, o Empregador 2 poderá dar o início aos seus lançamentos e cálculos. Caso seja necessário realizar alterações no Empregador 1, sugerimos que seja feito o cancelamento dos lançamentos e feitos novamente na ordem que deseja enviar as informações ao governo.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
