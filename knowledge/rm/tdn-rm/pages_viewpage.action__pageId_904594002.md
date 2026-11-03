---
content_hash: 725a008e8581ffb84bfc8c3267e9cec6cc84c9b0102f0a86e40109facd94395b
fetched_at: '2026-06-29T00:12:03.202512+00:00'
page_id: '904594002'
product: rm
source: tdn-rm
title: Geração de Movimento por Regime de Caixa (Rest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=904594002
version: 15
---

### 01. Visão geral

Através do serviço **RestProcess**, via ***RESTful***, o usuário poderá executar o processo de geração de movimento por regime de caixa.  

Essa solicitação está disponibilizada através do método: **POST** e serão processados utilizando os valores dos parâmetros do processo. Esses parâmetros podem ser obtidos através do método **GET** com o serviço **GetSchema**.

No link [serviços RESTful](https://tdn.totvs.com/x/WBJnF) no RM é possível obter todas as informações sobre os serviços disponibilizados.

Importante

Para utilização dos serviços, é necessário que seja utilizada a forma de autenticação básica, onde deverão ser passados os valores de usuário e senha do usuário de acesso ao sistema.

Conforme documentação disponibilizada pela equipe de **FrameWork**, os serviços via ***RESTful*** estão disponibilizados, à partir da versão 12.1.6 da linha RM.

**[Se necessário clique aqui para obter ajuda na configuração do Host.](https://tdn.totvs.com/pages/viewpage.action?pageId=338376631)**

### 02. Processos - Geração de Movimento por Regime de Caixa

#### Para a geração de movimento por regime de caixa, temos 02 processos possíveis: ***EduNFESliceableData, EduNFEData***.

---

#### Processo - EduNFEData

Até **a versão 12.1.2406 e antes do patch 12.1.2410.149**, esse processo é utilizado no menu "***Financeiro / Contábil → NF-e***" na opção ***"Geração de Movimento".*** E executamos o processo de geração de movimento por regime de caixa para os boletos selecionados pelo filtro informado.

O processo utiliza a informação da propriedade **FiltroBoleto** para identificar quais os boletos serão selecionados

#### FiltroBoleto

* Informar o valor do filtro no seguinte formato: [

  "FLANBOLETO.IDBOLETO = :F1",

  14470

  ]

#### **Observa que o filtro para selecionar os boletos no primeiro tem  é a consulta SQL, e depois os parâmetros para essa consulta informada, exemplo:**

[  
        "FLANBOLETO.CODCOLIGADA = :F1 AND FLANBOLETO.IDBOLETO = :F2",  
        15,  
        14470  
]

---

#### Processo - *EduNFESliceableData* *(Disponívela partir do patch 12*.1.2410.149 e versões superiores*)*

Esse processo é utilizado no menu "***Financeiro / Contábil → NF-e***" na opção ***"Geração de Movimento".*** E executamos o processo de geração de movimento por regime de caixa para os boletos selecionados pelo filtro informado.  Ele **permite o fracionamento de jobs** para geração de movimento por regime de caixa.

O processo utiliza a informação da propriedade **FiltroBoleto** para identificar quais os boletos serão selecionados

#### FiltroBoleto

* Informar o valore do filtro no seguinte formato: [

  "FLANBOLETO.IDBOLETO = :F1",

  14470

  ]

#### **Observa que o filtro para selecionar os boletos no primeiro tem  é a consulta SQL, e depois os parâmetros para essa consulta informada**

#### **, exemplo:**

[  
        "FLANBOLETO.CODCOLIGADA = :F1 AND FLANBOLETO.IDBOLETO = :F2",  
        15,  
        14470  
]

O processo utiliza outros campos para filtrar e identificar quais boletos terão seus movimentos por regime de caixa gerados. 

#### Filtros utilizados:

* Filtro de boletos selecionados.
* Data de emissão do lançamento
* Data de vencimento do lançamento
* Status do lançamento.

#### Para utilizar o fracionamento de jobs é necessário informar os seguintes parâmetros:

ProcessName

* Deve ser informado com o valor padrão **"Serviços gerais de movimento"**, os jobs utilizam o nome do processo para identificação.

ServerName

* Informar o nome do processo que está sendo executado: **"EduNFESliceableData****".**  Esta informação é utilizada para identificar se existe fracionamento configurado.

SlicesCount

* Deve conter a quantidade de frações utilizadas para execução do processo, este número deve respeitar o máximo de frações cadastrado em Ambiente/Processos/Segurança de Jobs Fracionáveis. Por exemplo, o número máximo de frações configurada neste caso é de 4, sendo assim mesmo que seja informado um valor maior que 4 só serão criados 4 jobs durante a execução.

### 03. Parâmetros do processo - GetSchema

Para a execução de um processo, é necessária a informação dos valores dos parâmetros retornados. Para sabermos quais são os parâmetros do processo, podemos utilizar o serviço ***GetSchema***que retornará todas as informações necessárias.

A execução do ***GetSchema*** é necessária a utilização da URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rest/restprocess/getschema/<NOMEDOPROCESSO>***

A execução do processo de geração de movimento por regime de caixa, podemos fazer a consulta com a utilização dos 02 processos:

Exemplo: 

<http://localhost:8051/>rest/restprocess/getschema/EduNFEData

<http://localhost:8051/>rest/restprocess/getschema/EduNFESliceableData

***Obs.:*** O retorno é o mesmo, independente do processo. Os dois processos utilizam a mesma estrutura de campos.

Retorno do GetSchema:

xmlCorpo do retornotruetrue

### **04. Execução do processo**

Para a execução do processo é necessário utilizar a URL:

***HTTP://<SERVIDOR>:<HTTPORT>/rest/restprocess/executeprocess/<NOMEDOPROCESSO>***

Para a realização dessa requisição, deverá ser utilizado o método: **POST**.

#### Geração de movimento por regime de caixa - NOMEDOPROCESSO (EduNFEData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo:

xmlCorpo da mensagemtruetrue

#### Geração de movimento por regime de caixa - NOMEDOPROCESSO (EduNFESliceableData)

Segue o exemplo de um conjunto de informações necessárias para a execução do processo:

xmlCorpo da mensagemtruetrue

### **05. Descrição dos campos e tipos de dados**

Abaixo segue uma descrição de cada tag do JSON de retorno do ***getSchema***.

* **TipoTarefa**: Tipo de tarefa que o processo irá utilizar na sua execução e é esperado um valor inteiro, referente ao código do tipo de tarefa desejado. Valores possíveis:
  + 0: Geração/Regeração de movimento por regime de caixa
  + 1: Exclusão do movimento por regime de caixa
  + 4: Cancelamento do movimento por regime de caixa

* **StatusLan:** Campo utilizado para informar o status do lançamento a ser selecionado presente no boleto: Valores possíveis:
  + -1: Todos os lançamentos
  + 0: Somente os lançamentos em aberto
  + 1: Somente os lançamentos baixados
  + 3: Somente os lançamentos baixados por acordo

* **GerarMovimentoValorZero:** Campo utilizado para informar se deve gerar movimento com valor zerado. Valores possíveis:
  + true,
  + false.

* **FiltroBoleto:** Lista do filtro para seleção dos boletos para a geração do movimento por regime de caixa.

* **CodColigada**: Código da coligada que será considerada na execução do processo. Esse campo espera um valor inteiro.

* **CodFilial**: Código da filial que será considerada na execução do processo. Esse campo espera um valor inteiro.

* **CodTipoCurso**: Código do nível de ensino que será considerada na execução do processo. Esse campo espera um valor inteiro.

* **MovimentoNFEParams:** Conjunto de campos necessários para a execução do processo.
  + **CodColigada**: Código da coligada que será considerada na execução do processo. Esse campo espera um valor inteiro.

* + **CodFilial**: Código da filial que será considerada na execução do processo. Esse campo espera um valor inteiro.

* + **CodTipoCurso**: Código do nível de ensino que será considerada na execução do processo. Esse campo espera um valor inteiro.

* + **CodTMv:** Campo utilizado para informar o código do tipo de movimento a ser utilizado na geração do movimento por regime de caixa.

* + **CodSistemaLogado:** Campo utilizado para informar o sistema logado para indicar a origem do movimento a ser criado. Deve ser informado sempre com o valor de "**S**"

* + **CodUsuarioLogado:** Campo utilizado para informar o usuário logado. Deve ser informado o código do usuário logado no RM.

* + **PermiteRegerarMov**: Campo utilizado para informar se será permitido regerar o movimento por regime de caixa.

* + **PermiteMovValorLiquidoZero**: Campo utilizado para informar se será permitido gerar/regerar o movimento por regime de caixa com valor líquido igual a zero.

* + **DesconsideraBolsaCredito**: Campo utilizado para informar se serão desconsiderados os lançamentos de bolsa de crédito e para os valores de desconto.

* + **OrigemDataEmissao**: Campo utilizado para informar a origem da data de emissão do movimento. Valores possíveis:
    - 0: Data de emissão do lançamento
    - 1: Data de vencimento do lançamento
    - 2: Data de baixa do lançamento
    - 3: Data de competência do lançamento
    - 4: Data do atual do sistema

* + **DiaFixo**: Campo utilizado para informar o dia fixo para para ser a data de emissão do movimento baseado na data de origem de emissão. **Caso não for utilizado deve informar vazio ("")**.
    - Exemplo:
      * *OrigemDataEmissão* está configurada com o valor 0. Isto é, data de emissão do lançamento que é 15/01/2025. No campo **DiaFixo** tem o valor 20. Então da data de emissão do movimento será 20/01/2025. E essa data deve ser maior ou igual a data de emissão do lançamento e menor ou igual a data de vencimento do lançamento.

* + **DataEmissaoInicial**: Campo utilizado para informar o período inicial da data emissão dos lançamentos vinculados ao boleto. **Campo obrigatório**.

* + **DataEmissaoFinal**: Campo utilizado para informar o período final da data emissão dos lançamentos vinculados ao boleto. **Campo obrigatório**.

* + **DataVencInicial**: Campo utilizado para informar o período inicial da data vencimento dos lançamentos vinculados ao boleto. Pode receber valor nulo. Caso informe valor na data de vencimento inicial o sistema irá validar se a informação é válida. E deve ser informada também a data de vencimento final.

* + **DataVencFinal**: Campo utilizado para informar o período final da data vencimento dos lançamentos vinculados ao boleto. Pode receber valor nulo. Caso informe valor na data de vencimento final o sistema irá validar se a informação é válida. E deve ser informada também a data de vencimento inicial.

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

Campos necessários, para a utilização de **fracionamento de jobs**: (***EduNFESliceableData)***

* + **ProcessName**: Campo que espera um valor string e deverá ser utilizado quando por padrão utilizar "Serviços gerais de movimento".
  + **ServerName**": Campo que espera um valor string e deverá ser utilizado para o fracionamento de jobs, deve conter o nome do processo chamado ex: *EduNFESliceableData*.
  + **SlicesCount**: Campo que espera um valor inteiro e deverá para informar a quantidade de fracionamentos da execução do processo ex: 4.

Parâmetros internos que não precisam ser informados:

* + ****MesAno****
  + **LogEventoAtivado**
  + **RMSJobIds**
  + **EnableTracing**
  + **LocalOnlyExecutor**
  + **EnableJobErrorProgressbar**
  + **MovimentoNFEParams**
    - **CodServico**
    - **TipoRespFinanceiro**
    - **TipoTarefaMovimento**
    - **DataComp**
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
