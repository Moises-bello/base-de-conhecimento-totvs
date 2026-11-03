---
content_hash: 073fec123ed7cb1b7251b6097b2cabe566127bb2f7998e48429355ad057dcf05
fetched_at: '2026-06-29T00:08:57.125698+00:00'
page_id: '353273424'
product: rm
source: tdn-rm
title: DT Lançamento associado ao CSRF que contém Natureza Orçamentária Financeira
  Definida no Tributo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353273424
version: 14
---

**Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cadastro de Lançamentos/Gerenciar Lançamentos | Cadastro de Lançamentos/Gerenciar Lançamentos |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro de Natureza Orçamentária/Gerenciar a Natureza Orçamentária | Cadastro de Natureza Orçamentária/Gerenciar a Natureza Orçamentária | | Cadastro de Tributos/Gerenciar Cadastro de Tributos | Cadastro de Tributos/Gerenciar Cadastro de Tributos | |
| **Cadastros Iniciais:** | Tributo; Natureza Orçamentária; Lançamento |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4327> |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server; Oracle |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | Windows. |

## Descrição

No Gestão financeira os lançamentos relacionados a tributos (gerados na baixa), serão carregados com o valor default do campo de natureza orçamentária do tributo cadastrado no Gestão Fiscal.

**Procedimento para Utilização**

É necessário que o lançamento de origem tenha natureza orçamentária financeira e centro de custo cadastrados no rateio, que os tributos (IRRF e CSRF) cadastrados no fiscal tenha o default de natureza orçamentária preenchido. Para cadastrar e/ou editar o (s) tributo (s) para vincular uma Natureza Orçamentária Financeira padrão verifique a documentação do Gestão Fiscal.

Na inclusão do lançamento financeiro do tributo (lançamento gerado pela baixa), caso informada, natureza orçamentária default para no tributo, o sistema fará a substituição dos campos em todos os rateios por centro de custo. Caso exista rateios de mesmo centro de custo e diferente natureza orçamentária, ao substituir, será agrupado os registros já que terão o mesmo centro de custo e natureza. Para lançamentos de origem que não tenha informado no rateio a natureza orçamentária, o sistema não irá preencher o campo para o lançamento gerado na baixa.

Natureza orçamentária do tributo:

Natureza orçamentária do lançamento de origem:

Natureza orçamentária do lançamento de tributo gerado na baixa:
