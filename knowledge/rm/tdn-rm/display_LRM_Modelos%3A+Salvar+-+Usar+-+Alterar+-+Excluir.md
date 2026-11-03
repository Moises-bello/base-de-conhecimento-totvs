---
content_hash: 37e2a205f9d007cffd4d337a455a9dc8fb27c567962d104c1c234d01af4dda8a
fetched_at: '2026-06-29T00:10:31.944200+00:00'
page_id: '525013343'
product: rm
source: tdn-rm
title: 'Modelos: Salvar - Usar - Alterar - Excluir'
type: documentation
url: https://tdn.totvs.com/display/LRM/Modelos%3A+Salvar+-+Usar+-+Alterar+-+Excluir
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
   1. **Salvar modelo**
   2. **Usar modelo**
   3. **Alterar modelo**
   4. **Excluir modelo**

PainelVisão Geral

## **01. VISÃO GERAL**

Esta tela tem como objetivo apresentar para o usuário as funcionalidades de salvar e utilizar modelos do sistema.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

SalvarSalvar modelo

## **a. SALVAR MODELO**

Os modelos serão exibidos somente nas entidades (telas) correspondentes, por exemplo, um modelo de anamnese só aparecerá quando buscado na tela de anamnese, um modelo de evolução só aparecerá na tela de evolução.

* As telas que apresentam o botão "Salvar modelo" tem como objetivo registrar um modelo privado ou público para uso futuro.

* Ao clicar no botão "Salvar modelo", será exibido um modal para preencher as informações de nome do modelo, unidade de atendimento e privacidade do modelo:

a) **Nome**: campo para descrever o nome do modelo a ser salvo;

b) **Unidade de atendimento:** campo para selecionar uma ou mais unidades de atendimento vinculadas ao modelo. Caso nenhuma seja selecionada, o modelo é considerado vinculado a **todas**as unidades;

c) **Salvar modelo como público**: campo para definir a privacidade do modelo a ser salvo. O valor padrão é privado, ou seja, somente o usuário que cadastra poderá ver o modelo. Ao selecionar a opção público, todos os usuários poderão visualizar e utilizar o modelo; 

* Não é possível salvar um modelo com um nome já existente, caso tente realizar essa ação, ao clicar no botão "Salvar" será exibido na tela uma mensagem de alerta:

Usar Modelo

## **b. USAR MODELO**

Os modelos serão filtrados automaticamente pela unidade atual que o paciente do registro estiver.

* Esta tela tem como objetivo buscar os modelos salvos.

* Ao clicar no botão "Usar modelo", será exibido um modal com os modelos privados e públicos salvos no sistema.

1. **Abas "Meus Modelos" e "Modelos públicos":** o usuário poderá visualizar os modelos privados (salvos pelo mesmo usuário logado) e modelos públicos clicando sobre as abas;
2. **Campo "Buscar modelo":** o usuário poderá pesquisar o modelo através do campo de busca. A busca filtrará os dados pelo início, meio ou final do texto digitado.
3. **Selecionar:** ao clicar no botão "Selecionar" do modelo será exibido na tela o texto inserido no momento em que o modelo foi salvo, com a possibilidade do usuário alterar.

Alterar modelo

## **c. ALTERAR MODELO**

Somente o usuário que salvou o modelo poderá realizar alterações no mesmo.

* Opções de modelo: as opções de alterar e excluir serão exibidas ao clicar no ícone  no canto superior direito do modelo desejado.
* O ícone  só será exibido se for um modelo cadastrado pelo usuário logado.

* Ao clicar no botão "Alterar" , será exibido na tela o texto inserido no momento em que o modelo foi salvo, com a possibilidade do usuário alterar.

* Após finalizar a alteração, ao clicar no botão "Finalizar edição"  será exibido um modal para salvar a edição atual. O nome e a privacidade do modelo estarão preenchidos conforme o modelo original mas podem ser alteradas.
* Clique no botão "Salvar" para finalizar a edição.

* Caso o usuário tente navegar por uma das aletas laterais antes das alterações do modelo serem salvas, uma notificação é exibida na tela:

Excluir modelo

## **d. EXCLUIR MODELO**

* Esta funcionalidade tem como objetivo excluir um modelo salvo.
* Ao clicar no ícone  e no botão "Excluir", será exibido um modal solicitando confirmação para a exclusão.

* O modelo poderá ser excluído de duas formas: **"Sim"** para excluir em todas as unidades ou "**Não"** para excluir apenas na unidade atual. Após selecionar a opção desejada, clique no botão "Excluir" para efetuar a exclusão.

* Se o modelo for excluído com sucesso, o sistema apresentará uma mensagem de confirmação e retornará à lista, sem o modelo excluído.
