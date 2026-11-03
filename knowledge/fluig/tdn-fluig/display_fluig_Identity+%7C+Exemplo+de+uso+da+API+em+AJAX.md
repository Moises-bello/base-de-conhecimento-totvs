---
content_hash: 4cfaff76f9e408b54f43f9cf706bcbd08bec1b3f7dfd5aa3dc99eb575592e0ad
fetched_at: '2026-06-28T21:35:26.181034+00:00'
page_id: '347449226'
product: fluig
source: tdn-fluig
title: Identity | Exemplo de uso da API em AJAX
type: documentation
url: https://tdn.totvs.com/display/fluig/Identity+%7C+Exemplo+de+uso+da+API+em+AJAX
version: 15
---

# Índice

true.\*ndicenone

# Descrição

---

O exemplo disponibilizado nesta página demonstra como solicitar o token de acesso OAuth e realizar uma chamada à API do Identity via JavaScript (AJAX).

# Autorização

---

Para utilizar os *endpoints* da API com AJAX, primeiramente é necessário solicitar autorização para obter um token de acesso (*access token*). Os passos abaixo usam o Swagger como referência para explanar esse procedimento.

falseauthtruePasso 1

* Acessar a URL da API: https://[contexto].fluigidentity.com/rest/swagger-ui/index.html.

* O [contexto] é o subdomínio da empresa no Identity. Por exemplo, se a URL de acesso da empresa no Identity for <https://minhaempresa.fluigidentity.com.> o contexto é "minhaempresa".

Caso seja utilizado o ambiente de , a URL da API será https://[contexto].customerfi.com/rest/swagger-ui/index.html.

Passo 2  

* Expandir o serviço **oauth2**.

* Acessar o *endpoint* **GET /rest/v2/oauth2/clients/{clientId}/assertion**.

* Preencher o parâmetro **clientId** com o  da empresa.

Para obter o *clientId*, acessar o menu  → aba Segurança → REST API v2 → .

Passo 3

* Ao acionar ***Try it out****!***, será gerado o *Client Assertion* no *Responde Body*.

* O valor do *Client Assertion* deve ser copiado para utilização no próximo passo.

Passo 4

* Acessar o *endpoint* **POST** **/rest/v2/oauth2/auth**.

* Preencher o valor do *Client Assertion* obtido no passo anterior no campo ***assertion**.*

* Acionar ***Try it out!*** para obter o token de acesso (***access token***).

Passo 5

* Para utilizar todos os *endpoints* da API do Identity, copiar o *access token* para campo **api\_key** no canto superior direito da página e acionar ***Explore**.*

# Exemplo

---

O exemplo de código-fonte a seguir demonstra como realizar o procedimento de autorização e obtenção do *access token* via AJAX, bem como a chamada de um *endpoint* para recuperar os dados de uma empresa (contexto) através da API do Identity.

O *access\_token* obtido a partir da autorização na API deve ser enviado no *header* de todas as requisições.

jstrue'; // Substituir '' pelo clientId da empresa
var companyId =''; // Substituir '' pelo companyId da empresa
var domainUrl = 'https://.fluigidentity.com/'; /\* Substituir '' pelo contexto da empresa \*/
var apiUrl = domainUrl + 'rest/v2/';
// Get client assertion
function getClientAssertion(clientId) {
$.ajax({
url:apiUrl + 'oauth2/clients/' + clientId + '/assertion',
crossDomain:true // se necessário cross domain
})
.done(function(data){
getAccessToken(data);
})
.fail(function(error){
console.log(error);
});
}
// Grant a new refresh token
function getAccessToken(assertion) {
var data = {
'grant\_type':'urn:ietf:params:oauth:grant-type:jwt-bearer',
'assertion':assertion
};
$.ajax({
url:apiUrl + 'oauth2/auth',
crossDomain:true, // se necessário cross domain
data:data,
type:'POST'
})
.done(function(data){
getCompany(data.access\_token,companyId)
})
.fail(function(error){
console.log(error);
});
}
// Get a company
function getCompany(authorization, companyId) {
$.ajax({
url:apiUrl + 'companies/' + companyId,
crossDomain:true, // se necessário cross domain
headers:{
'Authorization':authorization
}
})
.done(function(data){
console.log(data);
})
.fail(function(error){
console.log(error);
});
}
getClientAssertion(clientId);
]]>
 ]]>
