---
content_hash: 8259aec81a581927ba80bf96a3d2e893bef51c1b0f43222ae1c12e8d0bb53a2d
fetched_at: '2026-06-29T00:09:12.909968+00:00'
page_id: '417701686'
product: rm
source: tdn-rm
title: Integração Produto x TReports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417701686
version: 16
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Realizar a integração de um Produto com o TReports e entender o fluxo da autenticação entre Produto X TReports X Provedor Integrado.

# Definições Gerais:

---

Para exemplificar a integração, será utilizado o projeto TReportsServerClient (<https://github.com/totvs/treports-server-client>)

       O TReports utiliza o Rac para gerenciamento dos usuários e permissões configurados por Tenant.

# Recuperando Access Token:

---

       Para realizar a integração do produto com o TReports, é utilizado o Fluxo Resource Owner (password). Este fluxo necessita de um usuário e senha válidos no Tenant configurado para o TReports para que a autenticação seja realizada.

       Este usuário precisa conter a permissão de execução de relatório (ExecuteReport).

       POST  
       Host: {Endereço do Rac}/connect/token  
       Host Ex.: http://localhost/totvs.rac/connect/token

       Content-type: application/x-www-form-urlenconded  
       Authorization: Basic {ClientId:ClientSecret}

**grant\_type=password**  
       **&username**=exampleuser  
       **&password**=1234luggage  
       **&scope=authorization\_api**  
       **&client\_id**=xxxxxxxxxx  
       **&client\_secret**=xxxxxxxxxx  
       **&acr\_values=tenant:**treports

       Segue em anexo a requisição via Postman: 

       Obs: O **ClientId** e **ClientSecret** podem ser passados no Body da requisição ou no Header Authorization codificado para base64 ClientId:ClientSecret

       Para mais informações: <https://developer.okta.com/blog/2018/06/29/what-is-the-oauth2-password-grant>

# Autenticação Externa - Rac:

---

       O Tenant pode ser configurado para realizar a autenticação externa, onde a validação do usuário e senha serão realizadas em um endpoint do produto.

       Será realizado uma chamada no endpoint do Produto configurado no Tenant do Rac para que o usuário e senha sejam validados pelo Produto, em casso de sucesso, o Access Token é retornado para o Produto.

# Executando um relatório:

---

       Com o Access Token gerado, ele deve ser enviado no Header Authorization em todas as requisições da Api do Reports.  
       Ex. “Authorization: Bearer {access\_token}”  
       O fluxo de toda a execução pode ser visto abaixo:

       A seguinte chamada deve ser realizada na api do TReports:

              POST

              Authorization: Bearer {access\_token}  
              Host: {Endereço do TReports}/api/trep/v1/reports/{UidReports}/execute  
              Content-type: application/json

              ... {Consultar o Swagger para obter lista completa de parâmetros}  
              generateParams: {  
                   ...  
                   isView: Boleando para informar se o relatório será visualizado em tela ou não. Para a geração através de API, sempre informar **false.**  
              }  
              UserName: Nome do Usuário que será enviado ao Provedor Integrado para aplicação de segurança.

Custom Data

Foi criada uma propriedade no objeto "GenerateParams" chamada "CustomData".

Trata-se de um propriedade do tipo string que receberá qualquer valor customizado a ser enviado na chamada do endpoint.

O valor enviado na propriedade "CustomData" será adicionado na lista de parâmetros do provedor (ProviderParams) que chegará em todos os endpoints definidos na API de "provedores integrados".

Obs: O objeto "GenerateParams" é usado para enviar informações na chamada do endPoint "/execute" (listado acima) para enviar informações de execução do relatório.

Exemplo:

Usuários do Protheus poderão enviar o "grupo de empresas" nessa propriedade para ser utilizada em filtros localizados nos provedores integrados do Protheus,

       Esta requisição gera uma solicitação de execução do relatório, mas não o executa imediatamente. Ele será executado pelo job do TReports. O retorno será um identificador único da requisição de execução (UidRequest)

       Para acompanhamento da execução do relatório, execute a seguinte chamada:

              GET  
              Authorization: Bearer {access\_token}  
              Host: {Endereço do TReports}/api/trep/v1/Generateds/{uIdRequest}/info  
              Content-type: application/json

              {Consultar o Swagger para obter lista completa de parâmetros}

       Nesta chamada será retornado o identificador da geração do relatório {id} e o status da execução {status} dentre outras informações. Caso o status seja finalizado, podemos realizar a chamada para obter o relatório gerado no formato desejado:

              GET  
              Authorization: Bearer {access\_token}  
              Host: {Endereço do TReports}/api/trep/v1/Generateds/{id}/file  
              Content-type: application/json

              ExportFileType=0 {Consultar o swagger para uma lista completa das opções de arquivo para download}

       Será retornado o binário do arquivo gerado no formato solicitado.

# Provedor Integrado:

---

       O fluxo completo utilizando provedor integrado pode ser visto abaixo:

      O provedor de dados integrado suporta os seguintes tipos de autenticação:

**Basic**

      É informado o usuário e senha para acesso ao provedor de dados. Essa informação será enviada no cabeçalho da requisição como autenticação Basic

**OpenID**

       O Provedor de dados integrado receberá o access\_token do TReports. O token contém o usuário logado no sistema, mas para o caso do fluxo Resource Owner sem a autenticação externa configurada, o usuário do token será sempre o usuário criado para realizar o fluxo Resource Owner. Desta forma, foi criado no Header da requisição a propriedade UserName contendo o nome do usuário informado nos parâmetros da requisição do Execute Request (endPoint: /api/trep/v1/reports/{UidReport}/execute). Caso não seja informado o usuário nos parâmetros do Execute Request, o UserName conterá o usuário do Token.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.22 ou Superiores

false

**Processo:** Integração TReports

falsefalse

**Status:** Pendente

false

**Data:**

false

**Autores:**
