---
content_hash: 3640cee582ffa2516b659c4e8494b52bd6868bfe6be6cab21bb69f5d1d04c69b
fetched_at: '2026-06-29T00:08:22.182858+00:00'
page_id: '269081276'
product: rm
source: tdn-rm
title: Distribuição de Valor de Serviço IRRF-PJ
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269081276
version: 5
---

# VALOR SERVIÇO / INTEGRAÇÃO COM FINANCEIRO

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| ****Segmento Executor:**** | Construção e Projetos. | | |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Movimento | MovMovimentoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Lançamento Financeiro | FinLANAction | | | |
| **Chamado:** | Não se aplica. | | |
| **Requisito (ISSUE):** | CPMOV001-820. | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | Parâmetros Financeiro do Tipo de Movimento: <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Financeiro.aspx>  Lançamento Financeiro - Cálculo do IRRF e INSS: <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.CalculoIRRF-INSS.aspx> | | |

## Objetivo

Permitir que o usuário defina que o Valor do Serviço seja deduzido na primeira parcela do lançamento financeiro.

## Definição da Regra de Negócio

Será criado um novo parâmetro na tabela Tipos de movimento (TTMVEXT) para que seja definido será realizada a Distribuição dos Valores do Serviço (DISTVALORSERV) para o IRRF de Pessoa Jurídica.

Na etapa **Fin – Faturamento 5/6** será criado o parâmetro: **Distribuição dos Valores do Serviço.**

As opções deste parâmetro serão:

* **Rateio:** o valor do serviço utilizado será rateado para todas as parcelas do lançamento. Este será o valor default.
* **Primeira Parcela:** o valor do serviço será lançado na Primeira Parcela do lançamento.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Movimento | Alteração | Gestão de Estoque, Compras e Faturamento \ Compras \ Aquisição de Serviços | - |
| Lançamento Financeiro | Envolvida | Gestão de Estoque, Compras e Faturamento \ Compras \ Aquisição de Serviços \ Edição de Movimento \ Lançamentos \ Financeiro | - |

**Tabelas Utilizadas**

* TTMVEXT – Tipos de movimento.

## Procedimento para Utilização

1. No Gestão de Estoque, Compras e Faturamento, acesse **Compras \ Aquisição de Serviços**  
   O sistema apresenta a janela de Aquisição de Serviços (Gestão de Compras). Informe o Tipo de Movimento  e clique em OK.  
   O sistema apresenta a janela de Filtros - Aquisição de Serviços (Gestão de Compras). Selecione um filtro e clique em Executar.
2. Na janela de Movimento clique em Incluir.
3. No Cabeçalho informe os dados de Fornecedor, Nº do Movimento e Data de Emissão.
4. Em Integrações \ Financeira informe a Condição de Pagamento.
5. Em Itens inclua o serviço.
6. Confira os dados e confirme.

**Observação:** o cenário de utilização acima pode variar conforme a configuração do tipo de movimento utilizado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **BackOffice/Gestão de Estoque, Compras e Faturamento/Ambiente/Parâmetros/**Gestão de Estoque, Compras e Faturamento****. Na janela de **Assistente de Implantação de Processos** selecione ****04.06 - Gestão de Compras/04.06.07 - Aquisição de Serviços****. Selecione o tipo de movimento que será configurado e na **Etapa Fin - Faturamento 5/6**e configure o parâmetro **Distribuição do Valor de Serviço.**

 

## Dicionário de Dados

**Arquivo ou Código do Script:** /\*$Versao=NU.2016.12\_01\*/

|  |  |
| --- | --- |
| **Tabela** | TTMVEXT |
| **Campo** | DISTVALORSERV |
| **Tipo** | SMALLINT |
| **Tamanho** | 2 |
| **Valor Inicial** | NULL |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Distribuição dos Valores do Serviço. |
| **Help de Campo** | Define como será realizada a distribuição do IRRF-PJ do valor do serviço. Esta distribuição pode ser na primeira parcela ou rateada nas parcelas. |
