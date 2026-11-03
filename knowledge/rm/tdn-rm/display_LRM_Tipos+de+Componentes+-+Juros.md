---
content_hash: fe6af12099013df64530736ede9fa126a39da5ceb32e3ca550bc7f03b77eb169
fetched_at: '2026-06-29T00:09:49.218072+00:00'
page_id: '435105255'
product: rm
source: tdn-rm
title: Tipos de Componentes - Juros
type: documentation
url: https://tdn.totvs.com/display/LRM/Tipos+de+Componentes+-+Juros
version: 4
---

**Juros - Componente Modalidade**   
 Ao cadastrar ou editar o componente de Juros da Modalidade da Venda, informe os seguintes campos:  
    
 **Juros Mensal(%):**  
 Informe o percentual de Juros de correção do contrato a ser cobrado neste componente caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.  
    
 **Periodicidade da Taxa:** Informe se o valor do percentual de juros informado é ao mês ou ao ano.  
    
 **Observação:**  
 Este campo somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Tabela Price.  
    
 **Periodicidade (Mês):**  
 Informe o prazo mensal para realização dos reajustes de Juros de contrato caso este seja fixo, se não for fixo, deixe o campo em branco para ser informado posteriormente na inclusão de uma venda ou aluguel.  
    
 **Data Próximo Reajuste:**  
 Informe a data que será realizada o próximo reajuste deste componente.   
    
 **Observação:**  
 Se este componente de Juros já existir na Modalidade escolhida para esta venda, este campo será preenchido automaticamente de acordo com a data base e a periodicidade.  
    
 **Tipo de Juros:**  
 Informe se será cobrado juros simples ou composto.   
    
 **Referência de entrega para o Componente:**  
 Informe qual será a data de referência para determinar se o componente terá ação antes ou após a entrega do empreendimento. As referências podem ser:

* Data da Entrega do Empreendimento
* Data do Habite-se
* Data da Entrega das Chaves
* Data da Assinatura  
      
   **Observação:**  
   Esta opção somente estará habilitada se o Modelo de cálculo escolhido no componente do tipo Principal desta modalidade for MODELO PADRÃO.  
      
   **Aplicar reajuste em:**  
   Informe se este componente de Juros irá reajustar as parcelas vincendas, vencidas ou ambas.  
      
   **Parâmetros:**  
      
   **Pro Rata Dia:**   
   Pro rata die" é o mesmo que "em proporção ao dia" isto é juros incidentes "por dia". É a cobrança proporcional (calculada por dia), feita quando a data do vencimento da parcela não compreende a todo o período estipulado do cálculo de reajuste do contrato foi criado 2 modelos para o cálculo. São eles:  
   Modelo 0 - Cálculo dos Juros Pro Rata Proporcional ao numero de dias do Mês
* Juros Simples: (Gráfico Linear)  
   i \* ( a / b ) "Primeiro mês de reajuste - Janeiro"  
   (i \* ( a / b )) + (i \* ( a / b )) "Segundo mês de reajuste - Fevereiro"  
      
   i = taxa de juros  
   a = Número de dias utilizados no mês (Janeiro)  
   b = Número de dias total do mês (Janeiro)  
   c = Número de dias utilizados no mês (Fevereiro)  
   d = Número de dias total do mês (Fevereiro)
* Juros Composto: (Gráfico Exponencial)   
   ( 1 + i ) ^ ( a / b ) - 1 "Primeiro mês de reajuste - Janeiro"  
   ( 1 + i ) ^ ( a / b ) \* ( 1 + i ) ^ ( c / d ) \* ... - 1 "Segundo mês de reajuste - Fevereiro"  
      
   i = taxa de juros  
   a = Número de dias utilizados no mês (Janeiro)  
   b = Número de dias total do mês (Janeiro)  
   c = Número de dias utilizados no mês (Fevereiro)  
   d = Número de dias total do mês (Fevereiro)  
   Modelo 1 - Cálculo dos Juros Pro Rata Proporcional a 30 dias
* Juros Simples: (Gráfico Linear)   
   Período = Data Final – Data Inicial  
   taxa Juros \* (período / 30)
* Juros Composto: (Gráfico Exponencial)   
   Período = Data Final – Data Inicial  
   ((1 + taxa Juros) ^ (período / 30) – 1)  
      
   **Juros Acumulado:**  
   Este campo informa que o reajuste de juros de contrato será calculado acumulativamente, ou seja, quando a periodicidade de reajuste for maior que 1, nos meses em que não houver reajuste, os juros serão acumulado.  
      
   **Exemplo:**  
   Venda efetuada em Janeiro de 2004 com uma parcela de sinal e 10 parcelas mensais, com periodicidade de reajuste de 4 em 4 meses e taxa de juros de 1%.
* Correção do mês de Maio de 2004 em uma parcela no valor de R$ 1000,00:  
               Juros: 1000,00 + 4% = 1040,00
* Correção do mês de Setembro de 2004 em uma parcela no valor de R$ 1000,00:  
               Juros: 1000,00 + 8% = 1080,00  
      
   Se este parâmetro não estivesse marcado, o sistema iria aplicar no mês de Maio apenas os juros de 1 % e no mês de Setembro 2 %.
* Correção do mês de Maio de 2004 em uma parcela no valor de R$ 1000,00:  
               Juros: 1000,00 + 1% = 1010,00
* Correção do mês de Setembro de 2004 em uma parcela no valor de R$ 1000,00:  
               Juros: 1000,00 + 2% = 1020,00  
      
   **Observação:**  
   Este parâmetro somente será marcado se o Prazo de Reajuste for maior que 1 mês e se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão.  
      
   **Exemplo:**  
   Venda efetuada em Janeiro de 2004 com uma parcela de sinal e 10 parcelas mensais, com periodicidade de reajuste de 4 em 4 meses.
* Correção do mês de Maio de 2004 em uma parcela no valor de R$ 1000,00:  
      
   Juros: 1000,00 + 4% = 1040,00
* Correção do mês de Setembro de 2004 em uma parcela no valor de R$ 1000,00:  
      
   Juros: 1000,00 + 8% = 1080,00  
      
   Se este parâmetro não estivesse marcado, o sistema iria aplicar no mês de Maio apenas os juros de 1 % e no mês de Setembro 2 %.  
      
   **Calcular o valor do Juros sobre:**   
      
   Veremos as três opções possíveis de serem usadas para o campo Calcular o valor do Juros sobre.  
      
   **Saldo devedor Principal da Parcela:**  
   Marque este campo quando o reajuste de juros de contrato será calculado sobre o valor original das parcelas.  
      
   **Observação:**  
   Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão  
      
   **Exemplo:**  
   Venda efetuada em Fevereiro de 2004 com 1 parcela de sinal e 10 parcelas mensais.
* Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:  
      
   Juros: 1000,00 + 1% = 1010,00
* Correção do mês de Abril de 2004 em uma parcela no valor de R$ 1000,00:  
      
   Juros: 1000,00 + 2% = 1020,00  
      
   **Saldo devedor Principal da Parcela + CM do mês anterior ao reajuste:**  
   Marque este campo quando o valor monetário calculado no mês anterior ao do reajuste de juros será somado ao valor base para o cálculo dos juros.   
      
   **Observação:**  
   Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão  
      
   **Exemplo:**  
   Venda efetuada em Fevereiro de 2004 com 1 parcela de sinal e 10 parcelas mensais.
* Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:  
      
   • Correção Monetária:  
      
   Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395   
      
   CM = (1,00643955 \* 1000) – 1000 = 6,43955  
      
   • Juros: 1000,00 + 1% = 1010,00
* Correção do mês de Abril de 2004 em uma parcela no valor de R$ 1000,00:  
      
   • Correção Monetária:  
      
   Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422  
      
   CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1000 ) – 1000 = 14,1430597  
      
   • Juros: 1006,43955 + 2% = 1026,568341  
      
   **Saldo devedor Principal da Parcela + CM até o mês do reajuste:**  
   Marque este campo quando o valor monetário calculado no mês do reajuste de juros será somado ao valor base para o cálculo dos juros.   
      
   **Observação:**  
   Este parâmetro somente será habilitado se já estiver sido cadastrado um componente do tipo principal do mesmo grupo e ter o modelo de cálculo igual a Modelo Padrão  
      
   **Exemplo:**  
   Venda efetuada em Fevereiro de 2004 com 1 parcela de sinal e 10 parcelas mensais.
* Correção do mês de Março de 2004 em uma parcela no valor de R$ 1000,00:  
      
   • Correção Monetária:  
      
   Índice de Fevereiro / índice de Janeiro = 302,578 / 300,624 = 1,0064395   
      
   CM = (1,00643955 \* 1000) – 1000 = 6,43955  
      
   • Juros: 1006,43955 + 1% = 1016,5039455
* Correção do mês de Abril de 2004 em uma parcela no valor de R$ 1000,00:  
      
   • Correção Monetária:  
      
   Índice de Março / índice de Fevereiro = 304,894 / 302,578 = 1,00765422  
      
   CM Capitalizada = ( ( 1,00765422 \* 1,00643955 ) \* 1000 ) – 1000 = 14,1430597  
      
   • Juros: 1014,1430597 + 2% = 1034,425920894  
      
   **Observação:**  
   Dependendo do tipo do Modelo de cálculo escolhido no componente do tipo Principal desta modalidade, irá ou não habilitar os parâmetros do componente de Juros.
