---
content_hash: 59f0e67c898ff0fdc67ab15ad0bb3aa22ed49706721e9f00e63a602ae11a4296
fetched_at: '2026-06-29T00:10:21.721753+00:00'
page_id: '492711685'
product: rm
source: tdn-rm
title: FISCAL01-7846 DT Cadastro - Código de Atividade Econômica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=492711685
version: 8
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Cadastro - Código de Atividade Econômica |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-7846 |

## **02. SITUAÇÃO/REQUISITO**

CPRB - Apuração - Regime de Caixa

Implementação do Cadastro de Atividade Econômica para que seja informada a Alíquota a ser pelo Produto.

## **03. SOLUÇÃO**

Foi implementado o Cadastro de Atividade Econômica junto ao Log de Alteração de Alíquota.

**Tabelas:**

DATIVIDADEECONOMICA

 - Código da Atividade Econômica

 - Descrição

 - Alíquota

DLOGATIVIDADEECONOMICA

 - Alíquota

 - Data Fim Vigência

Vinculo do Código Atividade Econômica nos Dados Fiscais do Produto

**Regras:**

  - Campo Alíquota deve estar entre 0 e 100.

  - Quando a Alíquota for altera irá criar um registro no Log com a Alíquota anterior e a Data de Vigência igual ao dia anterior a alteração.

  - Não pode haver mais de um Log com a mesma Data Fim Vigência.
