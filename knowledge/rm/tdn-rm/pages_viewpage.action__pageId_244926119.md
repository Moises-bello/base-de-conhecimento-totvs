---
content_hash: d5682bb24e983ab969426ff08c68404230e345ca408cd11a51b3d95936b2e03c
fetched_at: '2026-06-29T00:08:15.880502+00:00'
page_id: '244926119'
product: rm
source: tdn-rm
title: Fórmulas de Cálculo para Linearização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244926119
version: 4
---

|  |  |
| --- | --- |
| Descrição | Fórmulas de Cálculo para linearização |
| Observações | Descrição de Calculo das formulas de linearização |

O usuário poderá criar suas próprias fórmulas de cálculo, utilizando as funções de formula descritas no tópico *[Funções de Fórmula](http://tdn.totvs.com/pages/viewpage.action?pageId=244925107)* , através de consultas sql.

 Quando utilizar os Valores ou funções de fórmula fornecidos pelo sistema estarão recebendo os cálculos que descreveremos a seguir.

**ARRENDAMENTO MERCANTIL NAS DEMONSTRAÇÕES CONTÁBEIS DO ARRENDADOR**

De acordo com a o NBC TG 06 ou CPC 06 que contempla o arrendamento mercantil (financeiro e Operacional) e neste contexto a locação imobiliária, o reconhecimento da receita deve ocorrer na base da linha reta durante o prazo do arrendamento mercantil, assim como valores redutores de receita como desconto.

*Variáveis*

VO = Valor Original

VR = Valor de Reajuste

iT = Tempo Total do Contrato ou número total de meses da vigência Contratual;

ia= Tempo de Aplicação ou número total de meses de aplicação. Os meses de aplicação não necessariamente correspondem ao total de meses do contrato;

D= percentual de desconto dividido por 100;

**Cenário de Exemplo para aplicação das formulas**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Locatário** | **Aluguel original** | **Período** | **Carência** | **Início** | **Fim** |
| Munich Re do Brasil (6º andar) | 65.076,00 (**VO**) | 60 meses | 7 meses | 01/06/2015 | 30/05/2020 |
|  |  |  |  |  |  |
| Prazo | Base de calculo | Desconto | IGPM | Valor do reajuste | Total |
| 1º | 65.076,00 | 18,00% (D) | - | - | 53.362,32 |
| 2º ao 8 (carência) | - | 18,00% | - | - | - |
| 9 ao 12 | 65.076,00 | 18,00% | - | - | 53.362,32 |
| 13 ao 24 | 65.076,00 | 13,60% | 6,60000% | 4.295,02 | 60.520,68 |
| 25 ao 36 | 69.371,02 | - | 7,60000% | 5.272,20 | 74.643,21 |
| 37 ao 48 | 74.643,21 | - | 8,60000% | 6.419,32 | 81.062,53 |
| 49 ao 60 | 81.062,53 | - | 9,60000% | 7.782,00 | 88.844,53 |

**Receita Linear (RL)**

O NBC TG 06 estabelece que a receita deve ser reconhecida de forma linear e para isso será necessário estabelecer seu valor médio.

**RL = (∑período (VO\* ia) ) /iT**

O somatório do período representa a soma dos valores por período, ou seja períodos com valores diferentes devem ser calculados separadamente

*Se houver variação do VO por período o somatório deve ser feito multiplicando os valores originais semelhantes*

Se houvesse escalonamento estabelecido no início do contrato, cada período deveria ser calculado com seu respectivo valor, e o somatório seria a base para dividir pelo período total de meses do contrato. Vale ressaltar que se o escalonamento alterar o valor do contrato depois de seu início, o valor médio só deve ser considerado a partir da data que causou efeito (fato gerador = data inicial do escalonamento).

**Desconto Linear (DL)**

Conforme estabelecido pela NBC TG 06, os valores de descontos devem ser linearizados e contabilizados em conta especifica do ativo, sendo redutora de receita.

**DL= (∑período (VO\* D)\* ia) /iT**

Exemplo:

*DL= (((65076,00\*0,18)\*1)+ ((0,00\*0,18)\*7)+((65.076,00\*0,18)\*4)+(65.076,00\*0,136)\*12))) /60*

*DL= ((11.713,68)+ (0,00)+(46.854,72)+(106204,03)) /60*

*DL = (164.772,43) /60*

*DL =2.746,21*

**Recebimento (Rec)**

O recebimento corresponde ao valor que será efetivamente cobrado do cliente.

*VR = Valor de Reajuste do período.*

**Rec = ((VO+VR)\*(- D))+VO+VR**

*Exemplo*

*Rec = (65.076,00+0,00)\*(-0,18) +( 65.076,00+0)*

*Rec = -11.713,68 +65.076,00*

*Rec =53.362,32*

**Provisão Receita Linear (PRL)**

A provisão da Receita Linear será é resultado da previsão da receita acrescida do valor de desconto.

**PRL=( Rec -(-DL)**

 O desconto linear é de natureza redutora portanto seu sinal é negativo

*Exemplo*

*PRL =53.632,32-(-2.746,21)*

*PRL =56.108,53*

*Contabilização*

|  |  |
| --- | --- |
| D | C |
| Aluguel a receber | Receita de aluguel |
| 56.108,53 | 56.108,53 |

**Provisão da Linearização  (PL)**

A provisão da linearização é o valor que fará o ajuste linear da receita.

**PL= (RL+ (****-DL) ) –Rec**

*Exemplo*

***PL** =(57.483,80-2.746,21)- (53.362,32)*

***PL** =1.375,27*

*Contabilização*

|  |  |
| --- | --- |
| D | C |
| Aluguel a faturar (Linearização) | Receita de aluguéis a faturar (Linearização) |
| 1.375,27 | 1.375,27 |

**Provisão de Desconto Linear (PDL)**

O valor de provisão contábil de desconto corresponde ao valor do Desconto Linear

***PDL = DL***

*Contabilização*

|  |  |
| --- | --- |
| D | C |
| Descontos concedidos | Aluguel a receber |
| 2.746,21 | 2.746,21 |

**Carência**

Nos períodos de carência o valor de receita e linearização sofrem alteração conforme formula abaixo.

Provisão de Receita Linear

PRL=(Rec-(DL)

PRL =0-(-2.746,21)

PRL =2.746,21

*Contabilização*

|  |  |
| --- | --- |
| D | C |
| Aluguel a receber | Receita de aluguel |
| 2.746,21 | 2.746,21 |

Provisão de Linearização

**PL= (RL+ (****-DL) ) –Rec**

**PL** =(57.483,80-2.746,21)- (0)

**PL** =54.737,59

*Contabilização*

|  |  |
| --- | --- |
| D | C |
| Aluguel a faturar (Linearização) | Receita de aluguéis a faturar (Linearização) |
| 54.737,59 | 54.737,59 |

Provisão de Desconto Linear

*Contabilização*

|  |  |
| --- | --- |
| D | C |
| Descontos concedidos | Aluguel a receber |
| 2.746,21 | 2.746,21 |

Ao reajustar o contrato os valores devem ser recalculados e as provisões futuras devem ser alteradas. Não há alteração nos lançamentos anteriores a data do fato gerador (reajuste).
