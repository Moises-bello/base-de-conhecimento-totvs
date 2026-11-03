---
content_hash: b8c75a0c053b1d37855e4760b646ec6771c0ffa5ab7ee85849007119c163effd
fetched_at: '2026-06-29T00:09:49.543469+00:00'
page_id: '435105316'
product: rm
source: tdn-rm
title: Tipos de Componentes - Correção Monetária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105316
version: 9
---

**Monetária - Componente Modalidade**   
Ao cadastrar ou editar o componente de Correção Monetária da Modalidade da Venda, informe os seguintes campos:  
   
**Moeda:**  
Informe qual índice de reajuste será usado para corrigir as parcelas caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.   
   
**Periodicidade:**   
Informe o prazo mensal para realização dos reajustes de Correção Monetária caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.   
   
**Defasagem:**  
Informe qual a defasagem que o sistema usará para buscar a cotação do índice de correção caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.   
Exceto para o modelo de cálculo Padrão que a defasagem 0, significa 1 (mês anterior), defasagem 1 significa 2 e assim por adiante. **Exemplo:** Defasagem = 2 – Significa que no reajuste, os contratos serão corrigidos com a variação do índice referente a 2 meses anterior a da data do reajuste.

**% Moeda Aplicada:**  
Se preenchido o valor, o reajuste irar descontar a moeda todo mês antes de acumular o valor total, antes de ignorar a deflação ou qualquer outro parâmetro, ou seja, buscou a contação do mês, aplicou o desconto e depois aplica os demais parâmetros.  **Exemplo:** INCC 01/2021 = 0,8% apliquei desconto de 50%, o valor a ser reajustado será de 0,4%, e assim para os demais casos.   
   
**Coeficiente:**  
Informe se além da variação do índice, a parcela será acrescida de outro percentual caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.   
Este percentual é calculado sobre o valor do componente do tipo Principal somado ao valor do componente de CM  
   
**Exemplo:**  
Índice IGP-M + 5% - Informe no campo moeda "IGP-M" e no campo coeficiente "1,05". Serão calculados 5 % sobre a soma do componente do Tipo Principal + componente de CM. Este resultado será somado ao valor de CM.  
   
**Data Base:**  
Informe a data base deste componente. Será através da data base deste componente que o sistema levará em consideração para verificar a data de próximo reajuste, essa data não pode sobrepor a regra de data de referência de entrega e nem vice-versa. Será usada sempre a maior data entre as duas.

Em cenários que envolvem cálculo pro rata, o dia da data base do componente de CM deve ser exatamente o mesmo dia da [Data base para cálculo do vencimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105209) do componente gerador da parcela, para que a correção seja aplicada corretamente.

Exemplo:

Em uma venda com cálculo pro-rata, no qual o componente Mensal (gerador de parcela) foi parametrizado com a *data base para cálculo do vencimento* em **17**/06/2024 e a *data base* do componente de CM parametrizada para **07**/06/2024, somente terá a correção monetária aplicada corretamente na parcela, se o reajuste for executado com a Data de Reajuste igual, ou posterior a **17**/06/2024. Caso este reajuste seja executado com a data de reajuste de **16**/06/2024, por exemplo, a correção monetária será calculada na memória de cálculo do TCGI, porém não será aplicada no componente de CM desta parcela.

**Observação:**  
Se este componente Monetário já existir na Modalidade escolhida para esta venda, este campo será preenchido automaticamente com a data da venda.  
   
**Próximo Reajuste:**   
Informe a data de realização do próximo reajuste deste componente.   
   
**Observação:**  
Se este componente Monetário já existir na Modalidade escolhida para esta venda, este campo será preenchido automaticamente de acordo com a data base e a periodicidade.  
   
**Equilíbrio – Limite (%):**  
Informe o percentual de limite para o modelo de cálculo Equilíbrio caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda.  
   
**Observação:**  
Este campo somente será habilitado se o modelo de cálculo do componente do tipo principal de mesmo grupo for Modelo de Equilíbrio.  
   
**Data de referência para a correção:**  
Informe a data em que o sistema tomará como referência para efetuar os reajustes de Correções.  
As Referências podem ser:

* Data da Venda.
* Data de vencimento da parcela.
* Data de vencimento da primeira parcela.
* Data base da venda.
* Data base do componente.  
     
  **Observação:**  
  O sistema irá buscar a cotação do dia da data de referência, se não encontrar a cotação do dia, irá buscar a cotação do dia 01 do mês em questão.  
     
  **Parâmetros:**  
     
  **Cálculo de Correção Monetária "Pro-Rata Dia":**   
  Pro rata die" é o mesmo que "em proporção ao dia" isto é Correção Monetária incidentes "por dia".   
  É a cobrança proporcional (calculada por dia), feita quando a data do vencimento da parcela não compreende a todo o período estipulado do cálculo de reajuste do contrato foi criado 2 modelos para o cálculo. São eles:  
     
  **Modelo 0 - Pro-Rata Temporis (Gráfico Exponencial)**  
     
  ( 1 + i ) ^ ( a / b ) - 1 "Primeiro mês de reajuste - Janeiro"  
  ( 1 + i ) ^ ( a / b ) \* ( 1 + i ) ^ ( c / d ) \* ... - 1 "Segundo mês de reajuste - Fevereiro"  
     
  i = taxa de juros  
  a = Número de dias utilizados no mês (Janeiro)  
  b = Número de dias total do mês (Janeiro)  
  c = Número de dias utilizados no mês (Fevereiro)  
  d = Número de dias total do mês (Fevereiro)  
     
  **Modelo 1 - Pro-Rata Proporcional (Gráfico Linear)**  
     
  ( 1 + i ) \* ( a / b ) - 1 "Primeiro mês de reajuste - Janeiro"  
  (( 1 + i ) \* ( a / b )) \* (( 1 + i ) \* ( c / d )) \* ... - 1 "Segundo mês de reajuste - Fevereiro"  
     
  i = taxa de juros  
  a = Número de dias utilizados no mês (Janeiro)  
  b = Número de dias total do mês (Janeiro)  
  c = Número de dias utilizados no mês (Fevereiro)  
  d = Número de dias total do mês (Fevereiro)  
     
  **Ignorar deflação:** O campo "Ignorar Deflação" no Cálculo de Correção Monetária indica que as variações mensais negativas serão ignoradas ao calcular a variação acumulada  
  Se este parâmetro estiver marcado, quando o reajuste de Correção Monetária detectar deflação, o valor da Correção Monetária será zero.  
     
  **Aplicar Coeficiente Mensalmente:** O campo "Aplicar coeficiente mensalmente" no cálculo de Correção Monetária indica que o coeficiente será aplicado mensalmente e não ao final do cálculo.  
  Se este parâmetro estiver marcado, quando o reajuste de Correção Monetária for realizado, o sistema irá somar o percentual informado no campo "Coeficiente" ao percentual calculado da Correção Monetária no mês e depois calcular o valor da parcela. No reajuste dos meses seguintes, o sistema irá acrescentar o percentual do coeficiente em cada mês calculado.  
  Já com o parâmetro desmarcado, quando o reajuste de Correção Monetária for realizado, o sistema irá calcular a Correção Monetária do mês, somar com o valor principal e depois aplicar o percentual informado no campo "Coeficiente". No reajuste dos meses seguintes, o sistema irá acrescentar o percentual do coeficiente somente no final do cálculo da Correção Monetária de todos os meses somados ao valor principal.  
     
  **Tipo de Moeda:**  
  Informe se o sistema irá usar para corrigir a correção Monetária a Cotação (Moeda) ou Variação Mensal (índice). Na Cotação (Moeda) iremos informar a cotação acumulada mensalmente. Na Variação Mensal (Índice) iremos informar diretamente o Índice Mensal no cadastro de cotação.

          Diferença dos valores de cotação do índice acumulado e índice mensal:

   
**Referência da Entrega para o Componente:**  
          Informe qual será a data de referência para determinar se o componente terá ação antes ou após a entrega do empreendimento. As datas podem ser:

* Data da Entrega do Empreendimento
* Data do Habite-se
* Data da Entrega das Chaves
* Data da Assinatura  
     
  **Observação:**  
  Esta opção somente estará habilitada se o Modelo de cálculo escolhido no componente do tipo Principal desta modalidade for MODELO PADRÃO.
* Essa data não pode sobrepor a data base e nem vice-versa. Será usada sempre a maior data entre as duas.  
     
  **Aplicar reajuste em:**  
  Informe se este componente de correção irá reajustar as parcelas vincendas, vencidas ou ambas. O sistema toma como base a data do reajuste para verificar se as parcelas estão vincendas ou vencidas.  
     
  **Observação:**  
  Este parâmetro só irá aparecer se o tipo do Modelo de cálculo escolhido no componente do tipo Principal desta modalidade for Modelo Padrão ou Tabela Price.  
     
  **Calcular o valor da CM sobre:**  
     
  Veremos as três opções possíveis de serem usadas para o campo Calcular o valor da CM  sobre.  
     
  **Saldo devedor Principal da Parcela:**  
  Marque este campo quando o reajuste de Correção Monetária será efetuado sobre o valor original das parcelas.  
     
  **Observação:**  
  Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.   
     
  **Exemplo:**  
  Venda efetuada em Fevereiro de 2004 com uma parcela de sinal e 10 parcelas mensais com juros a 1%.
* Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:  
     
  • Juros: 1000,00 + 1% = 1010,00  
     
  • Correção Monetária:  
     
  Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395   
     
  CM = (1,00643955 \* 1000) – 1000 = 6,43955
* Correção do mês de abril de 2004 em uma parcela no valor de R$ 1000,00:  
     
  • Juros: 1000,00 + 2% = 1020,00  
     
  • Correção Monetária:  
     
  Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422  
     
  CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1000 ) – 1000 = 14,143059  
     
  **Saldo devedor Principal da Parcela + Juros do mês anterior ao reajuste:**  
  Marque este campo quando o reajuste de Correção Monetária será efetuado sobre o valor original das parcelas mais os Juros de Contrato calculado no mês anterior.  
     
  **Observação:**  
  Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.   
     
  **Exemplo:**  
  Venda efetuada em Fevereiro de 2004 com uma parcela de sinal e 10 parcelas mensais com juros a 1%.
* Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:  
     
  • Juros: 1000,00 + 1% = 1010,00  
     
  • Correção Monetária:  
     
  Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395   
     
  CM = (1,00643955 \* 1000) – 1000 = 6,43955
* Correção do mês de abril de 2004 em uma parcela no valor de R$ 1000,00:  
     
  • Juros: 1000,00 + 2% = 1020,00  
     
  • Correção Monetária:  
     
  Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422  
     
  CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1010 ) – 1010 = 14,284490  
     
  **Saldo devedor Principal da Parcela + Juros do mês do reajuste:**  
  Marque este campo quando o valor dos juros de contrato calculado no mês do reajuste de correção monetária será somado ao valor base para o cálculo da Correção Monetária.   
     
  **Observação:**  
  Este parâmetro somente será habilitado se o parâmetro "Reajusta correção monetária sobre o valor original mais juros" já estiver sido marcado e se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.   
     
  **Exemplo:**  
  Venda efetuada em Fevereiro de 2004 com uma parcela de sinal e 10 parcelas mensais com juros a 1%.
* Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:  
     
  • Juros: 1000,00 + 1% = 1010,00  
     
  • Correção Monetária:  
     
  Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395   
     
  CM = (1,00643955 \* 1010) – 1010 = 6,5039455
* Correção do mês de Abril de 2004 em uma parcela no valor de R$ 1000,00:  
     
  • Juros: 1000,00 + 2% = 1020,00  
     
  • Correção Monetária:  
     
  Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422  
     
  CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1020 ) – 1020 = 14,425920  
     
  **Observação:**  
  Dependendo do tipo do Modelo de cálculo escolhido no componente do tipo Principal desta modalidade, irá ou não habilitar os parâmetros do componente de Correção Monetária.
