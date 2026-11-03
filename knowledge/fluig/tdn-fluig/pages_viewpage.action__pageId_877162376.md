---
content_hash: 2c92632752b88e62181412a61942b095ade21ce76f0a55499dfe01ffe25cd2e0
fetched_at: '2026-06-28T21:35:31.153512+00:00'
page_id: '877162376'
product: fluig
source: tdn-fluig
title: Configuração de proxy reverso Apache
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=877162376
version: 15
---

Fique atento!

Esta página foi revisada para considerar as configurações de *server* do TOTVS Fluig **a partir** da atualização **1.6**.

4.\*ndice

# Objetivo

---

Este guia orienta a configuração do Apache como *Proxy* Reverso e a implementação de Rate Limit para assegurar a disponibilidade da plataforma contra acessos abusivos.

Dicas!

* Após a configuração do *proxy* reverso, não esqueça de alterar a URL de acesso ao portal nas Configurações do sistema da plataforma. [Clique aqui](http://tdn.totvs.com/x/EO4KDg) e saiba como fazer.

* Obtenha mais informações sobre DMZ em .

* [Clique aqui](https://httpd.apache.org/docs/current/platform/windows.html) para ver a documentação do próprio fornecedor sobre a configuração de *proxy* reverso utilizando **Apache no Windows**.

* Se não for configurado, o padrão de *timeout* do *proxy* reverso do Apache é 60 segundos. A configuração recomendada é 300 segundos – que é o *timeout* padrão do TOTVS Fluig – podendo ser ajustado para mais ou para menos de acordo com a necessidade.
Importante!

Salientamos que, ao utilizar um *proxy* reverso, uma prática de segurança recomendada para a plataforma é não expor o servidor de aplicação diretamente na Internet.

e veja outras boas práticas de segurança recomendadas para o seu ambiente.

# Pré-requisitos

---

* Apache™ versão 2.4. O instalador e a documentação oficial do Apache™ podem ser encontrados em <http://httpd.apache.org/>.

* Se for utilizar SSL, também será necessário converter o certificado utilizado na configuração da plataforma para os formatos **.cer**, **.key** e **.pem**. O guia para configurar a plataforma em SSL (HTTPS) encontra-se [aqui](http://tdn.totvs.com/x/vdMgFQ).

* Para a porta do realtime (7777) no Apache é necessário habilitar o módulo SSL em todos os vhosts que utilizarem o *realtime*   **SSLEngine On**e **SSLProxyEngine On**.

# Módulos Apache

---

Certifique-se de que os seguintes módulos estão sendo carregados pelo Apache:

Nota:

Na versão 2.4 do Apache no Windows, o módulo **LoadModule proxy\_fdpass\_module modules/mod\_proxy\_fdpass.so** não existe.

Se for utilizar SSL no lado DMZ, certifique-se ainda de que o seguinte módulo está sendo carregado pelo Apache:

# Configuração do Apache (sem SSL)

---

**01**. Acesse a pasta **/etc/httpd/conf.d.**

Nota:

O caminho da pasta pode variar, esse caminho do exemplo é de uma instalação Linux CentOS.

****02**. Crie um arquivo de configuração para a plataforma (chamado **fluig.conf**, por exemplo), com o seguinte conteúdo:**

xml"
Header set Access-Control-Allow-Headers: "Content-Type, X-Requested-With, accept-version"
Header set Access-Control-Allow-Methods: "GET, PUT, OPTIONS, DELETE, POST"
Header Set Access-Control-Request-Method: "GET, PUT, OPTIONS, DELETE, POST"
ProxyRequests Off
ProxyVia On
AllowConnect 7777
AllowConnect 21]]>

### Listener HTTP

---

xml
ServerName 
ProxyPreserveHost On
ProxyPass / http://:/
ProxyPassReverse / http:///
]]>

### Listener do RealTime

---

xml
RequestHeader set X-Forwarded-Proto https
RequestHeader set Access-Control-Allow-Origin: "https://"
RequestHeader set X-Forwarded-Host :7777
ServerName 
SSLProxyEngine On
SSLEngine On
ProxyRequests Off
ProxyPreserveHost On
Include /etc/letsencrypt/options-ssl-apache.conf
SSLCertificateFile  /cert.pem
SSLCertificateKeyFile /privkey.pem
# allow for upgrading to websockets
RewriteEngine On
RewriteCond %{HTTP:Upgrade} =websocket [NC]
RewriteRule /(.\*) ws://:7777/$1 [P,L]
RewriteCond %{HTTP:Upgrade} !=websocket [NC]
RewriteRule /(.\*) http://:7777/$1 [P,L]
ProxyPass "/" "http://:7777"
ProxyPassReverse "/" "http://:7777/"
ProxyPass "/" "ws://:7777/"
ProxyPassReverse "/" "ws://:7777/"
]]>

### Listener FTP

---

xml
ServerName 
ProxyPreserveHost On
ProxyPass / ftp:///
ProxyPassReverse / ftp://:21/
]]>Legenda

**<Nome externo do servidor>**: nome que aparecerá na URL do navegador, por exemplo, http://**meuservidor.com.br**.

**<IP do servidor Fluig>**: endereço IP interno do servidor onde o Fluig está rodando, por exemplo, 10.10.2.35.

```

```

# Configuração do Apache (SSL) + Fluig (HTTP)

---

Se não for utilizado HTTPS na plataforma, deve possuir a seguinte configuração:

xml
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule (.\*) https://%{HTTP\_HOST}%{REQUEST\_URI}
ServerName 
RequestHeader set X-Forwarded-Host :443
RequestHeader set X-Forwarded-Proto https
SSLProxyEngine On
SSLEngine On
SSLCertificateFile .crt
SSLCertificateKeyFile .key
SSLCertificateChainFile .pem
ProxyPreserveHost On
ProxyPass / http://:/
ProxyPassReverse / https://

ServerName 
ProxyPreserveHost On
ProxyPass / ftp:///
ProxyPassReverse / ftp://:21/
]]>Legenda

<**Nome externo do servidor**>: nome que aparecerá na URL do navegador, por exemplo, http://**meuservidor.com.br**.

<**diretorio-certificado**>: diretório e nome do arquivo do certificado de domínio enviado pela entidade certificadora, por exemplo: /etc/httpd/ssl/cert-dominio.crt

<**diretorio-chave-privada**>: diretório e nome do arquivo da chave privada, enviada pela entidade certificadora, por exemplo: /etc/httpd/ssl/chave-privada.key

<**diretorio-cadeia-certificados**>: diretório e nome do arquivo que contém a cadeia de certificados, por exemplo: /etc/httpd/ssl/cert-cadeia-certificados.pem

Nota:

O caminho da pasta pode variar, esse caminho do exemplo é de uma instalação Linux CentOS.

**DICA**: O arquivo referente à cadeia de certificados pode ser criado concatenando os certificados de domínio, intermediários e raiz. No Linux, isto pode ser feito com o comando abaixo:

bash cert-cadeia-certificados.pem]]>

**OBS:** Os certificados intermediários e raiz normalmente podem ser encontrados para *download* no *site* da entidade certificadora que você escolheu.

<**IP do servidor fluig**>: endereço IP interno do servidor onde o Fluig está rodando, por exemplo, 10.10.2.35.

## Configuração para acessar a plataforma via *mobile*/OAuth

---

Essa configuração deve ser realizada para garantir que a requisição chega ao conector **HTTP** com o mesmo protocolo a partir do qual a requisição foi originada.

falseVersão1A partir da 2.0

**01**. Edite o arquivo **standalone.xml** localizado no diretório do servidor de aplicação **[diretório\_instalação]/appserver/standalone/configuration/**.

**02**. Localize o seguinte código:

xmlEclipsestandalone.xml


 






]]>

**03**. Na tag **http-listener** inclua o atributo **proxy-address-forwarding** com valor **true**, conforme mostrado abaixo:

]]>21.6 até 1.8.2

**01**. Edite o arquivo **domain.xml** localizado no diretório do servidor de aplicação **[diretório\_instalação]/appserver/domain/configuration/**.

**02**. Localize o seguinte código:

xmlEclipsedomain.xml


 






]]>

**03**. Na tag **http-listener** inclua o atributo **proxy-address-forwarding** com valor **true**, conforme mostrado abaixo:

]]>

# Configuração do Apache (SSL) + Fluig (SSL)

---

**01**. Acesse a pasta **/etc/httpd/conf.d**.

Nota:

O caminho da pasta pode variar, esse caminho do exemplo é de uma instalação Linux CentOS.

**02**. Crie um arquivo de configuração para a plataforma (chamado fluig.conf, por exemplo), com o conteúdo abaixo, caso seja utilizado HTTPS também no lado do Fluig.

Importante!

Lembrando que, se o seu ambiente utiliza , a [configuração de HTTPS](https://tdn.totvs.com/pages/viewpage.action?pageId=354472893#Configura%C3%A7%C3%A3oHTTPSdaplataforma-Configura%C3%A7%C3%A3odeHTTPSmanual) deve ser replicada manualmente para todos os servidores do Fluig.

xml"
Header set Access-Control-Allow-Headers: "Content-Type, X-Requested-With, accept-version"
Header set Access-Control-Allow-Methods: "GET, PUT, OPTIONS, DELETE, POST"
Header Set Access-Control-Request-Method: "GET, PUT, OPTIONS, DELETE, POST"
ServerName 
RequestHeader set X-Forwarded-Host :443
RequestHeader set X-Forwarded-Proto https
SSLProxyEngine On
SSLEngine On
SSLCertificateFile .crt
SSLCertificateKeyFile .key
SSLCertificateChainFile .pem
ProxyPreserveHost On
ProxyPass / https://:/
ProxyPassReverse / https:///

ServerName 
ProxyPreserveHost On
ProxyPass / ftp:///
ProxyPassReverse / ftp://:21/
]]>

# Configurar Rate Limit de requisições

---

### Pré-requisitos

---

É necessário ter o Apache com módulos habilitados:

* mod\_evasive (proteção contra abuso — recomendado)

### Usando mod\_evasive

---

**Instalação**

No Ubuntu/Debian: sudo apt install libapache2-mod-evasive

#f2f2f2#f2f2f2Ative

sudo a2enmod evasive  
sudo systemctl restart apache2

### Configuração básica

---

**Edite**: /etc/apache2/mods-enabled/evasive.conf

Exemplo
DOSHashTableSize 3097
DOSPageCount 5
DOSPageInterval 1
DOSSiteCount 50
DOSSiteInterval 1
DOSBlockingPeriod 10
DOSEmailNotify admin@seusite.com
]]>

## Aplicar ao endpoint específico

---

O mod\_evasive não limita diretamente por URL de forma nativa, mas é possível combinar com **Location**.

Estratégia

#f2f2f2#f2f2f2

VirtualHost + Location ServerName [seu\_dominio.com](http://seu_dominio.com) <location "="" api="" public="" social="" post="" publish"=""> SetEnvIf Request\_URI "^/api/public/social/post/publish$" rate\_limit

O **mod\_evasive** vai reagir automaticamente ao excesso de requisições nesse endpoint.

## Customizando o comportamento de bloqueio

---

O parâmetro `DOSBlockingPeriod` define a duração da restrição aplicada ao endereço IP identificado como abusivo.

* **Configuração:** `DOSBlockingPeriod 30`
* **Funcionamento:** Suspende o acesso do IP por **30 segundos**.

#f2f2f2#f2f2f2Reativação

Se o IP realizar uma nova requisição antes do término desse período, o contador é **reiniciado**, prolongando o bloqueio por mais 30 segundos a partir da última tentativa.

### Ajuste de sensibilidade (configuração restritiva)

---

Estes parâmetros definem o limiar de tolerância para requisições repetitivas ao mesmo recurso.

* **`DOSPageCount 3`**: Define o limite máximo de solicitações permitidas.
* **`DOSPageInterval 1`**: Define a janela de tempo (em segundos) para a contagem acima.
* **Resultado Prático**: O sistema bloqueia o IP se ele exceder **3 requisições por segundo** direcionadas ao mesmo endpoint (página ou objeto específico).

Recomenda-se testar esse limite em ambientes de homologação antes de aplicar em produção.

## Exemplo completo

---

Este exemplo estabelece uma política de limitação de taxa (*rate limiting*) para mitigar comportamentos automatizados abusivos, definindo limites de frequência por recurso individual e por volume global de tráfego originado de um único endereço IP.

css
DOSHashTableSize 3097
DOSPageCount 5
DOSPageInterval 1
DOSSiteCount 50
DOSSiteInterval 1
DOSBlockingPeriod 10
ServerName seu\_dominio.com
Require all granted
]]>

# Ocultar informações no cabeçalho HTTP

---

Para prevenir vulnerabilidades, é importante que as informações não fiquem expostas no cabeçalho HTTP.  e saiba como ocultá-las.
