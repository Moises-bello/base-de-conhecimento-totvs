---
content_hash: 206fb8de0fcd7faf3d74a58fe233eb60715fc08eedccbb2f79585a09975c2c83
fetched_at: '2026-06-29T00:10:26.077146+00:00'
page_id: '510513612'
product: rm
source: tdn-rm
title: API de Recuperação e Alteração de senha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=510513612
version: 21
---

# Sumário

---

Sumário

# Objetivo

---

      Esse documento tem o objetivo de exemplificar o uso da API utilizando todos os métodos implementados.

# 1 - Métodos

---

      Serão apresentados os métodos, implementados complementarmente na API de Usuários, são eles:

* ChangePassword (POST)
* RecoveryPassword (POST)
* ChangePasswordWithToken (POST)

# 1.1 - ChangePassword

---

false1.1 ChangePasswordfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users/{userId ou Email}/changePassword

falseExemplo de Configuração

**Domínio:**localhost  
**Porta:** 8051

**Url Utilizada:** http://localhost:8051/api/framework/v1/users/mestre/changePassword

falsePayload

A ser enviado na requisição

jsfalseExemplo de Resultado Positivo Postman

Em caso de sucesso, será retornado o respondeCode = 200 e a resposta em branco.

falseExemplo de Resultado Negativo

Em caso de inconsistência, será retornado o respondeCode = 404 e a na resposta informará qual é a inconsistência.

# 1.2 - RecoveryPassword

---

false1.2 RecoveryPassword

Ao executar a requisição Post, será enviado um e-mail para o e-mail cadastrado referente ao usuário informado na URL.

Este e-mail irá possuir um Token que é valido somente para o usuário informado e possui o tempo de vida de um dia. Este Token servirá para alterar a senha do usuário utilizando o serviço 1.3 (ChangePasswordWithToken)

Atenção

O Token é invalidado de **imediato** caso o usuário referente ao token consiga realizar acesso ao sistema.

O Token é valido de acordo com a forma que foi gerado. Caso o token tenha sido através do **CODUSUARIO**, ao utilizar o serviço "ChangePasswordWithToken" o mesmo deverá ser utilizado com o **CODUSUARIO**, caso o token tenha sido gerado através do **E-MAIL**, ao utilizar o serviço "ChangePasswordWithToken" o mesmo deverá ser utilizado com o e-mail

falseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/users//{userId ou Email}/recoveryPassword

falseExemplo de Configuração

**Domínio:**localhost  
**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/mestre/recoveryPassword](http://localhost:8051/api/framework/v1/users/mestre/changePassword)

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/mestre@totvs.com.br/recoveryPassword](http://localhost:8051/api/framework/v1/users/mestre/changePassword)

falseExemplo de Resultado Positivo Postman

Em caso de sucesso, será retornado o respondeCode = 200 e a resposta em branco.

falseExemplo de Resultado Negativo

Em caso de inconsistência, será retornado o respondeCode = 400 e a na resposta informará qual é a inconsistência.

# 1.3 - ChangePasswordWithToken

---

false1.3 ChangePasswordWithTokenfalseConfiguração

**Máscara de Url:** http://{domínio}:{porta}/api/framework/v1/{userId ou Email}/changePasswordWithToken

falseExemplo de Configuração

**Domínio:**localhost  
**Porta:** 8051

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/mestre/changePasswordWithToken](http://localhost:8051/api/framework/v1/users/mestre/changePassword)

**Url Utilizada:** [http://localhost:8051/api/framework/v1/users/mestre@totvs.com.br/changePasswordWithToken](http://localhost:8051/api/framework/v1/users/mestre/changePassword)

falsePayload

A ser enviado na requisição

jsfalseExemplo de Resultado Positivo Postman

Em caso de sucesso, será retornado o respondeCode = 200 e a resposta em branco.

falseExemplo de Resultado Negativo

Em caso de inconsistência, será retornado o respondeCode = 400 e a na resposta informará qual é a inconsistência.
