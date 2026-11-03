---
content_hash: 9c8b3a01a2d316a5a95a4fa4f66769431b951b8c2cd6e227bb4f543743f73155
fetched_at: '2026-06-29T00:10:10.469678+00:00'
page_id: '452719845'
product: rm
source: tdn-rm
title: Efetivar Benefícios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719845
version: 3
---

**Efetivar Benefícios**

A Efetivação de Benefícios tem por objetivo possibilitar a conclusão deste tipo de requisição através do processo "Efetivar Requisições de Benefícios". Ao executar o processo "Efetivar Requisições de Benefícios", será analisada individualmente cada requisição e se aprovado o lançamento será realizado.

Caso o sistema esteja parametrizado para utilizar Controle de Pontuação ao efetivar uma requisição de solicitação os pontos utilizados pelo funcionário ou seus dependentes serão subtraídos ao saldo disponível pelo funcionário. Assim como também ao efetivar uma requisição de recusa pelo funcionário e/ou seus dependentes os respectivos pontos dos mesmos serão creditados no saldo de pontos do funcionário.

**Atenção:**

- Para integrar os benefícios às requisições são necessárias associar a requisição ao beneficio no cadastro de beneficio. Assim pelo Portal, realizar a requisição de solicitação e/ou de recusa. Essa requisição de solicitação e/ou recusa deverá ser aprovada de acordo com o fluxo de aprovação definido no tipo de requisição.

- Não será possível editar uma requisição de recusa e o benefício não estiver Em Uso.

**Observação:**

- Somente podem ser concluídas as requisições gerais aprovadas.

- Beneficiários: exibe a lista de pessoas que foram associadas à requisição pelo Portal. Para cada uma dessas pessoas, exibe também as seguintes informações:

    Classificação: exibe "dependente" se o beneficiário for dependente. Caso contrário exibe "funcionário".

    Nome: exibe o nome do funcionário ou do dependente.

**Detalhes dos Dados para Efetivação do Benefício**

Para as requisições do tipo RECUSA serão apresentados os dados:

Data de Início: este campo deve ser apresentado desabilitado, mas, preenchido com a data de início do lançamento vigente.

**Atenção:**

Caso não exista lançamento vigente, o campo data de início não será preenchido.

Data de Término: este campo deve ser preenchido com a data atual.

Valor: este campo deve ser apresentado desabilitado, mas, preenchido com o valor do lançamento vigente. Caso não exista lançamento vigente, o campo valor não será preenchido.

Para as requisições do tipo SOLICITAÇÃO serão apresentado os dados:

Data de Início: este campo deve ser preenchido com a data atual do sistema se não existir lançamentos vigentes.

**Atenção:**

- Caso existam lançamentos vigentes e, se o usuário não alterou manualmente esta data, o campo data de início deve ser preenchido com a data de inicio do lançamento vigente.

- Caso existam lançamentos e, se o usuário não alterou manualmente esta data, o campo data de término deve ser preenchido com a data de término do lançamento vigente.

Data de Término: este campo deve ser preenchido com a data de término da vigência do cadastro de benefício se não existir lançamento.

Valor: este campo deve ser preenchido com o valor, fixo ou calculado, do cadastro de benefício se não existir lançamento vigente. Caso exista lançamento vigente e, se o usuário não alterou manualmente este valor, o campo valor deve ser preenchido com o valor do lançamento vigente.

**Dica:**

Os procedimentos de solicitação ou de recusa de benefício pelo Portal somente serão realizados mediante processo de efetivação de requisição. Uma requisição aberta para dependentes pode ser efetivada antes da requisição aberta para o funcionário.

**Atenção:**

Somente será efetivado o benefício que atender a todos os critérios do lançamento de benefícios. Caso o sistema esteja configurado para utilizar controle de pontuação, o total de pontos disponíveis para o beneficiário deve ser superior à soma da pontuação requerida pelo benefício.

Caso o beneficiário seja um dependente, deve ser considerado o total de pontos disponíveis do funcionário relacionado. Ao efetivar uma requisição de solicitação os pontos utilizados pelo funcionário ou seus dependentes serão subtraídos ao saldo disponível pelo funcionário. Assim como também caso um benefício seja recusado pelo funcionário e/ou seus dependentes os respectivos pontos dos mesmos serão creditados no saldo de pontos do funcionário.
