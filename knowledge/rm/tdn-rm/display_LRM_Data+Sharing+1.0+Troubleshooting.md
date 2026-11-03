---
content_hash: 31b9e1672eb647c4e7aa53c3817b546651b9439e7cbde9642b8b5e40fdb20125
fetched_at: '2026-06-29T00:11:12.337975+00:00'
page_id: '652216464'
product: rm
source: tdn-rm
title: Data Sharing 1.0 Troubleshooting
type: documentation
url: https://tdn.totvs.com/display/LRM/Data+Sharing+1.0+Troubleshooting
version: 23
---

### 2

### Problema

## **01.****Certificado não Confiável - Carol**

Ao tentar acessar o endereço <https://app.carol.ai> pelo navegador, a mensagem de erro é apresentada:

*“This site is not secure” error in a technical language is named as DLG\_FLAGS\_INVALID\_CA or DLG\_FLAGS\_SEC\_CERT\_CN\_INVALID. It occurs when people are trying to open certain websites. ... problems with website's security certificate; missing he trusted root certificate for the Certification Authority (CA) on the site."*

### Possível causa

Geralmente se trata de configurações de Firewall ou da GPO (group policy object) do servidor.

### Solução

Ajuste nas regras de GPO (group policy object) do servidor.

---

### Problema

## **02.****Firewall bloqueando endereços e portas**

Failed to connect to URL port 443: TIMED OUT

### Possível causa

O Firewall pode estar bloqueando a comunicação com algumas URLs que contenha "[google.com](http://google.com)", "totvs.app" e "[carol.ai](http://caroi.ai)", "[googleapis.com](http://googleapis.com)" e pode ocasionar TIMED OUT.

| Lista contendo os endereços usados pela integração RM x TotvsApp |
| --- |
| <https://admin.rac.totvs.app/totvs.rac/connect/token> |
| <https://provisioning.totvs.app/api/carol-definitions/v1/carolcredentials/RM> |
| <https://provisioning.totvs.app/api/carol-definitions/v1/entities/RM> |
| <https://app.carol.ai/> |
| <https://endpoint-registry.totvs.app/api/v1/services> |
| <https://provisioning.totvs.app/api/data-management/v1/apps/by-tenant> |
| <https://totvs.rac.totvs.app> |
|  |

### Solução

O Firewall precisa liberar todos os endereços listados acima inclusive os endereços que contenham: "[googleapi.com](http://google.com)" nas portas 80 e 443, caso contrário pode dar erro de Timed out.

Obs: deve-se utilizar o aplicativo de curl em todas as máquinas de JobServer do ambiente do cliente conforme abaixo. Esse comando deve ser rodado pelo "cmd no módulo admin". E a resposta da execução desse comando deverá retornar um json contendo os dados.

Exemplo:

| curl --location --request GET "<https://endpoint-registry.totvs.app/api/v1/services>" --header "User-Agent: RM" --header "Accept: \*/" |
| --- |

-------------------------------

**Ferramentas de teste de solução de problemas de conexão SSL / TLS (Totvs App precisa de TLS1.2 handshake)**

Existe um troubleshooting da Microsoft abordando diversas formas de se testar a comunicação:

<https://techcommunity.microsoft.com/t5/azure-paas-blog/ssl-tls-connection-issue-troubleshooting-test-tools/ba-p/2240059>

**Utilizando CURL**

curl -v [https://endpoint-registry.dev.totvs.app/api/v1/services](https://endpoint-registry.dev.totvs.app/api/v1/services "https://endpoint-registry.dev.totvs.app/api/v1/services") --tlsv1.0

curl -v <https://admin.rac.totvs.app/totvs.rac/connect/token> --tlsv1.0

curl -v [https://endpoint-registry.dev.totvs.app/api/v1/services](https://endpoint-registry.dev.totvs.app/api/v1/services "https://endpoint-registry.dev.totvs.app/api/v1/services") --ciphers ECDHE-RSA-NULL-SHA --tlsv1.2

Resposta esperada (Sucesso)

## **03.** **Erro ao buscar aplicativos**

No assistente de configuração do TotvsApps no RM.exe, ao buscar os aplicativos disponíveis, poderá ocorrer o seguinte erro: **"Falha ao carregar**"

|  |
| --- |

Ao clicar no botão "", nesse momento, **3 api's** da plataforma TotvsApp's serão executadas para fornecimento de informações, entre elas:

**a) - Api responsável em retornar todos os endereços disponíveis da plataforma TotvsApps.**

| Ambiente | Endereço |
| --- | --- |
| Desenvolvimento | <https://endpoint-registry.dev.totvs.app> |
| Staging | <https://endpoint-registry.staging.totvs.app> |
| Produção | <https://endpoint-registry.totvs.app> |

O retorno dessa api, oferecerá todos os outros endereços de conexão na plataforma Totvsapps.

Algum problema de conectividade poderá ocorrer nessa chamada. Portanto, é importante utilizar o aplicativo "**curl**" para verificar se a chamada está sendo realizada com sucesso.

Nesse caso, basta rodar o comando abaixo em todas as **máquinas de servidor de aplicação (máquinas que respondem a solicitações de tela)** do ambiente de **produção** do cliente conforme exemplo

| curl --location --request GET "<https://endpoint-registry.totvs.app/api/v1/services>" --header "User-Agent: RM" --header "Accept: \*/" |
| --- |

Se o comando curl não estiver disponível na máquina, basta baixá-lo do endereço a seguir: <https://curl.se/windows/>

Deve ser retornado um json no seguinte formato, conforme exemplo:

| [     {         "service": "carol-staging-tables-sync",         "endpoints": [             {                 "version": "2",                 "address": "<https://app.carol.ai/api/v2/staging/tables/{table}/sync>"             },             {                 "version": "3",                 "address": "<https://app.carol.ai/api/v3/staging/tables/{table}/sync>"             }         ]     },  .  . |
| --- |

**b) - Api responsável em retornar *accesstoken* de acesso no Rac**

| Ambiente | Endereço |
| --- | --- |
| Desenvolvimento | [https://admin.rac.dev.totvs.app/totvs.rac/connect/token](https://admin.rac.totvs.app/totvs.rac/connect/token) |
| Staging | [https://admin.rac.staging.totvs.app/totvs.rac/connect/token](https://admin.rac.totvs.app/totvs.rac/connect/token) |
| Produção | <https://admin.rac.totvs.app/totvs.rac/connect/token> |

O retorno dessa api, fornecerá o accessToken de acesso para todas as outras api's da plataforma TotvsApps.

Algum problema de conectividade poderá ocorrer nessa chamada. Portanto, é importante utilizar o aplicativo "**curl**" para verificar se a chamada está sendo realizada com sucesso. Nesse caso, basta rodar o comando abaixo em todas as **máquinas de servidor de aplicação (máquinas que respondem a solicitações de tela)** do ambiente de **produção** do cliente conforme exemplo

| curl --location --request POST "<https://admin.rac.totvs.app/totvs.rac/connect/token>" --header "Content-Type: application/x-www-form-urlencoded" --data-urlencode "grant\_type=client\_credentials" --data-urlencode "client\_id=1111111111111111111" --data-urlencode "client\_secret=222222222222222222222" --data-urlencode "scope=authorization\_api" |
| --- |

Deve ser retornado um json no seguinte formato, conforme exemplo:

| {     "access\_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjJiYjZmYzUyM2ZjNzQwZjI4NmMxOTZmY2ExMzUyNzE2IiwidHlwIjoiSldUIn0.eyJuYmYiOjE2NDc1Mzg0ODAsImV4cCI6MTY0NzUzOTY4MCwiaXNzIjoiaHR0cHM6Ly9hZG1pbi5yYWMudG90dnMuYXBwL3RvdHZzLnJhYyIsImF1ZCI6ImF1dGhvcml6YXRpb25fYXBpIiwiY2xpZW50X2lkIjoiODVhYWFmMjU5YTdhNGM2MWIwNmQwMDg3M2I0OWQ1M2QiLCJodHRwOi8vd3d3LnRuZi5jb20vaWRlbnRpdHkvY2xhaW1zL3Byb2R1Y3ROYW1lIjoiK1NhbGRvIiwiaHR0cDovL3d3dy50bmYuY29tL2lkZW50aXR5L2NsYWltcy9wcm9kdWN0SWQiOiIyMCIsImh0dHA6Ly93d3cudG5mLmNvbS9pZGVudGl0eS9jbGFpbXMvdGVuYW50SWQiOiI1ZGFkMDdjYy1mY2E0LTRmMWQtYmFiYi1iMTA0YzJhMTFjOTYiLCJpYXQiOjE2NDc1Mzg0ODAsInNjb3BlIjpbImF1dGhvcml6YXRpb25fYXBpIl19.wQi5JXsN\_7pMpC-kj7pmS9Pnr-RiV45anwZ2bopy3usKKPJH6Pk9W-sMvuQ3G\_mhIYSear1vQMK3OgTDwTNmLBHTjRu3AN6WW7L2oBn9bebYCpLZHtarK8DQ3JrHBpkwmhtsex62\_ZDFwDS0rFf8j7JBWJJN3uib2U9ttZ1OhEe\_\_PykmSFJ6yTdg51AlS4RSKrSMqzFIpiDKq8\_ZK4E\_rCJFwXNYx1dk7eChEfBy5o-CYDiM-YNLsFi2ingZDap7WnD1jpNgs9YyrxwUqYXGwX9hkE2ieUNHDxlw5Xp2hWTtvFSqdKjEpE4sGUA6K3Mi-tuZuNygbSoyWPcImENbQ",     "expires\_in": 1200,     "token\_type": "Bearer" } |
| --- |

**c) - Api responsável em retornar os aplicativos que o cliente tem acesso**

| Ambiente | Endereço |
| --- | --- |
| Desenvolvimento | [https://provisioning.dev.totvs.app/api/data-management/v1/apps/by-tenant](https://provisioning.totvs.app/api/data-management/v1/apps/by-tenant) |
| Staging | [https://provisioning.staging.totvs.app/api/data-management/v1/apps/by-tenant](https://provisioning.totvs.app/api/data-management/v1/apps/by-tenant) |
| Produção | <https://provisioning.totvs.app/api/data-management/v1/apps/by-tenant> |

O retorno dessa api, fornecerá um json contendo os aplicativos que o cliente tem acesso.

O acessToken recuperado na chamada acima deverá ser enviada nessa chamada de api conforme exemplo abaixo no postMan:

Algum problema de conectividade poderá ocorrer nessa chamada. Portanto, é importante utilizar o aplicativo "**curl**" para verificar se a chamada está sendo realizada com sucesso. Nesse caso, basta rodar o comando abaixo em todas as **máquinas de servidor de aplicação (máquinas que respondem a solicitações de tela)** do ambiente de **produção** do cliente conforme exemplo

| curl --location --request GET "<https://provisioning.totvs.app/api/data-management/v1/apps/by-tenant>" --header "split-metadata: true" --header "Authorization:Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjJiYjZmYzUyM2ZjNzQwZjI4NmMxOTZmY2ExMzUyNzE2IiwidHlwIjoiSldUIn0.eyJuYmYiOjE2NDc1Mzg2MjMsImV4cCI6MTY0NzUzOTgyMywiaXNzIjoiaHR0cHM6Ly9hZG1pbi5yYWMudG90dnMuYXBwL3RvdHZzLnJhYyIsImF1ZCI6ImF1dGhvcml6YXRpb25fYXBpIiwiY2xpZW50X2lkIjoiODVhYWFmMjU5YTdhNGM2MWIwNmQwMDg3M2I0OWQ1M2QiLCJodHRwOi8vd3d3LnRuZi5jb20vaWRlbnRpdHkvY2xhaW1zL3Byb2R1Y3ROYW1lIjoiK1NhbGRvIiwiaHR0cDovL3d3dy50bmYuY29tL2lkZW50aXR5L2NsYWltcy9wcm9kdWN0SWQiOiIyMCIsImh0dHA6Ly93d3cudG5mLmNvbS9pZGVudGl0eS9jbGFpbXMvdGVuYW50SWQiOiI1ZGFkMDdjYy1mY2E0LTRmMWQtYmFiYi1iMTA0YzJhMTFjOTYiLCJpYXQiOjE2NDc1Mzg2MjMsInNjb3BlIjpbImF1dGhvcml6YXRpb25fYXBpIl19.t8s4wJZEfOA1yGq1jUVzNdCVTs\_cXh8hMhP8pXzqMAoG1uSjsK88nDngvOXmbDwD5xBwJSoQistDDGNVFLEzrYXlgVSWd3hP26gZtvYIg-jM1MWwxayW8UXbFIIXDxG\_xv0GB81-CaE8T7Dy6b2xx3w766NADJsEAkvx1qLzSXHE8lLSr-cSdLG9xVb7YfbubD2s2Y1oyWKtkW9ZdGiUoAjR27neWNgVlRbBz9IDel2omTdUeDN5vohoADNJuHOlZ0Z6QelMLOq3KTAA48hASMc1-wgq5glRp-W2H54tUqyTdU9Gv1LjN\_F9Sjf4OMROZfMINjzOlBZuxFpcVU\_mQQ" |
| --- |

Deve ser retornado um json no seguinte formato, conforme exemplo:

| [     {         "productName": "Consignado",         "productKey": "saldo"     } ] |
| --- |

**HABILITAR TLS**

**Em alguns casos é necessário ajustar o TLS do servidor.**

Para ajustar basta criar um arquivo com a extensão .Reg e escrever o comando abaixo. Após criar o arquivo basta executar.

Importante que todos os servidores que processam Jobs estejam com essa configuração.

Atenção

**Antes de Executar é importante fazer o backup das todas as chaves descritas no bloco de código.**

## **04.** **App desativado**

### Problema

O app foi desativado na tela de integração:

A tela acima só está disponível a partir da versão **12.1.2306**.  
Nas versões anteriores o erro pode ser identificado através do log, utilizando a *tag* **TotvsApps**.

### Possível causa

Uma possível causa para esse problema é a de que as *triggers*(gatilhos no banco de dados) foram apagadas ou desativadas. Isso gera problemas na integração, que se desativa para garantir a integridade dos dados.

### Solução

Para solucionar esse problema, existem duas formas:

A primeira opção é a solução ótima, mas só está disponível a partir da versão **12.1.2306**.  
Para as versões anteriores, a opção 2 é ideal.

#### Opção 1

Na tela da integração, clicando na coluna de Ação do respectivo app, é necessário selecionar a opção **REPARAR**, e, então, clicar em Executar no canto inferior da janela:

#### Opção 2

A segunda forma é desativando e ativando novamente a integração. Desta forma, as *triggers* serão recriadas no momento da reativação.
