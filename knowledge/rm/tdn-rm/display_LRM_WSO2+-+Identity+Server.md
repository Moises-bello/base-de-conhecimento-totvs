---
content_hash: b2e9c5aeb42cc747ebfb4b863376f64007510132eb7a965ad399502efedf23cc
fetched_at: '2026-06-29T00:09:09.178662+00:00'
page_id: '392503461'
product: rm
source: tdn-rm
title: WSO2 - Identity Server
type: documentation
url: https://tdn.totvs.com/display/LRM/WSO2+-+Identity+Server
version: 7
---

# Instalação do Servidor de Identidade do WSO2

|  |  |
| --- | --- |
| **Produto:** | WSO2-ID |
| **Versões:** | Todas |
| **Ocorrência:** | Instalação e configuração do WSO2-ID |
| **Ambiente:** | Windows 2010  Java SE Development Kit (JDK) 8  WSO2 Identity Server 5.6.0 |
| **Passo a passo:** | Passo 1:  Fazer o dowload (<http://www.oracle.com/technetwork/pt/java/javase/downloads/jdk8-downloads-2133151.html>) e a instalação do JDK8.      Passo 2:  Adicione a variável de sistema JAVA\_HOME nas variáveis de ambiente.      Passo 3:  Edite a variável de sistema PATH nas variáveis de ambiente, adicionando o caminho C:\Program Files (x86)\Common Files\Oracle\Java\javapath      Passo 4:  Fazer o dowload (<https://wso2.com/identity-and-access-management/install>) e a instalação do WSO2-IS 5.6.0.      Passo 5:  Adicione a variável de sistema CARBON\_HOME nas variáveis de ambiente.      Passo 6:  Inicie o WSO2-IS pela batch C:\Program Files\WSO2\Identity Server\5.6.0\bin>wso2server.bat --run    Após o start da aplicação será demonstrada uma instrução com a URL do Management Console conforme abaixo  [2018-08-20 14:24:25,853]  INFO {org.wso2.carbon.ui.internal.CarbonUIServiceComponent} -  Mgt Console URL  : <https://localhost:9443/carbon/>  \*Aviso\*  Caso a aplicação não seja iniciada com sucesso, conferir a instrução "%JAVA\_HOME%\bin\java" %CMD\_LINE\_ARGS% org.wso2.carbon.bootstrap.Bootstrap %CMD% no final do arquivo wso2server.bat e conferir se todos os caminhos relativos contém "".    Passo 7: Ao accessar o link encontrará a página de Login para a configuração do Carbon, utilize o Username admin e Password admin.    O WSO2-IS foi instalado corretamente na sua máquina.   Importante - Sem estas configurações a integração com Portal do Aluno não funcionará   1) Aplicações que acessam o WSO2-IS para login via OpenId, deve conseguir acessar o endereço de descoberta:  **http(s)://<domínio da instalação>/oauth2/oidcdiscovery/.well-known/openid-configuration**  Por padrão o WSO2-IS deixa esse endereço bloqueado. Para liberá-lo siga as instruções abaixo:   1. Edite o arquivo <Pasta de instalação do WSO2-IS}/repository/conf/identity/identity.xml; 2. Localize a marcação: <Resource context="(.\*)/.well-known(.\*)" secured="true" http-method="all"/> 3. Mude o atributo secured para falso: <Resource context="(.\*)/.well-known(.\*)" **secured="false"** http-method="all"/> ou crie uma regra que libere somente o caminho **.well-known/openid-configuration**   Detalhes em: <https://openid.net/specs/openid-connect-discovery-1_0.html>    2) Em muitos casos as aplicações que acessam o WSO2-IS para login via OpenId utilizam um domínio diferente do servidor de identidade. Para isso é necessário liberar o CORS para que as aplicações consigam acessar os endereços de descoberta e de informações do usuário.  Siga os passos em: <https://docs.wso2.com/display/IS560/Invoking+an+Endpoint+from+a+Different+Domain> |
|  |  |
