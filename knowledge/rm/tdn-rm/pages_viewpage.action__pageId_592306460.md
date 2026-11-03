---
content_hash: 087aace3275be6a67067336937d854a86939e764371f812ed0ee0878493b3579
fetched_at: '2026-06-29T00:10:56.687544+00:00'
page_id: '592306460'
product: rm
source: tdn-rm
title: Solicitação de Exames na Prescrição médica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592306460
version: 14
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Grupos de exames**
4. **Indicação clínica (TISS)**
5. **Tabelas utilizadas**
6. **Impressão automática da solicitação de exames**

Solicitação de Exames na Prescrição médicaVisão Geral

## **01. VISÃO GERAL**

No prontuário eletrônico do paciente é possível realizar solicitações de exames dos tipos laboratorial ou imagem.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Acessar o menu lateral prescrição

Acessando o menu será possível visualizar os itens da prescrição, dentre eles os itens de solicitações de exames

Após o clique será exibido um painel para que seja inserida as informações sobre o exame

No campo de busca do exame digite o nome do exame desejado

Após selecionar o exame ele será exibido nas tabs disponíveis. O exame será visível sempre na tab de "Todos" e na tab referente ao o tipo laboratório ou imagem.

O checkbox **Replicar configurações** permite que os valores inseridos no cabeçalho sejam replicados para todos os exames selecionados.

É possível definir uma observação após clicar no checkbox "Obs", será exibido um campo de texto para digitação com limite de 2000 caracteres.

Após inserir todos os itens e clicar em incluir, o exame será adicionado e poderá ser visualizado no menu de exames.

É possível adicionar mais de uma opção para o mesmo exame. O sistema porém não permitirá que o mesmo exame seja lançado com as mesmas informações. Para tal, basta clicar no botão de adicionar.

É possível também selecionar o material para realização do exame.

As observações inseridas utilizando o checkbox "Obs" poderão ser visualizadas no RM através da tela de "Pedidos de exame".

Grupos de exames

## **03. GRUPOS DE EXAMES**

É possível também a realização da solicitação por grupos de exames. Onde ao selecionar um determinado grupo, todos os exames que compõem aquele grupo serão adicionados à solicitação.

Indicação clínica (TISS)

## **04. Indicação clínica (TISS)**

A partir da versão 12.1.2506, a página de prescrição médica do PEP passou por atualização visual e foi adicionada uma nova função, como a opção de definir a Indicação Clínica de uma determinada Solicitação de Exame:

Obs.: Como é possível incluir mais de uma Solicitação de Exame dentro da prescrição, somente a primeira indicação clínica inserida que será considerada e enviada para o RM.

Tabelas utilizadas

## **05. TABELAS UTILIZADAS**

| Campo | Descrição |
| --- | --- |
| JSOLICITACAOEXAME | Tabela da solicitação de exames |
| JSOLICITACAOEXAMEITEM | Itens da solicitação de exames |

Impressão automática da solicitação de exames

## **06. Impressão automática da solicitação de exames**

##### **Funcionalidade disponível a partir da versão 12.1.2510.**

Agora será possível configurar por meio de parâmetro, a impressão automática do relatório da solicitações de exame quando houver exames vinculados à liberação da prescrição.  
Com essa configuração habilitada em uma unidade de atendimento que não utiliza aprazamento e checagem, o relatório de solicitações de exames será gerado automaticamente ao **liberar a prescrição** ou ao **imprimir a liberação da prescrição** na tabela lateral de "Prescrições anteriores", desde que existam exames associados.

Na tabela lateral de "Prescrições anteriores", será impressa apenas a solicitação de exames referente à liberação selecionada.Ao clicar em imprimir no ícone da prescrição completa, o relatório individual da solicitação de exames não será gerado junto ao relatório principal com todos os itens da prescrição. Essa mesma regra também se aplica ao botão “Imprimir” localizado ao final da tela, que também realiza a impressão da prescrição completa e não gera o relatório individual da solicitação de exames.

Para unidades que utilizam aprazamento e checagem, o relatório da solicitação de exames não será gerado ao liberar a prescrição devido a necessidade de liberação do aprazamento para consolidar a data e hora da realização do exame.
