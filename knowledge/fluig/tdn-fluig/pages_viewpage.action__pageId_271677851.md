---
content_hash: fc7eb70fe9aba782c933a4bcf10c3ce46008476ac8f1ffe84a2f0c088a2d21bf
fetched_at: '2026-06-28T21:35:24.837329+00:00'
page_id: '271677851'
product: fluig
source: tdn-fluig
title: BPM 091 - Como utilizar campo de formulário para definir responsáveis em uma
  nova solicitação?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271677851
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**fluig

# Ocorrência

Em alguns casos, se tem a necessidade de definir os responsáveis de uma atividade de forma personalizada, considerando os dados do formulário. A partir da Atualização 1.5.12, disponibilizamos o uso da hAPI no [Mecanismo de atribuição personalizado](http://tdn.totvs.com/pages/viewpage.action?pageId=142804157), entretando, é indicada apenas para solicitações já iniciadas, uma vez que a hAPI depende dos dados do formulário gravado na solicitação.

# Solução

Quando é necessário considerar os dados do formulário no momento que está iniciando uma solicitação, aconselhamos customizar já no script do formulário, como é exemplificado abaixo.

Definindo os responsáveis conforme dados do formulário

0.5falsesamplesfadetrue1Passo 1

* Como exemplo, estaremos utilizando os Grupos "group1" e "group2" que devem ser alterados conforme grupo utilizado na plataforma.
* Criando o html, onde o usuário poderá escolher entre pegar os usuários de um grupo, ou, simplesmente enviar para o Pool de um Grupo.

xmlformulario.htmltrue


### Selecione o Grupo

Grupo 1

Grupo 2

Enviar para Pool

]]>jsformulario.jstrue2Passo 2

* Após publicar o arquivo HTML e JS como formulário fluig, o resultado será esse.

  **Figura 1 - Visualizando o formulário.**

3Passo 3

* Criar e vincular o Processo com o Formulário, publicado anteriormente.
* Definir a atividade para utilizar o Mecanismo "Atribuição por Campo de Formulário" e selecionar o campo "group\_selected", campo *hidden* presente no HTML, que terá o valor dos responsáveis pela atrividade.

**Figura 2 - Configurando Mecanismo de Atribuição.**

4Passo 4

* Feito os passos, a solicitação estará preparada para difinir os responsáveis conforme dados selecionados no formulário, neste exemplo, temos dois casos
  1. Selecionar o grupo e deixar o botão "Enviar para Pool" desligado: Será consultado o Dataset "colleagueGroup" para retornar os colaboradores do grupo;
  2. Selecionar o grupo e deixar o botão "Enviar para Pool" ligado: Não será consultado nenhum Dataset, o campo hidden ficará com o valor "Pool:Group:group\_code", com isso, a atividade estará para em Pool, esperando que algum colaborador do grupo assuma a atividade.

**Figura 2 - Configurando Mecanismo de Atribuição.**
