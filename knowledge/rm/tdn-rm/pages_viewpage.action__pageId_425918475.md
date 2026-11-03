---
content_hash: f0f15cffa0616c974168469a84bb88a3a69c272d0c76b8b1895de4b1a6124510
fetched_at: '2026-06-29T00:09:38.103269+00:00'
page_id: '425918475'
product: rm
source: tdn-rm
title: Mensagens de notificação - Testis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425918475
version: 12
---

Com intuito de otimizar o envio de mensagens, existe a central de notificações que permite ao usuário configurar o texto padrão do envio de e-mails para inscrição de candidato e resultado da prova.

O usuário poderá definir como será o formato do e-mail: HTML ou texto. Quando selecionado "HTML" o usuário poderá definir o padrão de e-mail utilizando diversos recursos como imagens, vídeos, tabelas, etc. Permite também estruturar o texto do e-mail através de recursos de formatação, entre outros itens.

Ao cadastrar a mensagem, poderá ser utilizadas tags predefinidas através do botão "Tags disponíveis", que serão substituídas por seus respectivos valores no momento do envio do e-mail.

Para o Totvs Avaliação e Pesquisa será possível cadastrar mensagem de envio de e-mail para:

* Informar aos inscritos em uma determinada prova sobre sua inscrição;
* Informar aos executores de uma determinada prova sobre o resultado da execução da prova;
* E-mail para executores com informações sobre final da avaliação do tipo pesquisa de opinião

Importante

Não será possível cadastrar mais de uma mensagem com o mesmo objetivo informado.

## **Parametrização e processo de envio**

Informar aos inscritos em uma determinada prova sobre sua inscrição

Para que a mensagem seja enviada, é necessário que o usuário marque o *checkBox*: Ativar envio por e-mail.

**Essa funcionalidade está disponível a partir do Patch: 12.1.2302.124.**

Essa mensagem permite enviar e-mail ( desde que que em seu cadastro possui e-mail parametrizado) para os candidatos sobre a sua inscrição em uma determinada prova.

Para enriquecer o conteúdo da mensagem , foram disponibilizadas novas TAGS no cadastro de mensagem, que serão substituídas por seus respectivos valores no momento do envio do e-mail.

Após parametrizar a mensagem, acessar o cadastro da Prova | Candidatos (selecionar o(s) candidato(s) e acessar | Processo | Enviar e-mail de inscrição

Após selecionar o processo, será aberto uma janela para que o usuário crie uma nova mensagem ou utilize alguma padrão (personalizada na etapa anterior).

Ao clicar, será substituído, a mensagem padrão previamente criada.

Clique em avançar, e selecione a opção: Envio.

Ao final do processo, será listado um log, contendo a informação:

* Total de e-mails processados
* Total de e-mails enviados
* Total de erros ( caso tenha).

Informar aos executores de uma determinada prova sobre o resultado da execução da prova

Essa mensagem tem como objetivo, enviar e-mail automático para o Executores da prova (E-mail parametrizado no cadastro da Coligada), que um determinando candidato finalizou a prova.

Opção de enviar por email

A opção para configurar o envio de e-mail é configurada através dos parâmetros do sistema. Saiba mais:

E-mail para executores com informações sobre final da avaliação do tipo: Pesquisa de opinião

Essa mensagem tem como objetivo, enviar e-mail automático para o Executores da prova (E-mail parametrizado no cadastro da Coligada), que um determinando candidato finalizou a prova do Tipo: *Pesquisa de Opinião*.

Opção de enviar por email

A opção para configurar o envio de e-mail é configurada através dos parâmetros do sistema. Saiba mais:
