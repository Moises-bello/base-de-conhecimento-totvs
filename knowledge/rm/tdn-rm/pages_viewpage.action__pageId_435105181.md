---
content_hash: 1b6eac876d2c246add07ceb6f2826c23a0350385ef4d1fe610cab417b551c352
fetched_at: '2026-06-29T00:09:48.526306+00:00'
page_id: '435105181'
product: rm
source: tdn-rm
title: Componente Correção Monetária - Parâmetro Componente de Correção Monetária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105181
version: 3
---

Cálculo de Correção Monetária "Pro-Rata Dia":  
 "Pro rata die" é o mesmo que "em proporção ao dia" isto é juros incidentes "por dia". É a cobrança proporcional (calculada por dia), feita quando a data do vencimento da parcela não compreende a todo o período estipulado do cálculo de reajuste do contrato. Foi criado 2 modelos para o cálculo. São eles:

* Modelo 0 - Pro-Rata Temporis (Gráfico Exponencial)

( 1 + i ) ^ ( a / b ) - 1 "Primeiro mês de reajuste - Janeiro" ( 1 + i ) ^ ( a / b ) \* ( 1 + i ) ^ ( c / d ) \* ... - 1 "Segundo mês de reajuste - Fevereiro"

* Modelo 1 - Pro-Rata Proporcional (Gráfico Linear)

Modelo 1 - Pro-Rata Proporcional (Gráfico Linear) ( 1 + i ) \* ( a / b ) - 1 "Primeiro mês de reajuste - Janeiro" (( 1 + i ) \* ( a / b )) \* (( 1 + i ) \* ( c / d )) \* ... - 1 "Segundo mês de reajuste - Fevereiro"   
 Onde:   
 i = taxa de juros a = Número de dias utilizados no mês (Janeiro) b = Número de dias total do mês (Janeiro) c = Número de dias utilizados no mês (Fevereiro) d = Número de dias total do mês (Fevereiro)  
    
 Ignorar deflação:  
 O campo "Ignorar Deflação" no Cálculo de Correção Monetária indica que as variações mensais negativas serão ignoradas ao calcular a variação acumulada.  
 Se este parâmetro estiver marcado, quando o reajuste de Correção Monetária detectar deflação, o valor da Correção Monetária será zero.  
    
 Aplicar Coeficiente Mensalmente:  
 O campo "Aplicar coeficiente mensalmente" no cálculo de Correção Monetária indica que o coeficiente será aplicado mensalmente e não ao final do cálculo.  
 Se este parâmetro estiver marcado, quando o reajuste de Correção Monetária for realizado, o sistema irá somar o percentual informado no campo "Coeficiente" ao percentual calculado da Correção Monetária no mês e depois calcular o valor da parcela. No reajuste dos meses seguintes, o sistema irá acrescentar o percentual do coeficiente em cada mês calculado.   
 Já com o parâmetro desmarcado, quando o reajuste de Correção Monetária for realizado, o sistema irá calcular a Correção Monetária do mês, somar com o valor principal e depois aplicar o percentual informado no campo "Coeficiente". No reajuste dos meses seguintes, o sistema irá acrescentar o percentual do coeficiente somente no final do cálculo da Correção Monetária de todos os meses somado ao valor principal.  
    
 Calcular a correção monetária sobre:

* Saldo devedor Principal da Parcela:

Marque este campo quando o reajuste de Correção Monetária será efetuado sobre o valor original das parcelas.   
 Observação: Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.

Exemplo: Venda efetuada em Fevereiro de 2004 com uma parcela de sinal e 10 parcelas mensais com juros a 1%. - Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:

Juros: 1000,00 + 1% = 1010,00  
Correção Monetária: Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395 CM = (1,00643955 \* 1000) – 1000 = 6,43955  
Correção do mês de abril de 2004 em uma parcela no valor de R$ 1000,00: • Juros: 1000,00 + 2% = 1020,00  
Correção Monetária: Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422 CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1000 ) – 1000 = 14,143059

* Saldo devedor Principal da Parcela + Juros até o mês anterior:

Marque este campo quando o reajuste de Correção Monetária será efetuado sobre o valor original das parcelas mais os Juros de Contrato calculado no mês anterior.   
 Observação: Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.

Exemplo: Venda efetuada em Fevereiro de 2004 com uma parcela de sinal e 10 parcelas mensais com juros a 1%. - Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:

Juros: 1000,00 + 1% = 1010,00  
Correção Monetária: Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395 CM = (1,00643955 \* 1000) – 1000 = 6,43955  
Correção do mês de abril de 2004 em uma parcela no valor de R$ 1000,00:  
Juros: 1000,00 + 2% = 1020,00  
Correção Monetária: Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422 CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1010 ) – 1010 = 14,284490

* Saldo devedor Principal da Parcela + Juros até o mês do reajuste:

Marque este campo quando o valor dos juros de contrato calculado no mês do reajuste de correção monetária será somado ao valor base para o cálculo da Correção Monetária.   
 Observação: Este parâmetro somente será habilitado se o parâmetro "Reajusta correção monetária sobre o valor original mais juros" já estiver sido marcado e se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.   
 Exemplo: Venda efetuada em Fevereiro de 2004 com uma parcela de sinal e 10 parcelas mensais com juros a 1%. - Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:

Juros: 1000,00 + 1% = 1010,00  
Correção Monetária: Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395 CM = (1,00643955 \* 1010) – 1010 = 6,5039455  
Correção do mês de Abril de 2004 em uma parcela no valor de R$ 1000,00:  
Juros: 1000,00 + 2% = 1020,00  
Correção Monetária: Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422 CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1020 ) – 1020 = 14,425920

Observação: Dependendo do tipo do Modelo de cálculo escolhido no componente do tipo Principal desta modalidade, irá ou não habilitar os parâmetros do componente de Correção Monetária.
