---
content_hash: 26cc6cfc0f6a4cfb25468e14e178d1e266a282629e3819cb5bcc60ef9ba589cc
fetched_at: '2026-06-29T00:10:37.125080+00:00'
page_id: '535857583'
product: rm
source: tdn-rm
title: Código de Cálculo 434 - BASE TRIBUTADA DE INSS 13º TERCEIRA FAIXA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=535857583
version: 11
---

Evento tipo base, valor.  
Este evento é calculado caso o sistema esta com o parâmetro 'Calcula INSS conforme eSocial' estiver marcado em Configuração | Parâmetros | Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Geral.  
   
Quando o funcionário utiliza o cálculo de INSS conforme o eSocial,  e é calculada a base de INSS de 13º salário, pode ser lançado o evento de código de calculo 434 com o valor da base que foi usada para fazer o cálculo de INSS de 13ºsalário. 

 **Exemplo:**

 Coligada 1: R$ 2200,00

 Coligada 2: R$1000,00

 **Tabela de INSS:**

Até  R$1045,00 - 7,5%

Até  R$2089 ,60 - 9%

Até  R$3134,40 - 12% 

Até  R$6101,06 - 14% 

O cálculo ocorrerá da seguinte forma:

Ao lançar o movimento para a **coligada 1**, será lançado o evento de código de calculo 432 no valor de  R$1045,00 que será a base para o cálculo do evento de INSS código de calculo 103 aplicando a alíquota de 7,5 % encontrando o valor de R$78,37. No código de calculo 433 foi tributado R$1044,60 na segunda faixa aplicando uma alíquota de 9% encontrando um valor de R$94,01.No código de calculo 434 foi tributado o restante na terceira faixa ( R$2200,00- R$1045,00- R$1044.60)= R$110,40 e aplicamos a alíquota de 12%= R$13,24.

Sendo descontado no código de calculo 103 as somas dos valores encontrado após o desconto progressivo  R$78,37+ R$94,01+ R$13,24= R$185,62

Ao lançar o movimento para **coligada 2**, será lançado o evento de código de calculo 434 com o valor de  R$934,40 que é( R$1044,80 - R$110,40),neste valor será aplicado o percentual de 12%.= R$112,12. Será lançado também o evento código de calculo 435 Base Tributada de INSS Folha quarta faixa ,neste evento será lançado o restante a ser tributado na quarta faixa. O sistema considera o total da base dos dois vínculos = R$3200,00, deste valor retiramos o que já foi tributado na primeira ,segunda e terceira faixa de 13º salario ( R$3200,00-  R$1045,00- R$1044.60- R$1044,80)= R$65,60 e aplicamos a alíquota de 14%= R$9,18

Sendo descontado no código de calculo 103 as somas dos valores encontrado após o desconto progressivo  R$112,12 + R$9,18= R$121,3

FIQUE ATENTO!

Para que a folha de pagamento realize o cálculo corretamente dos descontos de INSS de múltiplos vínculos em coligadas diferentes, é imprescindível respeitar a ordem para o cálculo. **Exemplo:** Empregador 1 deverá realizar o lançamento e calcular todos os valores referentes ao pagamento do seu vínculo para aquela competência, apenas após esse processo, o Empregador 2 poderá dar o início aos seus lançamentos e cálculos. Caso seja necessário realizar alterações no Empregador 1, sugerimos que seja feito o cancelamento dos lançamentos e feitos novamente na ordem que deseja enviar as informações ao governo.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
