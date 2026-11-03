---
content_hash: 4735b0ba0a97a24ee65587cc8a66bfc31146bf8c9bfeb49aabaaffb6b5e8d272
fetched_at: '2026-06-28T21:35:28.181803+00:00'
page_id: '621778238'
product: fluig
source: tdn-fluig
title: CORS (Cross-origin Resource Sharing)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=621778238
version: 23
---

4.\*ndice

# Objetivo

---

O objetivo deste guia é apresentar os procedimentos necessários para a configuração de CORS (Compartilhamento de Recursos de Origem Cruzada).

# Considerações iniciais

---

O CORS (Cross-origin Resource Sharing) é um mecanismo utilizado pelos navegadores para compartilhar recursos entre diferentes origens. O CORS é uma especificação do [W3C](https://fetch.spec.whatwg.org/) e faz uso de headers do HTTP para informar aos navegadores se determinado recurso pode ser ou não acessado.

# CORS no TOTVS Fluig Plataforma

---

O TOTVS Fluig Plataforma já contém as configurações necessárias para tratar o CORS. Porém, por padrão aceita conexões de qualquer origem.

## Bloqueando conexão de qualquer origem

---

Para impedir o acesso ao TOTVS Fluig Plataforma de qualquer origem que não seja o próprio produto, faça a seguinte configuração:

0.5falsesamplesfadetrue1Passo 1

* **A partir da atualização 2.0:**Abra o arquivo **standalone.xml** que está disponível em **[diretório\_instalação]/appserver/standalone/configuration** em um editor de texto.

* **Para atualizações 1.6 até 1.8.2**:  
  Abra o arquivo **domain.xml** que está disponível em **[diretório\_instalação]/appserver/domain/configuration** em um editor de texto.

true2Passo 2

* No arquivo correspondente à atualização do Fluig que você utiliza (**standalone.xml** ou **domain.xml**), procure pela seguinte linha:<response-header header-name="Access-Control-Allow-Origin" header-value="\*" name="Access-Control-Allow-Origin"/>

xml]]>3Passo 3

* Substitua o "\*" pela URL de acesso ao TOTVS Fluig Plataforma. Por exemplo, se a URL de acesso ao Fluig for "<https://www.minhaempresa.com.br>", ficaria assim:

xml]]>4Passo 4

* Reinicie os serviços da plataforma.

## Permitindo a conexão de uma única origem

---

Para permitir o acesso ao TOTVS Fluig Plataforma de uma origem confiável que não seja o próprio produto, faça a seguinte configuração:

0.5falsesamplesfadetrue1Passo 1

* **A partir da atualização 2.0:**Abra o arquivo **standalone.xml** que está disponível em **[diretório\_instalação]/appserver/standalone/configuration** em um editor de texto.

* **Para atualizações 1.6 até 1.8.2**:  
  Abra o arquivo **domain.xml** que está disponível em **[diretório\_instalação]/appserver/domain/configuration** em um editor de texto.

true2Passo 2

* No arquivo correspondente à atualização do Fluig que você utiliza (**standalone.xml** ou **domain.xml**), procure pela seguinte linha:

xml]]>3Passo 3

* Substitua o "\*" pela URL origem que terá permissão de acessar o TOTVS Fluig Plataforma. Por exemplo, se a URL de acesso ao fluig for "<https://www.minhaempresa.com.br>" e deseja-se liberar acesso a um site cuja URL de acesso seja "[https://www.outrosite.com.br](https://www.minhaempresa.com.br)", ficaria assim:

xml]]>4Passo 4

* Reinicie os serviços da plataforma

## Permitindo a conexão de múltiplas origens

---

O TOTVS Fluig Plataforma não possui uma forma interna de permitir a conexão de múltiplas origens diferentes.

Mas há uma solução: usar ferramentas de terceiros (como NGINX ou Apache), construindo uma rede DMZ. Inclusive a maneira mais segura de utilizar o TOTVS Fluig Plataforma é não expô-lo diretamente na internet, mas sim através de uma DMZ (Veja mais informações ).

Atenção!

Nesse caso, é necessário também **REMOVER** as seguintes linhas do arquivo **standalone.xml** (**a partir da 2.0**) ou **domain.xml** (**1.6 até 1.8.2**):

xml







]]>

### Utilizando NGINX para configurar CORS

---

Importante!

Somente é possível utilizar o NGINX **até a versão** **1.22** por conta da compatibilidade com o módulo nginx-stick-module-ng.

A seguir um exemplo de configuração para o NGINX que pode ser usado como base para configurá-lo para fazer a validação de CORS:

textfluig.confImportante!

Recomendamos o uso de chaves e protocolos mais modernos e seguros como os indicados no exemplo.

Porém, outras chaves também são suportadas:

DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA

Preencha a diretiva **ssl\_ciphers** do fluig.conf substituindo pelos valores suportados acima que estejam de acordo com sua política de segurança. As chaves podem ser validadas em <https://ciphersuite.info/>.

E também os protocolos: TLSv1, TLSv1.1 e TLSv1.2

Preencha a diretiva **ssl\_protocols** do fluig.conf substituindo pelos valores suportados acima que estejam de acordo com sua política de segurança.

### Utilizando Apache para configurar CORS

---

A seguir um exemplo de configuração para o Apache que pode ser usado como base para configurá-lo para fazer a validação de CORS. Essa configuração é um aprimoramento da configuração descrita em  - Configuração do Apache (SSL) + Fluig (HTTP)

textfluig.conf
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule (.\*) https://%{HTTP\_HOST}%{REQUEST\_URI}
ServerName minhaempresa.com
RequestHeader set X-Forwarded-Host 192.168.2.100:443
RequestHeader set X-Forwarded-Proto https
SSLProxyEngine On
SSLEngine On
SSLCertificateFile "conf/cert1.pem"
SSLCertificateKeyFile "conf/privkey1.pem"
SSLCertificateChainFile "conf/fullchain1.pem"
ProxyPreserveHost On
ProxyPass / http://192.168.2.100:8080/
ProxyPassReverse / https://minhaempresa.com/

ServerName minhaempresa.com
ProxyPreserveHost On
ProxyPass / ftp://192.168.2.100/
ProxyPassReverse / ftp://192.168.2.100:21/
]]>
