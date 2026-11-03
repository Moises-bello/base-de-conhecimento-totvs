---
content_hash: f1ecc261f7731a0b98da965445c5f5f4fbf992f0effeeaf51f364cda9c34a05d
fetched_at: '2026-06-29T00:11:03.219567+00:00'
page_id: '619754712'
product: rm
source: tdn-rm
title: Liberação da prescrição médica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=619754712
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Suspensão de itens sem PLT**

PainelVisão Geral

## **01. VISÃO GERAL**

Ao clicar em nova prescrição e realizar toda a prescrição para o paciente, que inicialmente terá os seus itens inseridos em forma de "rascunho/não liberados", será necessário tornar aquela prescrição vigente/válida para iniciar o tratamento do paciente de acordo com os itens inseridos na prescrição. 

Para essa rotina, é necessário informar na propriedade "hostName" o IP do servidor no arquivo config.json, conforme exemplo abaixo:

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

* Após iniciada uma nova prescrição e inserir ao menos um item na prescrição, que ficará como "rascunho/não liberado", habilita-se o botão de liberar a prescrição.

* Itens pendentes ou incorretos serão sinalizados pelo ícone em vermelho na listagem antes da liberação da prescrição. Ao expandir a lista, o item prescrito que apresenta alguma pendência para ser liberado estará com o nome da medicação e demais informações em vermelho.

* Ao clicar no item que necessita de ajustes será exibido na tela uma notificação descrevendo as alterações que devem ser preenchidas e os campos obrigatórios em vermelho.
* Após incluir as informações habilita-se o botão de "Atualizar":

* Após o ajuste e liberação da prescrição, os itens adicionados anteriormente como rascunhos se tornam vigentes/válidos, desabilitando inicialmente o botão de liberar.

* Neste momento, o sistema gera também a impressão da prescrição e requisição farmacêutica caso tenha sido configurada no RM. A impressão da prescrição médica também poderá ser solicitada pelo usuário através do botão de opções avançadas:

A requisição farmacêutica é impressa somente na liberação da prescrição e caso o RM esteja configurado para tal funcionalidade.

* A prescrição será incluída no menu de prescrições anteriores.

* Ao liberar uma prescrição médica no PEP RM, sendo que a unidade não utiliza o PLT, caso os itens liberados possuam em seu cadastro materiais agregados, estes deverão ser encaminhados na solicitação para a farmácia. Serão listados automaticamente nesta tela, os itens de materiais que estiverem vinculados aos cadastros dos itens da prescrição. Ex: seringa ou agulha que estiverem vinculados à um padrão de diluição no RM.
Suspensão de itens sem PLT

## **03. SUSPENSÃO DE ITENS SEM PLT**

* Após a liberação da prescrição, é possível que o usuário suspenda um ou mais itens da prescrição. Ao lado da descrição do item, na tela principal, existe o ícone para suspender individualmente. Caso o usuário opte por suspender, o item não é apagado da tela de prescrição, o mesmo fica sinalizado que está suspenso.

* Ao passar o mouse sobre um item suspenso, será exibido o responsável pela suspensão e o horário da suspensão.
* Itens suspensos serão representados pelo ícone em vermelho na listagem de prescrições anteriores.

* O usuário pode suspender todos os itens, clicando em opções avançadas e suspender todos.
