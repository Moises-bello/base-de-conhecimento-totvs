---
content_hash: af81f1ff59a859f17bc480e978d995ec0f91959dcaa72070da2cf6be651ad362
fetched_at: '2026-06-29T00:12:02.759608+00:00'
page_id: '904057769'
product: rm
source: tdn-rm
title: Objeto de Negócio - Totalizadores de ISS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=904057769
version: 11
---

Conteúdo

Conteúdo

# 1. Visão Geral

O objeto de negócio ISS Lançamentos Totalizados retorna  a somatória dos dados dos lançamentos cadastrados dentro do período desejado agrupados por tipo de recolhimento e alíquota.  
Este objeto está disponível pela ferramenta "Smart View". Serão disponibilizados pelo TOTVS Compartilhamento relatórios, tabelas dinâmicas e visões de dados que utilizam este objeto, mas também há a possibilidade de criar recursos personalizados com este objeto de negócio.

Cabe lembrar que este objeto de negócio possui o controle de segurança por perfil o que significa que o usuário deve possuir permissão no item "Encerrar período de apuração" (Gestão fiscal | Obrigações principais | Apuração | Período de apuração | Encerrar período de apuração) para conseguir acessar relatórios, tabelas dinâmicas e/ou visões de dados que utilizem este objeto de negócio.

# 2. Relatórios Disponíveis no TOTVS Gestão Fiscal

## 2.1 Tabela Dinâmica

É possível ter várias perspectivas diferentes sobre suas informações ao vincular o objeto de negócio de Lançamentos à uma tabela dinâmica.

Exemplo de tabela dinâmica

## 2.2 Visão de dados

A visão de dados permite uma visualização mais detalhada e extensa de cada informação.

Exemplo de visão de dados

## 2.03 Relatórios

250

# 3. Campos do objeto de negócio

Atualmente, são disponibilizados os seguintes campos referentes aos lançamentos no objeto de negócio:

Tabela de campos

| Nome | Tipo | Coluna |
| --- | --- | --- |
| Tipo Recolhimento | Literal | DTRBITEM.TIPOTRIBUTACAO |
| Alíquota | Decimal | DTRBITEM.ALQTRB |
| Total do Valor Contábil (Documento) | Decimal | DLAF.VALORCONT (Calculado) |
| Total da Base de Cálculo | Decimal | DTRBITEM.BASETRN (Calculado) |
| Total do Imposto | Decimal | DTRBITEM.VALORTRB (Calculado) |

# 4. Outras informações

Há cinco parâmetros obrigatórios a serem preenchidos para retornar dados neste objeto de negócio, sendo eles:

* Código da coligada;
* Código da filial;
* Data inicial período;
* Data final período;
* Tipo do lançamento

Caso para a coligada informada o usuário não tenha permissão no perfil de segurança do TOTVS RM (item "Encerrar período de apuração" - Gestão fiscal | Obrigações principais | Apuração | Período de apuração | Encerrar período de apuração), na tentativa de execução do relatório será apresentado um erro característico denotando essa situação.
