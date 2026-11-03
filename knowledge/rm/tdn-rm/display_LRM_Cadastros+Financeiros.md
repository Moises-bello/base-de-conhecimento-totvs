---
content_hash: a8332787677172ab2d48fb393b6f79ea11f2bc14a370287ab1858a666bbeae60
fetched_at: '2026-06-29T00:10:05.366600+00:00'
page_id: '452719285'
product: rm
source: tdn-rm
title: Cadastros Financeiros
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastros+Financeiros
version: 66
---

# **Parametrização dos Lançamentos Financeiros**

Cadastro de ocorrências financeiras, como líquido salarial, rescisão e encargos mensais (Guia INSS e DIRF), entre outros, que  poderão ser lançadas para o departamento financeiro a partir do menu Encargos | Financeiro | Geração dos Lançamentos, disponível no TOTVS Folha de Pagamento

**TIPOS DE LANÇAMENTO FINANCEIRO**

Selecione o tipo de lançamento financeiro que identificará sua finalidade. O cadastro de Tipos de Lançamentos Financeiros devem ser realizados através de uma tabela dinâmica, no menu Administração de Pessoal | Cadastros | Cadastros Globais | Tabelas Dinâmicas.

Segue abaixo os tipos de lançamentos válidos para este campo:

**Líquido Salarial**

É a diferença entre a soma dos valores de proventos e descontos dos eventos cadastrados na ficha financeira do funcionário para o mês e ano de competência especificados. Não são considerados funcionários que estão demitidos (situação igual a 'D').

**Líquido de Rescisão**

O valor do lançamento será igual a soma dos proventos menos os descontos da movimentação de rescisão do funcionário.

**Observação 1:**

Se o sistema estiver parametrizado para fazer a distribuição por centro de custo dos lançamentos, esta será calculada com base na movimentação por centro de custo da rescisão.

**Observação 2:**

Verificação de duplicidade

Os lançamentos de rescisão feitos com a opção Individual por Funcionário são classificados internamente como sendo de rescisão. Essa classificação permite ao sistema detectar, durante as gerações seguintes, se o usuário está tentando gerar um novo lançamento de rescisão para o mesmo funcionário e neste caso vai emitir um erro no log.

Se o lançamento englobar valores de rescisão complementar, ele não será classificado como rescisão, sendo possível gerar quantos forem necessários.

**Exemplo:**

Funcionário demitido no período 1, com rescisão complementar no período 2:

O lançamento do período 1 será classificado como rescisão. O sistema vai gerar um erro se for feito outro lançamento de rescisão para o mesmo funcionário.

O lançamento do período 2 não será classificado como rescisão, podendo ser gerados outros lançamentos de rescisão complementar para o mesmo funcionário.

O lançamento dos períodos 1 e 2 simultaneamente terão o valor da soma das rescisões. Não será classificado como rescisão, podendo ser gerados outros lançamentos de rescisão e/ou rescisão complementar para o mesmo funcionário.

**Líquido de Férias**

É a diferença entre proventos e descontos dos eventos cadastrados no recibo de férias dos funcionários para o mês e ano de competência especificados.

**INSS a Pagar**

É o mesmo valor calculado pela geração da Guia de INSS normal. Este tipo só será utilizado no campo "Parametrização a ser utilizada para lançamento" nos parâmetros específicos da coligada na geração da Guia de INSS (em Encargos | Recolhimento | menu Guia de INSS | botão Guia de INSS).

**IRRF a Pagar**

É a soma dos valores de todos os eventos de código de cálculo de descontos especificados abaixo, subtraindo a soma dos eventos de proventos, que estão na ficha financeira do funcionário para o mês e ano de competência especificados.

Desconto:

* + CC4 - IRRF
  + CC84 - IRRF calculado pelo usuário
  + CC127 - IRRF de participação nos lucros
  + CC346 - IRRF Retificação
  + CC207 - IRRF RRA

Provento:

* + 122 - Restituição de I.R.R.F.

**Observação:**

O evento de código de cálculo 127 será considerado na soma apenas se não for criado um lançamento financeiro do tipo \*IRRF de Participação nos Lucros\*

**Encargos de FGTS**

Não existe tratamento especial para cálculo de FGTS. O valor é o mesmo calculado pelo sistema para o SEFIP. O sistema aplica o percentual de recolhimento sobre a base de cada funcionário individualmente, a soma destes valores constitui o valor total do FGTS à recolher.

FGTS conforme SEFIP.

Esse lançamento é gerado pelo relatório do Sefip. O tipo de arquivo deve ser "Sefip Normal" e na pasta "Lançamentos financeiros", deverá estar marcada a opção "Gerar lançamentos financeiros".

O valor é o mesmo calculado pelo sistema para SEFIP. O sistema aplicará o percentual de recolhimento mais a contribuição social sobre a soma das bases de FGTS e FGTS 13º dos funcionários.

A contribuição social deve ser informada no campo "Acréscimo" no cadastro da parametrização dos lançamentos financeiros.

O rateio por centro de custo é feito com a seguinte prioridade:

a) Rateio que o lançamento segue, definido na parametrização do lançamento.

b) Rateio fixo do funcionário.

**Valor calculado por fórmula**

Gera lançamentos conforme resultado do valor de uma fórmula pré cadastrada.

**IRRF de Férias**

É a soma dos valores de todos os eventos de código de cálculo especificados abaixo que constam no envelope de férias dos funcionários no período de apuração especificados:

* + 030 - IRRF de Férias
  + 061 - IRRF de Diferença de Férias
  + 107 - IRRF de Férias Calculado pelo Usuário
  + 211 - IRRF Férias RRA

**Observação:**

Quando o funcionário tiver movimentação de férias informada no envelope (de folha), mas não tiver o envelope de férias cadastrado (recibo de férias), o sistema irá buscar do envelope do funcionário (de folha), caso contrário, buscará do envelope de férias.

Para a base parametrizada por centro de custo, o sistema irá verificar se o evento de IRRF de Férias tem o campo "Centro de Custo no Evento" preenchido. Caso não esteja preenchido, o sistema buscará do rateio fixo do cadastro do funcionário.

**IRRF de Rescisão**

O valor do lançamento financeiro referente ao recolhimento de imposto de renda constante na movimentação de rescisão do funcionário, será a soma dos valores dos eventos com os seguintes códigos de cálculos:

* + 004 - IRRF
  + 030 - IRRF de férias
  + 049 - IRRF de 13º salário
  + 061 - IRRF de diferença de férias
  + 084 - IRRF calculado pelo usuário
  + 106 - IRRF 13º calculado pelo usuário
  + 107 - IRRF de férias calculado pelo usuário
  + 127 - IRRF de participação nos lucros
  + 340 - Diferença de IRRF 13º Salário
  + 346 - IRRF Retificação
  + 347 - IRRF 13º Retificação
  + 348 - IRRF Férias Retificação
  + 207 - IRRF RRA
  + 211 - IRRF Férias RRA
  + 215 - IRRF 13º RRA

E subtraindo os valores dos eventos com os seguintes códigos de cálculo:

* + 052 - Restituição I.R.R.F. 13º Salário
  + 122 - Restituição de I.R.R.F.
  + 172 - IRRF 13º Sal descontado p/ previd ref lic maternidade

**Observação:**

O evento de código de cálculo 127 será considerado na soma apenas se não for criado um lançamento financeiro do tipo \*IRRF de Participação nos Lucros\*

**FGTS 13º**

O sistema aplica o percentual de recolhimento sobre a base de cada funcionário individualmente, a soma destes valores constitui o valor total do FGTS a recolher.

**INSS 13º a pagar**

É o mesmo valor calculado pela geração da Guia de INSS 13º (Encargos | Recolhimento | menu Guia de INSS | botão Guia de INSS).

**Atenção:**

Este tipo só será utilizado no campo "Parametrização a ser utilizada para lançamento" em Encargos | Recolhimento | menu Guia de INSS | botão Guia de INSS.

**IRRF 13º a pagar**

É a soma dos valores de todos os eventos de código de cálculo especificados abaixo, que constam na movimentação no período de apuração especificados:

* + 049 - IRRF 13º Salário
  + 106 - IRRF 13º Salário Calculado pelo Usuário
  + 340 - Diferença de IRRF 13º Salário
  + 347 - IRRF 13º Retificação
  + 215 - IRRF 13º Salário RRA

E subtraindo os valores dos eventos com os seguintes códigos de cálculo:

* + 052 - Restituição I.R.R.F. 13º Salário
  + 172 - IRRF 13º Sal descontado p/ previd ref lic maternidade

**Total da GRFC**

O Lançamento Financeiro será feito com base no total calculado pela GRFC.

**Atenção:**

Este tipo só será utilizado no campo "Parametrização a ser utilizada para lançamento" em Rescisão | Relatórios | GRFC/GRRF.

**Total da Pensão**

É a soma da movimentação constante na pasta de Movimento da Pensão (Cadastros | Funcionários | Base de Cálculo | Dependentes | Movimento da Pensão) de funcionários referentes à Pensão Alimentícia para o mês e ano de competência especificados. São computados os seguintes eventos com códigos de cálculos:  13, 195, 394, 113,197, 319, 326, 396, 397, 120, 196, 395 e 121

**Pensão Folha**

É a soma da movimentação constante na pasta de Movimento da Pensão Cadastros | Funcionários | Base de Cálculo | Dependentes | Movimento da Pensão do funcionário referente à Pensão Alimentícia Judicial e as diferenças para o mês e ano de competência especificados.  São computados os seguintes eventos com códigos de cálculos: 13, 195 e 394

**Pensão Férias**

É a soma da movimentação constante na pasta de Movimento da Pensão Cadastros | Funcionários | Base de Cálculo | Dependentes | Movimento da Pensão do funcionário referente à Pensão Alimentícia sobre Férias e as suas diferenças para o mês e ano de competência especificados. São computados os seguintes eventos com códigos de cálculos: 113, 197, 319, 326, 396 e 397

**Pensão 13º**

É a soma da movimentação constante na pasta de Movimento da Pensão Cadastros | Funcionários | Base de Cálculo | Dependentes | Movimento da Pensão do funcionário referente à Pensão Alimentícia sobre 13º Salário e as suas diferenças para o mês e ano de competência especificados.  São computados os seguintes eventos com códigos de cálculos: 120, 196 e 395

**Pensão Participação nos Lucros**

É a soma da movimentação constante na pasta de Movimento da Pensão Cadastros | Funcionários | Base de Cálculo | Dependentes | Movimento da Pensão do funcionário referente à Pensão Alimentícia sobre Participação nos Lucros para o mês e ano de competência especificados. É computado o evento com o código de cálculo 121.

**Atenção:**

Para que o sistema proceda corretamente, a parametrização do lançamento financeiro para os tipos de pensão deverá ser agrupada por dependente.

**Total de IRRF**

Neste tipo de lançamento são somados os demais tipos de lançamento de IRRF (IRRF de Férias, IRRF 13°, IRRF Folha, IRRF Rescisão, IRRF de participação nos lucros).

**IRRF de Participação nos Lucros**

É a soma dos valores de todos os eventos de código de cálculo 127 - IRRF de participação nos lucros, que constam na movimentação no período de apuração especificados.

**Total Guia INSS DCTFWeb**

Refere-se à soma dos valores totais enviados por meio do eSocial que compõem a DARF gerada na DCTFWeb em relação ao eSocial. O lançamento pode ser efetuado por filial ou coligada e tem a opção de ser rateado por centro de custo ou departamento.

É importante destacar que, atualmente, o valor da retenção 9.711/68 é enviado por meio da REINF. Diante dessa mudança, esse valor não faz mais parte do lançamento financeiro da folha de pagamento. Veja mais detalhes em:

Importante!

1. Não serão utilizados filtros de quebra de seção, seleção de funcionário, agrupamentos e períodos para esse tipo de lançamento financeiro.
2. Para realizar a validação do valores utilize .
3. Para realizar o cálculo dos valores dos encargos sociais (terceiros, patronal e outros) no lançamento financeiro, é fundamental que o parâmetro "**Discriminar Percentual de Terceiros**" esteja marcado. Além disso, é necessário garantir que os percentuais estejam cadastrados corretamente na seção [Cadastros | Seções | Anexos | Histórico de Percentuais para INSS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=496388652). Vale ressaltar que, nos casos em que não há recolhimento, como é comum em empresas filantrópicas isentas de determinados encargos, é fundamental preencher os percentuais com "0-zero".  Este procedimento assegura a precisão e a consistência no cálculo dos encargos.
4. A rastreabilidade do lançamento financeiro existente foi desenvolvida especificamente para funcionários cadastrados na folha de pagamento, sendo a chapa o identificador utilizado.
5. Com o intuito de evitar divergências durante a conferência, o **Relatório de Conferência de INSS Patronal** sempre levará em consideração os autônomos registrados no TOTVS Gestão Financeira. Portanto, o parâmetro "Desconsiderar Autônomos TOTVS Gestão Financeira" não será aplicado no referido relatório. Essa abordagem visa garantir a consistência e a coerência dos registros, facilitando o processo de verificação e prevenindo possíveis discrepâncias.

**Total Guia INSS DCTFWeb 13º Salário**

Refere-se à soma dos valores totais enviados por meio do eSocial que compõem a DARF gerada na DCTFWeb anual, específica para o 13º salário. O lançamento pode ser realizado por filial ou coligada e tem a opção de ser rateado por centro de custo ou departamento.

Importante!

1. Não serão utilizados filtros de quebra de seção, seleção de funcionário, agrupamentos e períodos para esse tipo de lançamento financeiro.
2. Para realizar a validação do valores utilize .
3. Para realizar o cálculo dos valores dos encargos sociais (terceiros, patronal e outros) no lançamento financeiro, é fundamental que o parâmetro "**Discriminar Percentual de Terceiros**" esteja marcado. Além disso, é necessário garantir que os percentuais estejam cadastrados corretamente na seção [Cadastros | Seções | Anexos | Histórico de Percentuais para INSS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=496388652). Vale ressaltar que, nos casos em que não há recolhimento, como é comum em empresas filantrópicas isentas de determinados encargos, é fundamental preencher os percentuais com "0-zero".  Este procedimento assegura a precisão e a consistência no cálculo dos encargos.
4. A rastreabilidade do lançamento financeiro existente foi desenvolvida especificamente para funcionários cadastrados na folha de pagamento, sendo a chapa o identificador utilizado.

**Total Guia FGTS Digital**

É a soma dos valores totais da Guia FGTS Digital (GFD). O lançamento pode ser efetuado por filial, lotação tributaria ou coligada e tem a opção de ser rateado por centro de custo ou departamento.

* + **Mensal**

Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando todos os funcionários, inclusive demitidos, com exceção demitidos com os tipos de demissão com direito a saque de FGTS.

* + **Rescisório**

Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando todos os funcionários demitidos com o tipo de demissão que tem direito a saque de FGTS e que possuem o parâmetro “**FGTS Mês anterior será recolhido na GRRF/FGTS Digital**“ desmarcado na rescisão.

* + **Rescisório + Mensal**

Ao selecionar esse tipo, o sistema irá gerar o lançamento considerando todos os funcionários demitidos com o tipo de demissão que tem direito a saque de FGTS e que possuem o parâmetro “**FGTS Mês anterior será recolhido na GRRF/FGTS Digital**“ marcado na rescisão, considerando o mês da demissão e o mês anterior a demissão. Para atender a situação descrita no [Manual de Orientação do FGTS DIGITAL - Página 80](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-do-orientacao-do-fgts-digital-versao-1-1-01-03-2024.pdf)

Importante!

1.O agrupador "Lotação tributária" só será habilitado quando a base estiver parametrizada para utilizar Tomador de serviço e irá considerar o valor retornado pelo RET.  

2. Na competência de **dezembro**, ao realizar a geração por período, não é permitido selecionar períodos que são de **Folha Mensal** e o **13º Salário** simultaneamente. Os lançamentos devem ser processados separadamente apontando cada período ou através da opção **'Todos'**

Veja mais detalhes na documentação [link](https://tdn.totvs.com/pages/viewpage.action?pageId=834247089)

**TIPO DE DOCUMENTO**

Selecione o tipo de documento, que será transferido para o RM Fluxus ao ser gerado o lançamento financeiro no RM Labore.

**Exemplo:**

NF- Nota Fiscal

**Observação:**

01 - Neste campo só serão apresentados os Tipos de Documento cuja Classificação seja "A Pagar" ou "A Pagar e a Receber".

02 - O cadastro de Tipos de Documento no RM Fluxus possui um campo chamado Classificação. Quando essa classificação é "Gera IRRF", "Gera INSS" ou "Gera IRRF e INSS", esse documento não é disponibilizado no RM Labore pois caso contrário o RM Fluxus geraria automaticamente valores de IR e INSS para os lançamentos que tivessem esse tipo de documento.

**CÓD. FORNECEDOR**

Informe o código para o cliente/fornecedor. Não é permitido a inclusão de códigos repetidos, portanto, um código somente refere-se a um determinado cliente/fornecedor. O campo é alfanumérico, definido através da máscara informada em RM| Back Office| Gestão Financeira| Ambiente| Configuração| Parâmetros| Cliente/ Fornecedor| Máscara do Código (no RM Fluxus).

**Observação 1:**

Quando houver dois códigos de Fornecedor iguais (coligada corrente e coligada global), ao informar o código o sistema acatará o código do Fornecedor da coligada corrente. Se o usuário desejar informar o código do Fornecedor da coligada global, o mesmo deverá ser selecionado pelo nome.

**Observação 2:** Neste campo somente serão apresentados Cód. Fornecedores ativos. Para isto, o campo "Ativo" em RM| Back Office| Gestão Financeira| Cadastros| Clientes Fornecedores| Identificação deverá estar marcado.

**Observação 3:** Se o campo contiver o código do Cód. Fornecedor, mas não apresentar o nome do mesmo, é sinal de que o Cliente/Fornecedor foi desativado em RM| Back Office| Gestão Financeira| Cadastros| Clientes Fornecedores| Identificação .

**Observação 4:** Neste campo só serão apresentado os Fornecedores que forem "Fornecedores" ou "Ambos", "Globais" ou não e "Ativos".

**Observação 5:** Caso a coligada possua licença de uso do Sistema de Controle Financeiro RM Fluxus e nos parâmetros do RM Fluxus, item "Parâmetros Lançamentos", esteja desmarcado o parâmetro "Permite Globais", não será possível associar em campos de cadastros do RM Labore, Cliente/Fornecedor que foram cadastrados como "Global".

**FÓRMULA**

Se o tipo da ocorrência for "Valor calculado por fórmula" este campo indicará qual fórmula que deverá ser utilizada no lançamento financeiro.

**APLICAR ARREDONDAMENTO SOBRE O VALOR TOTAL DO LANÇAMENTO**

Marque este parâmetro para que o sistema faça a soma de todos os valores que compõem o lançamento antes de realizar o arredondamento.

**RATEIO QUE LANÇAMENTO SEGUE**

Deve ser informado neste campo o código do rateio definido em CADASTRO | RATEIO DE EVENTOS. O Lançamento Financeiro com informação neste campo não seguirá o Rateio Fixo definido no cadastro de funcionários e SIM, seguirá ocorrência dos eventos que foram cadastrados no Rateio por Evento para que ele seja calculado. Ele só seguirá o Rateio Fixo definido no cadastro de funcionários, se os eventos cadastrados no Rateio por Evento não existirem na movimentação do funcionário.

**Atenção:**

Para os tipos de lançamentos "13-Total da GRFC", "4-INSS a Pagar" e "11-INSS 13º a Pagar", o sistema sempre irá utilizar a informação do campo "Rateio que o Lançamento Segue", mesmo quando o funcionário tiver o "Rateio Fixo" preenchido no cadastro. Essa situação é diferenciada devido estes lançamentos utilizarem os valores calculados através dos módulos de GPS ou GRFC.

**PERÍODO CÁLCULO DO RATEIO**

Este campo é de preenchimento obrigatório caso o parâmetro "Rateio que o lançamento segue" seja marcado. Nele poderá ser informado os seguintes períodos:

**1 - Mês Atual** - fará o rateio conforme os rateios fixos informados no cadastro do funcionário

**2 - Período Aquisitivo** - fará o rateio conforme os rateios realizados durante o período aquisitivo de Férias.

**3 - Ano de Competência** - fará o rateio conforme os rateios realizados durante o ano de competência atual.

**4 - Mês Anterior** - fará o rateio de acordo com o rateio por centro de custo utilizado no mês anterior, tomando como base, a ficha financeira por centro de curto. Quando essa movimentação não existir o sistema deverá buscar o centro de custo do "Rateio Fixo" do funcionário.

**5- Competência passada no Processo -**fará o rateio conforme os rateios realizados durante o ano competência passada.

**COMPLEMENTO DE HISTÓRICO**

Este campo será utilizado pelo usuário que desejar acrescentar maiores informações no histórico de lançamentos financeiros.

**FÓRMULA PARA COMPLEMENTO DE HISTÓRICO**

Além do histórico padrão e o complemento do histórico, o usuário poderá acrescentar mais informações no histórico do lançamento através de fórmulas. Para isto, o usuário deverá cadastrar previamente a fórmula desejada e selecioná-la neste campo.

**Exemplo:**

**Complemento de Histórico:**

Lançamento Financeiro ref. ao mês atual

Fórmula para Complemento de Histórico: MES (fórmula retorna o Mês competência atual).

Ao processar o lançamento financeiro o Complemento de Histórico gerado será o número da competência atual do RM Labore.

**Observação:**

Informando uma fórmula com a variável PAR serão levados para o complemento do histórico do lançamento financeiro o mês, o ano e o(s) período(s) da competência que está sendo gerado o lote.

O retorno da variável PAR assume dois formatos:

Formato 1 - Quando for(em) selecionado(s) período(s) específico(s) na competência:

MM-AAAA-P, onde:

MM = Mês da competência

AAAA = Ano da competência

P = Período(s) \[quando houver mais de um período, aparecem separados por vírgula\]

**Exemplo:**

01-2004-1,2 onde 01 = Janeiro

2004 = Ano de 2004

1,2 = Períodos 1 e 2

Formato 2 - Quando NÃO for(em) selecionado(s) período(s) específico(s) na competência:

  MM-AAAA, onde:

MM = Mês da competência

AAAA = Ano da competência

**Exemplo:** 12-2003 onde:

12 = Dezembro 2003 = Ano de 2003

**Atenção:**

O retorno da variável PAR na contabilização é sempre STRING, e os valores de Mês, Ano e Período(s) da competência são separados por hífen (-).

**USAR HISTÓRICO PADRÃO**

Com este parâmetro desmarcado, o sistema irá levar para o lançamento financeiro somente as informações do campo "Complemento do Histórico" e do campo "Fórmula para complemento de histórico". Caso contrário, o histórico do lançamento financeiro será a composição do histórico padrão (Descrição do lançamento financeiro + Mês e Ano competência + Período), do campo "Complemento do Histórico" e do campo "Fórmula para complemento de histórico".

**Atenção:**

Caso este parâmetro estiver marcado e os campos "Complemento do Histórico" e "Fórmula para complemento de histórico" não conterem informações, o lançamento financeiro será gerado com o histórico em branco, ou seja, sem informações.

[Voltar a pagina inicial](http://tdn.totvs.com/pages/viewpage.action?pageId=452719571)
