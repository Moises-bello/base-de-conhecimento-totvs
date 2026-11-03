---
content_hash: 3bc63de0ce91a27f9202e470af3e28213d2bc42121eb074ff264521228d31893
fetched_at: '2026-06-29T00:11:56.965545+00:00'
page_id: '873208316'
product: rm
source: tdn-rm
title: Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=873208316
version: 49
---

## **CONTEÚDO**

1. **Versão**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **T****abelas utilizadas**

## **01. VERSÃO**

false

**A partir dos patches:**

* 12.1.2402.238
* 12.1.2406.172
* 12.1.2410.107
* 12.1.2502 e Superiores

## **02. VISÃO GERAL**

Este documento tem o objetivo de demostrar como irá funcionar o cálculo da rescisão quando houver restituição de INSS/IRRF 13º mediante ao parâmetro '**Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão**' criado em [13º salário - Rescisão](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719912) para gerar retificação de 13º Salário automaticamente. 

## **03. EXEMPLO DE UTILIZAÇÃO**

Cálculo com Parâmetro marcado

Parâmetro marcado:

Foi realizado o cálculo da 2ª parcela de 13º salário integral pago no dia 05/12 na competência 12 e foi descontando INSS e IRRF de 13º Salário

Após pagamento do 13º Salário, ainda na competência 12 e em período diferente foi cadastrada e calculada a rescisão com data de desligamento para o dia 14/12. Neste caso, o direito ao 13º salário será de 11 avos e desconto da parcela adiantada referente a 12 avos.

Nesse caso haverá restituição de INSS e IRRF de 13º Salário lançado no período 10000 criado automaticamente no mês competência atual, ou seja, Dezembro.

Neste período foram lançados:

Evento com  o código de cálculo - 153 - RESTITUICAO INSS 13º - Para informar o valor restituído ao funcionário  
Evento com  o código de cálculo - 52 - RESTITUICAO DE IRRF 13º SALARIO - Para informar o valor restituído ao funcionário  
Evento com  o código de cálculo - 383 - LIQUIDO DE RETIFICACAO - DESCONTO - Para zerar o período de retificação  
Evento com  o código de cálculo - 476 - ESTORNO NA BASE DE IRRF 13º RETIFICADO - Para envio no XML do eSocial do valor estornado na base original da 2ª parcela de 13º salário enviado anteriormente  
Evento com  o código de cálculo - 474 - ESTORNO NA BASE DE INSS 13º RETIFICADO - Para envio no XML do eSocial do valor estornado na base original da 2ª parcela de 13º salário enviado anteriormente

Na rescisão foram lançados os eventos com os novos códigos de cálculo 473 e 475 para pagamento da restituição lançada no período 10000

Cálculo com Parâmetro desmarcado

Parâmetro desmarcado:

Foi realizado o cálculo da 2ª parcela de 13º salário integral pago no dia 05/12 na competência 12 e foi descontando INSS e IRRF de 13º Salário:

Funcionário com rescisão com data de desligamento em 14/12, portanto o direito ao 13º salário será de 11 avos e desconto da parcela de  13º Salário adiantada referente a 12 avos

Nesse caso será apresentada a mensagem: ”O sistema identificou restituição de INSS e/ou IRRF para o funcionário de chapa XXXXX. Porém, para o eSocial não é permitido ter restituição em período onde não consta o desconto com valor igual ou superior.  
Para criar um período de Retificação com os valores restituídos é necessário marcar o parâmetro "Gerar retificação de 13º quando existir restituição de IRRF e/ou INSS na rescisão", no Parametrizador, aba Rescisão/13º Salário.”

Serão lançados os eventos de restituição abaixo no período da rescisão do funcionário:

Evento com  o código de cálculo - 153 - RESTITUICAO INSS 13º

Evento com  o código de cálculo - 52 - RESTITUICAO DE IRRF 13º SALARIO

XML enviado pelo eSocial com o parâmetro marcado

Para a geração do XML o parâmetro 'Unificar período na retificação' deve estar marcado obrigatoriamente.

Parâmetro marcado:

Foi realizado o cálculo da 2ª parcela de 13º salário integral pago no dia 05/12 na competência 12 e foi descontando INSS e IRRF de 13º Salário

Após pagamento do 13º Salário, ainda na competência 12 e em período diferente foi cadastrada e calculada a rescisão com data de desligamento para o dia 14/12. Neste caso, o direito ao 13º salário será de 11 avos e desconto da parcela adiantada referente a 12 avos.

Período 10000 com valores da restituição

XMLs gerados e enviados na seguinte ordem - Todos Aceito RET

Para a Simulação foi seguido o cenário em que o usuário paga a 2ª parcela de 13º salário junto com o pagamento do salário no dia 05/12, então nesse caso enviaria primeiro um XML logo após o pagamento da 2ª parcela de 13º salário com pagamento de 12 avos

Após fazer a rescisão em 14/12 será enviado o XML da Rescisão com 11 avos de 13º salário

E o pagamento dos valores restituídos

Enviado o XML da Retificação

IMPORTANTE

É muito importante enviar esse XML por se tratar da retificação dos valores de INSS e IRRF de 13º salário que foram enviados a maior no pagamento da 2ª parcela de 13º salário integral.

Após envio da retificação os valores foram conferidos na aba Retorno da integração.

**Cálculo INSS13:**  
Valor base INSS13 = Base INSS13 primeiro envio - Estorno da retificação  
Valor base INSS13 = 3.190,91 - 265,91 = 2925,00

Valor INSS13 a pagar = INSS13 descontado primeiro envio - Valor restituição da retificação  
Valor INSS13 a pagar = 285,96 - 31,91 = 254,05

**Cálculo IRRF13:**  
Valor base INSS13 = Base INSS13 primeiro envio - Estorno da retificação  
Valor base INSS13 = 3.190,91 - 265,91 = 2925,00

Valor INSS13 a pagar = INSS13 descontado primeiro envio - Valor restituição da retificação  
Valor INSS13 a pagar = 56,91 - 19,94 = 36,97

Cancelar Rescisão

Períodos calculados para rescisão e retificação com os eventos de restituição:

Rescisão com lançamento dos eventos de código de cálculo 473 e 475:

E com o período retificado que foi criado com os valores de restituição de INSS e IRFF de 13º Salário:

Cancelando a rescisão com a opção para cancelar movimentação da rescisão para demitidos no mês atual:

Ambos períodos foram cancelados:

Rescisão Complementar após restituição na rescisão original por faltas

Cálculo INSS 13º salário da rescisão complementar

falseObservação:

**A partir da versão**

* 12.1.2502 e Superiores

Dados fictícios com um funcionário com o SALÁRIO: 3711,07

**2ª PARCELA 13º SALARIO PAGO EM 20/12** - 12 MESES  
**BASE CÁLCULO** = 3748,78  
**DESCONTO INSS13** = 352,90

**RESCISÃO ORIGINAL EM 30/12 COM 16 FALTAS** - 14 DIAS TRABALHADOS NO MÊS PERDE UM AVO DE 13º SALÁRIO

13º SALÁRIO RESCISÃO 11 MESES  
13º Salário = Salário(3.711,070000) / 12 \* Avos(11) = 3.401,814167  
MEDIA HORA EXTRA 13º RESCISAO = 34,570000  
TOTAL DA BASE = 3436,38  
ADIANTAMENTO 2ª PARCELA 13º SALARIO = 3.748,78 (DESCONTADO NA RESCISÃO REFERENTE A 2ª PARCELA DE 13º SALÁRIO PAGO ANTERIORMENTE)

              Calculando evento: 0011 - INSS 13º SALARIO  
              Código de Cálculo 11 - Prioridade 81  
                
                     Será lançado no período 10000 da retificação de 13o.  
                     o valor de 312,40 para estorno na Base de INSS 13o.  
                       
                     Base de INSS:   
                         Proventos = **3.436,38**                         Descontos = 3.748,78  
                         Base Líquida = **-312,40**                           
                     Base de INSS mesmo mês: 3.748,78  
                     INSS já descontado no mês: 352,90  
                     Total Base de INSS: 3.436,38  
                       
                     INSS: 7,5000% \* Base(1.320,00) = 99,00  
                     INSS: 9,0000% \* Base(1.251,29) = 112,61  
                     INSS: 12,0000% \* Base(865,09) = 103,81  
                     Valor do INSS: 315,42  
                     Abatendo INSS já descontado no mês: 315,42 - 352,90 = **-37,48**                     Será lançada uma restituição de INSS no valor de 37,48.  
                     Valor do evento: 0,00

**RESCISÃO COMPLEMENTAR -** ALTERANDO O SALÁRIO DO FUNCIONÁRIO PARA 4082,18  
13º SALÁRIO RESCISÃO 11 MESES  
13º Salário = Salário(4.082,180000) / 12 \* Avos(11) = 3.741,998333  
MEDIA HORA EXTRA 13º RESCISAO = 38,020000  
TOTAL DA BASE = **3780,02**  
ADIANTAMENTO 2ª PARCELA 13º SALARIO = **3.748,78**

Dica:

Veja que o valor da base com a alteração salarial fica maior que a base da 2ª parcela de 13º salário, com isso o funcionário fica devendo a parte restituída na rescisão mais a diferença encontrada no cálculo da rescisão complementar.

      Calculando evento: 0011 - INSS 13º SALARIO  
       Código de Cálculo 11 - Prioridade 81  
         
              Base de INSS:   
                  Proventos = **3.780,02**                  Descontos = 3.748,78  
                  Base Líquida = **31,24**                    
              Base de INSS mesmo mês: 3.748,78  
              INSS já descontado no mês: 352,90  
              Total Base de INSS: 3.780,02  
                
              INSS: 7,5000% \* Base(1.320,00) = 99,00  
              INSS: 9,0000% \* Base(1.251,29) = 112,61  
              INSS: 12,0000% \* Base(1.208,73) = 145,04  
              Valor do INSS: 356,65  
              Abatendo INSS já descontado no mês: 356,65 - 352,90 = 3,75  
              Somando Restituição de INSS já lançada no mês: **3,75 + 37,48 = 41,23**              Valor do evento: 41,23

Dica:

Veja que no cálculo da rescisão complementar o valor total da base **3.780,02** corresponde a soma do valor encontrado na rescisão original **3.436,38** com o valor da base da restituição **312,40** e a base líquida **31,24**, por isso o valor restituído ao funcionário na rescisão original deve ser somado para descontar do funcionário na rescisão complementar.

Rescisão Complementar após restituição na rescisão original por antecipação de 13º salário

Cálculo INSS 13º salário da rescisão complementar

falseObservação:

**A partir da versão**

* 12.1.2502 e Superiores

   
Dados fictícios com um funcionário com o SALÁRIO: 4771,00

**2ª PARCELA 13º SALARIO PAGO EM 05/12 -** 12 MESES  
**BASE CÁLCULO** = 4771,00  
**DESCONTO INSS13** = 493,84

**RESCISÃO ORIGINAL EM 14/12** - 14 DIAS TRABALHADOS NO MÊS PERDE UM AVO DE 13º SALÁRIO

13º SALÁRIO RESCISÃO 11 MESES  
13º Salário = Salário(4.771,000000) / 12 \* Avos(11) = 4.373,416667  
TOTAL DA BASE = 4.373,42  
ADIANTAMENTO 2ª PARCELA 13º SALARIO = 4.771,00 (DESCONTADO NA RESCISÃO REFERENTE A 2ª PARCELA DE 13º SALÁRIO PAGO ANTERIORMENTE)

              Calculando evento: 0011 - INSS 13º SALARIO  
              Código de Cálculo 11 - Prioridade 81  
                
                     Será lançado no período 10000 da retificação de 13o.  
                     o valor de 397,58 para estorno na Base de INSS 13o.  
                       
                     Base de INSS:   
                         Proventos = **4.373,42**                         Descontos = 4.771,00  
                         Base Líquida = **-397,58**                           
                     Base de INSS mesmo mês: 4.771,00  
                     INSS já descontado no mês: 493,84  
                     Total Base de INSS: 4.373,42  
                       
                     INSS: 7,5000% \* Base(1.320,00) = 99,00  
                     INSS: 9,0000% \* Base(1.251,29) = 112,61  
                     INSS: 12,0000% \* Base(1.285,65) = 154,27  
                     INSS: 14,0000% \* Base(516,48) = 72,30  
                     Valor do INSS: 438,18  
                     Abatendo INSS já descontado no mês: 438,18 - 493,84 = **-55,66**                     Será lançada uma restituição de INSS no valor de 55,66.  
                     Valor do evento: 0,00

**RESCISÃO COMPLEMENTAR** ALTERANDO O SALÁRIO DO FUNCIONÁRIO PARA 4.871,00  
13º SALÁRIO RESCISÃO 11 MESES  
13º Salário = Salário(4.871,000000) / 12 \* Avos(11) = 4.465,083333  
TOTAL DA BASE = **4.465,08**

BASE 13º SALÁRIO RESCISÃO = **4.373,42**

ADIANTAMENTO 2ª PARCELA 13º SALARIO = **4.771,00**

Dica:

Veja que o valor da base com a alteração salarial fica maior que a base do 13º salário rescisão e menor que a base da 2ª parcela de 13º salário, com isso a parte restituída na rescisão deveria ser menor e essa diferença será descontada na rescisão complementar.

      Calculando evento: 0011 - INSS 13º SALARIO  
       Código de Cálculo 11 - Prioridade 81  
         
              Base de INSS:   
                  Proventos = **4.465,08**                  Descontos = 4.771,00  
                  Base Líquida = **-305,92**                    
              Base de INSS mesmo mês: 4.771,00  
              INSS já descontado no mês: 493,84  
              Total Base de INSS: 4.465,08  
                
              INSS: 7,5000% \* Base(1.320,00) = 99,00  
              INSS: 9,0000% \* Base(1.251,29) = 112,61  
              INSS: 12,0000% \* Base(1.285,65) = 154,27  
              INSS: 14,0000% \* Base(608,14) = 85,13  
              Valor do INSS: 451,01  
              Abatendo INSS já descontado no mês: 451,01 - 493,84 = -42,83  
              Somando Restituição de INSS já lançada no mês**: -42,83 + 55,66 = 12,83**              Valor do evento: 12,83

Dica:

Veja que no cálculo da rescisão complementar o valor total da base **4.465,08** corresponde a soma do valor encontrado na rescisão original **4.373,42** com o valor da base da restituição **397,58** e a base líquida **-305,92**(valor negativo) .  
Nesse caso o cálculo retornou um valor a restituir que verificando é menor que o valor restituído anteriormente, com isso o funcionário deve pagar a parte da diferença entre as restituições.

## **04.** **TABELAS UTILIZADAS**

* PFPERFF
* PFFINANC
* PFRETIFICACAOPERIODO
* PPARAMADICIONAIS
* PEVENTO
