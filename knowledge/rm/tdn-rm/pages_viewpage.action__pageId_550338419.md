---
content_hash: e2741b435fc7070e84cd8cf34fb89f1f0e070691e0b5da05bca69b7f5f93ec02
fetched_at: '2026-06-29T00:10:43.820498+00:00'
page_id: '550338419'
product: rm
source: tdn-rm
title: FISCAL01-13171 DT Cópia do Cadastro de Código de Ajuste entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550338419
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Código de Ajuste |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13171 |

## **02. SITUAÇÃO/REQUISITO**

Criar o processo de cópia entre Coligadas para o cadastro de Código de Ajuste.

## **03. SOLUÇÃO**

Foi adicionado um novo processo no cadastro de Código de Ajuste para a realização de cópias entre Coligadas.

O sistema valida os registros pertinentes a outros cadastros da seguinte maneira:

* Fórmulas: A validação é realizada através do Código da Fórmula, caso uma Fórmula na Coligada de origem existir na Coligada de Destino, o processo realizará a cópia do registro;
* Processo Judicial: A validação é realizada através do Número do Processo, caso um Processo na Coligada de origem existir na Coligada de Destino, o processo realizará a cópia do registro.

Comportamento Esperado:

**Funcionalidade: Cópia de cadastro de código de ajuste por coligada**

**Cenário I: Cópia em que todas as lookups possuem correspondente na filial destino**

Dado que existem o mesmo código de fórmula de todas as fórmulas na coligada destino,

E existe um processo judicial com o mesmo número de processo na coligada de destino,

Ao executar o processo de cópia de um cadastro de código de ajuste por coligada,

Então o cadastro deve ser copiado para coligada destino com todas as lookups preenchidas

**Cenário II: Cópia em que todas as lookups NÃO possuem correspondente na filial destino**

Dado que NÃO existem o mesmo código de fórmula de todas as fórmulas na coligada destino,

E NÃO existe um processo judicial com o mesmo número de processo na coligada de destino,

Ao executar o processo de cópia de um cadastro de código de ajuste por coligada,

Então o cadastro deve ser copiado para coligada destino sem nenhuma das lookups preenchidas

**Cenário III: Cópia de cadastro já copiado e marcando a sobrescrita**

Dado que já existe o cadastro de código de ajuste na coligada destino,

Com o mesmo código de ajuste, aplicar em, registro, estado e descrição,

E foi marcada a opção de sobrescrita,

Ao executar o processo de cópia de um cadastro de código de ajuste por coligada,

Então o cadastro deve ser atualizado na coligada destino sem que para isso seja criado um novo registro

**Cenário IV: Cópia de cadastro já copiado e NÃO marcando a sobrescrita**

Dado que já existe o cadastro de código de ajuste na coligada destino,

Com o mesmo código de ajuste, aplicar em, registro, estado e descrição,

E foi NÃO foi marcada a opção de sobrescrita,

Ao executar o processo de cópia de um cadastro de código de ajuste por coligada,

Então o cadastro deve criar um novo registro
