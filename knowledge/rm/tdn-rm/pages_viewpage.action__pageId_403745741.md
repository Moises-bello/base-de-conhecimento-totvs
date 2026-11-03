---
content_hash: 0434d0db203ab294d74e7ba80b3a21e3a7eabd4a4bc3a6b2ff129bea79170c6f
fetched_at: '2026-06-29T00:09:11.300432+00:00'
page_id: '403745741'
product: rm
source: tdn-rm
title: DT Razão e Balancete - Ajuste Automático Valores Financeiros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403745741
version: 6
---

# Ajuste automático dos valores financeiros existentes nos relatórios Razão e Balancete

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Contábil |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Relatório | Relatórios Razão e Balancete |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de contas | Planos de Contas Contábil | | Cadastro de contas gerenciais | Plano de Contas Gerencial | | Cadastro de centros de custo | Centros de Custo | | Inclusão de lançamentos | Lançamentos Contábeis | |
| **Cadastros Iniciais:** | Plano de Contas Paralelo  Contas Paralelas |
| **Parâmetro(s):** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1848>  <http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-2029> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Tabelas Utilizadas:** | CPARTIDA, CSALDOEXERCICIO, GFILIAL, GCOLIGADA, CCONTA, CGERENCIA, GCCUSTO, FCFO, CRATEIOPC, CRATEIOLC |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.22 |

## Descrição

1 - Relatório Razão

Foi adicionada, na aba campos, a opção "Ajustar tamanho automaticamente". Se ela estiver marcada o tamanho dos campos, que representam valor financeiro, serão ajustados. Após o ajuste, caso o número de caracteres extrapole o limite de caracteres da linha o tamanho da fonte será reduzido para, no mínimo, cinco. Se a fonte chegar a cinco e a quantidade de caracteres da linha for insuficiente, então o campo Complemento diminuirá para, no mínimo, 15 caracteres. Os caracteres em branco, que sobrarem após a última coluna do relatório, serão adicionados a direita do último campo que não represente valor financeiro. Caso essa condição não seja atendida as colunas não terão seu tamanho alterado.

Ex: Digamos que o relatório seja formado pelos campos Código, Complemento, Crédito, Débito e Saldo Atual. Os caracteres que sobrarem, após o campo Saldo Atual, serão movidos para a direito do campo Complemento.

Vale ressaltar que esta opção não está disponível para o relatório Razão Contábil Sintético.

2 - Relatório Balancete

Foi adicionada, na aba campos, a opção "Ajustar tamanho automaticamente". Se ela estiver marcada o tamanho dos campos, que representam valor financeiro, serão ajustados. Após o ajuste, caso o número de caracteres extrapole o limite de caracteres da linha o tamanho da fonte será reduzido para, no mínimo, cinco. Se a fonte chegar a cinco e a quantidade de caracteres da linha for insuficiente, então o campo Descrição diminuirá para, no mínimo, 9 caracteres. Os caracteres em branco, que sobrarem após a última coluna do relatório, serão adicionados a direita do último campo que não represente valor financeiro. Caso essa condição não seja atendida as colunas não terão seu tamanho alterado.

Ex: Digamos que o relatório seja formado pelos campos Código, Descrição, Movimento e Saldo Atual. Os caracteres que sobrarem, após o campo Saldo Atual, serão movidos para a direito do campo Descrição.

Vale ressaltar que esta condição não está disponível para os balancetes orçamentários.

## Procedimento para Utilização

1 - Acesse a aba campos do relatório razão e marque a opção "Ajustar automaticamente". Ainda nesta aba altere o tamanho dos campos, que representam valor financeiro, para 4.

2 - Execute o relatório e observe os campos que representam valor financeiro.
