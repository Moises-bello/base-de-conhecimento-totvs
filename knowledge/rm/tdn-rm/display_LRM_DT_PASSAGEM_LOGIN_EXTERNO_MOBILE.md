---
content_hash: 1a90c7ace23e37cc621d440a76ae77423a0262e1b5188ddf72b36a58da254b3e
fetched_at: '2026-06-29T00:06:20.201122+00:00'
page_id: '221549208'
product: rm
source: tdn-rm
title: DT_PASSAGEM_LOGIN_EXTERNO_MOBILE
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_PASSAGEM_LOGIN_EXTERNO_MOBILE
version: 3
---

# PASSAGEM DE LOGIN EXTERNO NO MOBILE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **TOTVS Educacional** |
| **Módulo:** | **TOTVS Educa Mobile** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Login** | *Login* | |
| **Requisito (ISSUE):** | *PCREQ-8828* |
| **País(es):** | *Brasil* |
| **Versões/Release:** | *12.1.9* |

## Descrição

A passagem de login externo para o TOTVS Educa Mobile pode acontecer de duas formas diferentes:

* Através de uma página em um website;
* Através de um app para dispositivos móveis (smartphones/tablets).

Nos dois casos, alguns requisitos precisam ser seguidos, são eles:

* O endereço padrão deve ser sempre **"http://<url\_totvs\_educa\_mobile>/Account/LoginExterno"** onde **<url\_totvs\_educa\_mobile>** é o endereço de acesso ao TOTVS Educa Mobile instalado no cliente.
* O campo ou variável que receber o nome do usuário deve sempre ser nomeado **UserName**.
* O campo ou variável que receber a senha do usuário deve sempre ser nomeado **Password**.
* O padrão de envio HTTP deve ser sempre **"POST"**.

## Procedimento para Utilização

 Ao preencher as informações corretamente, a requisição do usuário será encaminhada para o TOTVS Educa Mobile que fará a validação do usuário, podendo ter os seguintes comportamentos:

* **Usuário autenticado com sucesso**: Caso o usuário tenha utilizado um formulário em uma página web, o TOTVS Educa Mobile será carregado na mesma janela do browser que foi utilizada para o login. Caso o usuário tenha utilizado um app de smartphone/tablet para realizar o login, deverá existir um redirecionamento do resultado da autenticação para um componente de browser nativo da plataforma utilizada, onde o TOTVS Educa Mobile será exibido corretamente, de acordo com os padrões de desenvolvimento adotados pela nossa arquitetura (web based application).
* **Usuário NÃO autenticado**: Caso o usuário não tenha sucesso na autenticação, será redirecionado para uma página de erro, indicando o problema.
* **Senha de usuário expirada**: Caso o usuário esteja com a senha expirada, será redirecionado para uma página de erro indicando o problema. Será apresentado link para solicitar a troca da senha através das telas originais do TOTVS Educa Mobile.
* **Qualquer outra mensagem de erro**: Caso aconteça qualquer outra mensagem de erro, o usuário será redirecionado para uma página de erro, indicando o problema.

Em todos os casos onde acontecer algum tipo de erro na autenticação, vinda de uma página web, será apresentado link para que o mesmo possa retornar à tela de login, o que não acontecerá no caso de app para smartphone/tablet, onde a implementação do retorno ficará a cargo do desenvolvedor do app.

divs
