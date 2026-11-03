---
content_hash: 8731d435f233ce934b705bdcd1c7772f212f8535588ce0696c68360fec6ab852
fetched_at: '2026-07-02T19:24:24.255312+00:00'
page_id: '471941134'
product: protheus
source: tdn-tec
title: Correção - TCheckBox executa bLClicked ao finalizar janela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=471941134
version: 1
---

Correção - TCheckBox executa bLClicked ao finalizar janela

|  |  |
| --- | --- |
| Situação | O bloco de código bLClicked do componente TCheckBox pode ser executado espontaneamente ao fechar uma janela. |
| Ocorrência | Em determinadas situações onde o bloco de código TCheckBox:bLClicked é preenchido com um código que manipula o conteúdo da variável do bSetGet, o bLClicked é executado espontaneamente ao finalizar a janela do componente, por exemplo ao clicar no botão "Confirmar" de uma janela MVC. |
| Correção | Foi aplicada uma correção que evita a execução indevida do TCheckBox:bLClicked ao finalizar a janela. |
| Informações adicionais | * Referente ao chamado: 4808505 * Referente à ocorrência: MTEC-2431 e MTEC-2522 * Disponível em builds iguais ou superiores a 7.00.170117A - 17.3.0.7 |
