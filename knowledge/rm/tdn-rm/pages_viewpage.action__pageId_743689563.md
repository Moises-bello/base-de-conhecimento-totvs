---
content_hash: 6c7ad04a049fb925d088d0dab23d62a84d92de21c634f98969027ce34017b817
fetched_at: '2026-06-29T00:11:32.058427+00:00'
page_id: '743689563'
product: rm
source: tdn-rm
title: Prévia dos valores do lançamento (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=743689563
version: 7
---

### 01. Visão geral

Através do serviço **RestProcess**, via ***RESTful***, o usuário poderá executar o processo de prévia dos valores do lançamento.  

Essa solicitação está disponibilizada através do método: **POST** e serão processados utilizando os valores dos parâmetros do processo. Esses parâmetros podem ser obtidos através do método **GET** com o serviço **GetSchema**.

No link [serviços RESTful](https://tdn.totvs.com/x/WBJnF) no RM é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTful*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](https://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### 02. Visão geral do processo de prévia dos valores do lançamento

Esse processo é executado através da tela que fica em: Educacional | Financeiro / Contábil | Financeiro | Gerar / Excluir Prévia de Valores do Lançamento.

Ele utiliza o dataserver **EduGeraPreviaLancData**.

Ele utiliza, além de outros campos e o tipo de filtro, as listas parametrizadas no processo para identificar quais parcelas terão suas prévias de lançamentos geradas.

Listas utilizadas:

* ListaTipoContrato: lista de tipos de contrato
* ListaTipoParcela: lista de tipos de parcela
* ListaPeriodoLetivo: lista de períodos letivos
* ListaSitMatricula: lista de situação de matrícula
* ListaServicos: lista de serviços da parcela
* ListaHabilitacaoFilial: lista de habilitação filial
* ListaPlanosPgto: lista de planos de pagamento
* ListaAlunos: lista de alunos
* ListaIdParcela: lista de parcelas
* ListaIdTurmaDisc: lista de id de turmas/disciplinas
* ListaContaCorrente: lista de conta-corrente

### 03. Parâmetros do processo - GetSchema

Para a execução de um processo, é necessária a informação dos valores dos parâmetros retornados. Para sabermos quais são os parâmetros do processo, podemos utilizar o serviço ***GetSchema***que retornará todas as informações necessárias.

Para a execução do ***GetSchema*** é necessária a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rest/restprocess/getschema/<NOMEDOPROCESSO>***

***Para a execução da obtenção dos parâmetros do processo de prévia dos valores do lançamento, devemos fazer a consulta abaixo:***

<http://localhost:8051/rest/restprocess/getschema/EduGeraPreviaLancData>

Retorno do GetSchema:

xmlCorpo do retornotruetrue

### **04. Execução do processo**

Para a execução do processo é necessário utilizar a URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rest/restprocess/executeprocess/<NOMEDOPROCESSO>***

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

***Para a execução do processo de prévia dos valores do lançamento, devemos fazer a consulta abaixo:***

<http://localhost:8051/rest/restprocess/executeprocess/EduGeraPreviaLancData>

Segue o exemplo de um conjunto de informações necessárias para a execução do processo:

xmlCorpo da mensagemtruetrue

### **05. Descrição dos campos e tipos de dados**

Abaixo segue uma descrição de cada tag do JSON de retorno do ***getSchema***:

* **TipoFiltro**: Tipo de filtro que o processo irá utilizar na sua execução e é esperado um valor inteiro, referente ao código do tipo de filtro desejado.

Possui os seguintes valores possíveis:

* + 0 - Nenhum (Necessário quando utilizado com os campos PrimaryKeyList e PrimaryKeyNames para execução com o processo "***EduGeraPreviaLancData***")
  + 1 - RA (Necessário quando informamos somente o campo **RA** para o filtro de alunos que terão suas parcelas consideradas na geração de lançamentos)
  + 2 - Matriz (Necessário quando informamos os campos relacionados a matriz para o filtro dos alunos que terão suas parcelas consideradas na geração de lançamentos: **CodCurso, CodHabilitacao, CodGrade, CodTurno e CodTurma**)
  + 3 - SQL (Necessário quando é utilizada uma sentença SQL para o filtro dos alunos que terão suas parcelas consideradas na geração de lançamentos, utiliza os campos **CodSentencaSql e ValorParamsConsultaSql**)
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

* + **OperacaoBolsaRetroativa**: Campo interno utilizado para operações com bolsa retroativa. Esse campo não precisa ser informado.
  + **CodContrato**: Campo interno utilizado em outro processo de geração de lançamento por contrato, ele não precisa ser informado.

Segue, abaixo, um conjunto de campos que serão utilizados:

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

* + **IsProcGeraPrevia:** Indica se o processo esta sendo executado no modo de prévia.
  + **IsExcluirPrevia:** Indica se foi selecionado o modo de exclusão do processo de geração de prévia.

Listas que precisam ser informadas:

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

Parâmetros internos que não precisam ser informados:

* + **ProcessName**
  + **ServerName**
  + **SlicesCount**
  + **NumBanco**
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
  + **Historico**
  + **CodColCxa**
  + **CodCxa**
  + **CodTabOp1**
  + **CodTabOp2**
  + **CodTabOp3**
  + **CodTabOp4**
  + **CodTabOp5**
  + **CampoAlfaOp1**
  + **CampoAlfaOp2**
  + **CampoAlfaOp3**
  + **DataOp1**
  + **DataOp2**
  + **DataOp3**
  + **DataOp4**
  + **DataOp5**

Os parâmetros relacionados ao fracionamento de jobs **ProcessName, ServerName e SlicesCount** não irão impactar o funcionamento do processo, pois, atualmente ele não está implementado para permitir fracionamento de jobs.
