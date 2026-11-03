---
content_hash: 769d01d9ac8597313aef2cb30c4db09e74eaabef8f2553588f938359133fd0ee
fetched_at: '2026-06-29T00:08:04.484089+00:00'
page_id: '235571918'
product: rm
source: tdn-rm
title: TTMRO1_DT_Outras_Deduções_Variáveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=235571918
version: 115
---

# Lançamento - Cálculo IR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional |
| **Módulo:** | Totvs Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Lançamento - Cálculo de IR | Serviço de cálculo de IRRF. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | * Cadastro Cliente Fornecedor | Cadastro Cliente Fornecedor. | | * Inclusão Lançamentos Financeiros | Serviço de Inclusão de Lançamentos Financeiros. | | * Cálculo Valor Líquido | Serviço de Cálculo do Valor Líquido. | | * Baixa de Lançamentos Financeiros | Serviço de Baixa de Lançamentos Financeiros | |
| **Cadastros Iniciais:** | Cadastro Cliente/Fornecedor, Cadastro de fórmulas |
| **Parâmetro(s):** | NA. |
| **Chamados Relacionados** | TTMRO1 |
| **Requisito (ISSUE):** | FINTRF000020 |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | Sql Server e Oracle. |
| **Tabelas Utilizadas:** | FCFO, FLAN, FLANHST |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Cadastro de Cliente/Fornecedor

1º. Criado novo campo (FORMULAVALDEDUCAOVARIAVEL) na tabela de cliente/fornecedor (FCFO), para cadastrar código da fórmula para o cálculo das “Outras Deduções Variáveis”.

2º. Modificado  o groupbox “Dados Relacionados ao IRRF”,  modificado para a inclusão do lookup de fórmula, associado ao novo campo.

Obs:  O lookup de fórmula para o novo campo fica visível somente se o cliente/fornecedor for pessoa física.

3º. Criado novo campo (VALORDEDUCAOVARIAVEL) na tabela de lançamentos (FLAN), para registrar o valor das “Outras Deduções Variáveis”.

Cálculo de Valor Líquido

4º.  O cálculo da fórmula será feito no serviço de cálculo do IRRF, pois esse serviço é chamado pelo valor líquido, inclusão de lançamento e baixa de lançamento. Assim o cálculo da formula fica centralizado no serviço de cálculo do IRRF.

OBS: O valor será cálculo sempre e somente na inclusão do lançamento financeiro independente da data base de geração do IRRF. Desta forma, para os demais casos o valor deverá ser buscado no novo campo criado na tabela FLAN.

5º. O cálculo do IRRF será executado conforme indicado abaixo:

a)      O valor será arredondamento com duas casas decimais.

b)      O contexto para execução da fórmula são os valores do lançamento (tabela FLAN) .

c)       O campo “Outras Deduções Variáveis” dos lançamentos que já houve retenção de IR no período devem ser somadas, da mesma forma como já ocorre para os campos “Valor Base IR”, “Valor IRRF” e “Valor INSS”.

Serviço de Inclusão de Lançamento

6º. O serviço de inclusão de lançamentos deverá gravar o valor das “Outras Deduções Variáveis”, da mesma forma como hoje já grava o valor do IRRF.

Cadastro de Lançamentos

7º. Na inclusão de lançamento a pagar, gerador de IRRF/PF, caso tenha uma fórmula definida para “Outras Deduções Variáveis” no cadastro de C/F, o botão de cálculo automático do Valor do IRRF deverá ficar desabilitado se o cliente/fornecedor pessoa física e tiver a fórmula cadastrada.

O comportamento deverá ser similar ao existente hoje para o valor líquido, que permanece desabitado até que o lançamento seja salvo.

8º. O mesmo requisito vale para o botão de cálculo definido no diálogo do IRRF.

Obs 1: O campo “Valor Dedução Variável” ficará visível somente se o cliente/fornecedor for pessoa física.

Obs 2: O campo “Valor dedução Variável” só fica habilitado caso o usuário edita o valor do IR. Assim o valor presente (informado ou não) no campo “Valor Dedução Variável” será usado no cálculo. E a fórmula cadastrada no cliente/fornecedor não será executada.

## Procedimento para Utilização

* *Descreva os procedimentos, passo a passo (caso de uso), que serão realizados pelos usuários para que a melhoria seja visualizada identificando as seguintes informações:*
* *Cadastrar uma formula que será utilizada para o cálculo do valor de outras deduções variáveis.*
* *No cadastro do cliente fornecedor que deve ter a formula executada, configurar o código da formula a ser utilizada.*
* *Ao incluir lançamentos a pagar gerador de IR, o cálculo do valor de outras deduções variáveis será feito no momento que o lançamento estiver sendo salvo.*

divs

divs
