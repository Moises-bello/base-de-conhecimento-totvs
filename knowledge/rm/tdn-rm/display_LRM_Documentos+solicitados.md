---
content_hash: 2694c0e1f2e93121856c977f7a33e6291290605642256a06a93171d684aa8871
fetched_at: '2026-06-29T00:09:31.772357+00:00'
page_id: '425458715'
product: rm
source: tdn-rm
title: Documentos solicitados
type: documentation
url: https://tdn.totvs.com/display/LRM/Documentos+solicitados
version: 23
---

Este anexo do cadastro de alunos exibe **todos os documentos exigidos** para o aluno durante o processo de matrícula, permitindo o acompanhamento detalhado das pendências e entregas documentais.

Para conceder permissão de acesso a essa funcionalidade, acesse: **Educacional > Currículo e Oferta > Aluno e Professor > Documentos Solicitados**.

Nesta tela é possível realizar a **inclusão de um documento**, informando a **quantidade entregue** e a **data de entrega**, facilitando o controle e o registro das documentações apresentadas.

Para realizar o cadastro de um novo documento, acesse: **Currículo e Oferta > Acadêmico > Auxiliares > Documentos**.

Após o cadastro, é necessário **vincular o documento a um curso** por meio da tela de **Parametrização por Curso**, no anexo **Documentos Exigidos**, garantindo que ele seja considerado durante o processo de matrícula.

É possível incluir, alterar e visualizar um arquivo digital. Foi incluído na tela os botões para incluir/alterar e visualizar o arquivo vinculado ao aluno.

A inserção e baixa dos documentos obrigatórios do aluno deve ser feita por contexto.

No cadastro existe dois campos que são **situação do documento**e .

* **Situação do documento:** fornece 4 status para seleção, sendo que estes status irão indicar a entrega efetiva ou não do documento.
  + **Não entregue**: indica que o aluno **não**entregou o documento.
  + **Entregue em validação**: indica que o aluno entregou o documento, mas está em validação pela instituição.
  + **Recusado**: indica que o aluno até entregou o documento, mas foi recusado pela instituição, este status **necessita** informa um **motivo de rejeição**.
  + **Validado**: indica que de fato o aluno entregou o documento.
* **Motivo da rejeição do documento:** obrigatório informar caso o status for **recusado**, para os demais status este campo deverá ser vazio.

Para os status **não entregue**, **entregue em validação** e **recusado** o sistema entenderá que o documento não está válido, portanto não é considerado como entregue, com isso, será cobrado o mesmo. Apenas o status **validado**, que o sistema considera como entrega do documento.

Além disso existe as mensagens: Validado pela IA, Recusado pela IA e Validado Pela IA com necessidade de revisão humana , a mensagem é exibida através do  . Caso seja alterado o status manualmente as mensagens não são exibidas.

Caso a verificação do documento foi realizada pela IA é exibido o seu grau de Precisão. Essas configurações são realizadas no cadastro de [documento de IA](https://tdn.totvs.com/pages/editpage.action?pageId=944267825).

No cadastro, existem dois campos principais: **situação do Documento** e ..

### Situação do Documento

Esse campo disponibiliza quatro status possíveis, que indicam a condição da entrega do documento:

* **Não Entregue**: o aluno **não entregou** o documento.
* **Entregue em Validação**: o documento foi entregue, mas ainda está **em análise pela instituição**.
* **Recusado**: o documento foi entregue, mas **foi recusado** pela instituição. Neste caso, é **obrigatório informar o motivo da rejeição**.
* **Validado**: o documento foi entregue e **aprovado pela instituição**.

Somente o status **Validado** é considerado como entrega efetiva. Para os status **Não Entregue**, **Entregue em Validação** e **Recusado**, o sistema entende que o documento **não é válido** e, portanto, **continua sendo cobrado** do aluno.

### Motivo da Rejeição do Documento

Esse campo é de preenchimento **obrigatório** apenas quando a situação do documento for **Recusado**. Para os demais status, o campo deve permanecer **em branco**.

### Validação Inteligente Utilizando a Inteligência Artificial

Durante o processo de , podem ser exibidas as seguintes mensagens:

* **Validado pela IA**
* **Recusado pela IA**
* **Validado pela IA com necessidade de revisão humana**

Essas mensagens são exibidas automaticamente com base no resultado da validação realizada pela inteligência artificial. Caso o status do documento seja alterado **manualmente**, **as mensagens não serão exibidas**.

Se o documento foi validado por IA, também será exibido o **grau de precisão** da validação. Essas configurações são definidas no **cadastro de [documentos de IA](https://tdn.totvs.com/pages/editpage.action?pageId=944267825)**.

**Obs.** Para os documentos com status **Recusado**, mediante parametrização, será enviado automaticamente um e-mail, por meio da  [Central de Notificações](https://tdn.totvs.com/pages/viewpage.action?pageId=425458864) e do [eduCONNET](https://tdn.totvs.com/display/LRM/03.5+-+Cadastro+de+Mensagens), para o Aluno/Responsáveis informando quais documentos foram recusados e o motivo da recusa. Funcionalidade disponível a partir da versão 12.1.2506.128.

Tela depreciada

Esta tela é disponibilizada até a 12.1.2502.
