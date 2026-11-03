---
content_hash: 7ff840e07dfb8911a2c8479a9c09a033dfa6ac9e45d0994d3bb4d33bb10e0572
fetched_at: '2026-06-29T00:06:01.894354+00:00'
page_id: '198941202'
product: rm
source: tdn-rm
title: API de comunicação com o RM Reports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198941202
version: 10
---

# Objetivo

---

Esse documento tem como objetivo auxiliar os desenvolvedores na migração dos códigos que utilizam o **RM Reports** nos seus produtos. Lembrando que a partir da versão 12.1.5 uma nova engine de execução de relatórios do **RM Reports** foi disponibilizada para nossos clientes.  
Para isso, foi criada uma API de comunicação com o **RM Reports** para facilitar o uso e a manutenção nos produtos RM que executam diretamente relatórios construídos no **RM Reports**.   
Ela possibilita a execução de relatórios tanto no lado cliente (actions, forms, etc) quanto no lado server, procurando isolar os componentes internos de execução dos relatórios da RM e da DevExpress, impedindo assim, que os consumidores alterem propriedades e executem métodos diretamente nesses componentes.

*Importante: A classe RptReport localizada na "RM.Rpt.Lib.dll" não poderá mais ser utilizada para gerar relatórios nos produtos. Com isso o método "CREATEDOCUMENT" não deve mais ser utilizado.*

*Importante: A dll RM.Rpt.Lib não deve mais ser adicionada como referência nos produtos que utilizam o Reports.*

# Execução de relatórios Server-Side

---

As informações abaixo auxiliam na criação dos códigos para execução de relatórios no em **server-side**.

Para utilizar as APIs do RM Reports em Server-Side é necessário:

* Adicionar referência para a dll "RM.Rpt.Executor.Intf.dll";
* Remover as referências para as outras dll's do reports;
* Utilizar a interface **IRptExecutor** localizada na dll **RM.Rpt.Executor.Intf**. Deve-se utilizar o RMSBroker para instanciar a implementação **RptExecutorServer** semelhante à seguir:

c#("RptExecutorServer");]]>

## IRptExecutor

---

Permite a execução de relatórios em **server-side**

### **GetReportInfo**

Retorna informações do layout do relatório **sem executá-lo**. Esse método deve ser utilizado quando houver a necessidade de recuperação de informações do layout do relatório antes de executá-lo. Ele retorna informações de parâmetros e filtros criados internamente no relatório para que os consumidores possam manipular esses dados de alguma forma.

#### Parâmetros

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **codColigada** | **int** | Código da coligada |
| **idReport** | **int** | Identificador do relatório |
| **codUsuario** | **String** | Código do usuário |

#### Retorno

|  |  |
| --- | --- |
| **Tipo** | **Descrição** |
| **RptReportInfo** | Informações do layout do relatório |

#### RptReportInfo

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **ParametersReport** | Lista | Parâmetros criados no relatório |
| **ParametersProvider** | Lista | Parâmetros de provider usados no provider do relatório |
| **FiltersReport** | Lista | Filtros disponíveis no relatório. |
| **FiltersFormulas** | MemoryStream | Filtros de fórmula disponíveis no relatório |
| **DataSourceSchema** | MemoryStream | Schema da fonte de dados do relatório. |
| **MemberInfo** | Membros | Informações dos membros de dados do report. |

---

### ExecuteReport

*(Principal método desta interface)* Executa o relatório e retorna informações da execução.

#### Parâmetros de entrada

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **codColigada** | **int** | Código da coligada |
| **idReport** | **int** | Identificador do relatório |
| **codUsuario** | **String** | Código do usuário |
| **params** | **RptExecutorPar** | Contem características de execução do relatório |

#### RptExecutorPar

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **CallBackExecutionProgress** | **Action<>** | Comunicação de incremento de barra de progresso. |
| **CallBackMessageExecution** | **Action<>** | Envio de mensagens do processo de execução. |
| **ParametersReport** | **Lista** | Parâmetros do relatório |
| **ParametersProvider** | **Lista** | Parâmetros do provider |
| **FiltersReport** | **Lista** | Filtros do relatório |
| **FiltersFormula** | **Lista** | Filtros de formula |
| **ExportFileType** | **RptExportFileType** | Tipo de exportação do relatório após sua geração. São eles: CSV, JPEG, HTML, XLSX, MHT, **PDF**, RTF, TXT |
| **GenerateDiagnostics** | **bool** | Informa se é para gerar as informações de diagnóstico da execução do relatório. |
| **GenerateType** | **RptReportGenerateType** | Forma de geração do relatório. |
| **StopExecutionOnError** | **bool** | Finaliza ou não a execução do relatório em caso de erro. Todas as informações de erros são gravadas no diagnóstico de execução se o mesmo for "true". |
| **MaxRowNumberPrint** | **Int** | Número máximo de linhas a serem impressas. O default 0 indica que é para imprimir todas as linhas. |
| **ContextStr** | **String** | Objeto RMSContext na forma de string. |
| **DataSourceExternal** | **DataSet** | DataSet preenchido com informações a serem usadas na geração do relatório. |
| **ReturnLayout** | **bool** | Informa se é para retornar o layout do relatório para rotina chamadora. |
| **AddGroupFields** | **Lista** | Adiciona *groupFields* antes da execução |
| **ClearAllGroupFields** | **Lista** | Permite limpar todos os *groupFields* no relatório antes da execução |
| **RemoveBands** | **Lista** | Bandas a serem removidas antes da execução. |
| **DataMemberExternalMain** | **String** | Nome do dataMember principal |
| **StartPageNumber** | **int** | Número inicial da página em caso utilização do controle de numeração de página customizada. |

#### Retorno

|  |  |
| --- | --- |
| **Tipo** | **Descrição** |
| **RptExecutorReturn** | Características de retorno de execução do relatório |

#### RptExecutorReturn

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **ExecutionId** | **Guid** | Identificador único de execução do relatório. |
| **ExecutionStatus** | **RptExecutionStatus** | Status de execução. [Sucesso ou erro] |
| **ExecutionMessage** | **string** | Mensagem de erro (em caso de erro) |
| **PrintReport** | **MemoryStream** | Resultado da execução do relatório. O conteúdo dessa propriedade pode ser enviado para serviços de impressão. |
| **LayoutReport** | **MemoryStream** | Layout do relatório gerado. |
| **CodSistema** | **string** | Código do sistema do relatório gerado. |
| **CodRelatorio** | **string** | Código do relatório gerado. |
| **DescRelatorio** | **string** | Descrição do relatório gerado. |

### ExecutePartialReport

Executa o relatório de forma parcial. Utilizado para execução de grandes relatórios e passando a fonte de dados externamente. Resolve o problema de estouro de memória da DevExpress*.*

#### Parâmetros

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **codUsuario** | **String** | Código do usuário |
| **params** | **RptExecutorPartialPar** | Contem características de execução parcial do relatório |

#### RptExecutorPartialPar

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **ExportFileType** | **RptExportFileType** | Tipo de exportação do relatório após sua geração. São eles: CSV, JPEG, HTML, XLSX, MHT, **PDF**, RTF, TXT |
| **ContextStr** | **String** | Objeto RMSContext na forma de string. |
| **PartialSources** | **Lista** | Lista de DataSet preenchidos com informações a serem usadas na geração do relatório. |
| **UseUniquePageNumber** | **bool** | Usa numeração de página sequencial. |

#### Retorno

|  |  |
| --- | --- |
| **Tipo** | **Descrição** |
| **RptExecutorPartialReturn** | Características de retorno de execução parcial do relatório |

#### RptExecutorPartialReturn

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **PrintReport** | **MemoryStream** | Resultado final da execução do relatório. O conteúdo dessa propriedade pode ser enviado para serviços de impressão. |

### Export

Exporta um relatório em um formato especifico a partir de um binário proveniente de uma geração prévia*.*Utilizado em casos em que a geração é executada em um momento e a exportação do arquivo, em outro.

#### Parâmetros

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **parms** | **RptExecutorExportPar** | Contem os parãmetros da exportação do relatório |

#### RptExecutorExportPar

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **ExportType** | **RptExportFileType** | Tipo de exportação do relatório após sua geração. São eles: CSV, JPEG, HTML, XLSX, MHT, PDF, RTF, TXT |
| **ReportResult** | **MemoryStream** | Stream contendo o resultado de uma geração do relatório |

#### Retorno

|  |  |
| --- | --- |
| **Tipo** | **Descrição** |
| **RptExecutorExportReturn** | Características de retorno de exportação do relatório |

#### RptExecutorExportReturn

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **ExportedReport** | **MemoryStream** | Resultado final da exportação do relatório. O conteúdo dessa propriedade pode ser enviado para serviços de impressão. |

## Exemplos de uso (server-side):

**Exemplo:** Utilização da API na migração da **ficha física financeira** do RM Nucleus.

**Antes**

c#

**Depois**

c#("RptExecutorServer");
//Recupera as informações do report. ex: filtros do report, parametros do report.
RptReportInfo repInfo = executorServer.GetReportInfo(codColRel, IdRel, this.parameters.Context.CodUsuario);
//Recupera o objeto que representa o filtro principal do report.
//Para isso foi utlizado o Helper "RptReportInfoHelper" que possui uma série de metodos que ajuda manipular
//o objeto RptReportInfo.
RptFilterReportPar mainFilter = RptReportInfoHelper.GetMainFilter(repInfo);
//Configura o filtro necessário.
mainFilter.Value = string.Format("TMOV.CODCOLIGADA = {0} AND TMOV.IDMOV = {1}", CodColigada, IdMov);
//Instancia a classe de parametros do método.
RptExecutorPar parms = new RptExecutorPar();
//Adiciona o filtro para os parametros.
parms.FiltersReport.Add(mainFilter);
//Configura o tipo de exportação.
parms.GenerationType = RptReportGenerationType.File;
parms.ExportFileType = RptExportFileType.PDF;
//Executa o relatório.
RptExecutorReturn result = executorServer.ExecuteReport(codColRel, IdRel, this.parameters.Context.CodUsuario, parms);
//Retorna o relatório gerado para alguma outra rotinal
return result.PrintReport;]]>

\_GoBack

**Exemplo:** Utilização da API sem uso do método **GetReportInfo**:

c#("RptExecutorServer");
RptExecutorPar parms = new RptExecutorPar();
//Adiciona valor para o parametro "IdPrd" definido no relatóiro
parms.ParametersReport.Add(new RptParameterReportPar("IDPRD", 84);
//Configura o tipo de exportação.
parms.GenerationType = RptReportGenerationType.File;
parms.ExportFileType = RptExportFileType.PDF;
//Executa o relatório.
RptExecutorReturn result = executorServer.ExecuteReport(1, 287, this.parameters.Context.CodUsuario, parms);
//Retorna o relatório gerado para alguma outra rotinal
return result.PrintReport;]]>

# Execução de relatórios Client-Side

---

As informações abaixo auxiliam no desenvolvimento dos códigos para execução de relatórios em **client-side**

Para utilizar as APIs do RM Reports em Server-Side é necessário:

* Adicionar referência para a dll **RM.Rpt.Executor.Intf.dll** e **RM.Rpt.Executor.Client.dll**
* Remover as referências para as outras dlls do reports, entre elas: **RM.Rpt.Lib.dll** e **RM.Rpt.Reports.intf.dll**
* Utilizar a interface **RptExecutorClient** localizada na dll **RM.Rpt.Executor.Client**. Deve ser instanciada normalmente, como no exemplo a seguir:

c#

## RptExecutorClient

---

*Permite a execução de relatórios em **client-side***

### AddParams(string, object)

Armazena temporariamente os valores de parâmetros para a execução do relatório

### AddParamsProvider(string, object)

Armazena temporariamente os valores dos parâmetros dos *providers* do relatório

### AddMainFilter(string)

Adiciona um filtro à execução principal do relatório (*report [RptReport]*)

### AddDetailFilter(string, string)

Adiciona um filtro à execução de uma banda específica do relatório.

### GetReportInfo(int, int, string)

Retorna informações do Layout do relatório através do objeto *RptReportInfo*já descrito na seção **Execução de relatórios Server-Side**

### GetRepositoryInfo(RptRepositoryPar)

Retorna informações acerca do repositório (informações do relatório)

### Show(bool, MemoryStream, int, int, bool, bool, bool)

Exibe o relatório a partir de um MemoryStream contendo o relatório já gerado. O parâmetro *showModal* quando ativo mostra o relatório em uma janela modal

### ExecuteReport(int, int, string, RptExecutorClientParams)

Executa o relatório em **server-side** e retorna as informações de execução para **client-side**

#### Parâmetros

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **codColigada** | **int** | Código da coligada |
| **idReport** | **int** | Identificador do relatório |
| **codUsuario** | **String** | Código do usuário |
| **params** | **RptExecutorClientParams** | Contem características de execução do relatóiro |

#### RptExecutorClientParams

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **showReport** | **bool** | Exibe ou não o relatório após sua execução |
| **ShowModal** | **bool** | Exibe ou não o relatório de forma modal |
| **ShowParameters** | **bool** | Exibe ou não a tela para preenchimento dos parâmetros do relatório. |
| **exportFileType** | **RptExportFileType** | Tipo de exportação do relatório após sua geração. São eles: CSV, JPEG, HTML, XLSX, MHT, **PDF**, RTF, TXT |
| **GenerationType** | **RptReportGenerationType** | Tipo de geração do relatório. |
| **GenerateHtmlImagesInBase64** | **bool** | Caso esteja realizando uma geração de relatórios em HTML, deve embutir as imagens em formato base64? |
| **PrintDialog** | **Bool** | Envia o relatório diretamente para impressora. |
| **PrintName** | **String** | Nome da impressora |
| **ShowFilters** | **Bool** | Será mostra uma tela de filtros contendo filtros do relatório. |
| **ReturnLayout** | **Bool** | Permite retornar o layout do relatório. |
| **Context** | **RMSContext** | Contendo RM de execução. |
| **DataMemberExternalMain** | **String** | Nome do dataMember principal |
| **MaxRowNumberPrint** | **int** | Número máximo de linhas a serem impressas no relatório. |
| **RemoveBands** | **Lista** | Permite remover bandas. |

#### Retorno

|  |  |
| --- | --- |
| **Tipo** | **Descrição** |
| **RptExecutorClientReturn** | Características de retorno de execução do relatório no cliente. |

#### RptExecutorClientReturn

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **ExecutionStatus** | **RptExecutionStatus** | Status de execução. [Sucesso ou erro] |
| **ExecutionMessage** | **string** | Mensagem de erro (em caso de erro) |
| **PrintReport** | **MemoryStream** | Resultado da execução do relatório. O conteúdo dessa propriedade pode ser enviado para serviços de impressão. |
| **CodRelatorio** | **string** | Código do relatório gerado. |
| **DescRelatorio** | **string** | Descrição do relatório gerado. |
| **LayoutReport** | **MemoryStream** | Layout do relatório |

### ExportReport

Exporta um relatório em um formato especifico a partir de um binário proveniente de uma geração prévia*.*Utilizado em casos em que a geração é executada em um momento e a exportação do arquivo, em outro.

#### Parâmetros

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **parms** | **RptExecutorClientExportPar** | Contem os parâmetros da exportação do relatório |

#### RptExecutorClientExportPar

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **ExportType** | RptExportFileType | Tipo de exportação do relatório após sua geração. São eles: CSV, JPEG, HTML, XLSX, MHT, PDF, RTF, TXT |
| **ReportResult** | MemoryStream | Stream contendo o resultado de uma geração do relatório |

#### Retorno

|  |  |
| --- | --- |
| **Tipo** | **Descrição** |
| **RptExecutorClientExportReturn** | Características de retorno de exportação do relatório |

#### RptExecutorClientExportReturn

|  |  |  |
| --- | --- | --- |
| **Nome do parâmetro** | **Tipo** | **Descrição** |
| **ExportedReport** | **MemoryStream** | Resultado final da exportação do relatório. O conteúdo dessa propriedade pode ser enviado para serviços de impressão. |

## Exemplos de uso (client-side):

**Exemplo:** Execução de relatório no "*client*" passando parâmetro para o provider;

c#

**Exemplo**: Execução de relatório no "*client*" passando parâmetro para o report;

c#

**Exemplo:** Execução de relatório no "*client*" passando filtro para o report principal;

c# 10 AND DATAEMISSAO >= '20015/01/01'");
//Seta o tipo de exportação para PDF.
execParams.GenerationType = RptGenerationType.File;
execParams.ExportFileType = RptExportFileType.PDF;
//O relatório gerado será mostrado após sua execução.
execParams.ShowReport = true;
//O relatório gerado não será mostrado em uma janela modal.
execParams.ShowDialog = false;
//Mostra a janela para alteração dos valores dos parametros do relatóiro.
execParams.ShowParameters = true;
exClient.ExecuteReport(3, 487, RMSSession.Context.CodUsuario, execParams)]]>Índice

2

falsefalse

**Produto:** RM Reports

false

**Versão:** 11.80.40

falsefalse

**Data**:

falseStatus

GreenCONCLUÍDO
