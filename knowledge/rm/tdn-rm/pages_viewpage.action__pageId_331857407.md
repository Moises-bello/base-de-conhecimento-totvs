---
content_hash: e7d76f3631aa0c744640423764a608dcc773f059afd99de6cc016ffd8a11697f
fetched_at: '2026-06-29T00:08:49.984570+00:00'
page_id: '331857407'
product: rm
source: tdn-rm
title: FINANCEIRO01-4112 Limite de isenção para os contribuintes com mais de 65 anos
  IRPF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=331857407
version: 4
---

# Geração de IRRF-PF

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Inclusão de Lançamentos.* | *Inclusão de Lançamentos* | | Baixa de Lançamentos | Baixa de Lançamentos |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Geração de IRRF-PF* | *Geração de IRRF-PF* | |  |  | |
| **Cadastros Iniciais:** | Fiscais - Valores Fixos |
| **Parâmetro(s):** | *Data Base para Geração do IRRF / PF* |
| **Tickets relacionados** | *<https://totvssuporte.zendesk.com/agent/tickets/1717616>* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4112> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *MS-SqlServer e Oracle* |
| **Sistema(s) Operacional(is):** | *MS-Windows* |

## Descrição

Sistema passa tratar dedução do IRRF-PF para pessoas com idade acima de 65 anos conforme legislação vigente (Lei 7.713.1988)

## Procedimento para Utilização

       1.            Acesse "Valores Fixos" no menu "Cadastro | Fiscais | Mais..." e definia valor para a Finalidade "Valor a Deduzir para funcionários maior que 65 anos" e o período de vigência

2.       Definir o campo complementar do cliente fornecedor no qual irá definir se é um Aposentado/Pensionista.

Obs. O nome do campo complementar deverá ser "APOSENTADOOUPENSIONI" do tipo "Lógico"

       3.            No cadastro de Cliente/Fornecedor a data de nascimento deverá está preenchida para que o calculo possa ser levado em consideração

4.       Definir se o cliente fornecedor é um Aposentado/Pensionista

       5.            O cálculo do imposto de renda pessoa física será verificado também se o CLI/FOR pessoa física tem mais de 65 anos, se positivo será necessário descontar o valor fixo existente na tabela de valores fixo. Este valor fixo deve possuir a finalidade "Valor a deduzir para funcionário maior que 65 anos".

Exemplo do cálculo:

Total de Vencimentos: R$ 10.480,39  
Contribuição Previdenciária: R$ 695,35  
Número de dependentes: 1 (valor a deduzir por dependente/2013 = R$ 171,97)  
Pensão alimentícia: R$ 293,78  
Dedução por idade (65 anos): R$ 1.710,78 (valor limite de isenção na tabela progressiva do ano vigente)

R$ 10.480,39 - R$ 695,35 - R$ 171,97 - R$ 293,78 - R$ 1.710,78 = R$ 7.608,51

Após as deduções, deve-se aplicar a alíquota e a a parcela a deduzir conforme tabela vigente no sistema

Obs.: Valores podem estar desatualizado com a tabela vigente
