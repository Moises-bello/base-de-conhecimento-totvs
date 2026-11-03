---
content_hash: 05033eff1b637da1dbe200362191e43e126a6f1d07bcd759065279ccf749dc55
fetched_at: '2026-06-28T21:35:18.754310+00:00'
page_id: '185730415'
product: fluig
source: tdn-fluig
title: Configurando Jetty para SSL (https)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185730415
version: 33
---

# Índice

4true.\*ndicenone

# Objetivo

---

Serviços em HTTPS tem como objetivo garantir maior segurança no tráfego de arquivos entre cliente-servidor. Neste documento abordaremos a configuração SSL do servidor de aplicação **jetty,** utilizado na [Replicação de Documentos](http://tdn.totvs.com/pages/viewpage.action?pageId=172297964), que será utilizado juntamente com o Fluig quando o WildFly estiver com o certificado SSL também ativo.

Atenção

Os procedimentos descritos neste guia foram testados e homologados na versão 9.4.8.v20171121 do [Jetty](https://www.eclipse.org/jetty/documentation/)

# Configurar SSL para Jetty

---

Para configurar o SSL no Jetty, é necessário:

* Gerar as chaves e os certificados auto-assinados (caso não possua o certificado).
* Carregar chaves e certificados.
* Configurar *sslContextFactory*.

# Gerando as chaves e os certificados auto-assinados

---

O caminho mais fácil para gerar as chaves e os certificados é usar a ferramenta *keytool*que vem na instalação da JDK.

Nota

Se você já possui as chaves e os certificados vá direto para o passo,**Carregando as chaves e certificados**, afim de verificar como carregá-los para dentro do *keystore* JSSE. Esta seção também se aplica no caso de renovação de certificados onde você deseja substituir um certificado que está expirando.

O exemplo abaixo gera somente chaves e certificados básicos. Você deve acessar a [documentação do Jetty](https://www.eclipse.org/jetty/documentation/) se precisar especificar o seguintes itens:

* O tamanho da chave
* A data de expiração do certificado
* Alterar a segurança dos providers

### Gerando chaves e certificados com keytool do JDK

O comando a seguir gera as chaves e o certificado diretamente no arquivo `keystore` :

xml

* Preencha todos as informações solicitadas e ao final digite **sim** e pressione **Enter** para confirmar.

Estes certificados auto-assinados não são válidos externamente.

# Carregando chaves e certificados

---

Se um certificado CA lhe foi enviado, ou se você gerou o seu próprio certificado sem `keytool` , você precisa carregá-lo em um keystore JSSE.

  

### Carregando Certificados com keytool

Você pode usar o `keytool` para carregar um certificado no formato PEM diretamente em um keystore. O formato PEM é uma codificação de texto de certificados; é produzido pela OpenSSL, e é devolvido por alguns CAs. Um exemplo de arquivo PEM é:

xml

```

```

### Utilizando certificados com extensão .crt

Se você já possui um certificado com a extensão .crt e a senha para acessá-lo utilize o comando abaixo. Este comando a seguir carrega o conteúdo do arquivo .crt para dentro do arquivo keystore JSSE:

xml

Ao executar o comando acima digite uma senha '**não pode ser deixado em branco'**. Esta é a senha de acesso ao arquivo keystore.

### Utilizando certificados com extensão .p12

Se você possui um certificado com a extensão .p12 utilize o comando abaixo. Este comando a seguir carrega o conteúdo do arquivo .crt para dentro do arquivo keystore JSSE:

xml

Ao executar o comando acima lhe será solicitado uma senha '**não pode ser deixado em branco'**. Esta é a senha de acesso ao arquivo keystore.

Será solicito uma segunda senha, esta é a de acesso ao certificado, guarde as duas senha.

É necessário copiar o arquivo *keystore* do local onde foi gerado para dentro da pasta **[instalação do jetty]/etc**

# Configurando SslContextFactory

---

O Jetty permite que seja criado um diretório específico para realizar as configurações, assim é possível manter uma separação entre os arquivos binários de instalação ($JETTY\_HOME) e as configurações personalizadas ($JETTY\_BASE). Veja mais detalhes em [Gerenciando Jetty Home e Jetty Base](https://www.eclipse.org/jetty/documentation/9.4.x/startup-base-and-home.html)

## Configuração em sistemas Linux:

---

0.5falsesamplesfadetrue1Passo 1

Primeiramente crie o diretório base:

bashtrue

Em seguida, será preciso habilitar alguns módulos, execute os comandos:

bashtrue

Com isso, os diretórios etc, start.d e webapps devem ser criados.

2Passo 2

Agora faremos as configurações para o Jetty funcionar em HTTPS, abra o arquivo $JETTY\_BASE/start.d/ssl.ini e edite as seguintes configurações:

**jetty.ssl.host** - Endereço/IP de conexão

**jetty.ssl.port** - porta de conexão

**jetty.sslContext.keyStorePath** - Caminho e nome do arquivo keystore (relativo ao $JETTY\_BASE)

**jetty.sslContext.trustStorePath** - Caminho e nome do arquivo Truststore (relativo ao $JETTY\_BASE)

**jetty.sslContext.keyStorePassword** - Senha de acesso ao keystore

**jetty.sslContext.keyManagerPassword** - Senha de acesso ao keymanager

**jetty.sslContext.trustStorePassword** - Senha de acesso ao truststore

Ofuscar senhas de acesso

Por questões de segurança, recomendamos que as senhas de acesso ao keystore, keymanager e truststore sejam ofuscadas.

O Jetty possuí uma [biblioteca](https://www.eclipse.org/jetty/documentation/9.4.x/configuring-security-secure-passwords.html) que possibilita ofuscar senhas, basta executar os comandos:

bashtrue

# Configuração específica para Jetty no Windows

---

É necessário adicionar o parâmetro abaixo no momento em que o Jetty será iniciado:

*-Dfile.encoding=UTF-8 -[Djavax.net](http://Djavax.net).ssl.trustStore=**[caminho do arquivo keystore gerado]***

Para iniciar o Jetty basta digitar no terminal do Windows o seguinte comando:

*java -Dfile.encoding=UTF-8 -[Djavax.net](http://Djavax.net).ssl.trustStore=**[caminho do arquivo keystore gerado]** -jar start.jar*
