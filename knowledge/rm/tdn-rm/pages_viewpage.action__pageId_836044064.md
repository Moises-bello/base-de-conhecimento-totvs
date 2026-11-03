---
content_hash: bc761c8dfd34110c0ad87dcbfb172aaa39b8485dc542a483aae1c3368c7627a2
fetched_at: '2026-06-29T00:11:49.613202+00:00'
page_id: '836044064'
product: rm
source: tdn-rm
title: Geração de Movimento por Competência (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=836044064
version: 15
---

### 01. Visão geral

Através do serviço **RestProcess**, via ***RESTful***, o usuário poderá executar o processo de geração de movimento por competência.  

Essa solicitação está disponibilizada através do método: **POST** e serão processados utilizando os valores dos parâmetros do processo. Esses parâmetros podem ser obtidos através do método **GET** com o serviço **GetSchema**.

No link [serviços RESTful](https://tdn.totvs.com/x/WBJnF) no RM é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTful*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](https://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### 02. Processos - Geração de Movimento por Competência

#### Para a geração de movimento por competência, temos 02 processos possíveis: ***EduNFECompetenciaSliceableData, Edu******NFECompetencia******Data***.

---

#### Processo - EduNFECompetenciaData

Até a versão 12.1.2402, esse processo é utilizado quando estamos na visão do contrato e executamos o processo de geração de movimento por competência para os contratos selecionados. E também pelo botão ***"Geração de Movimento por Competência"*** no menu "***Financeiro / Contábil → NF-e***".

A partir da versão **12.1.2406**, a visão do contrato passou a utilizar o processo **Edu*****NFECompetencia*****SliceableData**, que permite fracionamento de jobs.

O processo utiliza as informações das listas ***PrimaryKeyList*** e ***PrimaryKeyNames*** para identificar quais foram os contratos selecionados

#### PrimaryKeyNames

* Informar os valores: CODCOLIGADA, RA, IDPERLET e CODCONTRATO, para a geração de movimento por competência.

#### PrimaryKeyList

* Devem ser informados os valores referentes aos campos definidos na lista ***PrimaryKeyNames***.

---

#### Processo - *EduNFECompetenciaSliceableData* *(Disponível a partir da versão 12.1.2406)*

Esse processo é utilizado quando acessamos o botão ***"Geração de Movimento por Competência"*** no menu "***Financeiro / Contábil → NF-e***" do Educacional. E também na tela de visão de contrato quando executa o processo de geração de movimento por competência para os contratos selecionados.  Ele permite o fracionamento de jobs para geração de movimento por competência em ambas opções de acesso.

O processo via tela de visão de contrato utiliza as informações das listas ***PrimaryKeyList*** e ***PrimaryKeyNames*** para identificar quais foram os contratos selecionados

#### PrimaryKeyNames

* Informar os valores: CODCOLIGADA, RA, IDPERLET e CODCONTRATO, para a geração de movimento por competência.

#### PrimaryKeyList

* Devem ser informados os valores referentes aos campos definidos na lista ***PrimaryKeyNames***.

O processo via o menu utiliza, além de outros campos, o filtro para identificar quais contratos terão seus movimentos por competência gerados.

#### Filtro utilizado

* Filtro de contratos selecionados!
* Botão **Mostrar resultados** ao ser clicado irá listar os contratos selecionados conforme o filtro selecionado

#### Para utilizar o fracionamento de jobs é necessário informar os seguintes parâmetros:

ProcessName

* Deve ser informado com o valor padrão **"Inclusão/exclusão do movimento de competência"**, os jobs utilizam o nome do processo para identificação.

ServerName

* Informar o nome do processo que está sendo executado: **"*****EduNFECompetenciaSliceableData*****".**  Esta informação é utilizada para identificar se existe fracionamento configurado.

SlicesCount

* Deve conter a quantidade de frações utilizadas para execução do processo, este número deve respeitar o máximo de frações cadastrado em Ambiente/Processos/Segurança de Jobs Fracionáveis. Por exemplo, o número máximo de frações configurada neste caso é de 4, sendo assim mesmo que seja informado um valor maior que 4 só serão criados 4 jobs durante a execução.

### 03. Parâmetros do processo - GetSchema

Para a execução de um processo, é necessária a informação dos valores dos parâmetros retornados. Para sabermos quais são os parâmetros do processo, podemos utilizar o serviço ***GetSchema***que retornará todas as informações necessárias.

A execução do ***GetSchema*** é necessária a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rest/restprocess/getschema/<NOMEDOPROCESSO>***

A execução do processo de geração de movimento por competência, podemos fazer a consulta utilizando os 02 processos:

Exemplo: 

<http://localhost:8051/>rest/restprocess/getschema/EduNFECompetenciaData

<http://localhost:8051/>rest/restprocess/getschema/EduNFECompetenciaSliceableData

***Obs.:*** O retorno é o mesmo, independente do processo. Os dois utilizam a mesma estrutura de campos.

Retorno do GetSchema:

xmlCorpo do retornotruetrue

### **04. Execução do processo**

Para a execução do processo é necessário utilizar a URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rest/restprocess/executeprocess/<NOMEDOPROCESSO>***

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

#### Geração de movimento por competência - NOMEDOPROCESSO (EduNFECompetenciaData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo:

xmlCorpo da mensagemtruetrue

#### Geração de movimento por competência - NOMEDOPROCESSO (EduNFECompetenciaSliceableData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo com a utilização das **PrimaryKeyList e PrimaryKeyNames**:

xmlCorpo da mensagemtruetrue

Segue o exemplo de um conjunto de informações necessárias para a execução do processo com a utilização do **Filtro**:

xmlCorpo da mensagemtruetrue

### **05. Descrição dos campos e tipos de dados**

Abaixo segue uma descrição de cada tag do JSON de retorno do ***getSchema***.

* **TipoTarefa**: Tipo de tarefa que o processo irá utilizar na sua execução e é esperado um valor inteiro, referente ao código do tipo de tarefa desejado. Na geração por movimento por competência deve ser informado sempre o valor **ZERO.**

* **MesAno**: Campo utilizado para informar o mês e ano da competência para a geração do movimento. Deve ser informada no formato "**yyyy/MM/dd**" com a utilização via rest. Onde:
  + yyyy: Será ano da competência
  + MM: Será  mês da competência
  + dd: Será o último dia do mês da competência

* **GerarMovimentoValorZero:** Campo utilizado para informar se deve gerar movimento com valor zerado. Valores possíveis:
  + true,
  + false.

* **PrimaryKeyList:** Lista dos valores que serão utilizados na identificação dos contratos que serão processados.

* **PrimaryKeyNames:** Lista com os nomes dos campos que serão utilizados para identificação dos valores da lista acima.

* **MovimentoNFEParams:** Conjunto de campos necessários para a execução do processo.
  + **CodColigada**: Código da coligada que será considerada na execução do processo. Esse campo espera um valor inteiro.

* + **CodFilial**: Código da filial que será considerada na execução do processo. Esse campo espera um valor inteiro.

* + **CodTipoCurso**: Código do nível de ensino que será considerada na execução do processo. Esse campo espera um valor inteiro.

* + **CodTMv:** Campo utilizado para informar o código do tipo de movimento a ser utilizado na geração do movimento por competência.

* + **CodSistemaLogado:** Campo utilizado para informar o sistema logado para indicar a origem do movimento a ser criado. Deve ser informado sempre com o valor de "**S**"

* + **CodUsuarioLogado:** Campo utilizado para informar o usuário logado. Deve ser informado o código do usuário logado no RM.

* + **TipoRespFinanceiro:** Campo utilizado para informar o tipo de responsável financeiro que estará presente no movimento a ser criado. Valores possíveis:
    - 0: Indica que será o responsável do financeiro do aluno
    - 1: Indica que será o responsável do financeiro do contrato

* + **TipoTarefaMovimento:** Campo utilizado para informar o tipo de tarefa a ser executada para o movimento. Valores possíveis:
    - 1: Indica que os movimentos vinculados ao contrato serão excluídos
    - 2: Indica que os movimentos serão incluídos e vinculados ao contrato
    - 3: Indica que os movimentos vinculados ao contrato serão alterados
    - 4: Indica que os movimentos vinculados ao contrato serão cancelados. **ATENÇÃO: Essa opção não está disponível para a integração Protheus, pois no Protheus não o conceito de cancelamento no pedido de venda.**

* **Context**: Informações relacionadas ao contexto{  
    
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

Campos necessários, para a utilização de **fracionamento de jobs**: (***EduNFECompetenciaSliceableData)***

* + **ProcessName**: Campo que espera um valor string e deverá ser utilizado quando por padrão utilizar "Inclusão/exclusão do movimento de competência".
  + **ServerName**": Campo que espera um valor string e deverá ser utilizado para o fracionamento de jobs, deve conter o nome do processo chamado ex: *EduNFECompetenciaSliceableData*.
  + **SlicesCount**: Campo que espera um valor inteiro e deverá para informar a quantidade de fracionamentos da execução do processo ex: 4.
  + **CodColigada**: Código da coligada que será considerada na execução do processo. Esse campo espera um valor inteiro.
  + **CodFilial**: Código da filial que será considerada na execução do processo. Esse campo espera um valor inteiro.
  + **CodTipoCurso**: Código do nível de ensino que será considerada na execução do processo. Esse campo espera um valor inteiro.

Parâmetros internos que não precisam ser informados:

* + **StatusLanc**
  + **FiltroBoleto**
  + **RMSJobIds**
  + **EnableTracing**
  + **LocalOnlyExecutor**
  + **EnableJobErrorProgressbar**
  + **MovimentoNFEParams**
    - **CodServico**
    - **PermiteRegerarMov**
    - **PermiteMovValorLiquidoZero**
    - **DesconsideraBolsaCredito**
    - **OrigemDataEmissao**
    - **DataComp**
    - **DataEmissaoInicial**
    - **DataEmissaoFinal**
    - **DataVencInicial**
    - **DataVencFinal**
    - **DiaFixo**
    - **Context**
  + **Boletos**
    - **CodColigada**
    - **IdBoleto**
    - **CNABStatus**
    - **CodColCFO**
    - **CodCFO**
    - **NomeCliFor**
    - **DataVencimento**
    - **CodFilialNfe**
    - **FiltrouPorLancamento**
    - **ListIdLacamentosFiltrados**
    - **InternalId**
    - **ListaAcordos**
