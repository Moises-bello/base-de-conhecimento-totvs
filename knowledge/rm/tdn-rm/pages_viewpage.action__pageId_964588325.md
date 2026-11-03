---
content_hash: 32b80707aff2d14d0e3426906a2844bf74a81e699e4febf8235f49617e4f5817
fetched_at: '2026-06-29T00:12:14.084229+00:00'
page_id: '964588325'
product: rm
source: tdn-rm
title: FISCAL01-26112 - R-4010 - Tag <tpIsencao> Inclusão da opção Diária de Viagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=964588325
version: 2
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD REINF - R4010 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26112 |

## **02. SITUAÇÃO/REQUISITO**

O cliente solicita a geração do evento **R-4010** para pessoa física com **isenção de origem financeira** , utilizando a tag <tpIsencao> com o valor **2 (Diária de Viagem)** .

## **03. SOLUÇÃO**

Inclusão da opção **Diária de Viagem** no campo Indicador de Isenção:

O campo se encontra em Dados Fiscais do Lançamento Financeiro.

Quando informado a opção Diária de Viagem o registro 4010 irá inserir o valor 2 na tag <tpIsencao>:

Disponível à partir da biblioteca 12.1.2410
