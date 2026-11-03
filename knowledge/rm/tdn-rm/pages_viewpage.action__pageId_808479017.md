---
content_hash: ba4c79f5c5b49398b27cc78949507e435922814f1bb95e4ce85cb82178e65008
fetched_at: '2026-06-29T00:11:44.021516+00:00'
page_id: '808479017'
product: rm
source: tdn-rm
title: Flag ciclo entre aplicações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808479017
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

Flag ciclo entre aplicaçõesVisão Geral

## **01. VISÃO GERAL**

Funcionalidade que permite ao usuário prescrever inalação com o término de uso vinculado a quantidade de ciclos.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

A funcionalidade poderá ser utilizada quando o profissional prescrever medicamentos administrados por via inalatória para um paciente. Exemplificando, uma inalação com horário de início às 9h, frequência de 12h em 12h para ser administrada em 3 ciclos de inalação de 15 em 15 minutos. Assim, os horários para administração seriam:

* + 1º administração de 3 ciclos -> 9h, 9h15 e 9h30.
  + 2º administração de 3 ciclos -> 21h, 21h15 e 21h30.

* No menu "Prescrição médica", copie ou inicie uma nova prescrição. No submenu de "Inalações", selecione a medicação, a apresentação e o volume. Para incluir a quantidade de ciclos a serem realizados marque a checkbox "Utilizar ciclo entre aplicações" e os campos "Quantidade de aplicações" e "Intervalo entre aplicações" serão incluídos no modal.
* O campo "Intervalo entre aplicações" filtra e exibe apenas as frequências cadastradas que estão dentro do intervalo de 60 minutos.

* A quantidade de ciclos deve ter início e fim dentro da prescrição, com a frequência que o usuário optar, não sendo possível repetir o aprazamento. Caso o profissional queira repetir o ciclo, é obrigatório realizar uma nova prescrição.
* Após preencher os campos "Quantidade de aplicações" e "Intervalo entre aplicações", serão exibidos no campo "Horários definidos" os horários sugeridos de acordo com a frequência e início definidos.
* É possível marcar a prescrição como "Se necessário" ou "A critério médico". Caso marque a checkbox "Se necessário", o campo "Condição" se torna obrigatório.

* Para finalizar, clique no botão "Incluir" > Será exibido na tela uma mensagem de confirmação:

* Para que a prescrição se torne vigente clique no botão "Liberar".
