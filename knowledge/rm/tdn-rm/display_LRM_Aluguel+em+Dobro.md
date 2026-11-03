---
content_hash: f54d8e850110aa2d85d3a7c0eda7af0e8ee9d78891211548757dba88eb2b9508
fetched_at: '2026-06-29T00:08:57.063825+00:00'
page_id: '353272949'
product: rm
source: tdn-rm
title: Aluguel em Dobro
type: documentation
url: https://tdn.totvs.com/display/LRM/Aluguel+em+Dobro
version: 4
---

Em mês (es) determinado (ex: dezembro) o sistema deve permitir gerar mais uma cobrança do valor de Aluguel.   
Para isso deve ser criado um anexo ao contrato de locação que permita informar:

* Mês (janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro e dezembro) . Não deve ser informada uma data pois dificulta a usabilidade para o usuário
* Cobrar:
  + No mesmo Mês: se o usuário informar, por exemplo, o mês de dezembro e marcar esta opção significa que deve ser gerado o aluguel em dobro com vencimento no mesmo mês, ou seja em dezembro.
  + Mês seguinte: se o usuário informar, por exemplo, o mês de dezembro  e marcar esta opção significa que deve ser gerado o aluguel em dobro com vencimento no mês seguinte, ou seja em janeiro.
* %: o usuário deve informar o percentual que será aplicado sobre o valor do aluguel mensal (minimo), como default trazer 100%. Não permitir valor negativo.
* Data Inicial: se o registro estiver sendo incluído com o contrato de locação ainda "em preparação", trazer como default a "data de inicio da vigência" do contrato de locação. Se o registro estiver sendo incluído com o contrato de locação "Efetivado" trazer como default a atual. Não permitir informar uma data de início menor que a "data de inicio da vigência" do contrato de locação.
* Data Final: não trazer default. Permitir deixar em branco.
* Cobrança Avulsa (sim ou não) - Default="Não"
  + Não: se o campo não estiver marcado significa que o aluguel em dobro será cobrado no mesmo lançamento financeiro do aluguel mensal (mínimo) ;
  + Sim: se o campo for marcado significa que o aluguel em dobro será cobrado em um lançamento financeiro separado e para isso serão necessários os parâmetros:
    - Tipo de Evento: evento do tipo complementar;
    - Busca vencimento: Informar ou Contrato. Mesmo comportamento do Aluguel sobre faturamento.
    - Busca Parâmetro de Integração : Informar ou Contrato. Mesmo comportamento do Aluguel sobre faturamento.Ainda na opção "Sim" para gerar o lançamento financeiro a separado pode ser utilizado o processo já existente de aluguel Complementar processando juntos o Aluguel em Dobro e o Aluguel sobre Faturamento. Neste caso deve ser dada a opção para o usuário selecionar se deseja gerar Aluguel sobre Faturamento E/OU Aluguel em Dobro.   
    Exemplo:  
      
    Este processo pode ser executado através da lista de contratos de locação onde o usuário seleciona os contratos de locação desejados.   
      
    Para o processo de Aluguel Complementar do menu principal permitir processar os laçamentos selecionando multicoligadas
* Criar processo para excluir lançamentos financeiros de aluguéis complementares do contrato de locação. Na tela de processo o sistema deve permitir que o usuário escolha se deseja excluir os lançamentos de Aluguel sobre Faturamento E/OU Aluguel em Dobro. Sugestão: utilizar tela semelhante a tela de geração.
* Se um aluguel em dobro for gerado separadamente a data de Emissão do lançamento financeiro deve seguir o parâmetro da coligada
* Criação de um Anexo de "Parcelas Complementares" no Contrato de Locação com suas respectivas memórias de calculo para identificar as parcelas que foram geradas pelo aluguel em dobro e sobe faturamento. Esta tela é complementar a tela de Lançamentos financeiros que será tratada em outra tarefa e que deve apresentar todo e qq lançamento financeiro associado ao contrato de locação.    
  Exemplo de tela

**Considerações:**

* Um aluguel em dobro ou complementar não poderá ser excluido se já estiver sido Pago.
* Se o alguel em dobro for cobrado junto com o aluguel mensal deve ser levado para o financeiro como um valor de integração. Para isso deve ser criado um parametro da coligada para indicar qual é o valor de integração para aluguel em dobro "Agregado ao Aluguel Mensal";
* Deve ser permitido que o usuário altere os parâmetros de aluguel em dobro associados ao contrato de locação. Quando isso ocorrer uma data final deve ser informada e um novo registro deve ser criado com a data informada pelo usuáiro.
* Se o período de competência for composto por mais de um mês (ex: 15/12 a 14/01) e se neste mês houver **reajuste pró-rata dia**, o sistema deve fazer exatamente o mesmo calculo da cobrança.

Exemplo:

**“Rateio de Índice: Mês Civil” e “Aplicação de Índice: Mês Civil”:**

  Período: 15/12 a 14/01

15/12 a 31/12 = **16 dias**

  (Valor do Aluguel / Dias do Mês)\* Dias Período = R$ 1.000,00/ **31**)\***16** = **R$****516,13**

01/01 a 14/01 = **14 dias**

  Valor do Aluguel Corrigido = Valor do Aluguel \* Variação CM Anual = R$ 1.000,00 \* 0,10= 1.100,00

  (Valor do Aluguel / Dias do Mês)\* Dias Período = R$ 1.100,00/ **31**)\***14** =  **R$496,77**

  Valor a ser cobrado na parcela do mês de reajuste:

**R$ 516,13 + R$496,77**=  **R$1.012,90**

|  |
| --- |
| Data Inicial da Competência              Virada do Mês                             Data Final da Competência  15/12/2017                                01/01/2018                  14/01/2018  |                                        |                                         |  +---------------**16 dias**-----------------------+-------------**14 dias**-------------------+---------------------->  |                                        |                                         |  |                                        +Correção Monetária Anual de 10%  |                                      |                                         |  |             **R$ 516,13** |              **R$ 496,77** |  +----------------**R$ 1.012,90** (Valor da Parcela em 14/01/2018)--------------+ |
