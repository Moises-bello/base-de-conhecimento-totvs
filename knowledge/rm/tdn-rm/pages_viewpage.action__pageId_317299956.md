---
content_hash: 9951c92ca15e87bd128f0a3662a02ce29a9199e5830e127c7b87bfd208ad1b93
fetched_at: '2026-06-29T00:08:46.459360+00:00'
page_id: '317299956'
product: rm
source: tdn-rm
title: 1450691 RMSAU-205 DT Texto/Valor Default para Parâmetro resultado de exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317299956
version: 3
---

# TEXTO/VALOR DEFAULT PARA PARÂMETROS DE RESULTADO DE EXAME

**Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | Controle de Pedido de Exames |
| **Cadastros Iniciais:** | Cadastro de exames, Cadastro de Métodos e Parâmetros |
| **Tickets relacionados** | 1450691 |
| **Issue:** | RMSAU-205 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Tabelas Utilizadas:** | SZLABPARAMEXAMES |
| **Sistema(s) Operacional(is):** | Windows® |

## **Descrição**

A melhoria consiste em definir um valor padrão para determinados parâmetros de exames. Caso o parâmetro tenha uma lista de possíveis valores (lookup), um dos valores deve ser selecionado como default.

## **Procedimento para Utilização**

1. Acesse o menu Cadastros / Unidades de Diagnóstico / Métodos e Parâmetros de Exames
2. Selecione o exame que possua parâmetros
3. Caso o parâmetro possua grupo de texto padrão, deve-se selecionar um dos valores possíveis

   Importante

   Ao informar um resultado padrão através da opção de "Grupo de Textos Padrões para Resultados" será necessário informar apenas um item por parâmetro.
4. Caso o parâmetro não tenha Grupo de Texto padrão para resultados, o usuário deve digitar o valor padrão
5. Faço o pedido de exames e inclua o exame alterado
6. Acesse o menu Unidades Diagnóstico / Controle de Pedido de Exames, selecione o pedido e exame solicitado
7. Ao preencher o resultado do exame, o sistema deve preencher automaticamente todos os parâmetros que possuírem valores padrão.
