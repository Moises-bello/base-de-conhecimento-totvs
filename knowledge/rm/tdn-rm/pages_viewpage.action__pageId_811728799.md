---
content_hash: 85702221dd4b7d841142cb5f40ef1b4ae7cb95b2262fdfbd1285e345c67abbb0
fetched_at: '2026-06-29T00:11:44.302180+00:00'
page_id: '811728799'
product: rm
source: tdn-rm
title: Configuração para Exames de Curva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=811728799
version: 3
---

## 

## **CONTEÚDO**

1. **Cadastro de tempos de curva**
2. **Pedido de exame de curva**
3. **Lista de Amostras da Curva**
4. **Métodos e Parâmetros de Exame**
5. **Resultados laboratoriais**

itensCadastro de Tempos de Curva

## **01. Cadastro de tempos de curva**

Em Cadastro > Unidades de Diagnóstico > Exames e Serviços selecione o exame desejado e abra o anexo Exame de Curva.

Ao adicionar tempos de curva **ATIVO** para o exame ele passa automaticamente a ser considerado um exame de curva.

Caso todos os tempos sejam desativados o exame passa a ser considerado um exame normal.

Pedido de Exame de Curva

## **02. Pedido de exame de curva**

Unidade Diagnostico > Pedidos de exame > Novo Exame

Para exames de curva irá aparecer a tabela **Tempos de Curva de Exame** onde o usuário pode incluir os tempos

cadastrados para o exame no pedido.

Caso nenhum tempo seja incluído, o exame se comporta como um exame normal.

Ao salvar um exame com múltiplos tempos, uma amostra será criada para cada tempo.

Lista de Amostras da Curva

## **03. Lista de Amostras da Curva**

Na tela de Resultados laboratoriais é possível ver a quantidade de amostras e o código delas.

Para exames de Curva a coluna **Número da Amostra** vem em vazia e a coluna **Qtde Amostra de Curva** indicará a

quantidade de amostras presente no pedido de exame.

Anexos > Lista de Amostras da Curva

Métodos e Parâmetros de Exame

## **04. Métodos e Parâmetros de Exame**

É necessário criar um método apropriado para o exame de curva que contenha os tempos de curva como parâmetros.

Ao criar o método, com um exame que seja um **Exame de Curva**, os parâmetros referentes aos tempos cadastrados para

o exame serão criados automaticamente.

É possível incluir novos parâmetros de Tempo de Curva, basta selecionar a **Propriedades > Tempo de Curva** e indicar

a qual **Tempo de Curva (min)** o parâmetro corresponderá.

Caso o usuário tente adicionar novos Tempos de Curva após a criação do método e parâmetros é emitida uma

mensagem lembrando da necessidade de adicionar o tempo novo nos parâmetros, caso não o faça a tela de resultado

não considerará o tempo novo se este for adicionado no pedido de exame.

Resultados Laboratoriais

## **05. Resultados laboratoriais**

Apenas os parâmetros de tempo de curva referentes aos tempos que foram incluídos no pedido de exame que

irão aparecer na tela de resultados e estes serão tratados como **obrigatórios**.

No exemplo abaixo apenas três tempos foram incluídos no pedido, apesar de possuir cinco parâmetros / tempos cadastrados.
