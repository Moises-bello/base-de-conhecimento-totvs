---
content_hash: d7f2c21aec656d637b4146133b0b695e1ba7c95fce835751663b0078ac5b45cb
fetched_at: '2026-06-28T21:35:31.586548+00:00'
page_id: '941883789'
product: fluig
source: tdn-fluig
title: ARQ - Como configurar HTTPS da atualização 1.6.5 até 1.8.2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=941883789
version: 21
---

Fique atento!

Esta página é válida para as atualizações **1.6.5 até 1.8.2**do TOTVS Fluig.

Se você utiliza outra atualização, acesse:

* **Voyager (2.0) ou superior**: ;
* **1.6.4 ou inferior**: .
Plataforma em Cloud

Clientes cloud precisam entrar em contato com o time de Cloud para que eles realizem esse procedimento.

Dica!

Caso encontre dificuldades para cadastrar o serviço, essa documentação pode lhe ajudar: [Resolução de inconsistência (PKIX *path validation failed*) ao cadastrar serviço](https://centraldeatendimento.fluig.com/hc/pt-br/articles/4404174167575-Fluig-Plataforma-DES-Ao-cadastrar-servi%C3%A7o-retorna-o-erro-PKIX-path-validation-failed).

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é apresentar os passos necessários para utilização do TOTVS Fluig Plataforma com o protocolo HTTPS.

# Pré-requisitos

---

* Possuir um certificado digital válido;
* Ter um host no DNS configurado para a plataforma em um domínio específico.

# Obter um certificado válido

---

Para o certificado ser válido para a internet, este deve ser emitido para um domínio específico (WildCard) ou para um host deste domínio, o que torna obrigatório configurar a plataforma com o mesmo domínio do certificado caso deseje o uso de HTTPS (ex: \*.[suaempresa.com.br](http://suaempresa.com.br)).

Nota:

Se o certificado for vinculado ao TOTVS Fluig e o acesso continuar sendo via IP (e não pelo domínio), constantes mensagens de certificado não confiável serão apresentadas, pois o navegador tentará validar a URL de acesso com o domínio do certificado, retornando erro.

Caso sua empresa ainda não possua nenhum certificado, o mesmo deve ser adquirido de uma autoridade certificadora. Não é recomendado o uso de certificados *self-signed* (auto-assinado), já que alguns navegadores não aceitam este tipo de certificado e podem provocar comportamentos inesperados durante a utilização da plataforma.

Dicas!

* Uma alternativa gratuita é oferecida pela Linux Foundation através do site [Let's Encrypt](https://letsencrypt.org/). Saiba mais acessando a documentação .

* Caso tenha dúvidas sobre os procedimentos realizados no OpenSSL, consulte a documentação .

* Você também pode conferir se sua configuração HTTPS está funcionando corretamente, através da ferramenta: <https://www.sslshopper.com/ssl-checker.html>

# Configuração de HTTPS pelo wcmadmin

---

A partir da atualização **Crystal Lake (1.7.1)**, a configuração de HTTPS pode ser realizada diretamente pelo Painel de controle da plataforma, para isso é necessário seguir os passos abaixo.

Atenção!

A configuração pelo wcmadmin é suficiente para que o HTTPS funcione corretamente em ambientes que possuem apenas **um servidor** para o TOTVS Fluig. Se o seu ambiente possui , é necessário replicar a configuração manualmente em cada um dos demais servidores do TOTVS Fluig seguindo os passos .

falsePassos\_wcmadminPasso 1

* Acessar a plataforma com o usuário **wcmadmin**.
* No menu principal, acionar **Painel de Controle**, logo depois verificar o agrupador **WCM** e acionar **Configurações do sistema.**

Passo 2

* Na aba Portal, marcar a opção **HTTPS** no campo **Protocolo.**

Será apresentada uma mensagem informando que, ao alterar o protocolo para HTTPS, será necessário configurá-lo.

* Acionar **Configurar** para prosseguir com a configuração em tela.

Passo 3

* Selecionar no campo **Plataforma** como será configurado o protocolo HTTPS. As opções são: Apache, Nginx ou TOTVS Fluig Plataforma.

Nota:

A opção Apache ou Nginx é utilizada quando a plataforma é configurada através de um proxy reverso. Sempre recomendamos configurar um ambiente distribuído (com topologia DMZ) para reforçar a segurança de seu ambiente. Para mais detalhes consulte a documentação de .

O Nginx é possível utilizar somente **até a versão** **1.22** por conta da compatibilidade com o módulo nginx-stick-module-ng.

* Configurar o certificado digital de acordo com a opção escolhida:

48%

**TOTVS Fluig Plataforma**

---

Preencha os campos abaixo:

* **Certificado**  
  Selecione o certificado digital que será utilizado para estabelecer a conexão segura da plataforma. Os formatos de arquivos permitidos são: .p12 e .pfx
* **Senha**  
  Informe a senha do certificado digital para estabelecer a conexão segura da plataforma.
* **Caminho da chave**Informe o caminho completo (com extensão), da chave privada do certificado para estabelecer a conexão segura da plataforma.
2%50%

**Apache ou Nginx**

---

Primeiramente, preencha os campos abaixo:

* **Caminho do certificado**  
  Informe o caminho completo (com extensão .crt, .pem ou .p12), do certificado digital gerado para estabelecer a conexão segura da plataforma.
* **Caminho da chave**  
  Informe o caminho completo (com extensão .key ou .pem), da chave privada do certificado para estabelecer a conexão segura da plataforma.

Após isso, acione a opção **Gerar arquivo** para gerar um template com as configurações HTTPS.

Por último, baixe o arquivo gerado e utilize para finalizar a configuração na plataforma selecionada (Nginx ou Apache).

Passo 4

* Acionar **Salvar**.

Serão realizadas algumas verificações, para validar se o certificado está correto, se a senha informada corresponde ao certificado, entre outras. Se estiver tudo certo, a plataforma realiza as alterações necessárias para concluir a configuração. Ao final, será apresentada a mensagem de sucesso. 

Passo 5

* Reiniciar os serviços da plataforma.

Após configurar o HTTPS na instalação da plataforma, é recomendável conferir se está funcionando corretamente. O teste pode ser feito através da ferramenta [SSL Checker](https://www.sslshopper.com/ssl-checker.html).

Com a configuração, será possível acessar também o aplicativo TOTVS Fluig Mobile com HTTPS, sem necessidade de configurações adicionais.

manual

# Configuração de HTTPS manual

---

Caso opte por fazer a configuração manual ou esteja em uma atualização anterior a 1.7.1, os procedimentos de configuração de SSL devem ser realizados conforme os passos abaixo:

Atenção!

Se o seu ambiente possui , além de aplicar a configuração no servidor principal, ela deve ser replicada para todos os demais servidores do TOTVS Fluig também.

oculto

**Observação interna:**

A explicação abaixo foi repassada ao artigo: <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360027390832> (Como configurar a plataforma com o protocolo HTTPS)

Caso tenha alguma alteração, lembrar de repassar a esse artigo!

0.5falsesslfadetrue1Passo 1

* Parar os serviços do Fluig (fluig, fluig\_indexer, fluig\_RealTime e cache, caso estiver utilizando cache externo e.g: MemCached ou redis).

true2Passo 2

1. No arquivo **domain.xml**, localizado em [Instalação Fluig]/appserver/domain/configuration, incluir a tag **<https-listener>** no **subsystem "undertow"**. Não deve ser retirada a tag contendo as configurações HTTP.
2. Na tag HTTP, acrescente o atributo **proxy-address-forwarding="true"** conforme mostrado abaixo:
3. Caso deseje restringir o tráfego de **cookie** **de sessão** em conexões seguras (HTTPS), basta incluir nas configurações do **subsystem undertow** a tag **session-cookie** informando o atributo**secure ="true". (Opcional)**

   Dica!

   A partir da atualização Crystal Lake (1.7.1), é possível habilitar a opção **Flags "HttpOnly" e "Secure" nos cookies** nas [Configurações do sistema](https://tdn.totvs.com/pages/viewpage.action?pageId=235597328#Plataforma%E2%9D%99Configura%C3%A7%C3%B5esdosistema-Gerenciarconfigura%C3%A7%C3%B5esdosistema), não sendo mais necessário definir essa configuração manualmente.

xmlEclipsedomain.xml
<...>
 
 
<...>

<...>
 
<...>
]]>3Passo 3

alias

* A partir da atualização 1.7.0 (Lake), a tag **<security-realm>** não existirá mais, porém pode ser incluída conforme desejo do usuário em habilitar o uso do HTTPS. Nesse caso, será preciso procurar a tag **<security-realm>** no arquivo host.xml.

  
Disponibilizamos as instruções de configuração do repositório de certificados no formato **PKCS12** (p12) portanto, siga as instruções abaixo:  

* Incluir a tag **<server-identities></server-identities>** juntamente com **<ssl>** e o **<keystore>** conforme exemplicado no código abaixo;

* No atributo **path**, informe o diretório do repositório de certificados (keystore.p12).
* Em **key-password** e **keystore-password**, substitua a valor "suasenha" pela senha utilizada na criação do repositório de certificados (keystore).

Importante!

Em **<security-realm name="ApplicationRealm"**> também contém as configurações de certificado porém, suas informações não devem ser modificadas, deixando os valores padrões salvos.

xmlEclipsehost.xml





]]>Dica!

O diretório "certs" se refere à pasta onde os certificados são guardados. Recomendamos que esse diretório seja criado dentro do volume, para evitar que, em uma atualização ou migração de tecnologia, a pasta seja afetada.

Dúvidas sobre a utilização do OpenSSL ou sobre os comandos de exportação do PKCS12 (p12), consulte a documentação .

4Passo 4

* Iniciar novamente os serviços do TOTVS Fluig em sua ordem correta (cache, caso estiver utilizando cache externo e.g: MemCached ou redis, fluig\_indexer, fluig\_RealTime e fluig).
* **O acesso será realizado via HTTPS, na porta 8443.**

5Passo 5

* Após configurar o HTTPS na instalação do TOTVS Fluig, é necessário **ajustar o domínio de acesso** com o novo protocolo.
* Para isto, será necessário acessar a plataforma com o usuário **wcmadmin**, e nas configurações do sistema, na aba Portal, alterar o **Protocolo** para **HTTPS**. Caso não esteja utilizando um web server, é necessário também informar a **Porta** de acesso do servidor da plataforma. Para mais informações, consulte a documentação [Gerenciar configurações do sistema](https://tdn.totvs.com/x/EO4KDg#Configura%C3%A7%C3%B5esdosistema-Gerenciarconfigura%C3%A7%C3%B5esdosistema).

Importante!

É recomendável revisar o limite de tempo das requisições lentas, como forma de trazer mais segurança à plataforma. Acesse a documentação de [Prevenção de ataques DDoS Slow Post e Slow Headers](https://tdn.totvs.com/x/BzCPI) e saiba mais.

# Configurações adicionais

---

## Configuração para utilização do Fluig Studio com SSL

 A alteração abaixo é necessária para o correto funcionamento do plugin Fluig Studio no TOTVS Developer Studio ou Eclipse quando o SSL está habilitado.

0.5falsestudiofadetrue1Passo 1

1. No diretório em que o Fluig Studio foi instalado, **editar o** arquivo **eclipse.ini**;
2. Adicione a linha abaixo no final do arquivo.

bashEclipseeclipse.ini2Passo 2

* Para chamadas de **Web Service** é importante configurar o arquivo de configuração **domain.xml** localizado em [Instalação Fluig]/appserver/domain/configuration.
* Procurar o trecho abaixo:

xmlEclipsedomain.xml
true
10.80.73.203
 
...]]>

* Alterar para:

xmlEclipsedomain.xml
true
jbossws.undefined.host
https
443

...]]>Importante!

Alterar a porta da tag "<wsdl-secure-port>443</wsdl-secure-port>" para a porta de acesso utilizada (Portas padrões 443 e 8443).

## Configurar notificações em tempo real

O serviço responsável pelas notificações em tempo real (entrega de dados do servidor para os clientes) também deve ser preparado para funcionar via HTTPS, quando essa configuração for realizada.

Importante!

* Não é permitido utilizar barra invertida ou contra barras "\" para informar os caminhos do certificado e chave privada no arquivo package.json. Caso for utilizada, o serviço de RealTime (Node) não irá subir.
* Caso o certificado possua uma senha na chave informada, é necessário remover a senha. Caso contrário, o Node.js não será iniciado.
* Se o servidor possuir **proxy**, é necessário liberar as portas do serviço de notificações em tempo real para SSL nesse proxy*.*
* Caso seu certificado e chave estiverem no formato de repositório de certificados PKCS12 (p12), consulte a documentação  para obter os comandos de exportação dos mesmos. Para isso, é preciso que o pacote [OpenSSL](https://www.openssl.org/) esteja instalado no servidor.
* Importante mencionar que a linha que contém a porta nas configurações do SSL no arquivo package.json deve ser apagada.

Para isso, altere o arquivo de configuração deste serviço:

* Windows: <FLUIG>\node\fluig.rt\package.json
* Linux: <FLUIG>/node/bin/fluig.rt/package.json

Estrutura de configuração:

jsEclipsepackage.json

Os atributos devem ser configurados conforme abaixo:

|  |  |
| --- | --- |
| **Atributo** | **Descrição** |
| **usessl** | Informar *true,* para caracterizar a utilização de configuração HTTPS. |
| **key** | Informar o caminho do arquivo de chave. |
| **cert** | Informar o caminho do arquivo de certificado. |
| **ca** | Informar o caminho do arquivo de certificado. |
| **passphrase** | Esse parâmetro não é obrigatório. Caso tenha sido usada uma senha para geração do certificado, pode ser necessário adicionar esse parâmetro indicando a senha. |

Após a alteração do package.json, o serviço RealTime (Node.js) deve ser reiniciado.

## Certificado digital mobile

As plataformas de dispositivos móveis (iOS, Android) possuem limitações com relação aos certificados digitais. Por padrão, apenas o certificados homologados por elas são reconhecidos como confiáveis.

Para evitar a aquisição de certificados não homologados, é preciso consultar a documentação técnica de cada plataforma sobre a lista de certificados reconhecidos como confiáveis:

| Plataforma | Como consultar |
| --- | --- |
| iOS | A lista de certificados confiáveis para o iOS está disponível [aqui](http://support.apple.com/kb/HT5012?viewlocale=pt_BR). |
| Android | É necessário verificar no aparelho em: **Configurações > Segurança > Credenciais Confiáveis**  Na Aba **Sistema** existe a lista de certificados confiáveis para aquela versão do Android. Importante! Cada versão do Android pode ter uma lista de certificados confiáveis diferente. |

oculto

A explicação acima foi repassada ao artigo: <https://centraldeatendimento.fluig.com/hc/pt-br/articles/360034474534> (Erro ao informar o servidor no Android)

Caso tenha alguma alteração, lembrar de repassar a esse artigo!

Em caso de dúvidas, procure a unidade certificadora para assegurar que seu certificado é homologado pelas plataformas mencionadas acima.

Importante!

Caso o seu certificado não esteja na lista dos homologados, realize o procedimento descrito no item [Procedimentos de configuração de SSL](http://tdn.totvs.com/pages/viewpage.action?pageId=286516572#Configura%C3%A7%C3%A3oHTTPSnofluigdarelease1.6.0%C3%A0atual(1.6.4-Waterdrop)-Procedimentosdeconfigura%C3%A7%C3%A3odeSSL), mas lembre-se de que o arquivo .p12 que você utilizar deve conter também o certificado intermediário. Para gerar o arquivo .p12 com todos os certificados juntos siga esses passos:

1. Para gerar o Bundle (intermediário + root):  
   cat intermediario.pem root.pem > bundle.pem
2. Para gerar o PEM do [fluig.com](http://fluig.com/):  
   cat fluig.crt fluig.key bundle.pem > fluig.pem
3. Para gerar o PKCS#12 do [fluig.com](http://fluig.com/):  
   openssl pkcs12 -export -out fluig.p12 -inkey fluig.key -in fluig.crt -certfile bundle.pem
Importante!

Para acessar a plataforma com HTTPS através do Fluig Mobile, basta adicionar uma conta com a nova URL do portal no aplicativo. Para mais detalhes sobre o acesso, confira a documentação por sistema ( ou ).

$("b:contains('oculto')").parent().parent().hide();
]]>
