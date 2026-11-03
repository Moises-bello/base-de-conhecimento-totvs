---
content_hash: 223a2671b92cafc1b88e0b9c645b70f74ede3119a2f971e370a0966ec6419f50
fetched_at: '2026-06-29T00:10:04.178001+00:00'
page_id: '452719209'
product: rm
source: tdn-rm
title: Fórmulas / Funções – F
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719209
version: 10
---

**Função F**

Retorna Valor Fixo por data.

F  
   
**Função FAIXATABCALC**  
Retorna em que faixa da tabela de cálculo se encontra o valor informado no parâmetro, de acordo com a vigência da tabela referenciada.  
FAIXATABCALC (STRING, DATA, VALOR)  
O funcionário tem o salário de R$3.000,00 e foi cadastrada a tabela abaixo:  
Código: IRRF  
Vigência: 01/03/2013 a 31/03/2013  
Faixa 1 – 0,00 a 1.787,77  
Faixa 2 – 2679,30 a 3572,43  
Faixa 3 – 3572,44 a 4463,81  
Faixa 4 – acima de 4463,81  
Ao cadastrar a fórmula FAIXATABCALC ('IRRF', HOJE, RC) o resultado esperado será 3, devido o salário do funcionário se enquadrar na Faixa 3.  
O sistema sempre considera a tabela de cálculo que está com a vigência dentro da data informada no parâmetro da fórmula.  
   
**Função FDATA**  
Retorna o valor fixo cadastrado referente a data determinada, verificando o período de vigência em que a data está inserida.  
FDATA ('0011', '2013')  
   
**Atenção:**  
O resultado desta fórmula será o valor cadastrado no Valor Fixo de Código 0011. Caso a data não esteja cadastrada entre os períodos de vigência do Valor Fixo será retornado o valor zero.  
   
**Função FALSO**  
Retorna o valor 0 (zero) está com o valor falso.  
   
**Função FERIADOEMDUTIL**  
Retorna quantidade de feriados encontrados nos dias em que o funcionário tem jornada de trabalho programada, não sendo considerados os feriados em dias de compensado e de descanso.

Exemplo:

| Feriados | Jornada do Funcionário: | Retorno da Fórmula |
| --- | --- | --- |
| 02/11/2021 - Terça-Feira  15/11/2021 - Segunda-Feira  28/11/2021 - Domingo | Segunda a Sexta - Trabalhado  Sabado - Compensado  Domingo -  Descanso | 2 |

**Atenção:**  
A variável verifica admissão, demissão, afastamento, férias, histórico de seção e histórico de horário.  
Na rescisão para o próximo mês verifica os feriados da competência da rescisão.  
   
**Função** **FERIADOEMDUTILPER**  
Retorna o número de feriados encontrados nos dias em que o funcionário tem jornada de trabalho programada, não sendo considerados os feriados em dias de compensado e de descanso no período informado.  
Sintaxe: FERIADOEMDUTILPER (DATA, DATA)

Exemplo:

| Feriados | Jornada do Funcionário: | Formula | Retorno da Fórmula |
| --- | --- | --- | --- |
| 02/11/2021 - Terça-Feira  15/11/2021 - Segunda-Feira  28/11/2021 - Domingo | Segunda a Sexta - Trabalhado  Sabado - Compensado  Domingo -  Descanso | FERIADOEMDUTILPER ('11/11/2021', '30/11/2021') | 1 |

**Atenção:**  
A variável verifica admissão, demissão, afastamento, férias, histórico de seção e histórico de horário.  
Na rescisão para o próximo mês verifica os feriados da competência da rescisão.  
   
**Função FERIADOS**  
Retorna a quantidade de feriados entre duas datas conforme calendário informado na seção do funcionário.  
FERIADOS (DATA INICIAL, DATA FINAL)  
   
**Exemplo:**  
FERIADOS ('01/01/2014', '29/02/2014')  
   
**Função FERIADOSINT**  
Retorna nº de feriados em um intervalo do mês de competência.  
FERIADOSINT (DIAINICIO, DIAFIM)   
   
**Atenção:**  
Digite apenas os dias inicial e final, sem informar mês e ano.  
   
**Função FERIADOSMES**  
Retorna nº de feriados no mês  
   
**Função FNOMEMAE**  
Retorna nome da mãe do funcionário. String  
   
**Função FNOMEMAE**  
Retorna nome do pai do funcionário. String  
   
**Função FOR**  
Retorna resultado de uma fórmula  
FOR ('CÓD. DA FÓRMULA')  
   
**Exemplo:**  
SE FOR ('121') > RC\*1.2 ENTAO FOR ('122') SENAO FOR('123') FIMSE  
Neste exemplo, se o resultado da fórmula 121 for maior que o produto da multiplicação do salário-base do funcionário por 1.2, então o sistema executará a fórmula 122. Caso contrário, será executada a fórmula 123.  
   
**Função FRAC**  
Retorna parte fracionária de um valor.  
FRAC (Valor)  
   
**Exemplo:**  
FRAC (20.6). Retornará 0.6
