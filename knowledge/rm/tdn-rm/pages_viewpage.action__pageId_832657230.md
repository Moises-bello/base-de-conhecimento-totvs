---
content_hash: 56d9de292fbf382cc2106e16b42f3e9ca42878dc71fa16bcdf3a8c42d979fda7
fetched_at: '2026-06-29T00:11:49.423403+00:00'
page_id: '832657230'
product: rm
source: tdn-rm
title: TBC - Autenticação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=832657230
version: 3
---

## **Introdução**

A maior parte das Webservices do RM exigem que seja realizada a autorização/autenticação para concluir a chamada, por razões de segurança. Neste documento, serão explicadas e definidas as possíveis formas de autenticação para consumo dos webservices do RM, suas vantagens e desvantagens e como utilizá-las.

## **Autenticação Bearer - Indicada\***

---

Dentro do RM, é possível gerar um token, em formato JWT (Json Web Token) que será utilizado como token de autorização nos webservices do sistema.  
Confira nesta documentação como configurar e gerar um AccessToken JWT:

**Exemplo de utilização**

* Usando o Postman, gere um AccessToken pela api http://seudominio:8051/api/connect/token com as seguintes propriedades:
  + username: (seu usuário)
  + password: (sua senha)

* Copie o valor da propriedade access\_token
* Usando o SoapUI, abra uma nova requisição, clique na aba Headers, e adicione uma nova propriedade
  + Header: Authorization
  + Value: Bearer (insira aqui o access\_token gerado no passo anterior)

Verifique que a requisição foi realizada com sucesso e os dados foram apresentados corretamente.

## **Autenticação Basic**

---

A autenticação do tipo **Basic**não é recomendada pelo seu baixo nível de segurança. Sempre que possível, opte pela autenticação **Bearer** explicada acima

**Exemplo de utilização**

* Usando o SoapUI, abra uma nova requisição, clique na aba Auth, e adicione uma nova autorização do tipo Basic com os valores a seguir:
  + Username: (seu usuário)
  + Password: (sua senha)
  + Pre-Emptive auth: Authenticate pre-emptively
