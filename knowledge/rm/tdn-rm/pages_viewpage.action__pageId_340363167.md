---
content_hash: 4fe69c7e3d41044a775d6ac7db7ffd50aac4c687121841824b5455376b69af86
fetched_at: '2026-06-29T00:08:52.480691+00:00'
page_id: '340363167'
product: rm
source: tdn-rm
title: FAQ - Construção e Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=340363167
version: 106
---

**CODNATUREZAFINANCEIRADEFAULT** 

Aviso importante

* **Este documento não deve ser publicado para clientes;**
* O uso deste recurso tem como finalidade auxiliar no autoconhecimento dos participantes Totvs do Seguimento C&P;
* Toda informação que seja julgada importante, deve ser incorporada ao documento seguindo o padrão criado.
Seguimento SQUAD TOP1TOPSolum (Totvs Obras e Projetos)Totvs Obras e Projetos1Projeto2Cad. Gerais3Orçamento4PlanejamentoCampos Centro de Custo e Natureza Orçamentária Financeira obrigatórios no rateio.

**Mensagem apresentada:**

**Problema:**

Ao realizar o envio de um Pedido de Material para suprimentos/faturamento é que possua rateio por centro de custo e natureza orçamentária financeira ocorre o erro descrito acima.

**Solução:**

1ª Solução:

Verifique as parametrizações do tipo de movimento utilizado, pois as etapas devem estar configuradas corretamente.

Obs.: Abaixo como foi utilizado as configurações no tipo de movimento utilizado no teste em que ocorreu o erro.

* Etapa 46 - Orçamento

* Etapa 47 - Rateio C.Custo - Departamento

* Etapa "Mov - Tab - Global" e "Item - Tab - Global" foram configuradas da seguinte forma:

2ª Solução:

Aviso importante

Está solução somente se aplica aos tipos de movimentos que na Etapa - Fin - Faturamento 1/6 possua a flag "Faturar o Movimento" **marcada.**

* Acesse o Totvs Gestão Financeira (Fluxos) | Ambiente | Parâmetros | Totvs Gestão Financeira | Contas a pagar ou Contas a receber | Recursos Adicionais;
* No campo Rateio Centro de Custo/Natureza Orçamentária informe Usar Rateio para: "Ambos" e Obrigatoriedade: "Não Obrigatório".

3ª Solução:

Certifique-se que o produto utilizado na geração do Pedido de Material está com o campo "Natureza Orçamentária/Financeira" informado.

* Acesse os insumos utilizados é verifique o produto associado (aba "Produtos de Suprimentos/Faturamento");
* Selecione o produto e edite;
* Na aba "Detalhes" | Classificação | o campo Natureza Orçamentária/Financeira deve estar preenchido.

[Tipo Movimento: 1.1.04] - Item 0 - Produto xxxxxxxxxx do Movimento ?402?! - Série SC: Valor inválido para o Preço Unitário.

**Mensagem apresentada:**

**Problema:**

Ao gerar um movimento originado pelo pedido de material e apresentado o erro informando que o valor unitário e invalido.

**Solução:**

1º Solução :Acesse o cadastro de produto e procure pelo código do produto ou descrição informado na mensagem de erro "**01.37.0004.0001 - RF PLUS M6 P0300 ZA**"

Código: **01.37.0004.0001**

Descrição: **RF PLUS M6 P0300 ZA**

Selecione o produto, na aba Preço | informe o Preço do produto.

2º Solução

Acesse os parâmetros do tipo de movimento, etapa **Item - Preços**.

**Campo Edição de Preço**: Mostra

**Preço de Tabela**: Nenhum

**Buscar Preço Em**: Preço Final (campo preenchido na 1º Solução)

5ControleHabilitar campo de "Valor Extra" na tela de "Gerar integração com suprimentos/faturamento"

Para habilitar a aba de "Valores Extras" na tela de Gerar integração com suprimentos/faturamento é necessário acessar o tipo de movimento desejado, no exemplo abaixo é o 1.1.04.

* Acesse o Totvs Gestão Estoque compras e faturamento | Ambiente | Parâmetros | Gestão de estoque compras e faturamento | escolha a opção aonde o seu tipo de movimento se encontra, no caso do exemplo e Gestão de Compras.
* Ao abrir o tipo de movimento, acesse a etapa **Mov - Valores financeiros 1/4** e habilite os campos **Valor Extra 1** e **Valor Extra 2** (para habilitar a aba **Valores extras**, não é necessário habilitar os dois campo, somente um irá mostrar a aba).

Retorno do BackOffice: Parâmetro CODNATUREZAFINANCEIRADEFAULT não encontrado!.

Ao realizar a Liberação de Retenção ou Adiantamento contratual para o protheus gerando um **Titulo Financeiro** é apresentado o erro de:

Retorno do BackOffice:

Parâmetro **CODNATUREZAFINANCEIRADEFAULT** não encontrado!.

Ou

Solução:

Acesse os parâmetros de integração no modulo de Integração | EAI 2.0 | Parâmetros de integração | Cadastre o parâmetro.

Aonde está informado o Valor igual a "999" é o código da natureza financeira cadastrada no RM.

Caso a solução continue a gerar a mesma mensagem verifique a seção: Adiantamento e Retenções de Contratos - Liberar Adiantamento ou Retenção, da aba de **Parâmetros F6**

Caso o Titulo Financeiro não seja gerado no Protheus, acesse o tipo de movimento e certifique que na etapa 54 - Fin - Faturamento 1/6 a opção de Fatura o movimento e Fatura na inclusão devem estar marcadas.

Erro ao acessar informações no BackOffice. Falha ao consultar Faturamento BackOffice: O registro de Codigo/identificador "XX || XX" da entidade "Moeda" não encontrado na tabela De-Para ou não Foi integrado!

Esse aviso somente é apresentado quando possui integração com BackOffice Protheus.

Erro foi apresentado pois o de-para não existia na base de dados RM e protheus.

Para correção será necessário:

* Possuir o Adapter de CURRENCY cadastrado (MOEDA);
* Acessar o modulo SIGAADV e pesquisar por Moedas e cotações;  
  Em seguida cadastrar a moeda desejada ou alterar a moeda que foi apresentada o código na mensagem de aviso apresentada. Será criado o de-para da moeda e gerado mensagem de integração do CURRENCY;
6Gestão de Riscos7Concorrência Eletrônica8Relatórios

1. Ajuste de Relatório Padronizado:
   1. Identificar o relatório na pasta do SQA.
      1. Caminho TFS: **$/SQA/ObjetosGerenciais/12.1/Relatórios**
   2. Identificar o relatório na pasta do desenvolvimento.
      1. Caminho TFS: **$/RM/Documentos/Prj-Projetos/Relatórios/Arquivos Antigos/Relatorios Migrados - Somente consulta - favor subir fonte para o diretório padronizado**
   3. Salvar o relatório ajustado com o mesmo nome que estiver na pasta do SQA no novo diretório padronizado.
      1. Caminho TFS: **$/RM/Documentos/Prj-Projetos/Relatórios/Padrão/Fonte**
   4. Versionar arquivo do relatório.
      1. Criar atalho do RM.Exe
      2. Alterar o destino no RM.EXE
      3. Logar no Sistema, acessar RM Reports
      4. Editar o relatório e alterar a versão
   5. Salvar o arquivo do relatório versionado na pasta do SQA.
      1. Caminho TFS: **$/SQA/ObjetosGerenciais/12.1/Relatórios**
2. Relatório versão path. (Se o relatório for versão release, este passo dois é desnecessário)
   1. Enviar arquivo do relatório padronizado através do outlook:
      1. 1. Acesse no **[Portal da Engenharia](http://engenharia.bh01.local/DashboardExpedicao)**
         2. Acesse o menu **Gestão de Expedição | Ferramentas | Objetos Gerenciais**
         3. Informe as versões, selecione os arquivos e informar a categoria do objeto gerencial (Relatório).
         4. Após a conclusão da solicitação, os artefatos serão disponibilizados nos repositórios de acordo com a versão e categoria informados, e estarão disponíveis para o cliente nos próximos patches a serem gerados.
   2. Caso o relatório seja necessidade de algum cliente específico, além do passo 2.a, também é necessário solicitar ao P.O./S.M. a publicação do relatório:

      1. Ao final da publicação é necessário **conferir** se o comentário abaixo foi adicionado no Jira:

         \*\*\*\*\*Patch\*\*\*\*\*

         Prezado cliente [Cliente],  
         Estamos antecipando a correção do incidente referente ao ticket [ticket].  
         Disponível no <https://suporte.totvs.com/portal/p/10098/home>  
         (Versão: 12.1.xx.xxx)

         Obs: Você pode utilizar o Deploy Granular com este pacote. Acesse <http://tdn.totvs.com/x/FRwmDg>  
         Você será comunicado na entrega da solução homologada por notificação em seu e-mail.   
         Também pode acompanhar no Portal do cliente.

         Equipe TOTVS
9Segurança10HtmlHabilitar Portal Html - Projetos

Abaixo seguem instruções para criar uma ambiente HTML do TOP.

**Executar o restore, para o RM.Net, Corpore.Net e FrameHTML.**

**Realizar um Get full na pasta FramHTML no Visual Studio da versão correspondente. Adicionar na pasta FrameHTML o WebConfig de acordo com as infromações do config do Host.**

xml1Exemplo WebConfigtrue
















































































]]>

**Configurar o IIS e colocar as credências para acesso a rede.**

**Dê permissão para o usuário do ISS denominado IIS\_IUSRS:**

* Edita permissões na tela do ISS;
* Segurança;
* Editar;
* adicionar;
* [SEUHOST](http://localhost:8080/rm/Login/login.aspx)\IIS\_IUSRS;
* Controle total;

**Utilizar a URL [http://SEUHOST/rm/Login/login.aspx](http://localhost:8080/rm/Login/login.aspx) para realizar o login. Caso ocorra "Erro HTTP 404.0 - Not Found - O recurso que você está procurando foi removido, teve o seu nome alterado ou está temporariamente indisponível" utilize após o login a URL [http://SEUHOST/rm/totvs-html-framework/#/RM/Prj-Projetos](http://localhost:8075/rm/totvs-html-framework/#/RM/Prj-Projetos).**

11Parâmetros F6

Esta seção tem como objetivo esclarecer informações sobre os parâmetros que não podem ser informadas no Wiki Help.

Enviar retenção como desconto na liberação do período

* O parâmetro de "**Enviar retenção como desconto na liberação do período"** caso marcado o sistema irá enviar a retenção como desconto no campo "Desconto" do movimento do Nucleus.
* Caso o cliente utilize a formula de contrato "A" e o parâmetro de "**Enviar retenção como desconto na liberação do período"** esteja marcado, o sistema irá enviar a retenção 2x (esse problema não é bug e sim questão de parametrização do cliente).

Adiantamento e Retenções de Contratos - Liberar Adiantamento ou Retenção

O parâmetro que define o envio de Retenção Contratual e Adiantamento para o Backoffice Protheus se irá gerar Titulo financeiro ou Pedido de compra/venda possui umas particularidades para geração.

**Pedido de Compra/Venda**:

O tipo de movimento na etapa Orçamento, deve estar como "Não Edita".

**Titulo Financeiro a Pagar/Receber:**

* Tipo de movimento a ser gerado, deve possuir em sua parametrização a etapa **Fin - Faturamento 1/6** a opção de "**Fatura na Inclusão**" deve estar marcada;

* Cadastrar o Parâmetros Adapter | irá abrir a tela de parâmetros de integração, crie ou edite o parâmetro "CODNATUREZAFINANCEIRADEFAULT" e informar:  
  **Tipo**: String   
  **Valor**: código da natureza financeira cadastrada no sistema.

Discriminar Valores de Retenção e Dedução

* Na integração com o Protheus na versão 12.1.17 é necessário cadastrar os campos no dicionario de dados para que o Protheus receba os valores de retenção e dedução.
* No Nucleus(Totvs Gestão de Estoque Compras e Faturamento) é necessário que o parâmetro do tipo de movimento esteja com a etapa Item - Valores financeiros 2/2 campo Dedução e retenção como "Usa Valor";
* Parâmetro no Protheus "MV\_PMSITMU" deve estar ativo;

Os campos rque devem existir na base de dados Protheus são:

Tabela "**SC7 - Ped.Compra / Aut. entrega**":

C7\_RETENCA

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  |  |  |

C7\_DEDUCAO

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  |  |  |

C7\_FATDIRE

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  |  |  |

C7\_QUJERET

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  |  |  |

C7\_QUJEDED

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  |  |  |

* Não foi necessário o cadastro.

C7\_QUJEFAT

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  |  |  |

Tabela "**SD1 - Itens das Nf de entrada**":

D1\_RETENCA

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  | A120RDFRM("WHEN") |  |

D1\_DEDUCAO

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  | A120RDFRM("WHEN") |  |

D1\_FATDIRE

| Campo | Informações | Opções | Validações |
| --- | --- | --- | --- |
|  |  | A120RDFRM("WHEN") |  |

Discriminar quantidade e preço dos itens no movimento (Contrato de Insumos)

* O parâmetro “Discrimina quantidade e preço dos itens no movimento (Contrato de Insumos)” está marcado. Dessa forma, o sistema passa a considerar a Fórmula ‘C – Valor com Reajuste’ para todas as liberações de períodos de contrato. No envio dos itens ao movimento, o sistema deve respeitar a informação fornecida no campo Produto da Liberação (Contrato de Insumos).
* Para clientes **Protheus** o novo parâmetro não será exibido em tela e será considerado como marcado.

1. [TOPEXECONTROL01-2646](http://jiraproducao.totvs.com.br/browse/TOPEXECONTROL01-2646)
2ProtheusMicrosiga Protheus X Totvs Obras e ProjetosCódigo inválido. Grau superior XXX não cadastrado.

O problema é que o carácter de hífen ( - ) está utilizando no cadastro do código do centro de custo e na lib não permite hífen como separador de código.

Caracteres utilizados como separador de nível e não permitidos: " **.,-:/ ()** "

Informações válidas devem ser especificadas para analisar a cadeia de caracteres.

O problema é que registros da tabela FCFO na base de dados estavam com o campo PESSOAFISOUJUR com valor "EM BRANCO ou NULO".

Solução, foi dar update no campo passando para J ou F (Jurídico ou Físico).

Como verificar a data do fonte do Protheus

Segue uma dica sobre como conferir a Data de um Fonte Protheus de maneira rápida, sem acesso ao DevStudio ou TDS.

Acessar o cadastro de lançamento padrão na aba entidades:

Digitar o seguinte comando:

alert(getapoinfo("gpexini.prx")[4])

Obs:No lugar de **"gpexini.prx"** informar o nome da função que deseja consultar, após dar enter no campo que aparecerá a data da função.

Ao dar TAB no campo a Data do Fonte é exibida

Falha Erro ao salvar registro! Campo "Filial de Integração"obrigatório.

Problema:

Ao integrar Cliente Fornecedor ocorre o erro "Erro ao salvar registro! Campo "Filial de Integração"obrigatório. ".

Solução:

Compartilhamento da entidade no RM não é compatível com o compartilhamento no Protheus.

Ajustar:

Facilitar Detecção de Erros

**Problema:**

Bug de travamento ou erro não registrado no console.log ou no appserver em modo console.

**Solução:**

Incluir a tag FWLOGMSG\_DEBUG=1 no arquivo .ini do appserver, na seção do ambiente em uso.

Protheus EAIService:receiveMessage : Mensagem ITEM nao configurada ou configurada incorretamente para processamento pelo EAI

**Mensagem apresentada:**

xmlErro apresentado ao validar o XML no SoapUi


Sender
Protheus EAIService:receiveMessage : Mensagem ITEM nao configurada ou configurada incorretamente para processamento pelo EAI
]]>

**Problema:**

O erro e apresentado ao gerar a execução do XML de origem capturado no RM em "gerenciamento de mensagens". No SoapUi e executado o XML e alterado o UUID, após o erro e apresentado, pois no protheus o sistema não está parametrizado no "Adapter E.a.i" para receber a mensagem.

**Solução:**

Acesse o configurador do Protheus.

* Programa inicial: SIGACFG;
* Ambiente: 99;
* Ambiente | Schedule | Adapter E.a.i | Selecione a mensagem. Ex: "UNITOFMEASURE" | Campo "Recebe" deve está como "SIM";

Travamento - Integração ou Tela

**Problema:**

Travamento em processos ao realizar integração de movimentações do RM ao Protheus, ou até mesmo ao logar na Fila de Mensagens Schedule Schedule no SIGACFG.

**Solução:**

1 - Incluir a tag SPECIALKEY com um valor que não repita com outros usuários.

Cadastro de Fornecedor - Invalid Typecast in File FWInitCpo(a,b,c),xRet:=(MA020PcCgc()),FWCloseCpo(a,b,c,.T.),xRet

**Mensagem apresentada**:

THREAD ERROR ([17960], Alexandresilva, BHN050102864) 26/03/2018 14:05:27

invalid typecast in file d:\bamboo-agent-5.7.2\xml-data\build-dir\tp11-buildv2appsrv-tec11win32rpo32\advtec9\_tt11\advpl\instrvar.inl at line 821  
on {|a,b,c| FWInitCpo(a,b,c),xRet:=(MA020PcCgc()),FWCloseCpo(a,b,c,.T.),xRet }(PROTHEUSFUNCTIONMVC.PRX) 05/10/2017 18:39:41

[TOTVS build: 7.00.131227A-20170830 NG]  
Called from {|a,b,c| FWInitCpo(a,b,c),xRet:=(MA020PcCgc()),FWCloseCpo(a,b,c,.T.),xRet }(PROTHEUSFUNCTIONMVC.PRX) 05/10/2017 18:39:41

**Problema**:

Ao clicar em incluir apresenta o erro acima e fecha o smartclient.

**Solução**:

Acessar o smartclient no "Programa Inicial:" **APSDU** | Arquivo | Abrir | Selecione a opção no campo Driver referente ao tipo da sua tabela | OK | selecionar a tabela **SX3** (normalmente ctree) | Vá em utilitários "**Filtrar**" ou "**Ctrl + F**" e pesquise pela tabela **SA2** e campo **A2\_CGC**. Alterar o valor da coluna **X3\_PICTVAR** para **PICPES(M→A2\_TIPO)**

Gif mostrando como fazer a alteraçãoCtree Index Create - Clear Filter - Ctree Error 22 - IO Error: 2 - File number out of range File: c:\ambiente\eai20\versao\_rm\12.1.21\protheus\protheus\_data\semaforo\fwschd\_p12.lck on FWTBLCREATE(FWTABLEDDL.PRX) 

**Mensagem apresentada**:

THREAD ERROR ([11672], jonatas.faria, BHN050103152) 18/01/2019 08:26:26

c:\ambiente\eai20\versao\_rm\12.1.21\protheus\protheus\_data\semaforo\fwschd\_p12.lck: Ctree Index Create - Clear Filter - Ctree Error 22 - IO Error: 2 - File number out of range File: c:\ambiente\eai20\versao\_rm\12.1.21\protheus\protheus\_data\semaforo\fwschd\_p12.lck on FWTBLCREATE(FWTABLEDDL.PRX) 17/01/2019 17:42:38 line : 1413

**Problema**:

Ao tentar logar no smartclient e apresentado o erro, isso ocorre porque a pasta semáforo não existe ou falta de permissão no windows.

**Solução**:

Subir o server do Protheus como Administrador conforme imagem abaixo:

Acessar smartclient - Erro -35 (MYSQL;Protheus\_v17;localhost)

**Mensagem apresentada**:

Erro -35 (MYSQL;Protheus\_v17;localhost)

**Problema**:

Ao tentar acessar o smartclient e apresentado erro de falha de conexão.

**Solução**:

Acessar o arquivo appserver.ini e alterar o valor atribuido ao "DbDatabase" para DbDatabase=MSSQL;

Resposta do Servidor: {"errorCode":500,"errorMessage":"variable is not an object "}

**Mensagem apresentada**:

Resposta do Servidor: {"errorCode":500,"errorMessage":"variable is not an object "}

**Problema**:

Quando a execução dos testes automatizados começar a ocorrer este problema, será necessário a atualização do ambiente do protheus (Appserver e Smartclient).

Lembre-se que o ambiente 12.1.20 é "x32" os demais ambientes são "x64".

**Solução**:

* Acesse o site do <http://arte.engpro.totvs.com.br/>;
* Para baixar o appserver: <http://arte.engpro.totvs.com.br/totvstec_framework/appserver/versao12/>

x32: <http://arte.engpro.totvs.com.br/totvstec_framework/appserver/versao12/x32/windows> (sempre entre na pasta "latest");

x64: <http://arte.engpro.totvs.com.br/totvstec_framework/appserver/versao12/lobo_guara/windows/> (sempre baixe o arquivo da pasta "latest");

* Para baixar o SmartClient: <http://arte.engpro.totvs.com.br/totvstec_framework/smartclient/smartclient/>

x32:<http://arte.engpro.totvs.com.br/totvstec_framework/smartclient/smartclient/x32/windows/>

x64: <http://arte.engpro.totvs.com.br/totvstec_framework/smartclient/smartclient/x64/windows>/

Obs.: Sempre baixa o arquivo da pasta "latest".

WEBSERVICE - Using ABENDLOCK Configuration

**Mensagem apresentada**:

WEBSERVICE - Using ABENDLOCK Configuration

**Problema**:

Ao tentar realizar um processo no RM (Ex.: Gerar Integração com suprimentos/faturamento) a execução do processo fica em andamento por vários minutos, ao verificar o appserver nota-se a mensagem de **WEBSERVICE - Using ABENDLOCK Configuration** referente a documentação: , porém após 100 segundos, o processo ainda não e executado mesmo fechando e abrindo novamente o appserver e dbaccess.

**Solução**:

* Acessar o arquivo appserver.ini e informar a tag SPECIALKEY=nome de usuário;

Ex.: SPECIALKEY=JONATAS.FARIA (colocar maiúsculo )

* Reinicie o appserver e dbaccess.

INTEGDEF RETURN ERROR --&gt; [variable does not exist ARET] - [|THREAD ERROR ([6192], JOB\_WS, THIS) - MATI110

**Mensagem apresentada**:

INTEGDEF RETURN ERROR --&gt; [variable does not exist ARET] -

[|THREAD ERROR ([28636], JOB\_WS, THIS)   16/08/2018 11:59:12

variable does not exist ARET on MATI110(MATI110.PRX) 06/06/2018 18:30:27 line : 860

[TOTVS build: 7.00.131227A-20170830 NG]

Called from **MATI110** ( **MATI110**.PRX) 06/06/2018 18:30:27 line : 860|

Called from INTEGDEF (**MATA110**.PRX) 30/08/2017 11:10:56 line : 7723|

Called from FWUMESSAGE(PROTHEUSFUNCTIONMVC.PRX) 05/10/2017 18:39:41 line : 5626|

Called from FWEXECEAI(FWEAIUTIL.PRW) 05/10/2017 18:39:40 line : 533|

Called from FWEAI:SAVE(FWEAI.PRW) 05/10/2017 18:39:40 line : 1261|

Called from EAISERVICE:RECEIVEMESSAGE(EAISERVICE.PRW) 05/10/2017 18:39:40 line : 135|

Called from WSEXECUTE(XMLWSVCS.PRW) 05/10/2017 18:39:40 line : 2001|

Called from \_\_WSCONNECT(XMLWSVCS.PRW) 05/10/2017 18:39:40 line : 1104|

Called from STATICCALL(XMLWSVCS.PRW) 05/10/2017 18:39:40 line : 1104|]

**Problema**:

No cadastro de Adapter cadastramos a REQUEST para solicitação de armazém e de compra. Quando somente uma está cadastrada e apresentado o erro, no caso tinha somente a de solicitação de compra, apresentou o erro descrito acima.

**Solução**:

Realize o cadastro de todos os adpters de Request.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Integração** | **M. Única** | **Rotina** | **Mensagem** | **Envia** | **Recebe** | **Método** | **Operação** | **Canal** | **Versão Envio** | **Alias** | **Condição** |
| TOP x Protheus | Sim | MATA110 | Request | Não | Sim | Síncrono | Todas | EAI | 1.009(P12) ou 1.008(P11) |  | INTELIRES("SC1") |
| TOP x Protheus | Sim | MATA105 | Request | Não | Sim | Síncrono | Todas | EAI | 1.009(P12) ou 1.008(P11) |  |  |

Acessar smartclient - Arquivo SIGAADV.PSS inválido

**Mensagem apresentada**:

Arquivo SIGAADV.PSS inválido

**Problema**:

Ao tentar acessar o smartclient e apresentado erro Arquivo SIGAADV.PSS inválido.

**Solução**:

Copiar o arquivo "SIGAADV.PSS" do diretorio do espelho-porta. Colar o arquivo dentro da pasta system que se encontra dentro da pasta protheus\_data.

Ex.: C:\Ambiente\EAI20\Versao\_RM\12.1.20\Protheus\protheus\_data\System.

Acessar smartclient - ADS Error - Could not load ACE32.dll. on CHECKSMOFILE(APLIB100.PRW)

**Mensagem apresentada**:

**Problema**:

Ao tentar acessar o smartclient e apresentado erro, pois não foi possivel carregar a dll ACE32.dll

**Solução**:

Dentro da pasta do appserver existe uma pasta chamada "ace\_8.00" copie todos os arquivos dentro desta pasta e cole dentro do diretorio raiz do appserver.

Session [P12\_Congelada] not found in appserver.ini. Verify the "Environment in the Server" in file C:\advtec9\lib\config.cpp at line 78

**Mensagem apresentada**:

Session [P12\_Congelada] not found in appserver.ini. Verify the "Environment in the Server" in file C:\advtec9\lib\config.cpp at line 78

**Problema**:

Ao tentar acessar o smartclient é apresentado o erro descrito acima impedindo de acessar o ambiente Protheus.

**Solução**:

O erro ocorre, pois o arquivo do appserver.ini foi corrompido.

* Para solucionar o problema, copie todo conteúdo do appserver.ini para o bloco de notas, salve o arquivo novamente com a mesma descrição e extensão (Appserver.ini);
* Reinicie o serviço do appserver.ini é acesse o smartclient.
Open index error: c:\ambiente\eai10\versao\_rm\12.1.19\protheus\protheus\_data\system\sigamat.ind

**Mensagem apresentada**:

THREAD ERROR ([4764], jonatas.faria, BHD50100157) 27/06/2018 14:22:01

Open index error: c:\ambiente\eai10\versao\_rm\12.1.19\protheus\protheus\_data\system\sigamat.ind

on NEWSM0(APLIB100.PRW) 10/05/2018 12:15:48 line : 846

**Problema**:

Ao tentar acessar o smartclient é apresentado o erro acima, pois ao tentar abrir o arquivo sigamat.ind ele possui informações de um outro diretório diferente do informado.

Esse erro foi apresentado pois foi realizado a copia de um outro ambiente Protheus e renomeado somente algumas pastas, desta forma o arquivo sigamat.ind contém informações do antigo diretório.

**Solução**:

Acesse o ambiente Protheus, dentro da pasta **protheus\_data/system/** ache o arquivo sigamat.ind;

* Exclua o arquivo sigamat.ind;
* Reinicie o appserver e dbaccess;
* E tente acessar novamente o smartclient.

OBS.: caso ocorra erro com o arquivo sigamat.emp ou o ind execute o appserver, dbaccess e smartclient com administrador para que o arquivo seja criado e não ocorra erro de sigamat.emp.

[GLOBAL VAR] VarGetX → invalid ID: ""

**Mensagem apresentada**:

**Problema**:

Ao tentar incluir uma fase de projeto é apresentado erro no Appserver.exe em seguida a conexão e encerrada.

**Solução**:

Deve atualizar o diretório bin\appserver para um dicionário mais recente.

O erro em si aconteceu, pois, o dicionário do appserver estava desatualizado.

invalid field name in Alias

**Mensagem apresentada**:

THREAD ERROR ([6464], jonatas.faria, BHD50100157) 28/06/2018 08:59:36  
invalid field name in Alias SA2->A2\_EC05DB on REGTOMEMORY(MATXATU.PRX) 26/04/2018 15:04:01 line : 3533

**Problema**:

Ao abrir a tela de fornecedor é apresentado o erro acima, isso ocorre por que não existe a coluna **A2\_EC05DB** especificada no erro na tabela **SA2** informada.

**Solução**:

* Acesse o SIGACFG;
* Banco de dados | Dicionário | Banco de dados;
* Procure pela Tabela informada no erro, no caso da mensagem acima foi a tabela SA2;
* Verifique o campo **A2\_EC05DB** na tabela SA2 em seguida verifique o **tipo** e o **tamanho** do campo para fazer a inserção na base de dados;
* Execute o comando SQL na base de dados Protheus para criar o campo:   
  **ALTER TABLE** SA2T10 **ADD** A2\_EC06DB **VARCHAR(6) NULL**;
* Reinicie o appserver, dbaccess e smartclient.
Não foi possível encontrar a Coligada 1 no De-Para.

**Mensagem apresentada**:

****\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_** EAI 1.0 \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

Não foi possível encontrar a Coligada 1 no De-Para.

Ou

Não foi possível encontrar a Coligada -1 no De-Para.

**Segue o arquivo com o erro completo:**

**Problema**:

Ao tentar cadastrar uma condição de pagamento e apresentado o erro de "Não foi possível encontrar a Coligada 1 no De-Para." isso ocorre porque o De-para de GCOLIGADA está errado.

**Solução**:

O de-para de GCOLIGADA deve estar desta forma:

Cannot insert duplicate key row in object 'dbo.XX4T10' with unique index 'XX4T10\_UNQ'. The duplicate key value is ( ,MATA020,CUSTOMERVENDOR,,0)

**Mensagem apresentada**:

THREAD ERROR ([7852], jonatas.faria, BHD50100157) 25/04/2018 08:40:18  
XX4T10: DB error (Update): -29 File: XX4T10 - Error : 2601 (23000) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]Cannot insert duplicate key row in object 'dbo.XX4T10' with unique index 'XX4T10\_UNQ'. The duplicate key value is ( ,MATA020,CUSTOMERVENDOR,,0). ( From tISAMFile::Update )  
Thread ID [3636] User [Administrador] IO [8972] Tables [17] MaxTables [17] Comment [MATA020 - TCPIP - ThreadID(7852)] SP [ ] Traced [No] SQLReplay [No] InTran [No] DBEnv [MSSQL/P12\_CONGELADA] DBThread [(SPID 51)] Started [25/04/2018 08:39:59] IP [127.0.0.1:1313] IDLE [ ] InTransact [ ] Memory [503008] Running [ROP\_UPDATE] RCV [79987] SND [708925] TCBuild [20171117-20180215]   
UPDATE dbo.XX4T10 SET XX4\_ROTINA = ? WHERE R\_E\_C\_N\_O\_ = ?  
-- Binded Parameters List --  
#1 [C] [MATA020 ]  
#2 [N] [37.000000]  
on MSUNLOCK(APLIB060.PRW) 20/04/2018 11:00:30 line : 851

**Segue o arquivo com o erro completo:**

**Problema**:

Ao abrir a tela de fornecedor é apresentado o erro acima, isso ocorre por que existe mais de um Adapter cadastrado para aquela rotina.

**Solução**:

Deve acessar o SIGACFG | Ambiente | Schedule | Adapter E.a.i | Apagar o Adapter "MATA020", pois o Adapter correto para ser utilizado na integração do EAI 2.0 e o MATA020M.

THREAD ERROR DBSetOrder - Index not found: EVENTVIEWER Order Number: 1 on FWTABLEDDL:OPENTABLE(FWTABLEDDL.PRX)

**Mensagem apresentada**:

THREAD ERROR DBSetOrder - Index not found: EVENTVIEWER Order Number: 1 on FWTABLEDDL:OPENTABLE(FWTABLEDDL.PRX)

**Problema**:

Ao realizar algum cadastro é apresentado a mensagem de erro descrita acima.

**Solução**:

* Renomeie os arquivos SXI.dbf /dtc /cdx, \_schdtsk.dbf/dtc/cdx, \*.cdx e \*.fpt. localizado no diretório Protheus\_Data/ System.

Exemplo: sxi\_backup.cdx

**Obs.: Caso não exista o arquivo mencionado acima, faça o próximo passo.**

* Renomeie o diretório semaforo, o mesmo encontra-se dentro da pasta Protheus\_Data.

Exemplo: semaforo\_backup

* Reiniciar o serviço do Protheus e acessar o sistema, (ao acessar novamente o sistema o sistema recria estes arquivos que foram renomeados, e isso faz com que o erro seja solucionado pois provavelmente os arquivos que foram renomeados ficaram corrompidos)
* Testar novamente a rotina e verificar se ficou ok.
Rebuild - Ctree Error 485 - IO Error: 5 - Error creating sortwork.00x file.

**Mensagem apresentada**:

Rebuild - Ctree Error 485 - IO Error: 5 - Error creating sortwork.00x file.

**Problema**:

Ao tentar logar no Smartclient e apresentado erro de re-build.

**Solução**:

* Pare os serviços do Dbaccess e Appserver;
* Execute como ADM o Dbaccess e Appserver;
* Execute o smartclient como adm e faça o login para que o re-build seja feito;

Aplicativo integrado não encontrado na base de dados para o Produto 'PROTHEUS' e SourceApplication 'P1218'.

**Mensagem apresentada**:

Aplicativo integrado não encontrado na base de dados para o Produto 'PROTHEUS' e SourceApplication 'P1218'.

**Problema**:

Ao realizar algum cadastro ou ação no protheus que necessite fazer a chamada da integração com o RM é apresentada a mensagem de erro acima.

**Solução**:

* Acesse o modulo de Integração | EAI 2.0 | Aplicativos | Edite o aplicativo com o código do produto igual a "**PROTHEUS**" e informe o código especificado na mensagem no campo "**Código Do SourceApplication**", no caso o nosso é "**P1218**"
* Reinicie o Appserver em seguida realize o cadastro desejado...

Erro no parâmetro CODCLASSIFICPAIS

**Mensagem apresentada**:

**Problema**:

Ao tentar realizar uma rotina que necessita deste cadastro e apresentado erro referente ao parâmetro CODCLASSIFICPAIS do RM.

**Solução**:

* Acesse o Totvs Gestão Fiscal | Globais | Mais | Países e certifique que possui o cadastro do País;
* Acesse o Totvs Gestão Fiscal | Globais | Mais | Endereço | Classificação de País | e cadastre o código = 1 e Descrição = Brasil;
* No cadastro de Países | Anexo | Codificação de País | Informe o código 1 cadastrado anteriormente e também o valor "105" referente ao País;
* Acesse o Modulo de Integração | EAI 2.0 | Parâmetros de | encontre o parâmetro "CODCLASSIFICPAIS" e informe no campo "Valor do parâmetro" o valor "1" referente ao cadastro da "Classificação de Pais".

3AgilisTotvs Gestão de Relacionamento com o Cliente21Meus AtendimentosAtendimento [1-1-99]: Atendente não é chefe do responsável ou o responsável pelo atendimento

**Problema:**

Ao tentar realizar um Repassar atendimento, Repassar de volta ou Avanço de Etapa é apresentado o erro acima.

O erro ocorre por duas situações:

**1ª:** Você está tentando repassar ou avançar a etapa de um atendimento que não é do usuário logado.

Por exemplo: Usuário logado é o "mestre" e você está tentando repassar ou avançar um atendimento que é de responsabilidade do usuário "jonatas.faria" desta forma será apresentado a mensagem de erro.

**2ª:** Você não é chefe do usuário responsável pelo atendimento.

**Solução:**

**1ª Solução:**

Acesse o Totvs Gestão do Relacionamento com o Cliente com o usuário do responsável do atendimento desejado.

**2ª Solução:**

* Vincule o usuário que está responsável pelo atendimento a uma hierarquia que o chefe seja o usuário 'mestre' por exemplo.

Para isso acesse Atendente | Atendente | Atendentes | Edite o atendente responsável pelo atendimento | no campo Hierarquia, você deve informar uma hierarquia aonde o chefe seja o usuário desejado no meu caso é o usuário logado 'mestre'.

Veja o exemplo aqui

**3ª Solução:**

Crie uma hierarquia para definir que o usuário mestre seja o chefe dos demais usuários.

* Para isso acesse Atendente | Atendente | Hierarquias | crie uma nova hierarquia;
* Anexos | Atendentes | Adicione todos os atendentes que você deseja que o usuário mestre seja o chefe.

2Workflow3Atendimento4Atendente5Produto6Cliente/Representante7Marketing8Serviços9Configurações4FLUIGIntegração TOP x FLUIG5AutomaçãoErros apresentados na automação e como soluciona-los

Este card tem como finalidade auxiliar a equipe nos erros apresentados na automação de teste, desta forma agilizando na criação das automações e execuções manuais dos testes.

Unauthorized

**Mensagem de erro:**

xmlEclipseErro Unauthorized


a:Unauthorized
Unauthorized
]]>

**Problema:**

Ao tentar executar o XML desejado e apresentado erro de não autorizado (Unauthorized).

**Solução:**

1ª Solução:

Caso esteja utilizando o Soap UI, certifique-se que na parte inferior da estrutura XML informada, esteja as informações da autenticação.

São elas:

* Usuário: mestre
* Senha: totvs
* Marcar a opção "athenticate pre-emptively"

2ª Solução: Acesse o Test Flow 2.0 e verifique se a atividade de web service está com a autorização do usuário mestre.

Para verificar acesse a atividade web service em Cadastros | Atividades | Serviços | Web service, na aba propriedades o usuário e senha devem estar preenchidos.

3ª Solução:

* Executar o RM.Host.exe como administrador. Para isso clique no RM.Host.exe | Botão direito do mouse | Executar como Administrador.

Após executar o host como administrador tente realizar novamente a execução ou "Recuperar informações" (no Test Flow 2.0);

4ª Solução:

Verificar se o arquivo RM.Host.exe.config possui informada a tag <DefaultDB>, contendo o nome do Alias a ser utilizado.

System.Runtime.Serialization.SerializationException: Error in line 2 position 2. Expecting element 'PrjContratoAssociarItemParams' from namespace 'http://www.totvs.com.br/RM/'.. Encountered 'Element' with name 'PrjContratoLiberacaoPdoFaturamentoParamsProc', namespace 'http://www.totvs.com.br/RM/'.

**Mensagem de erro:**

**Problema:**

Ao executar o agendamento ou projeto de teste acontece um erro na atividade de web service, isso ocorre porque na atividade está utilizando um outro DataserverName.

**Solução:**

Acesse a atividade de web service e informe o DataServerName correto.

No caso descrito acima o **DataServerName** correto seria o "PrjContratoLiberacaoPdoFaturamentoParamsProc"

500: Internal Server Error - There is an error in xml document (0,0)..

**Mensagem de erro:**

**Problema:**

Ao tentar "Recuperar Informações" no cadastro de atividades web services e apresentado a mensagem de erro 500: Internal Server Error - There is an error in xml document (0,0)...

**Solução:**

1ª Solução:

* Desativar o Firewall do Windows.  
  Para desativar acesse o menu "Iniciar" e digite Firewall do Windows | Ativar ou Desativar o Firewall do Windows | Desative todas as opções. Após desativar o firewall, acesse o Test Flow | Cadastros | Atividades | Serviços | Web Services | Edite o web service | Limpe o Cache através do comando Ctrl + F5 | Tente recuperar as informações novamente.

Obs.: Certifique-se que o Agent esteja iniciado, o arquivo rm.host.exe.config esteja com a tag do DefaltDB e HTTPPORT, depois inicie o rm.host e teste a conexão no link "Servidor:Porta/wsPageIndex".

2ª Solução:

* Executar o RM.Host.exe como administrador. Para isso clique no RM.Host.exe | Botão direito do mouse | Executar como Administrador.

3ª Solução:

* No cadastro da atividade web service, o campo Uri (WSDL) utilize o nome do servidor da sua máquina ou o IP;

Exemplo:

Usando o nome do servidor: [http://bhd000009999:8051/wsProcess/MEX?wsdl](http://10.31.8.173:8051/wsProcess/MEX?wsdl)

Usando o IP: [http://10.31.6.71:8051/wsProcess/MEX?wsdl](http://10.31.8.173:8051/wsProcess/MEX?wsdl)

Para descobrir o IP da máquina, basta abrir o prompt de comando e digitar o comando ipconfig e pegar o endereço do IPV4.

**Obs.: Não utilize no Url (WSDL) como local host.**

4ª Solução:

Exclua todo seu ambiente e faça um novo Restore da versão utilizada.

5ª Solução:

Verifique as configurações do seu DefaultDB e certifique que possui o alias criado de acordo com o DefaultDB.

6ª Solução:

Utilize o HTTPPORT no config do host utilizando uma porta que tenha absoluta certeza que não está ocupada.

Por exemplo:

<add key="HTTPPORT" value="**9999**" />  
<add key="DefaultDB" value="Alias-Treinamento" />

7ª Solução:

Na execução do PROJETO DE TESTE é apresentado o erro descrito acima. Desta forma é necessário que execute o rm.host como administrador.

* Clique com o botão direito do mouse, Propriedades | Compatibilidade;
* Marque as opções "Executar este programa em modo de compatibilidade" igual a Windows 7 e Nivel de Privilégio igual à "Executar este programa como administrador";

OBS.: Caso seja exibido mensagem solicitando confirmação da execução em modo adm siga o seguinte link para desativar o UAC: [Desativar UAC Windows 10](https://www.tecmundo.com.br/windows/91481-windows-10-desativar-uac-dispensar-permissoes-administrador.htm)

Aviso importante

O Controle de Conta de Usuário (User Account Control), ou UAC, foi lançado junto do Windows Vista e Windows Server 2008 com o objetivo de proteger o SO da Microsoft de atividades e programas potencialmente danosos. Ao desativar o UAC você aceita que os programas de terceiros, façam a instalação sem a permissão do user ADM.

É recomendado que após a execução dos testes, retorne as configurações padrões do UAC.

Resposta do Servidor: {"errorCode":500,"errorMessage":"variable is not an object "}

**Mensagem apresentada**:

Resposta do Servidor: {"errorCode":500,"errorMessage":"variable is not an object "}

**Problema**:

Quando a execução dos testes automatizados começar a ocorrer este problema, será necessário a atualização do ambiente do protheus (Appserver e Smartclient).

Lembre-se que o ambiente 12.1.20 é "x32" os demais ambientes são "x64".

**Solução**:

* Acesse o site do <http://arte.engpro.totvs.com.br/>;
* Para baixar o appserver: <http://arte.engpro.totvs.com.br/totvstec_framework/appserver/versao12/>

x32: <http://arte.engpro.totvs.com.br/totvstec_framework/appserver/versao12/x32/windows> (sempre entre na pasta "latest");

x64: <http://arte.engpro.totvs.com.br/totvstec_framework/appserver/versao12/lobo_guara/windows/> (sempre baixe o arquivo da pasta "latest");

* Para baixar o SmartClient: <http://arte.engpro.totvs.com.br/totvstec_framework/smartclient/smartclient/>

x32:<http://arte.engpro.totvs.com.br/totvstec_framework/smartclient/smartclient/x32/windows/>

x64: <http://arte.engpro.totvs.com.br/totvstec_framework/smartclient/smartclient/x64/windows>/

Obs.: Sempre baixa o arquivo da pasta "latest".

Esta página não está funcionando - HTTP ERROR 400

**Mensagem de erro:**

Esta página não está funcionando.  
Se o problema continuar, entre em contato com o proprietário do site.  
HTTP ERROR 400

**Problema:**

Ao tentar executar um projeto de teste com web service e na execução do projeto acessar a página do DataServer ou DataProcess é apresentado o erro de Página não está funcionando. Posteriormente o projeto de teste não é executado com sucesso.

**Solução:**

* Apague o arquivo Alias.dat;
* No arquivo RM.Host.exe.config configure o DefaultDB e set o HTTPPORT uma porta diferente de 8051;
* Inicie o host e na atividade web service clique no botão "Recuperar Informações" abra o método utilizado para execução do web service.  
  Exemplo: ExecuteWithXmlParams;
* Copie o conteudo do campo "Soap Endpoint" e cole no xml original utilizado para execução do web service.
* Certifique-se também que o campo do Uri (WSDL) está correto também.
Log: Invalid object name 'XXXXX'.

**Mensagem de erro:**

Log: Invalid object name 'XXXX'.

**Problema:**

Ao realizar a execução do projeto de teste é apresentado erro de **Log: Invalid object name 'xxxxx'** na comparação SQL.

**Solução:**

* Caso utilize o programa C# "Cria conexão", certifique-se que o SQL Comparativo foi vinculado ao Programa C#.

Exemplo:

O Programa C# "Cria conexão" deve ser configurado da seguinte maneira:

* Clique sobre o Programa C# em seguida clique na opção "Propriedades da Atividade";
* Clique na opção "Code" , localizado no canto superior direto;
* O código abaixo deve ser colado no programa C#.

  jsEclipse

  Obs.: Se "DbType" igual a "0" então e banco de dados **SQL**, Senão "DbType" igual a "1" então e banco de dados **ORACLE**.

* Verifique se a Comparação SQL.  
  \* Valide o Servidor se está correto, nome do banco, usuário, senha e se a sentença Sql está correta.

Erros por causa do License Server - \\Engrmaut\AUTOMACAO\Bases TOTVS Tester\v1180\1180\Tst-Avaliação\SQL\TstResultado12120\_1.Temp

**Mensagem de erro:**

\\Engrmaut\AUTOMACAO\Bases TOTVS Tester\v1180\1180\Tst-Avaliação\SQL\TstResultado12120\_1.Temp

**Problema:**

Ao realizar a restauração de uma base de dados via Test Flow e apresentado o erro referente ao arquivo temporário TstResultado12120.

**Solução:**

* Acesse a base de dados RM;
* Ao apresentar a tela do **Licenserver,** aperte o atalho Shift + F6;

* Informe os dados:

CNPJ: 21.867.387/0001-58

CHAVE: D3595ED.3DADBD0.DDDED7D.FDEA053-5X2

* Salve;
* Tire um backup da base de dados para sobrepor a base que ocorre o erro, desta forma este backup não irá apresentar o erro;

Verificando erros de Web service quando somente o SQL apresenta erro e o WS ou REST foi executado com sucesso.

**Mensagem de erro:**

Ao realizar uma execução do Web service via agendamento ou execução pela tela de Projeto de teste, é apresentado erro de comparação de SQL. Ao clicar sobre a comparação que deu erro a tela de comparação apresenta somente um resultado referente ao mock realizado quando foi criado o teste automatizado.

Ex.:

**Problema:**

O problema é que ao verificar a execução não é apresentado erro no web service, somente a comparação que apresenta erro. Desta forma o automatizador não identifica qual é o real problema da execução do teste.

**Solução:**

Caso este problema ocorra conforme o **exemplo** abaixo:

Será necessário somente clicar sobre a atividade **web service,** desta forma é possívelidentificar o erro que ocorreu para que o SQL comparativo não seja executado corretamente.

**Exemplo:**

The server encountered an error and can't fulfill the request

**Mensagem de erro:**

The server encountered an error and can't fulfill the request

**Problema:**

O problema pode ocorrer na execução manual de um teste automatizado (REST), Agendamento ou execução do projeto de teste.

The server encountered an error and can't fulfill the request

**Solução:**

**1ª solução:**

* + - * + Acessar o diretório do arquivo appserver.ini (ex.:C:\Ambiente\EAI20\Versao\_RM\12.1.21\Protheus\bin\appserver );
        + Edite o arquivo appserver.ini;
        + Na seção [HTTPURI] informe na opção "Instances" o seguinte valor: 5,10,5,5

Exemplo:

No exemplo a seguir, o sistema disponibilizará 5 threads para atender as requisições chegando a um máximo de 20 threads.

Quando o número de threads livres cair para menos que 3, o sistema disponibilizará mais 5 threads.

```
[localhost/ws]
enable=1
path=c:\data\web\ws
environment=environment
instances=5,20,3,5
defaultpage=wsindex.apw
```

**2ª solução:**

Acesse o ambiente RM em seguida localize o arquivo rm.host.exe | propriedades | aba compatibilidade e marque a opção de executar como adm.

**3ª solução:**

Alterar o IP do License server do Protheus dentro da tag **[LICENSECLIENT].**

**[LICENSECLIENT]**

;informar o ip da maquina license alternativo: 10.171.67.144

;Licenser server RM 10.31.0.130

;server=10.171.67.144

server=10.31.0.130

port=5555

Erro na chamada do método ExecuteWithXmlParams. Unable to connect to the remote server 

**Mensagem de erro:**

#### [Validação de Execução de Operação ExecuteWithXmlParams](http://bh-testflow/testflow/webservices/update/75203)

HttpStatusCode: 400   
Log: Erro na chamada do método ExecuteWithXmlParams. Unable to connect to the remote server

**Problema:**

Ao realizar a validação do xml informado no metodo ExecuteWithXmlParams e apresentado o erro "Erro na chamada do método ExecuteWithXmlParams. Unable to connect to the remote server" isso ocorre porque o Soap EndPoint está preenchido incorretamente com outro servidor ou porta.

**Solução:**

* Abra a execução do metodo ExecuteWithXmlParams e informe no campo "Soap EndPoint" o servidor e porta corretos.

RM.Lib.RMSBrokerException: Classe não encontrada:

**Mensagem de erro:**

#### RM.Lib.RMSBrokerException: Classe não encontrada:

**Problema:**

Ao realizar a validação ou execução do teste automatizado e apresentado o erro descrito acima. O problema ocorre porque foi informado o XML ou o nome da classe do processo no campo errado.

**Solução:**

* Na atividade Web service, abra o método do xml e informe na tag <tot:ProcessServerName> o nome da classe do processo.

Ex.: <tot:ProcessServerName>**PrjConsultaApropEaiProc**</tot:ProcessServerName>

 Status Code: 404 Resposta do Servidor: Unable to connect to the remote server

**Mensagem de erro:**

#### 

#### Status Code: 404 Resposta do Servidor: Unable to connect to the remote server

**Problema:**

O problema ocorre porque ao executar a automação via Rest integrada com o Protheus as linhas da seção [OnStart] está comentada no arquivo appserver.ini:

[OnStart]  
JOBS=HTTPJOB  
RefreshRate=120

**Solução:**

Tire o comentário do arquivo appserver.ini e execute novamente o teste.

Log: Invalid object name 'MAPROP'.

**Mensagem de erro:**

#### 

Log: Invalid object name 'MAPROP'.

**Problema:**

O problema ocorre porque a atividade **26 - SQL Comparativo** - não está vinculada a **base de dados** para execução da sentença SQL, desta forma e apresentado o erro descrito acima.

**Solução:**

Acesse o projeto de teste e vincule a atividade de Comparação de banco de dados à atividade C# ou base de dados que deseja que a consulta SQL seja realizada.

 Status Code: 404 Resposta do Servidor: {"errorCode":404,"errorMessage":"The server can't find the requested resource."}

**Mensagem de erro:**

#### 

#### Status Code: 404 Resposta do Servidor: {"errorCode":404,"errorMessage":"The server can't find the requested resource."}

**Problema:**

O problema ocorre porque ao executar a automação via Rest integrada com o Protheus o pacote "**FSWDEFAULTREST**" não foi aplicado no RPO.

**Solução:**

Aplique o patch do Rest via Dev Studio e execute novamente o teste automatizado.

Folders for searching definition files [.ch] not entered. [Project: Apropriacao]

**Mensagem de erro:**

#### Folders for searching definition files [.ch] not entered. [Project: Apropriacao]

**Problema:**

Ao tentar realizar a compilação dos fontes no dev studio e apresentado o erro acima, isso ocorre porque não existe a referencia da pasta include informado no projeto.

**Solução:**

Clique com o botão direito do mouse sobre o projeto informado | Propriedades | Developer Studio | Includes | e adicione o diretório dos includes.

Invalid column name 'S5\_CODGRP

**Mensagem de erro:**

Resposta do Servidor: {"errorCode":400,"errorMessage":"Erro ao consultar Apropria��es de Despesa! Erro:\r\nSCGN000036: Error : 207 (S0022) (RC=-1) - [Microsoft][ODBC SQL Server Driver][SQL Server]

**Invalid column name 'S5\_CODGRP'.**\n ( From tMSSQLConnection::GetQueryFile )\nThread ID [2400]\tUser

[HTTP\_WT\_P12\_CONGELADA\_HTTPREST\_HTTPURI@T1�D�MG�01]\tIO [820]\tTables [32]\tMaxTables [33]\tComment []\tSP [ ]\tTraced [No]\tSQLReplay [No]\tInTran [No]\tDBEnv [MSSQL\/P12\_CONGELADA]\tDBThread [(SPID 57,60)]\tStarted

[09\/10\/2018 10:03:47]\tIP [127.0.0.1:1313]\tIDLE [ ]\tInTransact [ ]\tMemory [674544]\tRunning [ROP\_QUERY]\tRCV [14797]\tSND [80119]\tTCBuild [20180606-20180726]\tTCVersion

[18.1.1.1\_RC4]\tARCH [64]\tOS [WINDOWS]\tBUILD [RELEASE]\t\n

**SELECT** 1 REG FROM **SBMT10** DOM WHERE BM\_FILIAL = 'D MG 01 ' AND **BM\_GRUPO** = '7777' AND EXISTS (SELECT 1 FROM **SS5T10** CDOM **WHERE** S5\_FILIAL = 'D MG 01 ' AND **S5\_CODGRP** = '7777' AND CDOM.D\_E\_L\_E\_T\_ = ' ' ) "}

**Problema:**

Ao realizar a execução do Rest e apresentado um erro referente a tabela **SS5** isso ocorre porque existe uma inconsistência na base de dados.

**Solução:**

O erro em questão ocorre pois há um registro no dicionário de dados SX9 - Relacionamentos que estabelece um relacionamento entre as tabelas SBM e SS5 onde a chave de relação da SS5 contém um campo virtual, o que é inconsistente uma vez que campos virtuais não existem no banco de dados.  
Este registro da SX9 não é padrão, não consta em nenhuma versão de dicionário expedida. Assim, o registro em questão deve ser removido do ambiente do cliente.

* Acessar a APSDU
* Abri a tabela sx9t10.dtc
* filtrar por X9\_DOM=SBM e X9\_CDOM = SS5
* Deletar a linha toda.

Erro no XML de Web service Executado com secesso: System.Runtime.Serialization.SerializationException: Error in line XXX position Y. 'Element' 

**Mensagem de erro:**

**Problema:**

Esse erro é apresentado geralmente no Totvs Obras e Projetos, isso porque o sistema carrega os parâmetros no XML de alguns processos, isso faz com que ao incluir um novo parametro seja apresentado o erro:

System.Runtime.Serialization.SerializationException: Error in line 9253 position 6. 'Element' '**\_ParametroXXX**' from namespace '' is not expected. Expecting Element ''**\_ParametroNovo**'.

**Solução:**

1ª Solução:

* Execute o mesmo processo do teste manualmente em seguida abra o XML de parâmetro de Jobs e procure pelo "**\_ParametroNovo" .**
* Copie a tag do novo parâmetro;
* Verifique a tag que está acima;
* Pesquise a tag que está acima no XML com o erro;
* Cole a tag **\_ParametroNovo** abaixo conforme o xml capturado no XML de parâmetros de jobs.

6API / Mensagens Unica

DIcas:

1 - Portal API: <https://api.totvs.com.br/>

2 - Definir as Tags no Host: - Serviços REST RM passaram a serem armazenados no Host RM. Não temos o Swagger. URL Exemplo: <http://localhost:8098/API/construction-projects/top/v1/task-cost-assigments?companyId=1&projectId=2>

<add key="APIPORT" value="8098" />  
<add key="DefaultDB" value="exemplo\_120123" />

2 - Processo de Aprovação: <https://api.totvs.com.br/processoelaboracaomsgpadronizada.png>

2.1 - Ryver: <https://totvs.ryver.com/> - Resetar a senha. (Demora chegar o e-mail)

Acessar publicações: <https://totvs.ryver.com/index.html#posts/1871626>

3 - Processo Elaboração API - Resumo:

3.1 - Prefira utilizar os verbos: get, post, put delete e transaction?

3.2 - Publica o item no Ryver, com o nome da mensagem como tópico.  
Caso não exista tópico solicitar: [elvis.brito@totvs.com.br](mailto:elvis.brito@totvs.com.br)  
3.3 - Convide todos os POs do segmento para o tópico, conforme a planilha "Mapa de Clientes"

3.4 - Inclusão de campos - Aprovação via e-mail: [comiteintegracao@totvs.com.br](mailto:comiteintegracao@totvs.com.br), considerando 5 dias para respostas.

4 - Repositório Mensagens - Git Hub: <https://github.com/totvs/ttalk-standard-message/tree/master/jsonschema>

4.1: Começando com Git Hub

<http://blog.alura.com.br/comecando-com-git-aprendendo-versionar/>

5 - Vídeo com a reunião onde foram apresentadas as ultimas alterações no processo:

<https://drive.google.com/file/d/1PCICPMmnRxcdmN9SZinHu0k1lyZTHVtS/view>

6 - Elaboramento uma mensagem Padronizada:

<http://tdn.totvs.com/pages/viewpage.action?pageId=312149857>

7 - Elaboração de API.

[http://tdn.totvs.com/display/framework/7.+Aprovando+API+de+mensagem+padronizada](https://www.google.com/url?q=http://tdn.totvs.com/display/framework/7.%2BAprovando%2BAPI%2Bde%2Bmensagem%2Bpadronizada&sa=D&source=hangouts&ust=1541072920659000&usg=AFQjCNHOXkko2q7BSDKXWB5htE3Y_OHmQQ)

8 - Dica publicações Git :

<https://docs.google.com/document/d/1oBEsoLkeBkK7NzIX0-E9S5Tbr_n2oUMIN4twBgmWNRc/edit?usp=sharing_eil&ts=5bd99d17>

9 - Criar uma conta no Git

Erro: Log: Recurso específico selecionado para a atividade ScriptSqlAction não foi encontrado pelo projeto de testes.

Log: Recurso específico selecionado para a atividade ScriptSqlAction não foi encontrado pelo projeto de testes.

Quando ocorrer esse erro verificar o tipo de atividade definida para o script ou update.

7DesenvolvimentoAba destinada a auxiliar os novos participantes no desenvolvimento de software do TOP.

Está aba tem como finalidade auxiliar com dicas, instruções de como solucionar erros rotineiros e criação de toda e qualquer tipo de nova implementação (anexo, processo e etc...).

Criar um novo anexo na visão de contratos

Irá criar informações no RM.Prj.Contrato.Data, RM.Prj.Contrato.Form, RM.Prj.Contrato.Intf

continuar depois a criação.....
