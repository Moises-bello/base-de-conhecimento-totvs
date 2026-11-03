---
content_hash: 2123b8bdfe2355047c0467aa96360a37a3b780163823e88255688d7d9929ba16
fetched_at: '2026-06-29T00:08:15.578983+00:00'
page_id: '244911449'
product: rm
source: tdn-rm
title: Habilitar SSL/TLS no Host
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244911449
version: 32
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      Este documento tem como objetivo auxiliar o usuário na configuração do ambiente RM, para que a comunicação com os serviços HTTP seja protegida com SSL/TLS e a comunicação do RM.exe com o Host através de certificado digital.

# Instalação do Certificado no Servidor:

---

      Um certificado digital pode ser adquirido através de uma autoridade certificadora (AC), são facilmente encontradas na web, mas também é possível gerar certificados digitais auto assinados.

      Existem várias maneiras de se gerar um certificado digital auto assinado. Abaixo alguns links para ajuda e**, ,** um certificado auto assinado que pode ser utilizado para cifrar a comunicação, lembrando que o recomendado é que seja adquirido um através de uma AC.

* [PowerShell](https://technet.microsoft.com/library/hh848633)
* [IIS](https://technet.microsoft.com/pt-br/library/ff710475(v=ws.10).aspx)
* [Open SSL](https://www.openssl.org/source/)

falseImportante:

É recomendável que a AC escolhida para gerar o certificado já esteja no diretório de autoridades confiáveis raiz, do gerenciamento de certificados do computador, pois desta forma não será necessário importar a AC em todas as máquinas clientes.

       Salve o certificado no servidor e instale-o conforme imagens abaixo:

false.

**Processo de Instalação:**

1º Passo:2º Passo:3º Passo:4º Passo: 5º Passo: 6º Passo:

 Abra o gerenciamento de **certificados** **do computador (certlm.msc) como administrador** e dê permissão para o usuário do Host nas chaves privadas do certificado:

7º Passo:Atenção

Este passo serve somente para certificados auto assinados

Abra o gerenciamento de **certificados** **do computador (certlm.msc) como administrador** e verifique se o certificado também foi adicionado na pasta "Autoridades de Certificação Raiz Confiáveis". Se o certificado não se encontrar na pasta, será necessário adicioná-lo da seguinte maneira:

Copiar o certificado do repositório Pessoal:

Colar em Autoridades de Certificação Raiz Confiáveis:

8º Passo:

 Abra o certificado e copie a impressão digital (thumbprint no inglês) e armazene:

Em seguida, gere um GUID através do site <https://www.guidgenerator.com/online-guid-generator.aspx> e também armazene para ser utiliza-lo nos próximos passos.

# Registrando o Certificado na Porta Utilizada Pelos Serviços HTTP: WebService e WebAPI do HOST:

---

falseObservação (1):

Configuração necessária apenas para aqueles que forem habilitar segurança para os serviços HTTP (WebService e WebAPI).

falseObservação (2):

Caso a sua Porta já esteja reservada para outra Url, é necessário desfazer este registro. Use o seguinte comando:

* netsh http delete urlacl url=**<URL>**

Ex.: netsh http delete urlacl url=http://+:**<PORTA>**/

falseObservação (3):

O usuário do IIS e do Host precisa ter acesso ao arquivo de configuração global.

**Passo a Passo:**

* Utilizando o thumbprint copiado e o GUID, registre o certificado nas portas HTTP utilizadas pelo HOST. Por padrão o RM utiliza as portas 8050 para TCP e 8051 para WebService (HttpPort) e WebAPI (ApiPort), mas isso pode ser configurado. Veja mais sobre a configuração de portas .
* **Importante:** caso as portas HttpPort e ApiPort sejam diferentes, é necessário executar os comandos abaixo para ambas as portas.
* Abra o prompt de comando do Windows **como administrador.**
* Segue abaixo os comandos para registrar o certificado nas portas, e os dois exemplos reais.

**Exemplos:**

Modelos para aplicar as alterações

A sintaxe para aplicar as alterações deve seguir o modelo abaixo de acordo com as configurações do seu ambiente.

* netsh http add sslcert ipport=0.0.0.0:**<PORTA>** certhash=**<THUMBPRINT>** appid=<**GUID>**
* netsh http add urlacl url=https://+:**<PORTA>**/ user=**"<DOMINIO>\<USUARIO>"**

Maiores detalhes podem ser obtidos diretamente na documentação da Microsoft disponível no link <https://msdn.microsoft.com/en-us/library/windows/desktop/cc307236(v=vs.85).aspx>

* netsh http add sslcert ipport=0.0.0.0:**8051** certhash=**b4def01ef76a1ff154faef805e6eafce3d411459** appid=**{df85028c-5054-44f8-9d01-5a07ddc0f7c0}**
* netsh http add urlacl url=https://+:**8051**/ user=**"NT AUTHORITY\NETWORKSERVICE"**

Removendo as alterações

Para remover as regras aplicadas utilize os comandos com a sintaxe delete conforme exemplos abaixo.

* netsh http delete urlacl url=https://+:**<PORTA>**/
* netsh http delete sslcert ipport=0.0.0.0:**<PORTA>**

# Configurando o RM:

---

      Para proteger apenas os serviços HTTP, ou seja, os Web Services e serviços REST expostos pelo HOST, basta habilitar o parâmetro abaixo no arquivo de configuração do HOST (RM.Host.Service.exe.config/RM.Host.exe.config)

* <add key="**EnableWSSecurity**" value="true" />

      Os parâmetros abaixo, do arquivo de configuração do HOST (RM.Host.Service.exe.config), devem ser ajustados de acordo com o a instalação do certificado para que o mesmo seja encontrado pelo RM.

* <add key="**EnableSecurity**" value="true" /> [TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-EnableSecurity)

      Para proteger a comunicação entre as camadas Cliente e Servidor é necessário habilitar o parâmetro EnableSecurity nos arquivos de configuração em ambas as camadas **Cliente** (somente até a versão 12.1.33) e **Servidor**. Para mais informações acesse o TDN [EnableSecurity](https://tdn.totvs.com/pages/viewpage.action?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-EnableSecurity).

Atenção

A partir da versão **12.1.34, NÃO** é mais necessário inserir a tag **EnableSecurity**nos arquivos de configuração da camada **cliente** do sistema.

Como por exemplo os arquivos RM.exe.config (**RM.exe**), Web.config(**Portais**), RM.Lib.Gerador.Execute.exe.config e ETC.

**CERTIFICATESTORELOCATION:**

      Local do Store onde está armazenado o certificado.

* Valores possíveis: CurrentUser, LocalMachine
* Valor padrão: LocalMachine

**Exemplo:** <add key="CERTIFICATESTORELOCATION" value="LocalMachine" />

Maiores detalhes podem ser obtidos diretamente na documentação da Microsoft disponível no link:<https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.storelocation?view=netframework-4.7.2>

**CERTIFICATESTORENAME:**

      Store onde está armazenado o certificado.

* Valores possíveis: AddressBook, AuthRoot, CertificateAuthority, Disallowed, My,    Root, TrustedPeople, TrustedPublisher
* Valor padrão: My

**Exemplo:** <add key="CERTIFICATESTORENAME" value="My" />

Maiores detalhes podem ser obtidos diretamente na documentação da Microsoft disponível no link:<https://docs.microsoft.com/en-us/dotnet/api/system.security.cryptography.x509certificates.storename?redirectedfrom=MSDN&view=netframework-4.7.2>

**CERTIFICATEFINDTYPE:**

      Campo do certificado que será utilizado para realizar a pesquisa.

* Valores possíveis: FindByThumbprint, FindBySubjectName, FindBySubjectDistinguishedName, FindByIssuerName, FindByIssuerDistinguishedName, FindBySerialNumber, FindByTimeValid, FindByTimeNotYetValid, FindByTimeExpired, FindByTemplateName, FindByTemplateName, FindByApplicationPolicy, FindByCertificatePolicy, FindByExtension, FindByKeyUsage, FindBySubjectKeyIdentifier
* Valor padrão: FindBySubjectName

**Exemplo:** <add key="CERTIFICATEFINDTYPE" value="FindBySubjectName" />

Maiores detalhes podem ser obtidos diretamente na documentação da Microsoft disponível no link: <https://docs.microsoft.com/pt-br/dotnet/api/system.security.cryptography.x509certificates.x509findtype?view=netframework-4.7.2>

**CERTIFICATEFINDVALUE:**

      Campo do certificado que será utilizado para realizar a pesquisa.

* Valores possíveis: Qualquer texto sem caracteres especiais
* Valor padrão: TOTVS

**Exemplo:** <add key="CERTIFICATEFINDVALUE" value="TOTVS" />

falseObservação:

É necessário informar o nome do certificado do lado client, (RM.exe.Config) na propriedade "CERTIFICATEFINDVALUE"

# Validando as Configurações:

---

Após subir o serviço de Host do RM pode-se verificar se existe uma resposta para o wsdl de algum serviço disponível e assim validamos a toda a configuração realizada.

Como exemplo, acessamos a URL <https://localhost:8051/wsdataserver/MEX?wsdl> e obtemos sucesso na resposta conforme abaixo.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Habilitar SSL/TLS no Host

falsefalse

**Status:** Finalizado

false

**Data:** 16/08/2016

false

**Autores:**

false

**Download** **do arquivo:**
