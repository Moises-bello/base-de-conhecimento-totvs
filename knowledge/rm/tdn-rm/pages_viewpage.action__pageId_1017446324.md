---
content_hash: fbca26baffd6747de4b9ef3415b6b6745f530b574cd75d50d765ec99596d75e7
fetched_at: '2026-06-29T00:05:47.800762+00:00'
page_id: '1017446324'
product: rm
source: tdn-rm
title: Documentação de API
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1017446324
version: 3
---

O Open Api, anteriormente conhecido como Swagger, é hoje o padrão mais utilizado para documentar API's. No ASP.NET Core é muito fácil configurar. Ele disponibiliza mecanismos para testar sua API no Browser.

<http://localhost:8051/api/swagger/ui/index>

# **Autenticação**

Garantir a segurança dos dados também faz parte do desing de uma API, hoje o principal modelo utilizado pela comunidade é o Oauth 2.0, este é um padrão de autenticação, que foi construído para preservar os dados sensíveis de um usuário, minha recomendação seria sempre que possível utiliza-lo, porem caso não seja possível, não deixe sua API sem autenticação, no mínimo utilize uma autenticação do tipo basic, onde geralmente é criado um token em base64 a partir de um usuário e senha.

A utilização de Tokens de acesso, que são gerados pelo serviço REST  devem ser armazenados pelos clientes, via cookies ou HTML 5 Web Storage, devendo também ser enviados pelos clientes a cada nova requisição ao serviço.

Outras tecnologias e padrões para se trabalhar com Tokens:

* OAUTH;
* JWT (JSON Web Token);
* Keycloack.

# **Stateless**

Garanta que sua API não guarde nenhum tipo de estado referente a comunicação, toda requisição deve ser inteligente o suficiente para se resolver, sem armazenar quaisquer dados de seção.

# **Negociação de conteúdo**

Apesar do ideal ser trafegar apenas JSON, caso sua API trafegue outros tipos de dados, por exemplo XML, utilize as chaves Accept e Content-Type do protocolo HTTP para detalhar todas as possibilidades

# **Paginação**

Em requisições GET que retornem listas, devolva somente o necessário, pagine sua requisição, desta forma todos ganham, pois será trafegado somente o necessário, melhorando a experiência do usuário final.

# **Ordenação**

Otimize suas requisições, facilite ainda mais a vida de seus clientes, permita que sua Api, ordene sua resposta, desta forma o cliente pode não precisar realizar nenhum tipo de tratamento no dado.

# **Respostas Parciais**

Otimize ainda mais suas requisições GET, permita seus clientes recuperarem somente os campos que realmente necessitam, desta forma de ponta a ponta serão trafegado apenas os dados necessários.

# **Hateoas**

Hateoas representa o termo Hypermedia as the engine of application State (Hipermídia como o mecanismo do estado do aplicativo), é um padrão que sempre inclui links uteis junto as respostas de uma requisição

Os principais benefícios de seguir essa abordagem são:

1. As aplicações clients conhecem facilmente o limite e próximos passos de cada domínio
2. As aplicações clients podem recuperar seus paths dinamicamente sem a necessidade de colocar-los fixo no código
3. Os desenvolvedores da API podem alterar o esquema de paths sem quebrar as aplicações clients

<acao> <rel>self</rel> <uri><http://servicorest.com.br/pedidos/1459></uri> <method>GET</method> </acao>

# **Open Documentation**

Alem de seguir as melhores práticas, faça ainda mais que isso, utilize frameworks como o Swagger, que é um framework open source que apoia o desenvolvedor no desenho, documentação e especificação de suas Api's.
