---
content_hash: 4db2d916d6f19ca4051e651af36c281c8668f2e9d490ee47225286f822becae8
fetched_at: '2026-06-29T00:10:13.194784+00:00'
page_id: '454845529'
product: rm
source: tdn-rm
title: DT Lançamento Extemporâneo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454845529
version: 4
---

# Lançamento contábil extemporâneo

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Contábil |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastro | Lançamentos Contábeis |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Sped Contábil (ECD) | CtbSpedMod | | Lançamentos Contábeis | CtbLanData | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-2500> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Tabelas Utilizadas:** | CPARTIDA |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.24 |

## Descrição

A ECD autenticada somente pode ser substituída caso contenha erros que não possam ser corrigidos por meio de lançamento contábil extemporâneo. Para possibilitar a inclusão desses lançamentos a aba SPED Contábil, existente no cadastro de Lançamentos Contábeis, irá receber o campo Data Extemporânea.

Para facilitar seu preenchimento, a partir da inclusão da segunda partida, a Data Extemporânea será preenchida automaticamente com o valor do registro anterior.

Validações que envolvem esse campo:

* Todas as partidas que compõe o lançamento extemporâneo deverão ter o campo Data Extemporânea preenchido.
* A data extemporânea devera ser a mesma em todas as partidas do lançamento.
* Partidas originadas de outros módulos ou processos do sistema não poderão ter o campo Data Extemporânea preenchido.
* As partidas que possuírem o campo Data Extemporânea preenchido deverão ter o campo Tipo Geração alterado para Partida Extemporânea.

## Procedimento para Utilização

1 - No módulo contábil acesse o cadastro existente no menu Escrituração Contábil → Lançamento.

2 - Acesse a aba SPED Contábil, existente no cadastro de Lançamentos Contábeis.
