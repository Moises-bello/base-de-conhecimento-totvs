---
content_hash: e6a37ac000080ea2de11e6f464cd67d893f8df7ff1e752141cabb6477b004a63
fetched_at: '2026-06-29T00:08:33.476220+00:00'
page_id: '274321882'
product: rm
source: tdn-rm
title: DT DDA - Importação do Nome do Fornecedor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274321882
version: 9
---

# Importação do Nome do Fornecedor

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção & Projetos* |
| **Módulo:** | **TOTVS Gestão Financeira** |
| **Requisito/S****tory/Issue:** | *FINANCEIRO01-697* |

## Descrição

Esta implementação tem como objetivo apresentar no processo de "Conciliar Títulos em Cobrança" e na visão de "DDA - Débito Direto Autorizado" a coluna "Fornecedor" com a descrição contida no arquivo importado.

### Objetivo

Permitir que o usuário visualize o Nome do Fornecedor descrito no arquivo de captura.

**Tabela Utilizada**

* FCAPTURACOB - Captura de Títulos em Cobrança

**Procedimento para Configuração**

No Totvs Gestão Financeira, acessar o Banco e preencher as posições do "Layout Bancário" do DDA, referente ao campo **inicial** e **final** do "Nome do Fornecedor" utilizado para captura de títulos em cobrança.

**Procedimento para Utilização**

* Acessar o menu de Movimentações Bancarias | DDA - Débito Direto Autorizado, executar o processo de Conciliar Títulos em Cobrança, a tela apresenta a coluna "Fornecedor" com a descrição informada no arquivo importado.

* Acessar o menu Movimentações Bancarias | DDA - Débito Direto Autorizado, na visão possui a coluna "Fornecedor" com a descrição do arquivo capturado.

**Obs:** A coluna Fornecedor da visão de DDA e do processo de Conciliar é preenchida com as informações contidas nas posições informadas no layout bancário, sem nenhum vinculo com o Cliente/Fornecedor do Lançamento.
