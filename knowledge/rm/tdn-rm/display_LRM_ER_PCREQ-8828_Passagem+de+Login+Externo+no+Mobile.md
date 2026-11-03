---
content_hash: b79f2e40a6db7cbd181427285190e6d649bb615b2083e877057ba05a09a15d74
fetched_at: '2026-06-29T00:06:18.334323+00:00'
page_id: '215483690'
product: rm
source: tdn-rm
title: ER_PCREQ-8828_Passagem de Login Externo no Mobile
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8828_Passagem+de+Login+Externo+no+Mobile
version: 16
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | TOTVS Educa Mobile |
| **Segmento Executor** | Educacional | | |
| **Projeto** | R\_EDU\_EDU016 | **IRM** | PCREQ-8827 |
| **Requisito** | PCREQ-8828 | **Subtarefa** | PDR\_EDU\_EDU016-13 |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

### Objetivo

Descrever como deve ser a passagem de login externo para o TOTVS Educa Mobile

### Definição da Regra de Negócio

A passagem de login externo para o TOTVS Educa Mobile pode acontecer de duas formas diferentes:

* Através de uma página em um website;
* Através de um app para dispositivos móveis (smartphones/tablets).

Nos dois casos, alguns requisitos precisam ser seguidos, são eles:

* O endereço padrão deve ser sempre **"http://<url\_totvs\_educa\_mobile>/Account/LoginExterno"** onde **<url\_totvs\_educa\_mobile>** é o endereço de acesso ao TOTVS Educa Mobile instalado no cliente.
* O campo ou variável que receber o nome do usuário deve sempre ser nomeado **UserName**.
* O campo ou variável que receber a senha do usuário deve sempre ser nomeado **Password**.
* O padrão de envio HTTP deve ser sempre **"POST"**.

Ao preencher as informações corretamente a requisição do usuário será encaminhada para o TOTVS Educa Mobile que fará a validação do usuário, podendo ter os seguintes comportamentos:

* **Usuário autenticado com sucesso**: Caso o usuário tenha utilizado um formulário em uma página web, o TOTVS Educa Mobile será carregado na mesma janela do browser que foi utilizada para o login. Caso o usuário tenha utilizado um app de smartphone/tablet para realizar o login, deverá existir um redirecionamento do resultado da autenticação para um componente de browser nativo da plataforma utilizada, onde o TOTVS Educa Mobile será exibido corretamente, de acordo com os padrões de desenvolvimento adotados pela nossa arquitetura (web based application).
* **Usuário NÃO autenticado**: Caso o usuário não tenha sucesso na autenticação, será redirecionado para uma página de erro, indicando o problema.
* **Senha de usuário expirada**: Caso o usuário esteja com a senha expirada, será redirecionado para uma página de erro indicando o problema. Será apresentado link para solicitar a troca da senha através das telas originais do TOTVS Educa Mobile.
* **Qualquer outra mensagem de erro**: Caso aconteça qualquer outra mensagem de erro, o usuário será redirecionado para uma página de erro, indicando o problema.

Em todos os casos onde acontecer algum tipo de erro na autenticação, vinda de uma página web, será apresentado link para que o mesmo possa retornar à tela de login, o que não acontecerá no caso de app para smartphone/tablet, onde a implementação do retorno ficará a cargo do desenvolvedor do app.

### Protótipo de Tela (autenticação via página web)

Página com os requisitos necessários para realização do login externo.

Login realizado em um site diferente do TOTVS Educa Mobile, conforme mostrado abaixo

Após autenticação realizada, o redirecionamento acontece, conforme link destacado abaixo:

Caso a autenticação não tenha sucesso, acontece redirecionamento para página de erro.

### Protótipo de Tela (autenticação via app de smartphone/tablet - simulação)

Aplicativo com os requisitos necessários para realização do login externo

Após autenticação realizada, o resultado é exibido em um componente webbrowser, feito em C#, nesse exemplo.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
