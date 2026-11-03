---
content_hash: 6d2915844c0fbcd107b0295e8a0273599885c0bd19aede45b9ef8f8160c41ffa
fetched_at: '2026-06-29T00:08:50.874046+00:00'
page_id: '334344259'
product: rm
source: tdn-rm
title: 1821566- RMSAU-1910- DT Ampliação do campo Identidade profissional do Prestador
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334344259
version: 2
---

# Campo Identidade profissional

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Saúde* |
| **Módulo:** | **Gestão Hospitalar** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro > Uso geral > prestador* | *SauCadGeralAction* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **faturamento para convênios*.* | ***faturamento para convênios*.** | | **registro de informações* cirúrgicas.* | ***registro de informações cirúrgicas*.** | |
| **Cadastros Iniciais:** | *Prestador* |
| **Tickets relacionados** | *1821566* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *RMSAU-1910* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | ***SQL SERVER® e ORACLE®*** |
| **Tabelas Utilizadas:** | *SZCADGERAL* |
| **Sistema(s) Operacional(is):** | ***Windows®*** |

## Descrição

Aumento do tamanho do campo  IDENTIDADEPROF (identidade profissional) na tabela de prestador para 15 caracteres, visto que alguns médicos possuem registros maiores do que 8 caracteres e a TISS limita o campo numeroConselhoProfissional a 15 caracteres.

## Procedimento para Utilização

* No cadastro de prestador, campo Número no grupo identidade profissional aceitará até no máximo 15 caracteres.

* Os locais do sistema onde o campo é apresentado irão conter os 15 caracteres.

* No arquivo xml do faturamento irá gerar a tag <ans:numeroConselhoProfissional> com o valor completo do campo.
