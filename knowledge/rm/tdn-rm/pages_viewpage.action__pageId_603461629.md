---
content_hash: 493f6ea077356ee79de4fe6c43c5b1099ea2737f9c9b33236788e7028a4d1d76
fetched_at: '2026-06-29T00:10:58.110898+00:00'
page_id: '603461629'
product: rm
source: tdn-rm
title: Migração dados de Pacientes PEP 2 para PEP RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=603461629
version: 19
---

## **CONTEÚDO**

1. **Pré-Requisitos**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Configurações necessárias**
5. **Configurações**
6. **Execução dos conceitos**

sumarioPré-Requisitos

## **01. PRÉ - REQUISITOS**

* Imprescindível ter o ambiente do **RM**, **TBC** e **PEP 2** funcionando na **versão 32** para execução dos conceitos mencionados no item 3.
* O processo de migração dos dados será executado em **ambiente local** e só após sua conclusão o cliente deverá ser direcionado para o ambiente cloud.
* **Conexão VPN** liberada para possíveis  casos que necessite de uma análise mais detalhada (debug).

## **02. VISÃO GERAL**

A partir da versão 12.1.31 é possível importar dados do histórico clínico e formulários dinâmicos do paciente no PEP 2 para o PEP RM

Exemplo de utilização

## **03. EXEMPLO DE UTILIZAÇÃO**

| Código | Descrição |
| --- | --- |
| CONSAU001 | Migracao Histórico PEP 2 para PEP RM por paciente: Todo o histórico de um paciente específico será importado. |
| CONSAU002 | Migracao Histórico PEP 2 para PEP RM de pacientes em atend.: Todos os pacientes que possuem atendimento em aberto, seja ele externo ou internamento terão histórico importado. |
| CONSAU003 | Migracao Histórico Pacientes PEP 2 para PEP RM: Esta opção irá importar o histórico de todos os pacientes do PEP 2. |
| CONSAU004 | Migracao PEP 2 para PEP RM Formulários Dinamicos: Esta opção irá importar todos os registros lançados para um determinado Formulário Dinâmico independente do paciente lançado. Este item possui como pré-requisito a criação de um metadado correspondente no RM. (<https://tdn.totvs.com/pages/releaseview.action?pageId=556379167>) |
| CONSAU005 | Migracao PEP 2 para PEP RM Formulários Dinamicos: Esta opção irá importar todos os registros lançados para um determinado Formulário Dinâmico independente do paciente lançado. Este item não possui como pré-requisito a criação de um metadado correspondente no RM, pois os registros serão importados como PDF e ficarão disponíveis no histórico clínico. |
| CONSAU006 | CONSAU006 - Importar Formulario Dinâmico como anexo pacient.: Esta opção irá importar todos os registros lançados para um determinado Formulário Dinâmico independente do paciente lançado como anexo do paciente. Este conceito é indicado para formulários dinâmicos que não possuam o id do atendimento nos parâmetros de entrada. |
| CONSAU007 | Esta opção irá realizar a importação dos paciente que durante a migração dos dados (CONSAU003) foram identificados problemas. |

**IMPORTANTE:** Todos os conceitos obtêm dados até o dia anterior à data de execução e utilizam a data do último registro importado numa segunda execução. Com isso as execuções subsequentes tendem a durar menos tempo que a primeira além de não duplicar registros.

Configurações necessárias 

## **04. CONFIGURAÇÕES NECESSÁRIAS**

Para que o RM possa se comunicar com o PEP 2 é necessário acrescentar algumas configurações nos arquivos abaixo:

* Host.exe.config
* Host.Service.exe.config
* Host.JobRunner.exe.config
Configurações 

## **05. CONFIGURAÇÕES**

Na seção <appSettings> de cada arquivo adicione as seguintes configurações:

O parâmetro **path\_importacao\_historico\_pep2**deverá conter um caminho onde os pdf's importados serão salvos. Caso o RM esteja em arquitetura 3 camadas é necessário que este caminho esteja acessível por todos os hosts configurados. Caso esta configuração não seja definida os arquivos serão importados na tabela SZARQUIVOS.

05.1 CONNECTION STRING SQL SERVER

## **05.1 CONNECTION STRING SQL SERVER**

Na seção <configuration> adiciona a tag <connectionStrings> conforme exemplo abaixo:

**<connectionStrings>**

                                                                              <add name="PEP2Entities" connectionString="metadata=res://\*/Pep2DB.csdl|res://\*/Pep2DB.ssdl|res://\*/Pep2DB.msl;provider=**provider**;provider connection string=&quot;data source=**SOURCE**;initial catalog=**INITIAL\_CATALOG**;persist security info=True;user id=**USER\_ID**;password=**PASSWORD**;MultipleActiveResultSets=True;App=EntityFramework&quot;" providerName="System.Data.EntityClient"  />

<add name="RMEntities" connectionString="metadata=res://\*/RMDB.csdl|res://\*/RMDB.ssdl|res://\*/RMDB.msl;provider=**provider**;provider connection string=&quot;data source=**SOURCE**;initial catalog=**INITIAL\_CATALOG**;persist security info=True;user id=**USER\_ID**;password=**PASSWORD**;MultipleActiveResultSets=True;App=EntityFramework&quot;" providerName="System.Data.EntityClient" />

**</connectionStrings>**

*SQL SERVER - providerName="System.Data.SqlClient"*

*Substitua as palavras em negrito das strings de conexão para as configurações do seu banco de dados.*

05.2 CONNECTION STRING ORACLE

## **05.2 CONNECTION STRING ORACLE**

Na seção <configuration> adiciona a tag <connectionStrings> conforme exemplo abaixo:

**<connectionStrings>**

 <add name="RMEntities" connectionString="metadata=**PATH\RMDB.SSDL**|  
   res://\*/RMDB.csdl|  
   res://\*/RMDB.msl;  
   provider=Oracle.ManagedDataAccess.Client;   
   provider connection string='USER ID=**USERID**;PASSWORD=**PASSWORD**;DATA SOURCE=**SOURCE** ;PERSIST SECURITY INFO=True'"   
   providerName="System.Data.EntityClient" />   
     
  <add name="PEP2Entities" connectionString="metadata=**PATH\Pep2DB.SSDL**|  
   res://\*/Pep2DB.csdl|  
   res://\*/Pep2DB.msl;  
   provider=Oracle.ManagedDataAccess.Client;   
   provider connection string='USER ID=**USERID**;PASSWORD=**PASSWORD**;DATA SOURCE=**SOURCE** ;PERSIST SECURITY INFO=True'"   
   providerName="System.Data.EntityClient" /> 

**<connectionStrings>**

*Substitua as palavras em negrito das strings de conexão para as configurações do seu banco de dados.*

*Os arquivos **RMDB.SSDL e Pep2DB.SDLL** estão disponíveis na pasta bin da versão do RM.*

Exemplo de connectionstring no oracle em uma base local utilizando a versão 32:

**<connectionStrings>**

 <add name="RMEntities" connectionString="metadata=c:\RM\Legado\12.1.32\Sau-PEP\RM.Pep.MigracaoPEP2\RMDB.ssdl|  
   res://\*/RMDB.csdl|  
   res://\*/RMDB.msl;  
   provider=Oracle.ManagedDataAccess.Client;   
   provider connection string='USER ID=rm;PASSWORD=rm;DATA SOURCE=10.172.214.11/PEP:1521/ ;PERSIST SECURITY INFO=True'"   
   providerName="System.Data.EntityClient" />   
     
  <add name="PEP2Entities" connectionString="metadata=c:\RM\Legado\12.1.32\Sau-PEP\RM.Pep.MigracaoPEP2\Pep2DB.ssdl|  
   res://\*/Pep2DB.csdl|  
   res://\*/Pep2DB.msl;  
   provider=Oracle.ManagedDataAccess.Client;   
   provider connection string='USER ID=PEP;PASSWORD=PEP;DATA SOURCE=10.172.214.11/PEP:1521/ ;PERSIST SECURITY INFO=True'"   
   providerName="System.Data.EntityClient" /> 

**<connectionStrings>**

*ORACLE - providerName="Oracle.ManagedDataAccess.Client"*

05.3 SERVICE MODEL

## **05.3 SERVICE MODEL**

Ainda na seção <configuration> adicione a tag <system.serviceModel> com os dados abaixo:

<system.serviceModel>  
                                                                              <bindings>  
                                                                                              <customBinding>  
                                                                                                              <binding name="CustomBinding\_CommonService" openTimeout="01:10:00"  
                                                                                                                                                              closeTimeout="00:11:00"  
                                                                                                                                                              sendTimeout="00:11:00"  
                                                                                                                                                              receiveTimeout="00:11:00" >  
                                                                                                                             <binaryMessageEncoding />  
                                                                                                                             <httpTransport allowCookies="true"  
                                                                                                                                                maxReceivedMessageSize="20000000"  
                                                                                                                                                maxBufferSize="20000000"  
                                                                                                                                                maxBufferPoolSize="20000000"  
                                                                                                                                                                               keepAliveEnabled="true"  
                                                                                                                                         />  
                                                                                                              </binding>  
                                                                                              </customBinding>  
                                                                              </bindings>  
                                                                              <client>  
                                                                                              <endpoint address="<http://SERVIDOR_PEP2/TOTVS.PEP.WCF/Common/CommonService.svc>"  
                                                                                               binding="customBinding" bindingConfiguration="CustomBinding\_CommonService"  
                                                                                               contract="CommonServiceReference.CommonService" name="CustomBinding\_CommonService" />  
                                                                              </client>  
                                                                   </system.serviceModel>

### **Após realizar as configurações é necessário reiniciar o Host.**

* Em seguida importe os conceitos CONSAU001, CONSAU002, CONSAU003, CONSAU004 através do menu RM-> Integração -> Conceito -> Processos -> Importar conceito
Execução dos conceitos

## **06. EXECUÇÃO DOS CONCEITOS**

* Para executar acesse o menu Integração -> Conceito (ETL). Em seguida selecione o conceito Migração Histórico PEP 2 para PEP RM por paciente e no menu Processos clique na opção Processar novo conceito.

* Na tela que irá abrir clique no botão Avançar:

* Na tela a seguir preencha os campos CodColigada com a coligada configurada o PEP 2 e CodPaciente o Código do paciente que deseja importar, em seguida clique em avançar.

* Clique em executar.

* O processo de importação irá começar conforme imagem abaixo:

* Quando o processo for concluído a seguinte tela será exibida:

* Ao acessar o Histórico Clínico do paciente que teve os dados importados, será possível visualizar os registros importados e eles terão como nome do responsável HISTÓRICO CLÍNICO PEP2.

* Os dois próximos conceitos fazem importação de um grupo de pacientes e o único ponto de diferença do exemplo anterior é que precisam apenas do código da coligada como parâmetro.

  Desta forma seguiremos para o conceito Migrador PEP 2 para PEP RM Formulários Dinâmicos. Assim como no exemplo anterior selecione a opção desejada e clique em Processos -> Processar novo conceito para iniciar a importação:

* Clique em avançar para ir a tela de parâmetros de execução.

* Diferente dos processos anteriores este necessita de uma quantidade maior de parâmetros pois através deles que iremos mapear os dados entre o formulário dinâmico do pep 2 e o metadado do RM.

  CodColigada: Deverá ser preenchido com o mesmo código da coligada utilizado pelo PEP 2 (configurado no arquivo web.config do TBC)

  FormulárioPEP2Id: Este é o id do formulário dinâmico cadastrado no TOTVS.FormBuilder.Web e é possível visualizar esta informação ao editar um formulário cadastrado E.:

* ProjetoMetadadoRM: O Id do projeto de metadados no RM. Pode ser visto na coluna Id do Projeto no menu Serviços Globais -> Metadados -> Projetos

CodProfissional, CodPaciente, CodAtendimento, NomeProfissional: Estes campos são campos obrigatórios para a exibição de um metadado no PEP RM e por isso precisam de uma atenção especial. Existem três possibilidades de preenchimento para estes campos:

**ParametroEntrada.[NomeDoParametro]**: Ao preencher desta forma o valor atribuído a este campo será preenchido com o valor do parâmetro de mesmo nome na lista de parâmetros de entrada do formulário dinâmico do PEP 2. Ex.: Ao preencher o campo CodPaciente com o valor ParametroEntrada.patientId iremos obter o valor de cada formulário através do campo mostrado na imagem abaixo:

* **Formulario.[NomeDoParametro]**: A lógica é semelhante à do preenchimento anterior. A diferença está que desta forma iremos buscar os dados da seção Design do formulário conforme exemplo abaixo.

**OBSERVAÇÃO:**

---

Alguns nomes podem ser muito longos e com isso a visualização irá ficar incompleta com “...” assim como o exemplo da imagem. É importante que o nome passado esteja completo, para garantir essa informação você poderá ou deixar o mouse sobre o nome e ele irá aparecer completo ou buscar o metadado clicando sobre o nome “aqui” destacado com link na imagem.

* **Valor fixo**: Caso o valor passado não comece com “ParametroEntrada.” ou “Formulario.” o próprio valor irá ser atribuído a todos os formulários importados.

**STATUS:**

---

Diferente no PEP 2 nós controlamos alguns status dos registros médicos e após finalizado o item não pode mais ser deletado e sim cancelado. No PEP 2 não temos este controle por registro. Os status possíveis são os seguintes:

    0 = Rascunho: O item pode ser editado e excluído.

    1 = Finalizado: O item não pode ser editado e apenas cancelado

    9 = Cancelado.

Como não temos este controle no PEP 2 recomendamos o uso sempre do valor 1.

ArquivoCaminhoMapeamentoColunas: Como o metadados do RM é salvo numa base relacional, podendo ser Oracle ou SQL, o nome das colunas possuem um limite máximo de 32 caracteres, o que não acontece no formulário do PEP 2 por se tratar de um banco não relacional. Logo este parâmetro conterá o caminho para um arquivo txt que terá o mapeamento das colunas entre os dois formulários. Este arquivo será bem simples, conforme exemplo abaixo:

ANAMNESE\_EXA\_FISI\_DATA;ANAMNESE\_EXA\_FISI\_DATA

CABECALHO\_MEDICO;CABECALHO\_MEDICO

ANAMNESE\_EXA\_FISI\_QUEIXA\_PRINC;ANAMNESE\_EXA\_FISI\_QUEIXA\_PRINCIPAL

ANAMNESE\_EXA\_FISI\_ESPECIAL;ANAMNESE\_EXA\_FISI\_ESPECIAL

ANAMNESE\_EXA\_FISI\_HISTORIA\_PRE;ANAMNESE\_EXA\_FISI\_HISTORIA\_PREGRESSA

ANAMNESE\_EXA\_FISI\_HISTORIA\_SOC;ANAMNESE\_EXA\_FISI\_HISTORIA\_SOCIAL

ANAMNESE\_EXA\_FISI\_HISTORIA\_FAM;ANAMNESE\_EXA\_FISI\_HISTORIA\_FAMILIAR

* Cada linha representa um campo do formulário, sendo o valor a esqueda do ; o nome da coluna do Metadado do RM que irá armazenar o valor do metadado do Design de formulário do PEP 2 a esquerda da linha. Note que neste exemplo tentamos seguir com o mesmo nome, porém dado o limite de caracteres campos como ANAMNESE\_EXA\_FISI\_QUEIXA\_PRINCIPAL foi reduzido para ANAMNESE\_EXA\_FISI\_QUEIXA\_PRINC.

### Após o preenchimento de todos os campos basta clicar no botão avançar. Ao concluir será apresentada uma tela semelhante a imagem abaixo.

.
