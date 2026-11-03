---
content_hash: 516430f01ca026fd77ee90708a2a5ca7813760e5014dc6d3087fa8aaf30aaec6
fetched_at: '2026-06-29T00:12:15.405606+00:00'
page_id: '977846109'
product: rm
source: tdn-rm
title: Credential Helper
type: documentation
url: https://tdn.totvs.com/display/LRM/Credential+Helper
version: 7
---

# **Objetivo**

---

Este documento tem o objetivo de auxiliar as equipes no entendimento dos processos, tanto automático quanto manual, de funcionamento do Credencial Helper e assim servir como documento base.

# **Introdução**

---

O Credential Helper é um serviço disponível na plataforma TOTVS Apps para uso pelos ERPs e outras aplicações TOTVS que necessitem obter credenciais (Client ID e Client Secret) para habilitar a comunicação com a solução SmartLink.

Antes dessa nova implementação do Credential Helper, a obtenção das credenciais eram feitas de forma manual através da integração com SmartLink utilizando o Credential Helper TotvsApp, onde na etapa final de conclusão da configuração eram geradas as credenciais.

[Veja mais sobre Credential Helper](https://tdn.totvs.com/pages/viewpage.action?pageId=890537799).

# **Como as coisas funcionam**

---

Agora com as novas implementações, a obtenção das credenciais no RM é feita de 2 formas:

* **Execução Automática:**

Seguindo um processamento em fluxos que são executados no Servidor através do RM.Host;

* **Execução Manual e Resolução de Conflitos:**

Quando houver algum detalhe que impeça a execução automática, então haverá a necessidade de uma intervenção manual, através do processo de Resolução de Conflitos (Classificação de Ambientes e Configurador do SmartLink (Wizard de Recuperação de Credenciais)), que deve ser feita pelo Supervisor do RM.

## Objetos relacionadosCamposNovos

A tabela **GSmartLinkConfig** recebeu novos campos para que os fluxos de processamento possam ser executados corretamente. São eles: Controle, Origem, LastPoolingTaskExecution, TaskId e EnvironmentId.

Obs Campo Origem

Pode conter 3 valores de configurações diferentes (1, 2 e 3)

1. As credenciais não foram recuperadas pelo servidor do Credential Helper, foi adquirida pelo processo de sincronização das credenciais existentes.
2. As Credenciais foram recuperadas pelo servidor do Credential Helper através do processo automático.
3. As Credenciais foram recuperadas pelo servidor do Credential Helper através do processo manual.
Obs Campo Controle

É usado para o cálculo do CRC, que é feito sempre que alguma atualização na tabela GSmartLinkConfig é feita. Esse cálculo também leva em consideração as alterações no campo GParams.Environment, que também entra na regra do recálculo da tabela GSmartLinkConfig.

Importante ressaltar que qualquer alteração manual feita diretamente nas tabelas relacionadas deve interferir no recalculo do CRC impactando assim na veracidade das informações e nos processos e fluxos.

Os principais campos envolvidos no processamento do Credential Helper são:

* **GSmartLinkConfig.DataBaseId**: Informação referente à base de dados como Servidor e nome da base armazenado de forma segura;
* **GSmartLinkConfig.EnvironmentId**: Identificador único usado para identificar o ambiente que está sendo provisionado no servidor do Credential Helper
* **GSmartLinkConfig.Credenciais**: os dados de Credenciais (ClientId e SecretId) armazenados de forma segura
* **GSmartLinkConfig.TaskId**: Identificador único usado para acompanhar o andamento da criação do ambiente do Credential Helper.
* **GParams.Environment**: Usado para identificar o ambiente (dev, prod, staging) do RM.

## APIs de Integração:

O Credential Helper fornece APIs de comunicação por onde conseguimos realizar as seguintes operações:

* **Sincronizar credenciais existentes**

* + Considerando que já exista credenciais válidas e a comunicação com o SmartLink já esteja funcionando, e que essas credenciais foram obtidas de forma distinta do Credential Helper, é realizada a validação das credenciais existentes buscando elas da GTotvsApp, armazenando na GSmartLinkConfig e sincronizando com o Credential Helper.

* **Obter as credenciais**

* + Considerando que não exista Credenciais válidas na GSmartLinkConfig ou não existam integrações antigas é necessário solicitar novas Credenciais válidas.

* **Acompanhar o andamento da geração de credenciais**

+ Ao realizar a solicitação, o servidor do Credencial Helper inicia uma “tarefa” interna de geração do ambiente e das credenciais solicitadas. Enquanto essa tarefa interna não é finalizada, as novas credenciais não ficam disponíveis, consultas regulares são feitas para acompanhar o andamento dessa tarefa.

Os seguintes status de retorno podem acontecer:

* + - **Processando**: indica que a tarefa ainda está em andamento no Credential Helper;
    - **Falha**: indica que a tarefa não foi concluída por alguma falha grave, interrompendo assim o processo de acompanhamento. Junto com o status de falha é recebido um texto com os detalhes dessa falha.
    - **Completo**: indica que a tarefa foi completada pelo Credential Helper, juntamente com esse status é devolvido as Credenciais geradas (clientId e secretId).

* **Chamar o wizard**

+ Caso, após ser feita a chamada para Obter as credenciais, o Credential Helper identificar a necessidade de uma intervenção do usuário, com isso deve retornar o parametro de “abertura do Credential Wizard” juntamente com o “identificador de ambiente” para abertura do Wizard de “Recuperação de Credenciais” pelo RM.

# **O Credential Helper no RM.Host.**

---

O RM.Rost é responsável por executar o processo automático do Credential Helper para geração e manutenção das Credenciais usadas pelo SmartLink.

## Os Fluxos

* ### Startup inicial da integração;StartupInicial

Inicia o processo preparando a base de dados. Deve validar se existem registros na GSmartLinkConfig e Gparams.Environmen. Nesse ponto devemos garantir que pelo menos o DataBaseId está preenchido.

Requisitos para processamento do fluxo:

* + Base **não** estar convertida para Base Teste
  + A Tabela GSmartLinkConfig estar atualizada com os novos campos;
  + Ter registros na GSmartLinkConfig
  + GParams.Environment ser preenchido
  + O Campo Controle estar preenchido com o cálculo de CRC válido
  + Ter o DataBaseId preenchido e válido
  + Ter Credenciais válidas.

* ### Atualizador de credenciais;AtualizadorCredenciais

É a partir desse ponto onde se toma o rumo correto para o processamento do Credential Helper e a geração das Credenciais.

Requisitos para processamento do fluxo:

* + Cliente tem permissão por parte do License Server (Slot 7012) ou Se tem registros na GSmartLinkConfig ou Ter Credenciais válidas na GTotvsApp ou GSmartLinkConfig ou o Campo Origem estiver com o valor de -1
  + GParams.Environment ser preenchido
  + O Campo Controle estar preenchido com o cálculo de CRC válido
  + Ter o DataBaseId preenchido e válido
  + O Campo EnvironmentId não estar preenchido
  + Se o campo TaskId estiver preenchido: Vai para o fluxo
  + Se tiver Registro na GTotvsApp: Vai para o fluxo
  + Se não tiver Credenciais válidas na GSmartLinkConfig: Vai para o fluxo

* ### Sincronizar credenciais vindo da GTotvsApp;#SincronizarCredenciaisGTotvsApp

Essa etapa é responsável em realizar as validações necessárias para a sincronização dos dados da GTotvsApp com a GSmartLinkConfig, caso ainda não exista credenciais válidas na GSmartLinkConfig.

Requisitos para processamento do fluxo:

* + Verifica se as Credenciais da GTotvsApp são válidas e se tem integrações antigas (Consignado, Antecipa, RH…)
  + Se não tiver Credenciais válidas na GSmartLinkConfig: Vai para o fluxo Sincronizar credenciais existentes

* ### Sincronizar credenciais existentesSincronizarCredenciaisExistentes

Nessa etapa as Credenciais devem ser sincronizadas, via API, com o ambiente do Credential Helper. Isso é feito enviando as credenciais obtidas na GTotvsApp e recebendo o retorno OK ou se houve algum problema. O resultado desse fluxo é a gravação das credenciais vindas do GTotvsApp na GSmartLinkConfig

* ### Gerador de novas credenciais pelo CHGeradorNovasCredenciais

Inicia o processo de integração para obter as novas Credenciais via API de integração do Credential Helper.

Essa integração possui, no seu retorno de OK, 3 status esperados:

* + **Status Processando**: Significa que já existe uma solicitação de geração de ambiente para esse Tenat e que deve-se aguardar o término dessa geração. Esse status vem acompanhado do **TaskId**, que é o código usado para identificar o ambiente e o status da geração desse ambiente no servidor do Credential Helper.  
    Vai para o fluxo
  + **Status Completo**: Onde recebemos as Credenciais, ClientId e ClientSecret de forma separada e não criptografada, e é armazenada no Banco de dados de forma segura.
  + **Abrir Wizard de Credenciais**: Caso houver algum detalhe no servidor do Credential Helper que impeça a criação das novas Credenciais, é retornado o **EnvironmentId** que identifica o ambiente que deu o problema. Quando isso acontecer, é necessário acionar a obtenção das Credenciais de forma **Manual** através do Configurador do SmartLink  (Wizard de Recuperação de Credenciais) pelo RM. Esse processo manual pode ser realizado somente pelo Supervisor do RM quando é feito o Login.

* ### Acompanhar o andamento da geração de credenciaisAcompanharGeracaoCredenciais

Esse fluxo é acionado quando identificado que o campo **GSmartLinkConfig.TaskId** está preenchido, isso significa que o processo de integração para obter as novas Credenciais, ainda está com o status de **Processando**. Quando isso acontece, o fluxo de acompanhamento é acionado.

Responsável em acompanhar o andamento da solicitação de geração do ambiente no servidor do Credential Helper, esse fluxo é executado todos os dias durante 1 hora até que uma das situações abaixo seja identificada:

* + Quando status de **Completo** é retornado: Recebemos as Credenciais, ClientId e ClientSecret de forma separada e não criptografada, que é armazenada na tabela GSmartLinkConfig de forma segura. O campo Origem = 2 indica que as Credenciais foram geradas pelo processo automático;
  + Quando uma **falha** é identificada: Os dados da Tabela GSmartLinkConfig são limpos (com exceção do DataBaseId) e o acompanhamento é encerrado;
  + Quando **Abrir Wizard de Credenciais** é retornado: O EnvironmentId recebido é gravado na GSmartLinkConfig e o a acompanhamento é encerrado, pois deve-se seguir o fluxo **Manual** a partir desse ponto;

Ainda existe a possibilidade de receber o status **Processando**, isso quer dizer que o acompanhamento deve continuar a ser feito pois o ambiente no servidor do Credential Helper ainda não está pronto. Esse processo deve seguir a seguinte frequência de acompanhamento:

* + O intervalo entre as consultas deve ser de 10 segundos por 60 minutos, após esse tempo esse processo é retomado somente após 24 horas.

## Acompanhamento dos Fluxos:

Para acompanhamento dos processos e andamento dos fluxos, são gerados logs ao decorrer das execuções, esses logs nos ajudam a entender o que vai acontecendo durante o processamento.

Os logs são gerados pelo [TrackLog](https://tdn.totvs.com/display/GDPA/TrackLog+-+Log+de+Evento) em 3 níveis:

* **Debug**: Mais usado no processo, registrando todos os passos dos fluxos.
* **Warning**: Usado em alguma validação importante que tenha impacto no andamento dos processos
* **Error**: Usado nos momentos críticos que podem impactar e parar o andamento dos processos.

Os fluxos são identificados nos arquivos de Log da seguinte forma:  
[Modulo]-[Categoria]-[Funcionalidade]-[Mensagem]

**Exemplo**:  
[M:Integracoes]-[C:CredentialHelper]-[F:AutomaticCredentialsGenerator]-[<2410DEV>: Cliente não é permitido pelo LS mais possui credenciais já configuradas.]

As Funcionalidades são equivalentes aos processamentos. Abaixo o de/para identificando cada um.

| **Fluxo** | **Funcionalidade** |
| --- | --- |
| Startup inicial da integração | StartupIntegration |
| Atualizador de credenciais | CredentialsUpdater |
| Sincronizar credenciais vindo da GTotvsApp | SyncCredentialsByGTotvsApp |
| Sincronizar credenciais existentes | SyncExistsCredentials |
| Gerador de novas credenciais pelo CH | AutomaticCredentialsGenerator |
| Acompanhar o andamento da geração de credenciais | FollowProgressCredentialsGenerator |
| Resolução de Conflitos | ConflictResolutionByWizard |
| Acompanha algumas das iterações com a GSmartLinkConfig e o cálculo do CRC | DatabaseRepository |

Exemplo de acompanhamento da funcionalidade StartupIntegration no Log pelo arquivo de logs do RM.

[17:07:53.129]-[RM.Host]-[VRB]-[M:Integracoes]-[C:CredentialHelper]-[F:StartupIntegration]-[<CorporeRM>: BHN050103964:8050 - Iniciando a execução de fato (Execute) do ConSmartLinkStartupNotifyServerExecutor.]

[17:07:53.138]-[RM.Host]-[DBG]-[M:Integracoes]-[C:CredentialHelper]-[F:StartupIntegration]-[<CorporeRM>: Tem registro GSMARTLINKCONFIG.]

[17:07:53.139]-[RM.Host]-[DBG]-[M:Integracoes]-[C:CredentialHelper]-[F:StartupIntegration]-[<CorporeRM>: Tem Environment na GParams.]

[17:07:53.142]-[RM.Host]-[DBG]-[M:Integracoes]-[C:CredentialHelper]-[F:StartupIntegration]-[<CorporeRM>: CRC da GSmartLinkConfig é valido.]

[17:07:53.143]-[RM.Host]-[DBG]-[M:Integracoes]-[C:CredentialHelper]-[F:StartupIntegration]-[<CorporeRM>: Tem DataBaseID na GSMARTLINKCONFIG.]

[17:07:53.144]-[RM.Host]-[DBG]-[M:Integracoes]-[C:CredentialHelper]-[F:StartupIntegration]-[<CorporeRM>: O campo DataBaseId na GSMARTLINKCONFIG é válido.]

[17:07:53.144]-[RM.Host]-[DBG]-[M:Integracoes]-[C:CredentialHelper]-[F:StartupIntegration]-[<CorporeRM>: Não tem Credenciais na GSMARTLINKCONFIG.]

Para melhorar a visualização do [TrackLog](https://tdn.totvs.com/display/GDPA/TrackLog+-+Log+de+Evento), pode ser usado o Seq, uma ferramenta que disponibiliza algumas funcionalidades e facilita no acompanhamento dos Logs.

[Veja mais sobre Seq.](https://tdn.totvs.com/display/NPR/RMS+Tracklog+-+Meu+RH+e+RM)

[Veja mais sobre TrackLog.](https://tdn.totvs.com/display/GDPA/TrackLog+-+Log+de+Evento)

## Troubleshoot

O tracklog é a nossa fonte de informação quando o assunto é identificação das instabilidades que podem acontecer com o processamento do Credential Helper

* Startup inicial da integração não está sendo executado.

O que pode ocasionar:

Tabela GSmartLinkConfig não existe  
 Os [novos campos](https://docs.google.com/document/d/1L-fJ3X_nVv8EaJwCnLoI6wpF6bJMZIbNX9l61NUA848/edit?tab=t.0#bookmark=id.xed441rnd19d) da tabela não existem

* Startup inicial da integração não está preenchendo a tabela GSmartLinkConfig.

O que pode ocasionar:

Tabela GSmartLinkConfig não existe  
 Os [novos campos](https://docs.google.com/document/d/1L-fJ3X_nVv8EaJwCnLoI6wpF6bJMZIbNX9l61NUA848/edit?tab=t.0#bookmark=id.xed441rnd19d) da tabela não existem

* Credenciais não serão geradas em Base de Teste!

O que pode ocasionar:

A base foi convertida para Base de Teste

* Cliente não é permitido no LS e não possui credenciais configuradas.

O que pode ocasionar:

Cliente deve acessar o wizard do Credential Helper que está no Modulo Integração| Menu TOTVS App   | Ativação SmartLink

# **O Credential Helper na Resolução de Conflitos.**

---

Caso o processo do Credential helper que executa de forma automática tenha dificuldades em gerar as Credenciais, o processo Manual é inicializado, que envolve o processo de Resolução de Conflitos (**Classificação de Ambientes** e **Configurador do SmartLink** (Wizard de Recuperação de Credenciais)).

Esses processos manuais são acessados através do Login da MDI. Somente um usuário Supervisor de Globais vai ter acesso à esse processo, que é iniciado somente após serem realizadas validações de consistência.

**Requisitos para que o processo manual seja executado**:

* Os campos novos da tabela GSmartLinkConfig devem existir;
* A Base de Dados  não pode estar convertida para Base Teste;
* O Usuário de acesso ao RM deve ser Supervisor de Globais;

**Motivos que exigem a execução do processo manual:**

* Caso GParams.Enviroment, responsável por definir o ambiente (Produção, Homologação), não esteja preenchido;
* Caso DataBaseId esteja inválido por alguma inconsistência nos processos ou base de dados;
* E/ou GSmartLinkConfig.EnviromnetId tenha sido gerado pelo processo automático;

## Classificação de Ambientes no login

Essa tela é a primeira a ser apresentada, seu objetivo é fazer com que usuário confirme qual o Ambiente que o RM vai operar, Produção ou Homologação. 

Abaixo as inconsistências identificadas que a Classificação de Ambientes deve resolver:

1. Quando a classificação do ambiente não foi definida no RM;
2. Quando for identificado que houve alguma atualização na integração com o Smartlink;
3. Quando o Endereço da Base de Dados utilizada pela integração Smartlink está diferente da utilizada pelo RM;

[Veja mais sobre Classificação de Ambientes.](https://tdn.totvs.com/pages/viewpage.action?pageId=942049690)

[Material de apoio sobre Classificação de Ambientes](https://tdn.totvs.com/pages/viewpage.action?pageId=942063818)

Após a seleção de ambientes ser realizada, o processo de **Resolução de Conflitos** realiza validações para decidir qual caminho seguir no processo:

Caso, na seleção de ambientes, o ambiente for alterado

* Então o campo GParams.Enviroment é atualizado
* Os campos da GSmartLinkConfig são limpos e o DataBaseId é recalculado.

Caso, na seleção de ambientes, o ambiente não foi alterado

* Então o processo deve seguir para o **Configurador do SmartLink**

## Configurador do SmartLink (Wizard de Recuperação de Credenciais)

O Configurador do SmartLink, é quem habilita a integração do ERP com a Plataforma de Aplicações TOTVS, é a ferramenta que torna o processo de configuração mais ágil e seguro, orientando o usuário na obtenção das credenciais e na realização do vínculo do ERP com a plataforma.

[Veja mais sobre Configurador do SmartLink](https://tdn.totvs.com/display/FRAMWC/Configurador+do+SmartLink)

**Requisitos para que o processo seja executado:**

* Se o campo GSmartLinkConfig.EnviromnetId estiver preenchido, o que quer dizer que foi gerado pelo processo automático na tentativa de geração das Credenciais.
* O cliente tem permissão por parte do License Server (Slot 7012).
* Se o cliente não tiver permissão por parte do License Server porém possuir Credenciais (GTotvsApp ou GSmartLinkConfig)

Passando pelas validações dos requisitos citados acima, então o [Configurador do SmartLink (Wizard de recuperação de credenciais)](https://tdn.totvs.com/display/FRAMWC/Configurador+do+SmartLink) é iniciado.

Ao finalizar as etapas de seleção de ambientes e wizard de recuperação de credenciais, as **Credenciais** ou **TaskId** é retornado.

Caso seja retornado as **Credenciais**:

* A Base de dados é preparada com:

+ Limpeza os campos da GSmartLinkConfig;
+ Gravação do campo GSmartLinkConfig.Credenciais;
+ Recálculo do GSmartLinkConfig.DataBaseId;
+ Atualização do campo GSmartLinkConfig.Origem = 3 (vindo do CH Manual);

Caso seja retornado o **TaskId**:

* A Base de dados é preparada com:
  + Limpeza os campos da GSmartLinkConfig;
  + Recalcula o DataBaseId;
  + Gravação do campo **GSmartLinkConfig.TaskId** com o **TaskId** retornado. O TaskId é usado para a execução do processo automático “”, até que as credenciais estejam disponíveis;
