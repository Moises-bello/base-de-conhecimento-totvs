---
content_hash: 2774d2a3fe002062291b786b5bbea741225c9efd4b370d2ac7423805769b0ee7
fetched_at: '2026-06-29T00:09:47.254949+00:00'
page_id: '435105012'
product: rm
source: tdn-rm
title: Aluguel Complementar - Importação de Medição de Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105012
version: 16
---

Este processo tem como função facilitar a inserção das medições dos Locatários no sistema.

Ao executar o processo é exibida uma tela com os seguintes campos:

**Manter configurações para próxima importação:** Marcando este checkbox, as configurações feitas serão salvas, e numa próxima importação será possível utilizar as mesmas informações, ou alterar apenas as informações pontuais para importação.

Forma Seleção do Arquivo

Possibilita informar como será a seleção do arquivo de planilha para inserção das medições. Possui as seguintes opções:

* **Arquivo Excel Local:** Ao selecionar essa opção é exibido o campo "Arquivo de Planilha", onde é possível informar o caminho na máquina, em que o sistema está sendo executado, da planilha a ser importada;
* **Planilha Banco de Dados:** Ao selecionar essa opção é exibido o campo "Planilha Banco de Dados", onde será exibido os registros de planilha cadastrados na base RM;
Células dos Campos

Nessa área será configurado quais as células da Planilha possui a informação para importação da medição. Possui os seguintes campos:

* **Nome da Planilha:** Possibilita informar o nome da Planilha do arquivo importado que será utilizada;
* **Caixa de Forma de seleção do contrato:** Nesta caixa temos duas opções são elas Contrato de locação e Número do contrato de locação.
  + **Contrato de locação:** Possibilita informar a célula que possui o código identificador do contrato de locação a qual será associada a medição importada. Caso na planilha possua mais de um código de contrato de locação, cada linha irá gerar uma medição para o respectivo Contrato indicado;
  + **Número contrato de locação:** Caso esta opção esteja marcada, ao realizar a importação o sistema irá verificar o contrato de locação que possuí o Número contrato de locação preenchido que corresponda com a planilha usada na importação.

Observações

* O campo Número contrato de locação tem que ser único para cada contrato. Caso este campo esteja repetido entre os contratos existentes, a importação não será realizada.
* Caso o Número contrato de locação informado na planilha não seja encontrado será gerado um log para o mesmo, e os demais encontrados importados normalmente.
* Para garantir o sucesso da importação, as referências de célula devem ser preenchidas obrigatoriamente no padrão **Coluna/Linha** (ex: **A1, B1, C1**). O uso de formatos diferentes impedirá o reconhecimento dos dados pelo sistema.

* **Competência:** Possibilita informar a célula que possui a Competência da Medição;
* **Data Medição:** Possibilita informar a célula que possui a Data Medição ;
* **Valor Faturado:** Possibilita informar a célula que possui o Valor do faturamento da Medição;
* **Data de Vencimento**: Possibilita informar a célula que possui a data de vencimento do lançamento complementar que será gerado a partir da medição.
  + Se a data de vencimento não for informada na planilha, então o sistema irá calcular utilizando a regra de vencimento informada nos parâmetros do aluguel complementar do contrato. Neste caso a data de vencimento será sempre igual ou posterior à data de medição de acordo com o dia cadastrado na regra. Exemplo: Data da medição = 10/08/2022 e dia do vencimento da regra igual a 5. Portanto a data de vencimento será igual a 05/09/2022
* **Valor Faturado 2:** Possibilita informar a célula que possui o Valor Faturado 2 dos contratos de Shopping. Este campo não é obrigatório. Caso o faturamento não seja do tipo composto e não possua percentual de faturamento 2 em sua faixa, os valores não serão importados.
* **Valor Bruto do Faturamento:** Possibilita informar a célula que possui o Valor Bruto do Faturamento dos contratos de Shopping. Este campo não é obrigatório. Caso o faturamento não esteja marcado para informar valor bruto os valores não serão importados.
* **Valor Bruto do Faturamento 2:** Possibilita informar a célula que possui o Valor Bruto do Faturamento 2 dos contratos de Shopping. Este campo não é obrigatório. Caso o faturamento não seja do tipo composto, os valores não serão importados.
* **Substituir medições existentes**: Possibilita substituir as medições existentes no contrato na competência da medição.

Observação

Possibilita informar a célula que possui Observação da Medição. Este campo não é obrigatório;

Validações

O Processo de **Importação de Medição de Faturamento** realiza validações para que a medição seja realizada:

* Número do contrato de locação em mais de um contrato:
  + O campo Número contrato de locação tem que ser único para cada contrato. Caso este campo esteja repetido entre os contratos existentes, a importação não será realizada, logo será exibido no log do processo a seguinte mensagem:  O número contrato de locação xxx está associado a mais de um ao contrato locação. A importação não pode ser realizada para o contrato locação yyy.
* Faturamento Composto:
  + Caso o campo Valor Faturado 2 esteja definido nos parâmetros do processo, é necessário que o contrato possua faturamento composto definido em faixas do Aluguel Complementar para que seja importado os valores, neste caso os demais campos serão importados e será exibido a seguinte mensagem: Os contratos, não possuem definição de faturamento composto. Portanto apenas os valores de 'faturamento 2' não serão registrados. O Contrato de locação 'XXX' não possui faturamento composto.
* Competências duplicadas:
  + Caso o parâmetro "**Substituir medições existentes**", estiver desmarcado e o contrato conter medições para mesma competência, a medição não será importado e será exibido a seguinte mensagem: Não é permitido em um contrato de locação haver duas medições para a mesma competência.
* Para contratos rescindidos ou distratados, será possível inserir medições, contanto que sejam cadastradas em períodos que compreendam o tempo de vigência do contrato de locação.
Para que seja possível executar a importação da planilha, é necessário clicar no botão "Visualizar". Dessa forma a área de Pré-Visualização dos Dados, será preenchida. Dessa forma será possível verificar os dados importados antes de finalizar a importação.
