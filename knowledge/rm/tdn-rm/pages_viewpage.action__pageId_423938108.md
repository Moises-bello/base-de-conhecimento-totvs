---
content_hash: 6bfb9a8d0f9dc8403d93f682dad20ef73686936fc84f42e7aa62eeceaa71c9c1
fetched_at: '2026-06-29T00:09:25.302138+00:00'
page_id: '423938108'
product: rm
source: tdn-rm
title: Estornar Itens não Cotados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938108
version: 9
---

Este processo poderá ser executado para atender os seguintes objetivos:

* Estornar os itens não cotados, ou seja, itens que não foram cotados e não darão continuidade no processo de compras.
* Estornar os itens restante que tiveram ordem de compra gerada de forma parcial.

Para executar o processo o usuário precisa selecionar a cotação que terá os itens estornados e clicar em "Estornar Itens Não Cotados" que se encontra dentro de "Processos" na tela de cotação.

Para visualizar este processo o usuário deverá ter permissão no perfil, na tag "Estornar itens não cotados"

Para itens não cotados que estão participando da cotação, ao realizar o processo será realizado a baixa da solicitação de compras.

Durante a execução do processo, para cada item selecionado serão aplicadas as seguintes rotinas:

* **Baixa da Solicitação de Compras**: Será realizada a baixa da solicitação de compra que possui o item em questão, a quantidade do item no movimento será alterada para 0 e serão executadas todas as rotinas parametrizadas no tipo de movimento.
* **Status da Cotação**: O campo Status de cada item selecionado será alterado para "Estornado". Caso não exista mais nenhum item com Ordem de Compra a ser gerada, a cotação será Concluída.
* **Estorno no TCOP** Caso a solicitação de compra tenha sido gerada através do módulo Obras e Projetos, o sistema será responsável por retornar o saldo estornado para o TCOP.

Pontos de Atenção

* Não será possível selecionar mais de uma cotação para a execução do processo.
* O processo estará disponível apenas para cotações com o status "Ordem de Compra Parcialmente Gerada".
* Na tela do processo serão exibidos apenas os itens ativos da cotação.
* Itens parcialmente gerados para Ordem (ns) de Compra também serão exibidos para serem estornados, pontos de atenção para estes itens:
  + Executar o estorno de um item parcialmente gerado, impossibilitará o **Cancelamento/Exclusão da Ordem Compra gerada**.
  + Essa operação também impossibilitará o Estorno do(s) item(s) da Ordem de Compra.
* Pelo menos um item deverá ser selecionado para a execução do processo.
* Não é possível estornar itens de cotações que estejam integradas ao Paradigma ou ClicBusiness.
