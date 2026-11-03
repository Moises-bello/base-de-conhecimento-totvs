---
content_hash: 6dfd7704aed08d41931c70df83d60b13fd92c2b9c088721b5ea10dfc3bd9fd9d
fetched_at: '2026-06-29T00:11:23.013448+00:00'
page_id: '706133602'
product: rm
source: tdn-rm
title: Geração de lançamentos (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=706133602
version: 26
---

### 01. Visão geral

Através do serviço **RestProcess**, via ***RESTful***, o usuário poderá executar o processo de geração de lançamentos.  

Essa solicitação está disponibilizada através do método: **POST** e serão processados utilizando os valores dos parâmetros do processo. Esses parâmetros podem ser obtidos através do método **GET** com o serviço **GetSchema**.

No link [serviços RESTful](https://tdn.totvs.com/x/WBJnF) no RM é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTful*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](https://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### 02. Processos - Geração de lançamentos

#### Para a geração de lançamentos, temos 05 processos possíveis: ***EduGerarLancFromParcelaData***, ***EduGeraLancData, EduGerarLancFromParcelaSliceableData, EduGerarLancFromContratoSliceableData, EduGeraLancSliceableData***.

---

#### Processo - EduGerarLancFromParcelaData

Até a versão 12.1.2302, esse processo é utilizado quando estamos na visão de parcelas do contrato e executamos o processo de geração de lançamento para as parcelas selecionadas. A partir da versão 12.1.2306, a visão de parcelas do contrato passou a utilizar o processo **EduGerarLancFromParcelaSliceableData**, que permite fracionamento de jobs.

O processo utiliza as informações das listas ***PrimaryKeyList*** e ***PrimaryKeyNames*** para identificar quais foram as parcelas selecionadas.

#### PrimaryKeyNames

* Informar os valores: CODCOLIGADA, IDPARCELA, para a geração de lançamento por parcela.
* Informar os valores: CODCOLIGADA, RA, IDPERLET e CODCONTRATO, para a geração de lançamento por contrato.

#### PrimaryKeyList

* Devem ser informados os valores referentes aos campos definidos na lista ***PrimaryKeyNames***.

---

#### Processo - EduGeraLancData

Esse processo é utilizado quando acessamos o botão ***"Financeiro"*** no menu "***Financeiro / Contábil***" do Educacional.

Ele utiliza, além de outros campos e o tipo de filtro, as listas parametrizadas no processo para identificar quais parcelas terão seus lançamentos gerados. 

Listas utilizadas

* ListaAlunos - Lista de RA de alunos;
* ListaHabilitacaoFilial - Lista de matrizes aplicadas;
* ListaPeriodoLetivo - Lista de período letivos;
* ListaPlanosPgto - Lista de planos de pagamentos;
* ListaServicos - Lista de serviços;
* ListaTipoContrato - Lista de tipos de contratos;
* ListaTipoParcela - Lista de tipos de parcelas;

---

#### Processo - *EduGerarLancFromParcelaSliceableData (Disponível a partir da versão 12.1.2306)*

Esse processo é utilizado quando estamos na visão de parcelas do contrato e executamos o processo de geração de lançamento para as parcelas selecionadas, permite o fracionamento de jobs durante a geração de lançamentos.

1. Dessa forma, o processo utiliza as informações das listas ***PrimaryKeyList*** e ***PrimaryKeyNames*** para identificar quais foram as parcelas selecionadas.

   1. #### PrimaryNames

      1. Informar os valores: CODCOLIGADA e IDPARCELA, para a geração de lançamento por parcela.
   2. #### PrimaryKeyList

      1. Devem ser informados os valores referentes aos campos definidos na lista ***PrimaryKeyNames.***
2. Para uso do fracionamento de jobs informar os seguintes parâmetros:

   1. #### ProcessName

      1. Deve ser informado com o valor padrão **"Gerar lançamento"**, os jobs utilizam o nome do processo para identificação.
   2. #### ServerName

      1. Informar o nome do processo que está sendo executado: **"EduGerarLancFromParcelaSliceableData".**  Esta informação é utilizada para identificar se existe fracionamento configurado.
   3. #### SlicesCount

      1. Deve conter a quantidade de frações utilizadas para execução do processo, este número deve respeitar o máximo de frações cadastrado em Ambiente/Processos/Segurança de Jobs Fracionáveis. Por exemplo, o número máximo de frações configurada neste caso é de 4, sendo assim mesmo que seja informado um valor maior que 4 só serão criados 4 jobs durante a execução.

---

#### Processo - *EduGerarLancFromContratoSliceableData* *(Disponível a partir da versão 12.1.2306)*

Esse processo é utilizado quando executamos ***"Gerar lançamento"*** na listagem de contratos e permite o fracionamento de jobs durante a geração de lançamentos.

1. Dessa forma, o processo utiliza as informações das listas ***PrimaryKeyList*** e ***PrimaryKeyNames*** para identificar quais foram as parcelas selecionadas.

   1. #### PrimaryNames

      1. Informar os valores: CODCOLIGADA, RA, IDPERLET e CODCONTRATO, para a geração de lançamento por contrato.
   2. #### PrimaryKeyList

      1. Devem ser informados os valores referentes aos campos definidos na lista ***PrimaryKeyNames***
2. Para uso do fracionamento de jobs informar os seguintes parâmetros:

   1. #### ProcessName

      1. Deve ser informado com o valor padrão **"Gerar lançamento"**, os jobs utilizam o nome do processo para identificação.
   2. #### ServerName

      1. Informar o nome do processo que está sendo executado: **"*EduGerarLancFromContratoSliceableData*****".**  Essa informação é utilizada para identificar se existe fracionamento configurado.
   3. #### SlicesCount

      1. Deve conter a quantidade de frações utilizadas para execução do processo, este número deve respeitar o máximo de frações cadastrado em Ambiente/Processos/Segurança de Jobs Fracionáveis. Por exemplo, o número máximo de frações configurada neste caso é de 4, sendo assim mesmo que seja informado um valor maior que 4 só serão criados 4 jobs durante a execução.

---

#### Processo - *EduGeraLancSliceableData* *(Disponível a partir da versão 12.1.2306)*

Esse processo é utilizado quando acessamos o botão ***"Financeiro"*** no menu "***Financeiro / Contábil***" do Educacional. Ele permite o fracionamento de jobs para geração de lançamento.

Ele utiliza, além de outros campos e o tipo de filtro, as listas parametrizadas no processo para identificar quais parcelas terão seus lançamentos gerados. 

#### Listas utilizadas

* ListaAlunos - Lista de RA de alunos;
* ListaHabilitacaoFilial - Lista de matrizes aplicadas;
* ListaPeriodoLetivo - Lista de período letivos;
* ListaPlanosPgto - Lista de planos de pagamentos;
* ListaServicos - Lista de serviços;
* ListaTipoContrato - Lista de tipos de contratos;
* ListaTipoParcela - Lista de tipos de parcelas.

#### Para utilizar o fracionamento de jobs é necessário informar os seguintes parâmetros:

ProcessName

Deve ser informado com o valor padrão **"Gerar lançamento"**, os jobs utilizam o nome do processo para identificação.

ServerName

Informar o nome do processo que está sendo executado: **"*****EduGeraLancSliceableData*****".**  Esta informação é utilizada para identificar se existe fracionamento configurado.

SlicesCount

Deve conter a quantidade de frações utilizadas para execução do processo, este número deve respeitar o máximo de frações cadastrado em Ambiente/Processos/Segurança de Jobs Fracionáveis. Por exemplo, o número máximo de frações configurada neste caso é de 4, sendo assim mesmo que seja informado um valor maior que 4 só serão criados 4 jobs durante a execução.

### 03. Parâmetros do processo - GetSchema

Para a execução de um processo, é necessária a informação dos valores dos parâmetros retornados. Para sabermos quais são os parâmetros do processo, podemos utilizar o serviço ***GetSchema***que retornará todas as informações necessárias.

Para a execução do ***GetSchema*** é necessária a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rest/restprocess/getschema/<NOMEDOPROCESSO>***

Para a execução do processo de geração de lançamentos, podemos fazer a consulta utilizando os 05 processos:

Exemplo:

<http://localhost:8051/>rest/restprocess/getschema/EduGerarLancFromParcelaData

<http://localhost:8051/>rest/restprocess/getschema/EduGeraLancData

<http://localhost:8051/>rest/restprocess/getschema/EduGerarLancFromParcelaSliceableData

<http://localhost:8051/>rest/restprocess/getschema/EduGerarLancFromContratoSliceableData

<http://localhost:8051/>rest/restprocess/getschema/EduGeraLancSliceableData

***Obs.:*** O retorno é o mesmo, independente do processo. Os dois utilizam a mesma estrutura de campos.

Retorno do GetSchema:

xmlCorpo do retornotruetrue

### **04. Execução do processo**

Para a execução do processo é necessário utilizar a URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rest/restprocess/executeprocess/<NOMEDOPROCESSO>***

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

Importante

Para a utilização dos campos retornados do ***GetSchema***, é necessária a inclusão do ***CodUsuario*** junto ao conjunto de valores da ***ParamsGeraLanc***.

#### Geração de lançamento - NOMEDOPROCESSO (EduGeraLancData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo:

xmlCorpo da mensagemtruetrue

#### Geração de lançamento - NOMEDOPROCESSO (EduGerarLancFromParcelaData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo (Geração por parcelas):

xmlCorpo da mensagem - Por parcelatruetrueGeração por Contratos:xmlCorpo da mensagem - Por contratotruetrue

#### Geração de lançamento - NOMEDOPROCESSO (EduGerarLancFromParcelaSliceableData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo (Geração por parcelas):

xmlCorpo da mensagem - Por parcelatruetrue

#### Geração de lançamento - NOMEDOPROCESSO (EduGerarLancFromContratoSliceableData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo:

xmlCorpo da mensagem - Por parcelatruetrue

#### 

#### Geração de lançamento - NOMEDOPROCESSO (EduGeraLancSliceableData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo:

xmlCorpo da mensagemtruetrueImportante

O parâmetro "TipoSelecaoParcela", no conjunto "ParamsGeraLanc", precisa conter o valor "0" para informar para o serviço que será uma execução por parcela do contrato. Essa informação é importante, tanto para a execução por parcela quanto para contrato.

### **05. Descrição dos campos e tipos de dados**

Abaixo segue uma descrição de cada tag do JSON de retorno do ***getSchema***.

* **TipoFiltro**: Tipo de filtro que o processo irá utilizar na sua execução e é esperado um valor inteiro, referente ao código do tipo de filtro desejado.

Possui os seguintes valores possíveis:

* + 0 - Nenhum (Necessário quando utilizado com os campos PrimaryKeyList e PrimaryKeyNames para execução com o processo "***EduGerarLancFromParcelaData***")
  + 1 - RA (Necessário quando informamos somente o campo RA para o filtro de alunos que terão suas parcelas consideradas na geração de lançamentos)
  + 2 - Matriz (Necessário quando informamos os campos relacionados a matriz para o filtro dos alunos que terão suas parcelas consideradas na geração de lançamentos)
  + 3 - SQL (Necessário quando é utilizada uma sentença SQL para o filtro dos alunos que terão suas parcelas consideradas na geração de lançamentos)
  + 4 - Filtro (Necessário quando é informado um filtro personalizado através do campo "***ClausulasFiltroRa***" para o filtro dos alunos que terão suas parcelas consideradas na geração de lançamentos)
  + 5 - Arquivo (Esse tipo não é utilizado quando executado através da API)

* **SalvarParams**: Campo utilizado para informar para o processo que não deverão ser considerados os campos de listas: Lista de serviços, lista de alunos, lista de plano de pagamentos e lista de habilitação filial, para o filtro dos alunos que terão seus lançamentos gerados.

Valores possíveis:

* + true,
  + false

Campos necessários, caso o valor do campo ***SalvarParams*** seja "**true**:

* + **RA**: Campo que espera um valor string e deverá ser utilizado quando o tipo de filtro for por RA. Deverá receber o RA que será considerado no filtro dos alunos.

* + **CodCurso**": Campo que espera um valor string e deverá ser utilizado quando o tipo de filtro for por Matriz. Deverá receber o código do curso que será utilizado no filtro dos alunos.
  + **CodHabilitacao**: Campo que espera um valor string e deverá ser utilizado quando o tipo de filtro for por Matriz. Deverá receber o código da habilitação que será utilizado no filtro dos alunos.
  + **CodGrade**: Campo que espera um valor string e deverá ser utilizado quando o tipo de filtro for por Matriz. Deverá receber o código da grade que será utilizado no filtro dos alunos.
  + **CodTurno**: Campo que espera um valor inteiro e deverá ser utilizado quando o tipo de filtro for por Matriz. Deverá receber o código do turno que será utilizado no filtro dos alunos.
  + **CodTurma**: Campo que espera um valor string e deverá ser utilizado quando o tipo de filtro for por Matriz. Deverá receber o código da turma que será utilizado no filtro dos alunos.

* + **ClausulasFiltroRa**: Campo utilizado para informar um filtro personalizado para o filtro dos alunos considerados na execução da geração de lançamentos. Esse campo é considerado quando o tipo de filtro é RA ou por filtro.

Exemplo de valores esperados para o campo (conjunto de instruções SQL):

[

[

SALUNO.RA IN (:P1, :P2),

"ES-001",

"ES-002"

]

]

* + **CodSentencaSql**: Campo utilizado para informar o código da sentença SQL que será executada para obter os alunos que serão considerado na execução do processo.

Esse campo é utilizado quando o tipo de filtro está definido como SQL.

* + **ValorParamsConsultaSql**: Campo utilizado para informar o conjunto dos valores dos parâmetros da consulta utilizada no campo CodSentencaSql.

O valor esperado para o campo é um conjunto de valores para utilização na execução da sentença Sql informada anteriormente:

[

1,

"TESTE",

0

]

* **ParamsGeraLanc**: Conjunto de campos necessários para a execução do processo.

* + **ProcessaDescAntecipacaoDuranteGerPrevia**: Campo utilizado para informar se será considerado nos cálculos da prévia o desconto por antecipação (será considerado o maior desconto). (Execução com o processo "**EduGeraLancData**")

Valores esperados para esse campo:

* + - 0 - Não
    - 1 - Sim

* + **CodColigada**: Código da coligada que será considerada na execução do processo. Esse campo espera um valor inteiro.
  + **CodFilial**: Código da filial que será considerada na execução do processo. Esse campo espera um valor inteiro.
  + **CodTipoCurso**: Código do nível de ensino que será considerada na execução do processo. Esse campo espera um valor inteiro.

* + **ListaPeriodoLetivo**: Lista com os códigos dos períodos letivos que serão considerados nos filtros para a execução do processo.

Esse campo espera uma lista de valores inteiros com os códigos IDPERLET do período letivo.

Exemplos de valores esperados:

[

12,

1456

]

* + **TipoSelecaoParcela**: Valor que define qual será o filtro de parcela utilizado para identificação das parcelas,

Valores esperados para o campo:

* + - 1 - Por parcela
    - 2 - Por data

* + **OperacaoBolsaRetroativa**: Campo interno utilizado para operações com bolsa retroativa. Esse campo não precisa ser informado,
  + **CodContrato**: Deve ser informado quando a geração de lançamentos é realizada por contrato,

Esse campo espera um valor string com o código do contrato e precisa das seguintes condições:

* + - Deve ser utilizado quando executado com o processo "***EduGerarLancFromParcelaData***"
    - O campo PrimaryKeyNames deve conter o nome dos campos da chave primária do contrato: **CODCOLIGADA**, **RA**, **IDPERLET** e **CODCONTRATO**.
    - O campo PrimaryKeyList deve conter os valores dos campos informados como chave do contrato.

Segue, abaixo, um conjunto de campos que serão utilizados, somente, quando o processo executado for à partir do "**EduGeraLancData**":

* + **ParcelaInicial**: Numero da parcela inicial da parcela, quando o tipo de seleção de parcela for informado "**Por parcela**".
  + **ParcelaFinal**: Numero da parcela final da parcela, quando o tipo de seleção de parcela for informado "**Por parcela**".
  + **CotaInicial**: Numero da cota inicial da parcela, quando o tipo de seleção de parcela for informado "**Por parcela**".
  + **CotaFinal**: Numero da cota final da parcela, quando o tipo de seleção de parcela for informado "**Por parcela**".
  + **DataInicial**: Data inicial da parcela, quando o tipo de seleção de parcela for informado "**Por data**".
  + **DataFinal**: Data final da parcela, quando o tipo de seleção de parcela for informado "**Por data**".
  + **OrigemParcela**: Parâmetro interno do sistema.
  + **AgrupamentoBoleto**: Define se a geração de lançamentos irá considerar a realização um agrupamento de boletos.

Valores esperados para o campo:

* + - 0 - Por responsável
    - 1 - Contrato
    - 2 - Aluno
    - 3 - Não irá realizar agrupamento

* + **BoletoPorServico**: Informar se o sistema irá realizar um agrupamento utilizando serviços diferentes num mesmo boleto.

Valores esperados para o campo (Caso não seja utilizado, não precisa ser informado):

* + - 0 - Não
    - 1 - Sim

* + **AgrupaBolentroDeOutrasFiliais**: Informar se o sistema irá considerar o boleto de outras filiais no agrupamento do lançamento.

Valores esperados para o campo (Caso não seja utilizado, não precisa ser informado):

* + - false
    - true

* + **ContratoHabNull**: Informa se serão consideradas parcelas de contratos que não possuem matrizes aplicadas.

Valores esperados para o campo (Caso não seja utilizado, não precisa ser informado):

* + - 0 - Não
    - 1 - Sim

* + **CodMoeda**: Deve ser informado o código da moeda que será utilizado na geração de lançamento.

Valores esperados para o campo:

* + - R$

* + **TipoContabilLan**: Define o tipo contábil do lançamento.

Valores esperados para o campo:

* + - 0 - Não contábil
    - 1 - Contábil
    - 2 - Baixa contábil
    - 3 - À contabilizar

* + **CodTipoDocumento**: Código do tipo de documento.
  + **TipoContaCaixa**: Define qual será a origem da configuração da conta caixa. (Parâmetro interno não precisa ser informado)

Valores esperados para o campo:

* + - 0 - Padrão (Parâmetros gerais do sistema)
    - 1 - Responsável
    - 2 - Serviço
    - 3 - Parametrização por curso

* + **Historico**: Define o histórico que será registrado no lançamento,
  + **CodColCxa**: Código da coligada da conta caixa que será utilizada.
  + **CodCxa**: Código da conta caixa.
  + **CodTabOp1**: Código da tabela opcional 1.
  + **CodTabOp2**: Código da tabela opcional 2.
  + **CodTabOp3**: Código da tabela opcional 3.
  + **CodTabOp4**: Código da tabela opcional 3.
  + **CodTabOp5**: Código da tabela opcional 3.
  + **CampoAlfaOp1**: Campo alfa opcional 1.
  + **CampoAlfaOp2**: Campo alfa opcional 2.
  + **CampoAlfaOp3**: Campo alfa opcional 3.
  + **DataOp1**: Data opcional 1.
  + **DataOp2**: Data opcional 2.
  + **DataOp3**: Data opcional 3.
  + **DataOp4**: Data opcional 4.
  + **DataOp5**: Data opcional 5.

Listas que precisam ser informadas, caso seja executado o processo "**EduGeraLancData**":

* + - **ListaTipoParcela**: Lista com os tipos de parcelas que serão consideradas na execução do processo.

Valores esperados para o campo:

* + - * + 0 - Plano
        + 1 - Adicional
        + 2 - Extra

* + - **ListaTipoContrato**: Lista com os tipos de contratos que serão considerados na execução do processo.

Valores esperados para o campo:

* + - * + 0 - Plano
        + 1 - Serviço

* + - **ListaServicos**: Lista de serviços que serão utilizados na execução do processo. (Campo ***SalvarParams*** com valor ***"false")***
    - **ListaHabilitacaoFilial**: Lista de habilitações filiais que serão consideradas para a identificação da parcela no processo. (Campo ***SalvarParams*** com valor ***"false")***
    - **ListaPlanosPgto**: Lista com os planos de pagamentos que serão utilizados no processo. (Campo ***SalvarParams*** com valor ***"false")***
    - **ListaAlunos**: Lista de alunos que terão os lançamentos de suas parcelas gerados. (Campo ***SalvarParams*** com valor ***"false")***

Listas que precisam ser informadas, caso seja executado o processo: "***EduGerarLancFromParcelaData":***

* + - **PrimaryKeyList**: Lista dos valores que serão utilizados na identificação das parcelas que serão processadas.
    - **PrimaryKeyNames**: Lista com os nomes dos campos que serão utilizados para identificação dos valores da lista acima.

* + "**Context**": Informações relacionadas ao contexto{  
      
            "\_params": {  
                "$EXERCICIOFISCAL": -1, (Não é utilizado pelo Educacional e pode ser informado com -1)  
                "$CODLOCPRT": -1, (Não é utilizado pelo Educacional e pode ser informado com -1)  
                "$CODTIPOCURSO": 1, (Código do nível de ensino)  
                "$EDUTIPOUSR": "-1", (Não é utilizado pelo sistema e pode ser informado com -1)  
                "$CODUNIDADEBIB": 1, (Não é utilizado pelo Educacional e pode ser informado com -1)  
                "$CODCOLIGADA": 1, (Código da coligada)  
                "$RHTIPOUSR": "-1", (Não é utilizado pelo Educacional e pode ser informado com -1)  
                "$CODIGOEXTERNO": "-1", (Não é utilizado pelo Educacional e pode ser informado com -1)  
                "$CODSISTEMA": "S", (Código "S" necessário para informar que é uma execução do módulo Educacional)  
                "$CODUSUARIOSERVICO": "", (Não é utilizado pelo Educacional e pode ser informado com "")  
                "$IDPRJ": 2, (Não é utilizado pelo Educacional e pode ser informado com -1)  
                "$CHAPAFUNCIONARIO": "-1", (Não é utilizado pelo Educacional e pode ser informado com -1)  
                "$CODFILIAL": 1 (Código da filial)  
            },  
            "Environment": 4 (É necessário informar o código 4 para que o sistema identifique a execução em ambiente desktop)  
        }  
    }

Campos necessários, para a utilização de **fracionamento de jobs**: (***EduGerarLancFromParcelaSliceableData, EduGerarLancFromContratoSliceableData, EduGeraLancSliceableData)***

* + **ProcessName**: Campo que espera um valor string e deverá ser utilizado quando por padrão utilizar "Gerar Lançamento".
  + **ServerName**": Campo que espera um valor string e deverá ser utilizado para o fracionamento de jobs, deve conter o nome do processo chamado ex: EduGerarLancFromParcelaSliceableData.
  + **SlicesCount**: Campo que espera um valor inteiro e deverá para informar a quantidade de fracionamentos da execução do processo ex: 4.

Parâmetros internos que não precisam ser informados:

* + **NumBanco**
  + **NumAgencia**
  + **NroConta**
  + **CodColigadaConta**
  + **TipoCob**
  + **CnabCarteira**
  + **DataVencimento**
  + **DataCompetencia**
  + **CodCCusto**
  + **CodDepto**
  + **CodEvento**
  + **CodColCfo**
  + **CodCfo**
  + **ValorOriginal**
  + **ValorBolsaRetroativa**
  + **IncluirExcluirBolsaRetroativa**
  + **IsIncluirExcluirBolsaRetroativa**
  + **IsBolsaRetroativaModAntigo\_NaoReGerarBoleto**
  + **PermiteAtualizarContaCorrente**
  + **IsSimulaLancamento**
  + **OrigemSimulacaoIsBolsaRetroativa**
  + **TipoCalculoPorCredito**
  + **IsGeracaoPreviaLancamento**
  + **IsSomenteContratosAtivos**
  + **CodTipoDocumentoAPagar**
  + **CodColCxaAPagar**
  + **CodCxaAPagar**
  + **NumBancoAPagar**
  + **NumAgenciaAPagar**
  + **TipoContabilLanAPagar**
  + **CodColNatFinanceira**
  + **CodNatFinanceira**
  + **IsPlanoPagamentoDefault**
  + **CodPlanoPgto**
  + **ConsideraDescAntecipacao**
  + **ConsideraDescAntecipacaoBolsa**
  + **TipoBolsaContrato**
  + **ListaIdParcela**
  + **ListaIdTurmaDisc**
  + **ListaContaCorrente**
  + **CodStatusMatriculaDisc**
  + **MatriculaOnlineContextoParams**
  + **IsProcGeraPrevia**
  + **IsExcluirPrevia**
