---
content_hash: b3c3a0c259452cd6a1746b0f058b36d95d51e6f71ba189d1819ad43e999c0a19
fetched_at: '2026-06-29T00:11:55.885534+00:00'
page_id: '864351337'
product: rm
source: tdn-rm
title: FISCAL01-23700 - Importação de XML com erro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864351337
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Fiscal |
| Processo | NFe |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-23700 |

## **02. SITUAÇÃO/REQUISITO**

1. Acessar o Módulo Gestão de Estoque, Compras e Faturamento;
2. Informar a Coligada 1 e Filial 53;
3. Selecionar o menu Compras >> Importação de Arquivo XML - Cadastro de XML;
4. Selecionar o registro de Identificador 50 referente à Chave de Acesso 31240821477534000264550020001539881215583294;
5. Acessar a opção Processos >> Inclusão de Movimentos através de XML - NF-e;
6. Clicar em NÂO para não buscar Pedidos Automaticamente;
7. O Sistema apresenta a mensagem:

**Erro de validação de instância: '4' não é um valor válido para TNFeInfNFeInfAdicProcRefIndProc.**

## **03. SOLUÇÃO**

Alteração na tag indProc para tipo string, dessa forma a tag poderá ser preenchida com qualquer valor, inclusive o 4 que apresentava erro.

Disponível à partir da biblioteca 12.1.2310
