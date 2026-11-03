---
content_hash: 49aaada55cab2e2da99707fd684b2b41929102bcce1ff58fdc4eef734b19d583
fetched_at: '2026-06-29T00:09:47.990368+00:00'
page_id: '435105117'
product: rm
source: tdn-rm
title: Componente de Juros - Parâmetro Componente de Juros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105117
version: 10
---

* **Juros Pro Rata Dia**: "Pro rata dia" é o mesmo que "em proporção ao dia" isto é juros incidentes "por dia". É a cobrança proporcional (calculada por dia), feita quando a data do vencimento da parcela não compreende a todo o período estipulado do cálculo de reajuste do contrato. Foi criado 2 modelos para o cálculo. São eles:
  + **Modelo 0 - Cálculo dos Juros Pro Rata Proporcional ao numero de dias do Mês**

falseJuros Simples: (Gráfico Linear)

i \* ( a / b ) "Primeiro mês de reajuste - Janeiro"  
(i \* ( a / b )) + (i \* ( a / b )) "Segundo mês de reajuste - Fevereiro"

falseJuros Composto: (Gráfico Exponencial) 

( 1 + i ) ^ ( a / b ) - 1 "Primeiro mês de reajuste - Janeiro" ( 1 + i ) ^ ( a / b ) \* ( 1 + i ) ^ ( c / d ) \* ... - 1 "Segundo mês de reajuste - Fevereiro"   
Onde: i = taxa de juros a = Número de dias utilizados no mês (Janeiro) b = Número de dias total do mês (Janeiro) c = Número de dias utilizados no mês (Fevereiro) d = Número de dias total do mês (Fevereiro)

* + **Modelo 1 - Cálculo dos Juros Pro Rata Proporcional a 30 dias**

Juros Simples: (Gráfico Linear) Período = Data Final – Data Inicial Taxa Juros \* (período / 30) Juros Composto: (Gráfico Exponencial)Período = Data Final – Data Inicial  =  ((1 + taxa Juros) ^ (período / 30) – 1) 

* **Juros Acumulado**: Este campo informa que o reajuste de juros de contrato será calculado cumulativamente, ou seja, quando a periodicidade de reajuste for maior que 1, nos meses em que não houver reajuste, os juros serão acumulado.

Este parâmetro somente será marcado se o Prazo de Reajuste for maior que 1 mês e se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão. Este parâmetro está inabilitado para alterações, ou seja, se a periodicidade for maior que 1, sempre será juros acumulado.    
Exemplo:

Venda efetuada em Janeiro de 2004 com uma parcela de sinal e 10 parcelas mensais, com periodicidade de reajuste de 4 em 4 meses.   
Correção do mês de Maio de 2004 em uma parcela no valor de R$ 1000,00: Juros: 1000,00 + 4% = 1040,00;  
Correção do mês de Setembro de 2004 em uma parcela no valor de R$ 1000,00: Juros: 1000,00 + 8% = 1080,00.

Se este parâmetro não estivesse marcado, o sistema iria aplicar no mês de Maio apenas os juros de 1% e no mês de Setembro 2%.

* **Calcular o valor do Juros sobre:**
  + Saldo devedor Principal da Parcela: Marque este campo quando o reajuste de juros de contrato será calculado sobre o valor original das parcelas.

false

Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão    
Exemplo:

Venda efetuada em Fevereiro de 2004 com 1 parcela de sinal e 10 parcelas mensais.  
Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00: Juros: 1000,00 + 1% = 1010,00;  
Correção do mês de Abril de 2004 em uma parcela no valor de R$ 1000,00: Juros: 1000,00 + 2% = 1020,00

* Saldo devedor Principal da Parcela + CM até o mês anterior: Marque este campo quando o valor monetário calculado no mês anterior ao do reajuste de juros será somado ao valor base para o cálculo dos juros.

false

Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.    
Exemplo:

Venda efetuada em Fevereiro de 2004 com 1 parcela de sinal e 10 parcelas mensais.  
Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:

Correção Monetária: Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395 CM = (1,00643955 \* 1000) – 1000 = 6,43955;  
Juros: 1000,00 + 1% = 1010,00 - Correção do mês de Abril de 2004 em uma parcela no valor de R$ 1000,00;  
Correção Monetária: Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422 CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1000 ) – 1000 = 14,1430597;  
Juros: 1006,43955 + 2% = 1026,568341.

* Saldo devedor Principal da Parcela + CM até o mês do reajuste: Marque este campo quando o valor monetário calculado no mês do reajuste de juros será somado ao valor base para o cálculo dos juros.

Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.  
Exemplo:

Venda efetuada em Fevereiro de 2004 com 1 parcela de sinal e 10 parcelas mensais.

Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:

Correção Monetária: Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395 CM = (1,00643955 \* 1000) – 1000 = 6,43955;  
Juros: 1006,43955 + 1% = 1016,5039455 - Correção do mês de Abril de 2004 em uma parcela no valor de R$ 1000,00;  
Correção Monetária: Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422 CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1000 ) – 1000 = 14,1430597;  
Juros: 1014,1430597 + 2% = 1034,425920894.

Dependendo do tipo do Modelo de cálculo escolhido no componente do tipo Principal desta modalidade, irá ou não habilitar os parâmetros do componente de Juros.
