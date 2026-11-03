---
content_hash: d6478f082cc19affeac2d97da6d5f41f5a4f4f7f2e0f6a6dcc6a2213e92bbbbe
fetched_at: '2026-06-29T00:10:47.419134+00:00'
page_id: '557319605'
product: rm
source: tdn-rm
title: NPS - Respondendo a pesquisa de satisfação no RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=557319605
version: 24
---

**6circle**

## **01. VISÃO GERAL**

Está sendo implementado em todo o sistema RM um projeto de pesquisa de satisfação do cliente.

Nosso objetivo é melhorar o produto por meio dos feedbacks dos nossos usuários de forma segura e centralizada, contribuindo diretamente para a melhoria contínua do produto com base na experiência real, para que possamos entregar mais **valor** e **satisfação** aos nossos clientes.

## **02. Como responder a pesquisa**

Ao abrir algumas telas do sistema, baseada em regras implementadas dinamicamente pela TOTVS e seus segmentos de produtos, será exibida a pesquisa de satisfação do módulo.

**Exemplo:**

Pesquisa exibida ao abrir um módulo:

Existem 3 opções de resposta nessa tela:

* **Cancelar e não perguntar novamente:** Será enviado para a totvs uma resposta de cancelamento e a pesquisa deste módulo não será exibida novamente até se completar um novo ciclo.
* **Confirmar e enviar para a Totvs:**A(s) resposta(s) serão enviadas para a Totvs e a pesquisa deste módulo não será exibida novamente até se completar um novo ciclo.
* **Lembrar mais tarde:** Sua resposta não será enviada e a pesquisa fechada. Na próxima vez que a tela for aberta, por exemplo a de Coligadas, a pesquisa será exibida novamente.

Atenção

Ao responder a pesquisa, observe o módulo que está sendo avaliado. Após selecionar uma nota, será exibido um campo para comentários:

Deixe registrado o que motivou a nota da resposta anterior, essa informação é muito importante para nossa melhora.

As regras de tempo para exibição de uma nova pesquisa podem variar entre os módulos do sistema.

**Marcando** a opção de aceitar compartilhar as informações, os campos **Nome e E-mail** do usuário que estiver respondendo a pesquisa serão armazenados junto com a resposta, assim será possível entrar em contato com o usuário para saber mais sobre a sua resposta.

**Não Marcando** a opção, **apenas** o **resultado da pesquisa** será enviado, onde não será possível saber o **Nome e o  E-mail** do usuário para que um possível contato seja realizado.

## **03. Pré-requisitos de rede**

É necessário que esteja liberado o acesso ao endereço: [nps-service-oficial.azurewebsites.net](http://nps-service-oficial.azurewebsites.net/), esta API é utilizada para registrar as respostas das pesquisas de NPS (Net Promoter Score) realizadas no sistema RM.
