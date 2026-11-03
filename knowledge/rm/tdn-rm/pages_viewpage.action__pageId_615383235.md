---
content_hash: 0388d0b9e5d8792797de32b469a423981cf4a12ea2589dbe25a5ea90c4acf7f9
fetched_at: '2026-06-29T00:10:59.710365+00:00'
page_id: '615383235'
product: rm
source: tdn-rm
title: Cópia de prescrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=615383235
version: 11
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

PainelVisão Geral

## **01. VISÃO GERAL**

Funcionalidade que permite ao usuário a realização da cópia da prescrição.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

No menu de prescrição, caso o usuário não possua uma prescrição vigente, ou que possua, porém esteja dentro do horário de corte definido no cadastro da unidade no RM, o sistema permitirá a realização da cópia da prescrição.

O sistema permitirá copiar prescrições anteriores e/ou vigentes, desde que obedeça a regra citada anteriormente.

O usuário poderá copiar acessando a prescrição através do menu de prescrições, onde terá o histórico de todas as prescrições realizadas para aquele paciente. Onde basta o usuário clicar na prescrição que deseja copiar e clicar no botão de copiar prescrição.

Ao clicar no botão "Copiar prescrição" será exibido na tela todos os itens prescritos **(exceto itens com dose única)**. Todos os itens são automaticamente assinalados para cópia e o usuário tem a opção de desmarcar o que não será copiado (exceto item antibiótico após finalização do uso).

Caso a prescrição não possua itens elegíveis para cópia, será exibida uma mensagem informativa. Um exemplo de item que não pode ser copiado são os itens de dose única.

Ao realizar cópia de uma prescrição com antibiótico que finalizou tempo de uso, este não estará assinalado e será exibido em vermelho e com a sinalização de um ícone de calendário ao final.

Ao realizar a cópia, será gerada uma nova prescrição a partir da selecionada anteriormente. A mesma estará em forma de rascunho e dependerá da liberação do usuário para ficar vigente.

O usuário poderá incluir outros itens normalmente, conforme padrão do sistema.

Os horários que ficarão definidos para os itens com frequência e início definidos serão os calculados de acordo com o último horário da prescrição de origem da cópia, caso configurado a rotina de horário padrão os horários fixos também irão ser copiado para nova prescrição.

Parametrização para que ao realizar a cópia da prescrição os novos horários de aprazamentos sejam gerados a partir do último horário e de acordo com a frequência selecionada.  
Ou seja, mesmo que os aprazamentos do item original possuam horários específicos (diferentes do intervalo da frequência), ao realizar a cópia, todos os novos horários serão recalculados de acordo com o intervalo da frequência, tendo início a partir do último horário de aprazamento do item original.
