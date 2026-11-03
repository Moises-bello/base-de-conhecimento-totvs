---
content_hash: b0e2a838525770ab50399727b0e32980cbe6b6c750efda3d0e7de037ef31f938
fetched_at: '2026-06-29T00:05:55.181918+00:00'
page_id: '126192093'
product: rm
source: tdn-rm
title: Parâmetros dos Arquivos de Configuração (*.config)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=126192093
version: 47
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**12.1.33 |
| **Processo** | **:** | Parâmetros para Config |
| **Subprocesso** | **:** | Configuração arquivos \*.Config |
| **Data da publicação** | **:** | 04/08/2021 |

 Os arquivos config's do Host e executáveis contém uma série de configurações importantes para o funcionamento do sistema. Assim sendo, abaixo uma lista das principais opções, seus valores default's e descrições, de forma a facilitar o entendimento das configurações.

### **ActionsPath**

* **Descrição:**Caminho onde estão as actions utilizadas no sistema. Pode conter mais de um caminho, separado por ponto e vírgula.
* **Tipo:**String
* **Default:***..\\RM.net\\;..\\Corpore.net\\*
* **Exemplo:**

  xml]]>

### **Aliaspath**

* **Descrição:** Tem como objetivo definir um único Alias.dat a ser utilizado por todos os hosts do ambiente, para isso devemos adicioná-la nos arquivos RM.AliasManager.exe.config e RM.Host.exe.config ou RM.host.Service.exe.config.
* **Tipo:**String
* **Default:** Vazio
* **Exemplo:**

  xml]]>

### **AllowAssemblySignCheck**

* **Descrição:** Permite que os assemblies carregados pelo host tenham sua assinatura validada. Caso exista algum assembly que esteja com sua assinatura inválida, o host automaticamente o bloqueará e bloqueará todas as outras chamadas consequentes.
* **Tipo:** Booleano
* **Default:*False***
* **Exemplo:**

  xml]]>

### AllowOnlyBookedManagementObjects

* **Descrição:** Restringe a importação de Objetos Gerenciais onde somente objetos do Book de Objetos Gerenciais da TOTVS poderão ser importados através do TOTVS Compartilhamento.
* **Tipo:**bool
* **Default:** false
* **Versão:**12.1.34
* **Exemplo:**

  xml]]>

### **ApiPort**

* **Descrição:** Porta utilizada para expor [serviços de API](https://tdn.totvs.com/x/yYooI) do RM.
* **Tipo:** Numeric
* **Default:** vazia (Se não preenchida utiliza o valor preenchido na tag **HttpPort**)
* **Exemplo:**

  xml]]>

### **CertificateStoreLocation**

* **Descrição:** Nome do lugar onde a Store do certificado de segurança do WCF está localizado. Habilitada somente no host.
* **Tipo:**Valores pré-determinados
* **Possíveis Valores:** 
  + *CurrentUser*
  + *LocalMachine*
* **Default:** *LocalMachine*
* ****Exemplo:****

  xml]]>

### **CertificateStoreName**

**Descrição:** Nome do Store onde o certificado de segurança do WCF está armazenado. Habilitada somente no host.

* **Tipo:**Valores pré-determinados
* **Possíveis valores:**
  + *AddressBook*
  + *AuthRoot*
  + *CertificateAuthority*
  + *Disallowed*
  + *My*
  + *Root*
  + *TrustedPeople*
  + *TrustedPublisher*
* **Default:** *My*
* ****Exemplo:****

  xml]]>

### **CertificateFindType**

* **Descrição:** Campo pelo qual o certificado de segurança será procurado no Certificate Store. Este valor ajuda a encontrar o certificado correto com que a comunicação do sistema será protegida. Habilitada somente no host.
* **Tipo:**Valores pré-determinados
* **Possíveis valores:**
  + *FindByThumbprint*
  + *FindBySubjectName*
  + *FindBySubjectDistinguishedName*
  + *FindByIssuerName*
  + *FindByIssuerDistinguishedName*
  + *FindBySerialNumber*
  + *FindByTimeValid*
  + *FindByTimeNotYetValid*
  + *FindByTimeExpired*
  + *FindByTemplateName*
  + *FindByApplicationPolicy*
  + *FindByCertificatePolicy*
  + *FindByExtension*
  + *FindByKeyUsage*
  + *FindBySubjectKeyIdentifier*
* **Default:** *FindBySubjectName*
* ****Exemplo:****

  xml]]>

### **CertificateFindValue**

* **Descrição:** Valor pelo qual o certificado de segurança será procurado no Certificate Store. Habilitada no host e deve conter o nome do certificado no client. Este valor ajuda a encontrar o certificado correto com que a comunicação do sistema será protegida. Trabalha em conjunto com a chave *CertificateFindType*. Para que seja levada em conta, a comunicação deve estar ocorrendo em WCF e a chave *SecurityEnabled* habilitada.
* **Tipo:**String
* **Default:** *TOTVS*
* **Exemplo:**

  xml]]>

### **ConfigAutoGenerate**

* **Descrição:** Habilita a criação automática de arquivos de configuração quando utilizada a funcionalidade de Gerenciamento de Config.
* **Tipo:**Boolean
* **Default:***True*
* **Exemplo:** 

  xml ]]>

### **ConfigPath**

* **Descrição:** Tem como objetivo definir um único arquivo de configuração a ser utilizado por todos os aplicativos do ambiente.
* **Tipo:**String
* **Default:** Vazio
* **Observações:**Para mais informações acesse o link: [Gerenciador de Config](http://tdn.totvs.com/x/XgRFCg).
* **Exemplo:**

  xml]]>

### **DbSchemaCacheMaxSize**

* **Descrição:** Define a quantidade de Schemas que serão guardados em cache.
* **Tipo:** Numeric
* **Default:***100*
* **Exemplo:**

  xml]]>

### **DBSCommandTimeout**

* **Descrição:** Define o tempo máximo que uma Consulta SQL pode levar antes de retornar erro de timeout, em segundos.
* **Tipo:** Numeric
* **Default:***120*
* **Exemplo:**

  xml]]>

### ***DBSConnStrExtensions***

* **Descrição:**Acrescenta extensões à string de conexão atualmente em uso.
* **Tipo:** String
* **Default:** Vazio
* **Observações:** Para alterar o timeout de comandos nativos do SQL, tal qual *Rollback*, esta tag deve ser utilizada, ao invés da tag ***DBSCommandTimeout***
* **Exemplo:**

  xml]]>

### **DefaultDB**

* **Descrição:**Banco de dados default para qualquer operação que possa vir a ser realizada antes do momento do login, quando o banco de dados definitivo é definido. Essencial para o uso de APIs
* **Tipo:** String
* **Default:** *CorporeRM*
* **Exemplo:**

  xml]]>

### **DisableCompression**

* **Descrição:** Desabilita compressão de dados em WCF
* **Tipo:** Boolean
* **Default:** false
* **Camada:** 

  | Versão | Camada |
  | --- | --- |
  | Até 12.1.33 | Client e Server |
  | 12.1.34 e Superiores | Server |
* **Exemplo:**

  xml]]>

### **EnableSecurity**

* **Descrição:** Determina se a comunicação WCF utilizará a segurança da camada de transporte garantida por certificados e se permitirá que credenciais sejam enviadas aos serviços. Ao determinar esta tag como *true*, suas respectivas tags de parametrização também precisam ser configuradas, são elas: ***CertificateFindValue, CertificateFindType, CertificateStoreName, CertificateStoreLocation***, que basicamente definem onde e como encontrar o certificado adequado.
* **Tipo:** Boolean
* **Default:** False
* **Observações:** *para mais informações, acessar:*
* **Camada:** 

  | Versão | Camada |
  | --- | --- |
  | Até 12.1.33 | Client e Server |
  | 12.1.34 e Superiores | Server |
* **Exemplo:**

  xml]]>

### **Host**

* **Descrição:** Nome da máquina em que o host está sendo executado (não recomendável pois acrescenta o overhead de ir ao DNS). O ideal é informar o IP diretamente.
* **Tipo:** String
* **Default:** *localhost*
* **Exemplos:**

  xmlUtilizando nome da máquina]]>xmlUtilizando IP]]>

### **Http\_BaseUrl**

* **Descrição:** Tem a finalidade de informar ao Client qual é o endereço HTTP que deve ser utilizado para acessar os recursos disponibilizados pelo Host. Essa configuração permite que o Client identifique corretamente a URL do serviço HTTP, independentemente da infraestrutura onde a aplicação está hospedada.
* **Quando não é necessária**:

A configuração da tag **HTTP\_BASEURL** normalmente **não** é necessária quando:

* + A comunicação entre Client e Server ocorre diretamente;
  + Não existem camadas intermediárias que alterem a URL de acesso ao serviço;
  + O endereço utilizado pelo consumidor é o mesmo endereço conhecido pela aplicação.

Nesses cenários, a própria biblioteca consegue identificar automaticamente o endereço HTTP correto do serviço.

* **Quando é necessária:**

A configuração da tag **HTTP\_BASEURL** é recomendada ou obrigatória quando:

* + A aplicação está hospedada em ambientes de nuvem;
  + Existem Load Balancers, Reverse Proxies, API Gateways ou Application Gateways;
  + São utilizadas regras de URL Rewrite ou redirecionamentos;
  + O endereço público utilizado pelos consumidores é diferente do endereço interno da aplicação;
* **Tipo:** String
* **Default:** *Vazio*
* **Exemplo:**

  xml]]>

Alterações após a migração para WCF Core (12.1.2606 ou superior):

Após a migração dos serviços para **WCF Core**, os endpoints HTTP passaram a exigir obrigatoriamente o sufixo: `\wwwroot`

Dessa forma, sempre que a tag **Http\_BaseUrl** for utilizada, ela deverá apontar para a URL pública do serviço incluindo esse sufixo.

**Exemplo**

URL publicada:

```
https://empresa.exemplo.com/rm
```

Configuração:

<add key="Http\_BaseUrl" value="`https://empresa.exemplo.com/rm/wwwroot`" />

### **HttpPort**

* **Descrição:** Porta utilizada pela comunicação WCF quando o protocolo de comunicação for HTTP. Tanto o Server quanto o Client devem estar configurados sempre na mesma porta, para que possam se comunicar corretamente.
* **Tipo:** Numeric
* **Default:** *8051*
* **Exemplo:**

  xml]]>

### **JobServer3Camadas**

* **Descrição:** Informa se a aplicação está trabalhando em três camadas. Deve ter o mesmo valor tanto nos config's dos Clients quanto do Host.
* **Tipo:** Boolean
* **Default:** *true*
* **Exemplo:**

  xml]]>

### JWTRefreshTokenExpireMinutes

* **Descrição:** Define a duração do *refresh* token, em minutos. Pode ser configurada entre 1 e 129600 minutos.
* **Tipo:** *Numeric*
* **Default:** 960
* **Exemplo:**

  xml]]>

### JWTTokenExpireMinutes

* **Descrição:** Define a duração do *access* token, em minutos. Pode ser configurada entre 1 e 43200 minutos.
* **Tipo:** *Numeric*
* **Default:** 5
* **Exemplo:**

  xml]]>

### **LdapProvider**

* **Descrição:** Possível provider que irá responder por operações relacionadas a autenticação caso exista a integração LDAP.
* **Tipo:** String
* **Default:** *Vazio*

### **LibPath**

* **Descrição:** Diretório onde estão as dll's da Lib.
* **Tipo:** String
* **Default:***..\\RM.net\\*
* **Exemplo:**

  xml]]>

### **LogPath**

* **Descrição:** Caminho do diretório de log.
* **Tipo:** String
* **Default:***Vazio*
* **Exemplo:**

  xml]]>

### **NotificationsPerLicenceServerCicle**

* **Descrição:** Inteiro maior que 0 - Número de notificações que o ERP fará no License Server a cada ciclo do mesmo. O License Server exige que a cada intervalo de três minutos, pelo menos uma notificação seja feita pelo cliente. Contudo, por problemas de rede, algumas notificações podem se perder ou atrasar. Devido a isto mais notificações podem ser configuradas. Quanto pior a rede, maior deve ser o número de notificações. Se algum valor inválido for informado, o default três é utilizado. Definido nos config's dos clientes.
* **Tipo:** *Numeric*
* **Default: *3***
* **Exemplo:**

  xml]]>

### **PerformanceLogEnabled**

* **Descrição:** Tag utilizada para mostrar o tempo gasto para abrir/editar/gravar dados. Indicado ser utilizada quando o cliente reclamar de performance, coletando os dados para análise. Exemplo: Com a TAG ativada nos arquivos config's ( RM.exe.config, RMLabore.exe.config e etc) o sistema exibirá uma tela mostrando o tempo gasto em operações gerais como abertura de uma tela de visão
* **Tipo:** *Boolean*
* **Default:** *False*
* **Exemplo:**

  xml]]>

### **Port**

* **Descrição:** Informa em que porta Host e Client se comunicarão. Tanto o Server quanto o Client devem estar configurados sempre na mesma porta, para que possam se comunicar corretamente.
* **Tipo:** *Numeric*
* **Default:** *8050*
* **Exemplo:**

  xml]]>

### **SelfHosted**

* **Descrição:** Informa se a aplicação starta o Host automaticamente caso ele não esteja iniciado. Se o serviço RM.Host.Service.exe estiver habilitado, inicia-o. Caso o serviço não esteja ou não exista, inicia o Host desktop. Este parâmetro é configurado nos clientes, não sendo levado em consideração quando configurado no server.
* **Tipo:** *Boolean*
* **Default:***False*
* **Exemplo:**

  xml]]>

### **ServiceAlias**

* **Descrição:** Define o alias que responderá pelos serviços executados sem autenticação
* **Tipo:** *Boolean*
* **Default:***False*

### **ServicesBaseUrl**

* **Descrição:** Define o endereço base dos serviços HTTP(SOAP) que serão expostos pelo Host.
* **Tipo:** String
* **Default:**host:porta
* **Exemplo:**

  xml]]>

### **SubdomainMask**

* **Descrição:** Tag responsável por realizar a **[tenantização dos serviços do RM.](https://tdn.totvs.com/x/XYu9Mg)**
* **Tipo:** String
* **Default:** vazia
* **Exemplo:**

  xml]]>Onde **[ALIAS]** é tratado como uma variável onde será sobrescrito com o nome de um Alias do banco de dados cadastrado ao inicializar os serviços do sistema, para mais informações sobre tenantização acesse o TDN <https://tdn.totvs.com/x/XYu9Mg>.Atenção

  É imprescindível que a variável **[ALIAS]** esteja presente no valor da tag, pois é este valor que será sobrescrito pelo nome do Alias de banco de dados.

### **TcpPort**

* **Descrição:** Porta utilizada pela comunicação WCF quando o protocolo de comunicação for TCP. Tanto o Server quanto o Client devem estar configurados sempre na mesma porta, para que possam se comunicar corretamente.
* **Tipo:**Numeric
* **Default:** 8050
* **Exemplo:**

  xml]]>

### **TraceConsole**

* **Descrição:** Loga em arquivo as informações que forem inseridas pela aplicação no console.
* **Tipo:**Boolean
* **Default:** false
* **Exemplo:**

  xml]]>

### **TraceFile**

* **Descrição:** Indica se irá salvar algum log de execução do host dentro pasta *\Processos\Logs\*.
* **Tipo:**Boolean
* **Default:** false
* **Exemplo:**

  xml
  ]]>

### **TraceFluigIdentity**

* **Descrição:** Habilita a criação do log de comunicação entre o as integrações "**RM x Identity**", "**RM x Fluig**" e integrações ***SAML***, o log será gravado dentro pasta *\Processos\Logs\*.
* **Tipo:**Boolean
* **Default:** false
* **Exemplo:** 

  xml]]>

### UpdateServerEnabled - <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003565411-Framework-Linha-RM-Frame-Habilitar-TOTVS-Update>

* **Descrição:** Indica que um determinado Host (RM.Host.exe.config) será utilizado como base/servidor para que máquinas Client possam baixar as atualizações (**SmartClient**), mas para isso essas máquinas Client precisam da tag habilitada.
* **Tipo:**Boolean
* **Default:** *false*
* **Observações:** Após inserir as *tags* no servidor de atualização, é necessário reiniciar o serviço RM.Host.Service.
* **Exemplo:**

  xml]]>

### UpdateServerUpdateServer - <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003565411-Framework-Linha-RM-Frame-Habilitar-TOTVS-Update>

* **Descrição:** Indica que um determinada máquina Client (**SmartClient**) pode se comunicar com o Server para baixar atualizações.
* **Tipo:**String
* **Default:** host:porta
* **Exemplo:**

  xml]]>

### **UseDbSchemaCache**

* **Descrição:** Indica se o sistema guardará em cache os esquemas obtidos pelas consultas.
* **Tipo:**Boolean
* **Default:** *false*
* **Observações:**Pode ser utilizado na Configuração N camadas, conforme informações em
* **Exemplo:**

  xml]]>

### **UseRMUser**

* **Descrição:** Determina o uso de um usuário do RM para fazer login no **RM.Atualizador** e **RM.TotvsAudit**, quando adicionado no respectivo arquivo config.
* **Tipo:** Boolean
* **Default:***false*
* **Exemplo:**

  xml]]>

### **UseSecurityExtCache**

* **Descrição:** Indica se o sistema guardará em cache as informações de segurança estendida obtidas a cada verificação.
* **Tipo:**Boolean
* **Default:** *false*
* **Observações:**para mais informações:
* **Exemplo:**xml]]>

### **WcfProtocol**

* **Descrição:** Protocolo utilizado pela comunicação entre Host e Client  (NamedPipe / HTTP / TCP / Todos).

Os valores aceitos são HTTP, TCP, NamedPipe e Todos. Este parâmetro deve ter o mesmo valor tanto no Server quanto no Client. Somente o host pode ser configurado para "Todos". Neste caso, ele publicará os Servers tanto em HTTP quanto em TCP, e os clientes poderão se comunicar com ele em qualquer dos protocolos.

A opção NamedPipe é a mais rápida das três. Contudo, esta comunicação só pode ser configurada quando host e client estiverem na mesma máquina. Para fazer esta verificação, a chave JobServer3Camadas é conferida. Caso esteja setada para true, utiliza o padrão TCP mesmo que esteja configurado para NamedPipes.

* **Tipo:** Valores específicos
* **Default:***TCP em 3 camadas, NamedPipes em 1 camada*.
* **Exemplo:**

  xml]]>
