---
content_hash: c0154a922e47b0fdc961491680fc6d1d47651bc5eecd5a583e84a8e6b93f019d
fetched_at: '2026-06-29T00:11:32.071493+00:00'
page_id: '744458598'
product: rm
source: tdn-rm
title: Oncologia - Checagem
type: documentation
url: https://tdn.totvs.com/display/LRM/Oncologia+-+Checagem
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Ações de Checagem**

Checagem1. Visão Geral

## **01. Visão Geral**

A Checagem de Oncologia é uma funcionalidade que permite aos usuários registrarem a administração de medicamentos nos pacientes em tratamento oncológico. Essa funcionalidade tem como objetivo garantir que o paciente receba o tratamento adequado e no momento certo, além de proporcionar um registro preciso das medicações administradas.

A checagem de oncologia permite que os usuários registrem o início e término da administração dos medicamentos, bem como adicionar observações relevantes sobre o tratamento. O campo para registrar observações não é obrigatório e pode ser utilizado para informar intercorrências, caso o paciente apresente alguma reação adversa durante a administração do medicamento.

2. Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Para acessar a funcionalidade de checagem, acesse o menu Oncologia → Quimioterapia.

Ao acessar a tela de "Quimioterapia" e selecionar o protocolo, fase e ciclo atual, serão listados os itens prescritos com o devido status.

**Para iniciar o processo de checagem** o item deverá estar com o status "Liberado" conforme imagem:

Ao clicar no ícone de checagem deverá ser aberto uma modal para realização da checagem.

Nesta modal, além de retornar as informações do item a ser checado, outros campos são exibidos para preenchimento:

* + Data/Hora Início: Data e hora do início da administração do medicamento.
  + Responsável: Este é um campo somente para leitura que exibirá o nome do último usuário a manipular o campo Data/Hora Início.
  + Data/Hora Término: Data e Hora do término da administração do medicamento.
  + Responsável: Este é um campo somente para leitura que será preenchido com a informação do último usuário a manipular o campo Data/Hora Término.
  + Houve Intercorrência?: Campo para indicar se houve ou não intercorrência durante administração do medicamento.
  + Motivo intercorrência: Campo de texto livre para informar quais intercorrências ocorreram durante a administração do medicamento. Caso a opção "***Houve Intercorrência?"*** esteja marcada, este campo passa a ser obrigatório e o usuário deverá fornecer uma descrição dessa(s) intercorrência(s).
  + Observações: Campo de texto livre para inserir observações relevantes sobre a administração do medicamento.

As ações disponíveis nesta modal são:

**Executar:**

Essa ação realiza a checagem e indica que a medicação foi administrada.

Para executar esta ação, é necessário que os campos de ***data/hora de início e término*** estejam preenchidos corretamente. Além disso, o status atual da checagem deve estar como ***rascunho*** ou a última checagem deve estar ***desfeita*** para que essa ação seja executada.

**Não Executar:**

Essa ação realiza a checagem e indica que a medicação não foi administrada.

O status atual da checagem deve estar como ***rascunho*** ou a última checagem deve estar ***desfeita*** para que essa ação seja executada. Além disso é obrigatório informar uma ***justificativa*** para não administração do medicamento.

**Fechar:**

Fecha o modal retornando para tela de listagem modificando o status da checagem para checagem iniciada (Rascunho).

**Desfazer:**

Essa ação desfaz as checagens anteriores. Também é necessário informar uma ***justificativa*** para desfazer a checagem realizada anteriormente. Após a confirmação, o medicamento ficará disponível para checagem novamente.

**Suspensão de um medicamento:**

Para suspender uma medicação, clique no ícone "X" do respectivo medicamento. Uma modal será exibida para confirmação e preenchimento de justificativa. O usuário poderá também suspender os itens associados ao medicamento marcando o respectivo checkbox, se necessário.

Após a suspensão, os itens suspensos ficarão riscados e com o ícone "S".

**AutoSave:**

Esta modal possui o recurso de autosave, que realiza as alterações ao parar de editar algum dado.

As checagem que estão como finalizadas (EXECUTAR/NÃO EXECUTAR) não poderão ser editadas.

3. Ações de Checagem

## **03. Ações de Checagem**

Após realizar as ações de checagem, o sistema fará algumas atualizações no ciclo da Quimioterapia:

a. Após todos os itens prescritos do dia no ciclo em questão estiverem com a checagem finalizada (EXECUTAR/NÃO EXECUTAR) o status do tratamento do dia do ciclo deverá ser atualizado para "Checagem Concluída".

Vale lembrar que tanto itens padrões prescritos quanto itens complementares são levados em consideração.

b. Caso alguma checagem seja desfeita, o status deverá ser novamente atualizado para "Checagem pendente".
