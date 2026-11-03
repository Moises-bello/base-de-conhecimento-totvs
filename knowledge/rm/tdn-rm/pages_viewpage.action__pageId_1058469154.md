---
content_hash: 9358f37514895bfaf7f16d04b7ae4781ee9fdc3c83b3ed5349e511b79a489e7d
fetched_at: '2026-06-29T00:05:52.674213+00:00'
page_id: '1058469154'
product: rm
source: tdn-rm
title: Objeto de Negócio Demonstrativo Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058469154
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Relatórios que Utilizam esse Objeto de Negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio **FopContabilizacaoBusinessObject** tem como finalidade extrair os lançamentos contábeis gerados pela Folha de Pagamento. Ele permite a conferência detalhada de partidas dobradas (Débito e Crédito), Centros de Custo e Históricos, servindo como base para auditoria antes ou após a integração com o módulo Contábil.

* **Módulo:** Folha de Pagamento
* **Time Responsável:** Rotinas

## **02.  PARÂMETROS DE ENTRADA**

Este objeto possui parâmetros específicos para controlar a profundidade do histórico e a visibilidade de dados sensíveis:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Coligada | Código da Empresa | Filtra dados por uma coligada especifica |
| Lote | Código do Lote | Filtra um lote especifico |
| Mês Referência | Mês Contábil | Filtra os lançamentos pelo mês da data da partida |
| Ano Referência | Ano Contábil | Filtra os lançamentos pelo ano da data da partida |

## **03.  Estrutura de Dados**

Os dados são mapeados através da entidade **`FopContabilizacaoObjectEntity`:**

* **BatchCode (`CODLOTE`):** Identificador do lote contábil.
* **PeriodoData (`DATA`):** Data de competência do lançamento.
* **CompanyName / Cnpj:** Dados da coligada de origem.
* **BranchCode / BranchName:** Código e nome da filial do lançamento.
* **DebitAccount / CreditAccount:** Contas contábeis de Débito e Crédito.
* **Valor:** Montante financeiro do lançamento.
* **CostCenterCode:** Código do Centro de Custo associado.
* **HistoryDescription:** Texto descritivo do histórico padrão utilizado.
* **CompanyLogo:** Imagem da logo da coligada carregada dinamicamente.

## **04. Regra de Negócio**

* **Trava de Segurança de Filtro:** Para evitar buscas exaustivas que degradem a performance do banco de dados, o objeto exige que o usuário forneça o **Lote** ou o combo **Mês + Ano**. Se ambos os critérios forem preenchidos com **-1**, o objeto retorna uma lista vazia por segurança.
* **Filtro por Período:** Diferente de relatórios legados que filtram apenas por data inicial/final, este objeto utiliza funções nativas de extração (MÊS e ANO) sobre o campo PPARTIDA.DATA, permitindo que o usuário visualize o mês fechado independente do dia do lançamento.

## **05. Exemplo de Utilização**

Este objeto é o componente base para:

* **Conferência Pré-Integração:** Validação se os valores de provisão de férias e 13º salário estão nas contas corretas.
* **Relatório de Lançamentos por Lote:** Utilizado quando o RH gera lotes específicos para encargos mensais.

## **06. Relatórios que utilizam esse objeto de negócio**
