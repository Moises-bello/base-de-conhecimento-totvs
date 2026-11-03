---
content_hash: 9c722eb357217bfb43f5e87c4d2a84ce0cbe49f87ccce6b5085aaeaaadee2e0e
fetched_at: '2026-06-29T00:11:28.650451+00:00'
page_id: '732688394'
product: rm
source: tdn-rm
title: Filtro de Eventos
type: documentation
url: https://tdn.totvs.com/display/LRM/Filtro+de+Eventos
version: 25
---

#f5f5f5#363636noneFiltro de Eventos

## **Conteúdo**



## **01. Visão GeralVisaoGeral**

O Anexo **Filtro de Eventos** será habilitado para o processo "**EFD-REINF"**.

Este formulário indicará quais Tributos e Naturezas de Rendimento serão gerados nos Eventos R-4010, R-4020 e R-4080 da Rotina EFD-REINF.

## **02. Campos do FiltroCamposDoFiltro**

O cadastro possui os seguintes campos:

* **Código Filtro** **Evento**- Campo interno do cadastro, preenchido automaticamente
* **Tipo Evento**: Selecionar qual evento será parametrizado: R-4010, R-4020 ou R-4080
* **Origem**: Fiscal\Financeiro

1. Financeiro: Serão selecionados os Lançamentos Financeiros incluídos no Gestão Financeira\Fluxus.
2. Fiscal: Serão selecionados os Lançamentos Fiscais incluídos no Gestão Fiscal\RM Liber.

* **Tipo Tributo**: Um campo de seleção onde é possível escolher o tipo do tributo.
* **Natureza Rendimento**: Abre o cadastro da Natureza de Rendimento. Para mais informações, clique [aqui](https://tdn.totvs.com/display/LRM/Natureza+de+Rendimentos)

## **03. Navegando na árvore de Filtro de EventosNavegando**

O cadastro de filtro de eventos é disponibilizado em forma de Árvore (TreeView). Sua visualização é parecida com do cadastro de CFOP.  
Para cadastrar todos os níveis da Árvore, siga os passos a seguir:

2true1Passo 1

Árvore vazia: Será permitido incluir um evento. Clique no botão de incluir.

Exemplo

Para incluir outros eventos, basta que nenhum item da árvore esteja selecionado. Para desfazer as seleções da árvore, basta clicar no botão de Atualizar.

2Passo 2

Após cadastrado um evento, será permitido incluir um tributo naquele evento. Para isso, selecione o evento e clique no botão de incluir.

Exemplo

O tributo virá com os campos cadastrados no evento bloqueados para edição. O único campo desbloqueado será o do tipo do tributo.  
Para incluir mais de um tributo seguido, basta clicar no botão de inserir do formulário.   
Para incluir mais tributos após fechar o formulário, basta selecionar o evento no qual se deseja incluir o tributo e clicar no botão de incluir.

3Passo 3

Para incluir uma Natureza de Rendimento, o caminho é parecido com a inclusão de um tributo no evento. Selecione o tributo no qual se deseja incluir a Natureza de Rendimento e clique no botão de incluir.

Exemplo

Neste nível, exceto pela natureza de rendimento - que será informada no cadastro - todos os outros campos estarão bloqueados para edição, inclusive o tipo do tributo.  
Também é possível incluir várias naturezas de rendimento em um tributo pelo formulário, clicando no botão de inserir, da mesma forma como é feito pelo tributo.   
  
As naturezas de rendimento que forem inseridas na árvore, cujo campo "Rendimento Isento/Não Tributável" estiver marcado, terão seu texto na cor azul.

Exemplo natureza isenta

Obs.: Não e permitido salvar registro neste Nível sem a Natureza de Rendimento.

## **04. Outras informaçõesOutrasInformacoes**

Informações

Disponível a partir da biblioteca 12.1.2205

Validações

Não é permitido cadastrar Evento com o mesmo Tipo de Evento e Origem.
