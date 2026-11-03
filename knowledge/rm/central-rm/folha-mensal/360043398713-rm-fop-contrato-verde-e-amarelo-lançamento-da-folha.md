---
article_id: 360043398713
category: Folha Mensal
content_hash: 0a8782165d41cf7f9baa253400ccc5949ee1f5e8d9a16b8f44d15b16af2a019f
fetched_at: '2026-06-28T22:46:59.515836+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RM - FOP - Contrato Verde e Amarelo: Lançamento da Folha'
type: support-article
updated_at: '2021-06-21T13:25:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043398713-RM-FOP-Contrato-Verde-e-Amarelo-Lan%C3%A7amento-da-Folha
---

**Dúvida**Como realizar o Lançamento do Grupo de Eventos da Folha para os funcionários na modalidade Contrato Verde e Amarelo?  
   
 **Ambiente**RM – Folha de pagamento – A partir dos Patches 12.1.27.121 | 12.1.26.178  |  12.1.25.230  |  12.1.24.281  
  
**Solução**Pagamento será mensal, salvo acordo entre as partes que estipule prazo menor.

* ao final de cada mês, o empregado receberá o pagamento imediato das seguintes parcelas: remuneração; décimo terceiro salário proporcional; e férias proporcionais com acréscimo de um terço e sobre todo o montante incidirá a alíquota mensal de dois por cento à título de FGTS.
* as parcelas referidas à décimo terceiro e férias proporcionais são devidas ao empregado **independentemente** do número de dias trabalhados no mês.

**A indenização sobre o saldo do Fundo de Garantia do Tempo de Serviço – FGTS** poderá ser paga pela metade, quando antecipada ao empregado juntamente com as parcelas mensais sendo o seu pagamento irrevogável, independentemente do motivo de demissão do empregado, mesmo que por justa causa. Deverá ser **paga diretamente ao empregado**, sem necessidade de depósito em conta vinculada. Tal valor, deverá ser obrigatoriamente discriminado na folha de pagamento.  
  
Para atender a determinação acima, orientamos os clientes a criarem eventos com código de Cálculo 0 (Zero), calculados por fórmulas, para as verbas de os avos de 13º Salário e Férias e a multa rescisória para os casos de antecipação da mesma. Abaixo iremos exemplificar algumas sugestões de fórmulas:  
  
Considerando que o Salário Contratual do funcionário é  R$1500,00 com data de admissão dia 13/01 e o mesmo obteve as seguintes remunerações:  
  
Competência 01:

![](https://tdn.totvs.com/download/attachments/530186732/image2020-1-19_15-52-35.png?version=1&modificationDate=1579459955537&api=v2)

Competência 02

![](https://tdn.totvs.com/download/attachments/530186732/image2020-1-19_15-53-11.png?version=1&modificationDate=1579459991853&api=v2)  
  
***Férias***

Para o cálculo do avo de Férias poderá retornar o salário nominal  e dividir por 12: **((RC / 12)/30)\*ND**

Para o cálculo de Médias por valor, poderá retornar a soma dos valores dos eventos que compões a média e dividir por 12: **(C('0082')+C('0083'))/12.**

Para o cálculo de Média por Hora, poderá usar a função de fórmula CALCMED, conforme o exemplo: **((CALCMED('101')\*(NDFERIASAQ /2.5))/12)- (MV (17,0,'7002'))**Assim, ao lançar as verbas de Férias, o envelope ficará conforma abaixo na competência 02:

![](https://tdn.totvs.com/download/attachments/530186732/image2020-1-19_17-28-30.png?version=1&modificationDate=1579465710283&api=v2)  
  
Para o cálculo do Adicional de Férias, poderá retornar os valores dos eventos de Férias e dividir por 3:  **(C('7000')+C('7001')+C('7002'))/3.**Na competência 02, lançou o adicional conforme abaixo:

![](https://tdn.totvs.com/download/attachments/530186732/image2020-1-19_17-29-35.png?version=1&modificationDate=1579465775747&api=v2)  
  
***13º Salário***Para o cálculo do avo de 13º Salário poderá retornar o salário nominal  e dividir por 12: **((RC / 12)/30)\*ND**

Para o cálculo de Médias por valor, poderá retornar a soma dos valores dos eventos que compões a média e dividir por 12: **(C('0082')+C('0083'))/12.**

Para o cálculo de Média por Hora, poderá usar a função de fórmula CALCMED, conforme o exemplo: **(((CALCMED(201)\* INCMES(NMESES,1))/12)) - MV (18,0,'7012')**Assim ao Lançar as verbas de 13º Salário, o envelope ficará conforme abaixo na competência 02

![](https://tdn.totvs.com/download/attachments/530186732/image2020-1-19_17-30-24.png?version=1&modificationDate=1579465824477&api=v2)

***Antecipação da Indenização sobre o saldo do FGTS***Para o cálculo da antecipação da indenização sobre o saldo do FGTS, poderá somar as bases de FGTS folha e FGTS 13º, multiplicar por 0.02 e multiplicar por 0.20:  
  
**((BSFGTS13 + BASEFGTS)\* 0.02)\* 0.20**

![](https://tdn.totvs.com/download/attachments/530186732/image2020-1-19_17-30-55.png?version=1&modificationDate=1579465855763&api=v2)

**Atenção**  
  
As fórmulas acima são somente **sugestões** para calcular o 13º Salário e Férias proporcional que devem ser pagos junto com a remuneração do funcionário. As mesmas podem ser alteradas ou o usuário pode utilizar outras conforme a sua necessidade.  
  
Maiores informações sobre lançamento de Folha no Contrato Verde e Amarelo, [clique aqui.](https://tdn.totvs.com/display/public/LRM/Movimento+Mensal)Informações sobre o Cadastro de Funcionários no Contrato Verde e Amarelo, [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=528465156)Informações sobre Rescisões no Contrato Verde e Amarelo, [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=531010306)  
  
Informações sobre Guia de INSS, Encargos, SEFIP/FGTS no Contrato Verde e Amarelo, [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=533740337)
