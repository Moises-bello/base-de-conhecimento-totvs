---
content_hash: a3fdb394d12e5090b3cc42bd2a1ce20acb396d1e22af85494768c8b1e3d1c1d7
fetched_at: '2026-06-29T00:10:37.093252+00:00'
page_id: '535857540'
product: rm
source: tdn-rm
title: Código de Cálculo 428 - BASE TRIBUTADA DE INSS FOLHA PRIMEIRA FAIXA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535857540
version: 8
---

Evento tipo base, valor.

Este evento é calculado quando o parâmetro 'Calcula INSS conforme eSocial' estiver marcado em Configuração | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral.

Quando o funcionário utiliza o cálculo de INSS conforme o eSocial, este evento é lançado no movimento como base para tributação do percentual de 7,5% .

 **Exemplo:**

 Coligada 1 :R$1000,00 

 Coligada 2 :R$1000,00 

 **Tabela de INSS:**

Até   R$1045,00 - 7,5%

Até   R$2089 ,60 - 9%

Até   R$3134,40 - 12% 

Até   R$6101,06 - 14% 

O cálculo ocorrerá da seguinte forma:

Ao lançar o movimento para a **coligada 1**, será lançado o evento de código de calculo 428, que será a base para o cálculo do evento de INSS código de calculo 3, aplicando a alíquota de 7,5 % encontrando o valor de R$75,00.

Ao lançar o movimento para **coligada 2**, será lançado o evento de código de calculo 428 com o valor de 45,00 que é (R$1045,00- R$1000,00), que será a primeira base para o cálculo do evento de INSS código de calculo 3, aplicando a alíquota de 7,5 % =R$3.37.

Será lançado também o evento código de calculo 429 Base Tributada de INSS Folha segunda faixa e neste evento será lançado o restante a ser tributado na segunda faixa. O sistema considera o total da base dos dois vínculos= R$2000,00, deste valor retiramos o que já foi tributado na primeira faixa, ( R$2000,00-  R$1045,00)= R$955,00 e aplicamos a alíquota de 9%= R$85.95

Sendo descontado na coligada 2 o total de  R$3,37+ R$85,95=  R$89,32

FIQUE ATENTO!

Para que a folha de pagamento realize o cálculo corretamente dos descontos de INSS de múltiplos vínculos em coligadas diferentes, é imprescindível respeitar a ordem para o cálculo. **Exemplo:** Empregador 1 deverá realizar o lançamento e calcular todos os valores referentes ao pagamento do seu vínculo para aquela competência, apenas após esse processo, o Empregador 2 poderá dar o início aos seus lançamentos e cálculos. Caso seja necessário realizar alterações no Empregador 1, sugerimos que seja feito o cancelamento dos lançamentos e feitos novamente na ordem que deseja enviar as informações ao governo.

 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
