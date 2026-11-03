---
content_hash: 26dd2d79b1c301686f4a22b2c2cc4e49b94593a7e7e56b60943ccd3e5f08cb95
fetched_at: '2026-06-29T00:10:37.108330+00:00'
page_id: '535857562'
product: rm
source: tdn-rm
title: Código de Cálculo 431 - BASE TRIBUTADA DE INSS FOLHA QUARTA FAIXA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535857562
version: 11
---

Evento tipo base, valor.

Este evento é calculado quando o parâmetro 'Calcula INSS conforme eSocial' estiver marcado em Configuração | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral.

Quando o funcionário está usando o cálculo de INSS conforme o eSocial, este evento pode ser lançado no movimento como base para tributação do percentual de 14% .

 **Exemplo:**

 Coligada 1: R$7000,00

 Coligada 2: R$1000,00

 **Tabela de INSS:**

Até  R$1045,00 - 7,5%

Até  R$2089 ,60 - 9%

Até  R$3134,40 - 12% 

Até  R$6101,06 - 14% 

O cálculo ocorrerá da seguinte forma:

Ao lançar o movimento para a **coligada 1**, será lançado o evento de código de calculo 428 no valor de  R$1045,00 que será a base para o cálculo do evento de INSS  salario código de calculo 3 aplicando a alíquota de 7,5 % encontrando o valor de R$78,37.

No código de calculo 429 foi tributado sobre  R$1044,60, segunda faixa aplicando uma alíquota de 9% encontrando um valor de  R$94,01.

No código de calculo 430 foi tributado sobre  R$1044,80  terceira faixa aplicando um alíquota de 12% encontrando um valor de  R$125,37 

E por ultimo o código de calculo 431 tributado sobre  R$2966,66 quarta faixa aplicando a alíquota de 14%.encontrando um valor de R$415,33.

Sendo descontado no código de calculo 3 as somas dos valores encontrado após o desconto progressivo  R$78,37+ R$94,01+ R$125,37 + R$415,33= R$713,08

Ao lançar o movimento para **coligada 2**, não será descontado o eventos de INSS salario Código de calculo 3 pois já foi descontado o teto na coligada 1

FIQUE ATENTO!

Para que a folha de pagamento realize o cálculo corretamente dos descontos de INSS de múltiplos vínculos em coligadas diferentes, é imprescindível respeitar a ordem para o cálculo. **Exemplo:** Empregador 1 deverá realizar o lançamento e calcular todos os valores referentes ao pagamento do seu vínculo para aquela competência, apenas após esse processo, o Empregador 2 poderá dar o início aos seus lançamentos e cálculos. Caso seja necessário realizar alterações no Empregador 1, sugerimos que seja feito o cancelamento dos lançamentos e feitos novamente na ordem que deseja enviar as informações ao governo.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
