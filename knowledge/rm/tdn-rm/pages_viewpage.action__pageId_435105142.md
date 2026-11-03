---
content_hash: bb3f8f9cd462f4be36745485f0405e3fc192e97a0a7aa2828e5c1e5331badad1
fetched_at: '2026-06-29T00:09:48.403665+00:00'
page_id: '435105142'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis   - Web - Antecipação de Parcelas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105142
version: 7
---

Neste módulo do TOTVS Portal Incorporação, temos ferramentas para o cliente efetuar o acompanhamento do seu financiamento e o pagamento de parcelas antecipadamente. O cliente poderá visualizar o saldo devedor do seu contrato até a data escolhida, visualizar o valor original das parcelas com a correção monetária, juros contratuais e multas e juros das parcelas em atraso, gerar boletos de quaisquer parcelas, vencidas ou vincendas, com valores atualizados on-line na data escolhida pelo cliente.   
Para a utilização da Antecipação de Parcelas no TOTVS Portal Incorporação, foram cirados novos parâmetros no sistema TOTVS Incorporação: Parâmetro Relatório para impressão do boleto e Dados bancários do boleto, que será definido por coligada e por filial. Nos Dados Bancários teremos os parãmetros Filial, Banco para impressão do boleto, Agência e Conta corrente para impressão do boleto que deverão ser preenchidos para a geração de boletos.

**Contexto Incorporação:**  
Ao entrar no módulo Antecipação de Parcelas, será apresentado a seleção de Contexto. Nesta página, iremos selecionar um contrato para a sua vizualização.  
Nessa página mencionada, serão listadas todas as vendas associadas ao cliente logado no TOTVS Portal Incorporação. Serão exibidas as seguintes informações: Número do contrato, Empreendimento, Unidade e SubUnidade. O cliente irá selecionar o contrato para ser apresentado o Plano de Financiamento.

Não será apresentado o Plano de vendas "Distratadas" e  "Em Preparação".

Após a seleção do contrato, será exibida uma página para a seleção do tipo da parcela do contrato selecionado.   
Nessa página, serão listados todos os tipos das parcelas que compõem o contrato selecionado. Haverá também a opção de selecionar todos os tipos de parcelas. O cliente irá selecionar os tipos da parcelas para ser apresentado o Plano de Financiamento.   
Após a seleção do contrato e do tipo da parcela, será apresentado as informações do Contrato e o Plano de Financiamento.

Serão exibidas no topo da página do TOTVS Portal Incorporação as seguintes informações: Código e nome do cliente logado, Número do contrato. Modalidade de Venda, Emprendimento, Unidade e SubUnidade.  
Será apresentado também um Link para selecionar outro Contrato e um Link para selecionar outro Tipo de Parcela. A qualquer momento, o cliente poderá alterar o contrato selecionado. Para isso, basta clicar no link "**Selecionar outro contrato**", que será exibida novamente a página para a seleção do contrato. Poderá também alterar o tipo de parcela selecionado. Para isso, basta clicar no link "**Selecionar outro Tipo de Parcela**", que será exibida novamente a página para a seleção do Tipo de Parcela.

**Data de Posição Para Pagamento:** Será apresentado um campo para que seja informada a data de posição para pagamento a ser considerada no cálculo das parcelas. Esta data será utilizada na simulação do reajuste (correção monetária, juros contratuais, Juros de Mora e Multa de Atraso). Este campo será do formato data e, por default, virá preenchido com a data do sistema. Deverá ser dia útil, ou seja, não poderá ser sábado, domingo ou feriado. O cliente poderá alterar a data de posição para pagamento para a data desejada para o cálculo das suas parcelas, desde que exista índices monetários cadastrados para a nova data.

Na simulação, o contrato e o lançamento financeiro não serão atualizados no banco de dados.

Após informado a data de posição para pagamento, será apresentado as seguintes informações:

**Extrato de Contas a Pagar:**

* Empresa: nome da coligada corrente;
* Filial: nome da filial do contrato de venda selecionado;
* Empreendimento/Unidade/Subunidade: descrição do empreendimento; descrição da Unidade; descrição da Subunidade referente do contrato de venda selecionado;
* Cliente: nome do cliente logado no RM Portal Incorporação;
* Contrato: Número do Contrato;
* Plano de venda: descrição da modalidade da venda;
* Período de referência: data da venda até a data do vencimento da última parcela;
* Emissão: data/hora do sistema;
* Posição para pagamento em: data de posição para pagamento informada;
* Mensagem: Caro cliente, os boletos emitidos a partir deste extrato terão vencimento para o dia <<data de posição para pagamento informada>>. Se desejar outro dia para o vencimento, visualize o seu extrato com uma nova posição para pagamento;
* Será exibido as parcelas recuperadas já reajustadas em um grid com as seguintes colunas:

* + Número da parcela,
  + Tipo da parcela,
  + Data de vencimento,
  + Atraso (número de dias de atraso, se a parcela não estiver em atraso, esta coluna ficará em branco),
  + Principal,
  + Atualização monetária,
  + Juros contratuais,
  + Multa de atraso e Juros de Mora (caso a parcela esteja em atraso, será calculada multa e Mora até a data de posição para pagamento informada),
  + Valor líquido (valor principal + atualização monetária + juros contratuais + multa + mora),
  + Link Imprimir boleto

* Também será exibido o somatório das seguintes colunas do grid:

* + Quantidade de títulos listados no grid,
  + Principal,
  + Atualização monetária,
  + Juros contratuais,
  + Multa, Mora e Valor líquido.

**Imprimir Boleto:**

* Ao clicar no link "Imprimir boleto", o sistema irá: - Recuperar na parametrização do sistema o relatório a ser utilizado na impressão do boleto, a parametrização os dados bancários: Banco, Agência e Conta corrente, definidos para a filial da venda selecionada - Gerar: Nosso número, IPTE, Código de barras. - Executar o relatório a ser utilizado na impressão do boleto.

Será impresso um boleto para cada parcela, não sendo permitido agrupar diversas parcelas e imprimir um único boleto.Parâmetro para Definir Regra de Antecipação !

Parâmetros para definir as regras de antecipação no PDC ou no APP.  **Versão 12.1.34 em diante!!**

* Permite a antecipação de parcelas quando o contrato possuir parcelas em atraso (inadimplente)
* Regras de antecipação:
  + Qualquer parcela - default;
  + Da primeira para a última;
  + Da última para a primeira.

O default dos parâmetros terão o comportamento atual, ou seja, permitir a antecipação mesmo que tenha parcelas em atraso e a regra é a antecipação de qualquer parcela.

Essas regras só terão efeito quando a antecipação for realizada pelo portal ou APP.

Os parâmetros devem seguir a mesma regra dos demais para o PDC.
