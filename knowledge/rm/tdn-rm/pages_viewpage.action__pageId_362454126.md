---
content_hash: eb35e36904ba9d6d99b103e5d9819ee112f3dced2c5f82e391fdd46064086447
fetched_at: '2026-06-29T00:08:59.449706+00:00'
page_id: '362454126'
product: rm
source: tdn-rm
title: RMSAU-3276 Gerar apenas o XML de Honorários quando não houver outro lançamento
  na conta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=362454126
version: 2
---

# RMSAU-3276 Gerar apenas o XML de Honorários quando não houver outro lançamento na conta

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Condições contratuais com convênios | Parâmetros de Convenio |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Geração do XML de Faturamento | Faturamento com xml de terceiros | |  |  | |
| **Cadastros Iniciais:** | Condições contratuais com convênios |
| **Parâmetro(s):** | Não gerar XML de faturamento para o Hospital |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | RMSAU-3276 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle e SQLServer |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Não Gerar XML de faturamento para o Hospital

RmSaude > Cadastro > Faturamento > Condições Contratuais com Convenio

Aba Eletrônico Tiss 3

Selecionar Informações Específicas (Faturamento para Médicos)

Parâmetro: Não gerar XML de Faturamento para o Hospital

XMLs de terceiros:

* Guia de Honorário Individual (início do nome do arquivo com número 5)
* Guia de SPSADT (início do nome do arquivo com número 2)
* Guia do Hospital (início do nome do arquivo com o número 0)

Irá gerar apenas um arquivo XML com o faturamento para o médico
