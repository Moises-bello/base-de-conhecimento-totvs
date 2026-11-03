---
content_hash: c2f5657d0c35440f099d08d99690ff5e2af85cbf3ef06053114e70e3b6978232
fetched_at: '2026-06-29T00:09:10.520408+00:00'
page_id: '398755758'
product: rm
source: tdn-rm
title: DT Limite de isenção IRPF para contribuintes com mais de 65 anos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=398755758
version: 4
---

# Limite de isenção IRPF para contribuintes com mais de 65 anos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Inclusão de Lançamentos. | Inclusão de Lançamentos | | Baixa de Lançamentos | Baixa de Lançamentos |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Geração de IRRF-PF | Geração de IRRF-PF | |  |  | |
| **Cadastros Iniciais:** | Fiscais - Valores Fixos |
| **Parâmetro(s):** | Data Base para Geração do IRRF / PF |
| **Tickets relacionados** | <https://totvssuporte.zendesk.com/agent/tickets/3154904> |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7865> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | MS-SqlServer e Oracle |
| **Sistema(s) Operacional(is):** | MS-Windows |

## Descrição

Sistema passa tratar dedução do IRRF-PF para pessoas com idade acima de 65 anos conforme legislação vigente (Lei 7.713.1988)

## Procedimento para Utilização

* Acesse "Valores Fixos" no menu "Cadastro | Fiscais | Mais..." e definia valor para a Finalidade "Valor a Deduzir para funcionários maior que 65 anos" e o período de vigência:

* Marcar no cadastro do cliente/fornecedor o campo "Aposentado/Pensionista", disponível na aba "Identificação", abaixo do campo "Número de Dependentes":

* É importante lembrar que a data de nascimento precisará estar preenchida para que o sistema possa valer-se do cálculo diferenciado.
* No cálculo do imposto de renda pessoa física será verificado se o cliente/fornecedor pessoa física tem mais de 65 anos. Se positivo, será realizado o desconto do valor cadastrado na tabela de valores fixos. Este valor fixo deve possuir a finalidade "Valor a deduzir para funcionário maior que 65 anos".
* Para os clientes que já utilizavam o campo complementar "Aposentado ou Pensionista", toda a parametrização existente será migrada para utilização do novo campo, sem a necessidade de nova parametrização.

Exemplo do cálculo:

Total de Vencimentos: R$ 10.480,39  
Contribuição Previdenciária: R$ 695,35  
Número de dependentes: 1 (valor a deduzir por dependente = R$ 171,97)  
Pensão alimentícia: R$ 293,78  
Dedução por idade (65 anos): R$ 1.710,78

R$ 10.480,39 - R$ 695,35 - R$ 171,97 - R$ 293,78 - R$ 1.710,78 = R$ 7.608,51

Após as deduções, deve-se aplicar a alíquota e a a parcela a deduzir conforme tabela vigente no sistema.

Obs.: Valores acima podem estar desatualizados com a tabela vigente e servem apenas de exemplo prático.
