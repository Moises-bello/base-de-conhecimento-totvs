---
content_hash: bc8c50503aabbd569c4121115fd482784dd9a5b1d0d64981fe367037e9d29601
fetched_at: '2026-06-29T00:09:54.888009+00:00'
page_id: '445655898'
product: rm
source: tdn-rm
title: Exemplos relacionados ao processo de fatura
type: documentation
url: https://tdn.totvs.com/display/LRM/Exemplos+relacionados+ao+processo+de+fatura
version: 4
---

**Exemplo para utilização do processo de inclusão de fatura**

Existe um lançamento financeiro que deve ser dividido em parcelas.

Utilizando o processo de Inclusão de Fatura é possível gerar vários lançamentos para representar este lançamento, eles podem ser de qualquer valor, mas o somatório será o valor do lançamento original. Os lançamentos gerados ficarão vinculados ao lançamento original, que será baixado apenas quando todos os lançamentos forem baixados.

O lançamento original recebe o nome de “Lançamento Faturado” e os lançamentos gerados recebem o nome de “Vencimento de Fatura”.

**Passo a passo para realizar a Inclusão de Fatura**

Quando estiver faltando alguma informação obrigatória (nome do campo, por exemplo) o botão “Avançar” ficará desabilitado na tela de inclusão de fatura.

1º) configurar os parâmetros que definem regras para a Inclusão de Fatura e geração do lançamento de Vencimento de Fatura;

2º) Selecionar os lançamentos (clicar na linha do registro e pressionar a tecla “espaço”) que serão faturados e iniciar o processo através do ícone “Incluir Fatura”;

3º) selecionar o método para a inclusão, Métodos - Inclusão de Fatura

4º) preencher as informações que serão incluídas no lançamento de Vencimento de Fatura;

Esse passo é realizado apenas no método “Uma fatura para todos os lançamentos selecionados”.

5º) definir como o Número de Documento da Fatura será gerado;

O número do documento da Fatura pode ser gerado automaticamente ou manualmente.

**Automaticamente**

Marcando o parâmetro “Copiar Referência para a Fatura” (Assistente de Implantação de Processos | Etapa Fatura dos Lançamentos Financeiros) ao concluir o processo de Inclusão de Fatura o “Número do Documento” da Fatura incluída é preenchido com o número da “Referência” da Fatura no cadastro de Fatura. Que é sequencial e nunca se repete.

**Manualmente**

Com o parâmetro “Copiar Referência para a Fatura” (Assistente de Implantação de Processos | Etapa Fatura dos Lançamentos Financeiros) desmarcado, é apresentado o campo “Número da Fatura” no processo. Neste campo deve ser informado o número do Documento da Fatura.

**Observações**

O tamanho do número do documento da fatura é definido pelo parâmetro “Tamanho do Número do Documento” (Assistente de Implantação de Processos | Etapa Inclusão dos Lançamentos Financeiros)

O tamanho limite para o Número do Documento da Fatura é de 15 (quinze) posições. Mesmo se no parâmetro “Tamanho do Número – Documento” existir uma quantidade maior, o número será gerado com 15 (quinze) posições.

Quando houver mais de um Cliente/Fornecedor é necessário preencher esta informação para cada um.

Quando houver mais de um Movimento é necessário preencher esta informação para cada um.

Quando houver mais de um Meio de Pagamento é necessário preencher esta informação para cada um.

6º) definir a quantidade de lançamentos que serão gerados;

Informe no campo “Quantidade” a quantidade de lançamento de Vencimento de Fatura que será gerado.

**Observações**

Quando houver mais de um Cliente/Fornecedor e esta informação não for a mesma para todos é necessário selecionar o Cliente/Fornecedor antes de preencher a informação.

Quando houver mais de um Movimento e esta informação não for a mesma para todos é necessário selecionar o Movimento antes de preencher a informação.

Quando houver mais de um Meio de Pagamento e esta informação não for a mesma para todas é necessário selecionar o Meio de Pagamento antes de preencher a informação.

****7º)**** Definir a Data de Vencimento dos lançamentos de Vencimento de Fatura;  
A data de vencimento será a data informada no campo "Data Base".  
 O campo é apresentado preenchido por default com a data do sistema, podendo ser alterado.

**Intervalo em dias**

Caso a "Quantidade" de lançamentos de Vencimento de Fatura seja maior que "1", é possível definir um intervalo em dias entre as datas de vencimento, sendo a primeira data a data informada no campo "Data Base".  
**Exemplo**  
Quantidade = 2  
 Intervalo em dias = 30  
 Data Base = 12/01/2011

A data de vencimento do 1º Vencimento de Fatura será "12/01/2011"  
 A data de vencimento do 2º Vencimento de Fatura será "11/02/2011"

Ou seja, terá um intervalo de 30 dias.

**Manter o mesmo dia de vencimento**Ao invés de definir o intervalo em dias, também é possível "manter o mesmo dia de vencimento", ou seja, marcando esta opção os "dias" de vencimento dos lançamentos de Vencimento de Fatura sempre serão os mesmos, cada um em um mês, sendo a primeira data a data informada no campo "Data Base".

**Exemplo**

Quantidade = 4  
 Data Base = 20/01/2011  
 Manter o mesmo dia de vencimento

A data de vencimento do 1º Vencimento de Fatura será "20/01/2011"  
 A data de vencimento do 2º Vencimento de Fatura será "20/02/2011"  
 A data de vencimento do 3º Vencimento de Fatura será "20/03/2011"  
 A data de vencimento do 4º Vencimento de Fatura será "20/04/2011"

Ou seja, as datas de vencimento terão o mesmo "dia", mas cada um em um mês.  
Caso o "dia" informado na "Data Base" não exista nos meses nos quais deva ser gerado um Vencimento de Fatura o sistema selecionará o primeiro dia anterior.

**Exemplo**

Quantidade = 4  
 Data Base = 31/01/2011  
 Manter o mesmo dia de vencimento

A data de vencimento do 1º Vencimento de Fatura será "31/01/2011"  
 A data de vencimento do 2º Vencimento de Fatura será "28/02/2011"  
 A data de vencimento do 3º Vencimento de Fatura será "31/03/2011"  
 A data de vencimento do 4º Vencimento de Fatura será "30/04/2011"

Ou seja, o dia informado na Data Base foi "31", no mês de fevereiro não existia esse dia então o sistema selecionou o primeiro dia anterior "28", no mês de abril também não existia então o sistema selecionou o dia "30".

**Observações**

Quando houver mais de um Cliente/Fornecedor e esta informação não for a mesma para todos é necessário selecionar o Cliente/Fornecedor antes de preencher a informação.

Quando houver mais de um Movimento e esta informação não for a mesma para todos é necessário selecionar o Movimento antes de preencher a informação.

Quando houver mais de um Meio de Pagamento e esta informação não for a mesma para todas é necessário selecionar o Meio de Pagamento antes de preencher a informação.

8º) Definir os valores de “Multa (% diário)”, “Juros (% diário)” e “Capitalização Mensal” para serem incluídos nos Vencimentos de Fatura;

**Multa (% diário)**

Percentual diário de multa, atribuído nos lançamentos de Vencimento de Fatura no caso de atraso no pagamento, este cálculo será efetuado no processo de Baixa o lançamento.

**Juros (% diário)**

Percentual diário de juros, atribuído nos lançamentos de Vencimento de Fatura no caso de atraso no pagamento, este cálculo será efetuado no processo de Baixa o lançamento.

**Capitalização Mensal**  
 Para Capitalizar os lançamentos de Vencimento de Fatura é necessário informar a taxa, que será calculada no momento do processo de Baixa do lançamento, o sistema irá capitalizar o valor original do lançamento pela taxa indicada neste campo e pelo período da data de emissão até a data da baixa do mesmo.

**Observações**

Quando houver mais de um Cliente/Fornecedor e esta informação não for a mesma para todos é necessário selecionar o Cliente/Fornecedor antes de preencher a informação.

Quando houver mais de um Movimento e esta informação não for a mesma para todos é necessário selecionar o Movimento antes de preencher a informação.

Quando houver mais de um Meio de Pagamento e esta informação não for a mesma para todos é necessário selecionar o Meio de Pagamento antes de preencher a informação.

Os valores de “Valor Multa” e “Valor Juros” informados na janela de “Detalhes dos Vencimentos de Fatura” tem prioridade sobre os valores “Multa (% diário)” e “Juros (% diário)”, ou seja, os valores dos campos “Multa (% diário)” e “Juros (% diário)” não serão levados para os lançamentos de Vencimento de Fatura.

O valor de “Capitalização” informado na janela de Edição do lançamento selecionado tem prioridade sobre o valor de “Capitalização Mensal”, ou seja, o valor do campo “Capitalização Mensal” não será levado para os lançamentos de Vencimento de Fatura.

9º) Definir como o Número de Documento dos Vencimentos de Fatura será gerado;

**Observações**

Quando houver mais de um Cliente/Fornecedor e esta informação não for a mesma para todos é necessário selecionar o Cliente/Fornecedor antes de preencher a informação.

Quando houver mais de um Movimento e esta informação não for a mesma para todos é necessário selecionar o Movimento antes de preencher a informação.

Quando houver mais de um Meio de Pagamento e esta informação não for a mesma para todos é necessário selecionar o Meio de Pagamento antes de preencher a informação.

10º) Definir se será realizado algum processo de Integração Bancária;

**Observações**

Quando houver mais de um Cliente/Fornecedor e esta informação não for a mesma para todos é necessário selecionar o Cliente/Fornecedor antes de preencher a informação.

Quando houver mais de um Movimento e esta informação não for a mesma para todos é necessário selecionar o Movimento antes de preencher a informação.

Quando houver mais de um Meio de Pagamento e esta informação não for a mesma para todos é necessário selecionar o Meio de Pagamento antes de preencher a informação.

11º) Incluir, Editar e Excluir Vencimento de Fatura

**Observações**

Quando houver mais de um Cliente/Fornecedor e esta informação não for a mesma para todos é necessário selecionar o Cliente/Fornecedor antes de preencher a informação.

Quando houver mais de um Movimento e esta informação não for a mesma para todos é necessário selecionar o Movimento antes de preencher a informação.

Quando houver mais de um Meio de Pagamento e esta informação não for a mesma para todos é necessário selecionar o Meio de Pagamento antes de preencher a informação.

12º) Concluir o Processo.

Os Vencimentos de Fatura apresentados na última tela do processo são gerados automaticamente.

**Campo Intervalo em dias, exemplos:**

No campo “Quantidade” é informado “1”;

No campo “Data Base” é informado “01/10/2008”.

Ao concluir a inclusão da fatura é gerado o lançamento:

Lançamento 01 – vencimento: 01/10/2008

**Geração de três lançamentos com o intervalo de 30 (trinta) dias entre as datas de vencimento**

No campo “Quantidade” é informado “3”;

No campo “Intervalo em dias” é informado “30”;  
 No campo “Data Base” é informado “30/09/2008”.

Ao concluir a inclusão da fatura são gerados os lançamentos:

Lançamento 01 – vencimento: 30/09/2008  
 Lançamento 02 – vencimento: 30/10/2008  
 Lançamento 03 – vencimento: 29/11/2008

**Geração de cinco lançamentos com o intervalo de 15 (quinze) dias entre as datas de vencimento**

No campo “Quantidade” é informado “5”;

No campo “Intervalo em dias” é informado “15”;

No campo “Data Base” é informado “30/09/2008”.

Ao concluir a inclusão da fatura são gerados os lançamentos:

Lançamento 01 – vencimento: 30/09/2008

Lançamento 02 – vencimento: 15/10/2008  
 Lançamento 03 – vencimento: 30/11/2008  
 Lançamento 04 – vencimento: 14/10/2008  
 Lançamento 05 – vencimento: 29/11/2008

****Campo Data Base, exemplos:****

Data de Vencimento dos Lançamentos selecionados diferente

Lançamento 01 – vencimento: 19/01/2009  
 Lançamento 02 – vencimento: 20/01/2009  
 Lançamento 03 – vencimento: 21/01/2009

A data apresentada no campo “Data Base” é “18/01/2009”, ou seja, a data do “Sistema”.

Data de Vencimento dos Lançamentos selecionados igual

Lançamento 01 – vencimento: 20/01/2009  
 Lançamento 02 – vencimento: 20/01/2009  
 Lançamento 03 – vencimento: 20/01/2009

A data apresentada no campo “Data Base” é “20/01/2009”, ou seja, a “Data de Vencimento” dos lançamentos selecionados.

****Manter o mesmo dia de vencimento, exemplos:****

Exemplo da geração de um lançamento

No campo “Quantidade” é informado “1”;  
 No campo “Data Base” é informado “30/09/2008”;  
 O campo “Manter o mesmo dia de vencimento” é marcado.

Ao concluir a inclusão da fatura é gerado o lançamento:

Lançamento 01 – vencimento: 30/09/2008

Exemplo da geração de cinco lançamentos com o mesmo dia de vencimento

No campo “Quantidade” é informado “5”;  
 No campo “Data Base” é informado “30/09/2008”;  
 O campo “Manter o mesmo dia de vencimento” é marcado.

Ao concluir a inclusão da fatura são gerados os lançamentos:

Lançamento 01 – vencimento: 30/09/2008  
 Lançamento 02 – vencimento: 30/10/2008  
 Lançamento 03 – vencimento: 30/11/2008  
 Lançamento 04 – vencimento: 30/12/2008  
 Lançamento 05 – vencimento: 30/01/2008

No campo “Quantidade” é informado “5”;  
 No campo “Data Base” é informado “15/09/2008”;  
 O campo “Manter o mesmo dia de vencimento” é marcado.

Ao concluir a inclusão da fatura são gerados os lançamentos:

Lançamento 01 – vencimento: 15/09/2008  
 Lançamento 02 – vencimento: 15/10/2008  
 Lançamento 03 – vencimento: 15/11/2008  
 Lançamento 04 – vencimento: 15/12/2008  
 Lançamento 05 – vencimento: 15/01/2008

**Gerar Número do Documento de acordo com as opções, exemplo:**

No processo de Inclusão de Fatura é informada a “Quantidade” de “6” Vencimentos de Fatura.

É marcada a opção “Gerar Número do Documento de acordo com as Opções”.

No campo “Número Base” é informado “222”.

No campo “Separador” é selecionado “/”.

No campo “Parcela Inicial” é informado “1”.

Ao concluir a inclusão são gerados os lançamentos:

Lançamento 1 – número do documento 000222/1  
 Lançamento 2 – número do documento 000222/2  
 Lançamento 3 – número do documento 000222/3  
 Lançamento 4 – número do documento 000222/4  
 Lançamento 5 – número do documento 000222/5  
 Lançamento 6 – número do documento 000222/6

**Proporcionalizar Valores dos lançamentos de Vencimento de Fatura, exemplo:**

Selecionados dois lançamentos:

Lançamento 1 – Valor Original R$ 650,30  
 Lançamento 2 – Valor Original R$ 650,30

Na janela “Edição dos Vencimentos de Fatura” do processo é apresentado:

Lançamento de Vencimento 1 – Valor Original R$ 650,30  
 Lançamento de Vencimento 2 – Valor Original R$ 650,30

Vencimentos - Valor Original: 1.300,60  
 Fatura – Valor Original: 1.300,60

É editado o primeiro lançamento de Vencimento de Fatura e alterado o Valor Original para 700,00.

Ao confirmar a edição o sistema oferece a possibilidade de proporcionalizar os valores, caso seja informado que “NÃO” é apresentado:

Lançamento de Vencimento 1 – Valor Original R$ 700,00

Lançamento de Vencimento 2 – Valor Original R$ 650,30

Vencimentos - Valor Original: 1.350,30  
 Fatura – Valor Original: 1.300,60

Caso seja informado que “SIM” é apresentado:

Lançamento de Vencimento 1 – Valor Original R$ 700,00  
 Lançamento de Vencimento 2 – Valor Original R$ 600,60

Vencimentos - Valor Original: 1.300,60  
 Fatura – Valor Original: 1.300,60

****Contabilização - Vencimento de Fatura****

Passo a Passo de como incluir Lançamento de Vencimento de Fatura com informações Contábeis.

1º) Parametrização;

No Assistente de Implantação de Processos devem ser realizadas as seguintes parametrizações:

Etapa Contabilização do Financeiro:

Marcar os parâmetros:

Usar Integração Contábil;  
 Usar Evento Contábil.

No parâmetro “Tabela Default para Evento” selecionar uma Tabela para default, ou seja, essa Tabela possui em seu cadastro Eventos Contábeis, ao ser incluída no lançamento de Vencimento de Fatura o sistema buscará automaticamente os Eventos Contábeis da Tabela.

2º) Informar a Tabela Default para Evento Contábil;

A Tabela Default deve ser incluída no lançamento a ser faturado ou dentro do processo.

**Observações**

Só é possível informar a Tabela Default dentro do processo quando é utilizado o método “Uma fatura para todos os lançamentos selecionados ”.

Se for selecionado mais de um lançamento para faturamento e o Tipo Contábil do lançamento de Vencimento de Fatura for “Contábil”, a Tabela Default para Evento Contábil deve ser a mesma para todos os lançamentos. Caso não seja, a Inclusão da Fatura não será permitida.

3º) definir o Tipo Contábil;

Se o Tipo Contábil do lançamento selecionado para faturamento for “Contábil”, o Tipo Contábil do lançamento de Vencimento de Fatura poderá ser “Contábil” ou “Baixa Contábil”, essa definição deve ser feita através do campo “Tipo Contábil” apresentado no processo de Inclusão de Fatura.

4º) concluir o processo de Inclusão de Fatura;

O lançamento de Vencimento de Fatura é gerado, se for “Contábil”, com as informações contábeis preenchidas, se for “Baixa Contábil”, sem informações contábeis.

5º) Contabilização da Baixa.

Se o lançamento de Vencimento de Fatura for do Tipo Contábil “Baixa Contábil”, o preenchimento da contabilização é realizado no processo de Baixa.
