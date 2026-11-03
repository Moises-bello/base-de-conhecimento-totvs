---
article_id: 360044840733
category: ADVPL - Web Service
content_hash: 81b7ba9a33371bf6425af97c6d3ae43e345301bba08b32f17a62159e5d8cca50
fetched_at: '2026-06-28T22:40:10.484847+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - JSON Web Token
  (JWT)? '
type: support-article
updated_at: '2021-12-20T14:09:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044840733-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-JSON-Web-Token-JWT
---

**Dúvida**O que é o JSON Web Token?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.25  
  
**Solução**O **JSON Web Token** (JWT) é um padrão aberto ( [**RFC 7519**](https://tools.ietf.org/html/rfc7519) ) que define uma maneira compacta e independente de transmitir com segurança informações entre partes como um objeto **JSON**. Essas informações podem ser verificadas e confiáveis ​​porque são assinadas digitalmente. Os **JWTs** podem ser assinados usando um segredo (com o algoritmo **HMAC** ) ou um par de chaves pública / privada usando **RSA** ou **ECDSA** .

**JWT no REST PROTHEUS**

Antes de tudo, é importante dizer que essa funcionalidade está **disponível a partir da LIB versão 20190705**

Esse token é resultado de um **POST** no endpoint **/token** e tem uma validade de curta duração. Seu contexto de acesso pode variar de acordo com o usuário que está se autenticando.

Nesse modelo fica necessário então o tráfego de usuário e senha apenas nessa requisição de acesso (que é fortemente recomendado que seja protegida por **SSL - Secure Sockets Layer** para não ser interceptada por terceiros), e após a obtenção, basta incluir o token no cabeçalho de cada requisição para garantir o acesso às demais API’s que o usuário tenha direito.

Após a expiração da validade do token de acesso é necessário repetir a requisição através do fornecimento de usuário e senha ou, melhor ainda, também é possível a utilização de um token de refresh para obter outro token de acesso sem a necessidade de trafegar a senha novamente.

Esse token de refresh é obtido juntamente com o token de acesso na primeira requisição e tem um tempo de expiração bem superior ao do token de acesso. Atualmente o tempo de expiração do token de acesso está definido em uma hora e o de refresh em vinte e quatro horas.

Uma vez que é requisitada a atualização dos tokens, o prazo de validade de ambos é renovado e com isso é possível manter o acesso garantido pelo tempo que for necessário de forma circular.

Caso a atualização não seja requisitada até o momento de expiração do token de refresh, não será mais possível obter acesso por atualização, sendo então necessário solicitar o token de acesso informando usuário e senha novamente.

**Saiba Mais  
[API para obtenção do token de acesso às API’s REST no Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=465383509)****[API TOKEN](https://api.totvs.com.br/apidetails/Token_v1_000.json)****[JWT](https://jwt.io/introduction/)**
