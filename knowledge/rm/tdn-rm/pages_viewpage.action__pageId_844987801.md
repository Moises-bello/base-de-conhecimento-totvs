---
content_hash: 0c3767f27d633bfeb9fd0d324675bf5da6a09114abde709457b07f5d57a6929f
fetched_at: '2026-06-29T00:11:50.692502+00:00'
page_id: '844987801'
product: rm
source: tdn-rm
title: FISCAL01-22727 - Criar Processo Preencher os Parâmetros das Rotina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844987801
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Obrigações Acessórias =>Rotinas Fiscais => Processo => Parâmetros da Rotina |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-22727](https://jiraproducao.totvs.com.br/browse/FISCAL01-22727) |

## **02. SITUAÇÃO/REQUISITO**

Criação do processo Parâmetros da Rotina no cadastro da rotina.

## **03. SOLUÇÃO**

Inclusão do menu “Processo Parâmetros da Rotina” no cadastro da Rotina. Este menu possibilita a inclusão automática dos campos do Layout do Gerados de Saídas.

Os campos serão armazenados na tabela TPARAMETROSDAROTINA.

O campo Chave se refere ao Nome do campo no Layout.

O campo Valor se refere ao Valor do campo no Layout.

O campo Descrição se refere a descrição do campo no Layout.

Passo 1: Seleção do Layout desejado.

Após seleção do Layout o botão "Avançar" será habilitado, ao acioná-lo sistema apresenta tela para preenchimento dos campos.

Passo 2: Preencher os campos do Layout

Ao acionar "Executar" o processo será acionado e os campos e seus respectivos valores serão armazenados na base de dados.

OBS: Apenas serão armazenados os campos do Layout que possuírem ligação dos Parâmetros de Geração com o Contexto da Classe

Disponível à partir da biblioteca 12.1.2402
