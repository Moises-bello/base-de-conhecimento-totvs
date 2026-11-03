---
content_hash: a410c92cf094d79807843ab5ac07be5c973258116e947d3fcda8408df64be332
fetched_at: '2026-06-29T00:10:07.263779+00:00'
page_id: '452719387'
product: rm
source: tdn-rm
title: Cálculo das Horas de Substituição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719387
version: 5
---

O cálculo é realizado em duas etapas :   
   
**1º. etapa :**  
Calcular a média diária dos eventos do tipo hora e referência que incidam em substituição informada no cadastro de eventos.   
   
MÉDIA DIARIA = ?( NÚMERO HORAS \* PERC. INCID.)/ DIAS ÚTEIS), no caso de eventos do tipo Hora ou   
MÉDIA DIÁRIA = ?( REFERÊNCIA \* PERC. INCID.)/ DIAS ÚTEIS), no caso de eventos do tipo Referência.  
   
Onde :  
NÚMERO DE HORAS é o número de horas lançado do evento   
PERC. INCID. é o percentual de incidência do evento  
DIAS ÚTEIS é o campo *"número dias úteis mês do funcionário"* ( PFUNC.DIASUTEISMES )  
REFERÊNCIA é a referência lançada no evento.  
   
 **2º. etapa:**  
Calcular o valor de cada substituição  
 VALOR SUBSTITUIÇÃO = (NRO HORAS SUBST. INFOR. +   
(MÉDIA DIÁRIA )\*NRO DIAS SUBSTITUIÇÃO) \*VALOR HORA SUBST.  
   
Onde:  
NRO HORAS SUBST. INFOR. É o número de horas substituição informado no cadastro do funcionário. Geralmente o usuário informa o número de dias, o sistema transforma em horas dividindo a jornada do funcionário por 30 dias e armazena o número de horas encontrado.  
MÉDIA DIÁRIA é o número de horas encontrado na 1a. etapa.  
VALOR HORA SUBST.: SAL. HORA SUBSTITUÍDO - SAL. HORA SUBSTITUTO  
   
**Exemplo:**  
   
Supondo que o funcionário 00002 esteja substituindo os funcionários 00003 e 00005 no mês atual.  
Considere os seguintes salários e jornadas, respectivamente:

* Funcionário 00002: 580,00 - 220:00, salário/hora: 2,64
* Funcionário 00003: 1939,08 - 220:00, salário/hora: 8,81
* Funcionário 00005: 688,60 - 220:00, salário/hora: 3,13

O cálculo do adicional de substituição para este funcionário é o seguinte:   
   
CÁLCULO DO ADICIONAL DE SUBSTITUIÇÃO: Funcionário 00002  
   
1ª Parte - Média diária dos eventos do tipo hora e referência:Evento 0082 (tipo HORA) -> 3:00 \* 1,50 / 21 = 0:12 (Número Horas do Evento \* Percentual / Número Dias Úteis)Evento 0083 (tipo HORA) -> 10:00 \* 2,00 / 21 = 0:57 (Número Horas do Evento \* Percentual / Número Dias Úteis)Média diária = 1:09  
   
2ª Parte: Cálculo das Horas de Substituição:  
Salário hora do funcionário substituto 00002: 2,64

1ª Substituição:    
Número de Horas de Substituição: 73:20 + (1:09 \* 10) = 85:00 (Número Horas Original + Média Diária \* Número de Dias de Substituição)  
Salário hora do funcionário substituído 00005: 3,13  
Valor do evento adicional de substituição = (3,13-2,64)\*85:00 = 41,96  
   
2ª Substituição:    
Número de Horas de Substituição: 73:20 + (1:09 \* 10) = 85:00 (Número Horas Original + Média Diária \* Número de Dias de Substituição)  
Salário hora do funcionário substituído 00003: 8,81  
Valor do evento adicional de substituição = (8,81-2,64)\*85:00 = 525,10  
Valor total do evento adicional de substituição = 567,06  
   
**Observação:**  
Não necessariamente o funcionário estará substituindo outro funcionário. O funcionário poderá estar substituindo uma vaga no quadro de pessoal ( uma função). Neste caso o salário informado  é da tabela salarial.

Somente para funcionário Horista, em meses de 31 dias será permitido cadastrar 31 dias de substituição.

***O sistema não faz o lançamento automático. O cálculo só é efetuado se o usuário lançar este evento na movimentação atual.***

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários

Ficha Financeira
