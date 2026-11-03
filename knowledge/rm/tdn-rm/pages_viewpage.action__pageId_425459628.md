---
content_hash: dd441027d8059b607bb8614c2f196daddf0d4981d5cf83cb60014e728297fcb0
fetched_at: '2026-06-29T00:09:37.519041+00:00'
page_id: '425459628'
product: rm
source: tdn-rm
title: Alteração de Parâmetros do Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459628
version: 1
---

**Alteração de Parâmetros do Atendimento**   
Este processo tem como objetivo alterar os parâmetros do tipo de atendimento dos atendimentos selecionados na visão.   
Para realizar a alteração dos parâmetros, é necessário, selecionar o(s) atendimento(s) na tela de visão de atendimentos. Clicar em processos e selecionar a opção "Alteração de parâmetros do atendimento".   
É necessário observar algumas regras antes de alterar os parâmetros:

* Para execução deste processo deverá existir pelo menos um atendimento selecionado.
* Os campos de parâmetros apresentados vão depender da etapa em que o atendimento se encontra. As definições de campos invisíveis e somente leitura definidos no cadastro de etapas vão ser respeitadas. Ou seja, os campos definidos como invisíveis não vão ser exibidos e os campos somente leitura não vão poder ser alterados.
* Para execução do processo, o usuário deverá ser responsável ou chefe do atendente responsável pela ocorrência.
* O atendimento não poderá estar fechado. Ou seja, os atendimentos que estiverem com o status de Concluído Respondido, Concluído Confirmado e Cancelado, os parâmetros não podem ser alterados.
* Todos os atendimentos selecionados deverão estar no mesmo grupo e tipo de atendimento além de estarem na mesma etapa do fluxo.
* Caso exista algum atendimento sem tipo de atendimento selecionado, será apresentada uma mensagem informando a necessidade de preenchimento deste campo.
* Após a execução do processo os valores dos campos de parâmetros receberão os novos valores. Os campos de parâmetros que ficaram com valores em branco, irão permanecer com os valores antigos.  
  Esse processo pode ser executado pela tela de Visão de Atendimentos e pela tela de Pesquisa de Atendimentos.
