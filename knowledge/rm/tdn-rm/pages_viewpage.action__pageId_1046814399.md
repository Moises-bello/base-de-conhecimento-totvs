---
content_hash: 85e5f6ff1fdc5cc91d68ec06b2b50260f2c54b3b0aef7b76166f6dab656835e5
fetched_at: '2026-06-29T00:05:51.011123+00:00'
page_id: '1046814399'
product: rm
source: tdn-rm
title: Objeto de Negócio Folha Analítica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046814399
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**

## **01. V****ISÃO GERAL**

O objeto de negócio FopFolhaAnaliticaBusinessObject é o principal motor de dados para a conferência mensal da folha de pagamento. Ele consolida informações da ficha financeira, cadastrais e de movimentação, permitindo a geração da Folha Analítica em diversos níveis de quebra (Filial ou Centro de Custo).

* Módulo: Folha de Pagamento
* Time Responsável: Rotinas
* Principal Fonte de Dados: Procedure interna de processamento de folha (FopDSFolhaAnalitica).

## **02.  PARÂMETROS DE ENTRADA**

Ao utilizar este objeto no Smart View, os seguintes filtros podem ser aplicados para refinar os dados:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Mês/Ano Competência | Competência da Folha | Define o período de apuração dos eventos financeiros. |
| Tipo de Quebra | Centro de Custo / Filial | Define se os totais serão agrupados por Centro de Custo (Rateio) ou Filial. |
| Situação | Filtro de Status | Permite filtrar por situações específicas (A-Ativo, D-Demitido, F-Férias, etc). |
| Período | Filtro de Períodos | Seleção de períodos específicos da folha (Ex: Período 1, Período 2). |
| Fórmulas | Seleção de Fórmulas | Permite selecionar até 15 fórmulas para exibição de valores calculados customizados. |
| Bases | Seleção de Bases | Define quais bases de cálculo (FGTS, INSS, IRRF) serão demonstradas. |
| Eventos Zerados | Sim/Não | Define se eventos com valor R$ 0,00 devem constar no objeto. |
| Autônomos | Gestão Financeira/Externos | Define se deve importar dados de autônomos vindos do módulo Financeiro. |

## **03. Estrutura de Dados**

### Cabeçalho e Identificação

* CompanyName / CompanyCnpj: Dados de identificação da Coligada.
* CompanyLogo: Logotipo da empresa recuperado da tabela GIMAGEM.
* FinancialStatementMonth/Year: Mês e Ano de competência formatados.

### Dados do Funcionário e Financeiros

* Employeecode / Employeename: Identificação do colaborador.
* Events (Lista): Contém os Proventos (Earnings), Descontos (Discounts) e Bases de Envelope.
* Basescalclist (Lista): Bases de cálculo específicas selecionadas nos parâmetros.
* Totalslist / Formulalist: Totais gerais e resultados das fórmulas de cabeçalho.
* Totalnetreceivable: Valor líquido a receber (Proventos - Descontos).

### Agrupadores e Totais de Quebra (CCusto / Filial)

* CostCenterTot / BranchCodeTot: Listas de agrupamento que trazem totais de verbas e contadores de funcionários por unidade.
* SelfEmployed (Lista): Dados de autônomos rateados conforme a quebra selecionada.

## **04. Regra de Negócio**

1. Tratamento de Rateio: Se a quebra por Centro de Custo estiver ativa, o objeto utiliza a lógica de rateio para distribuir os eventos do funcionário proporcionalmente entre os centros de custo cadastrados.
2. Contadores de Movimentação: O objeto calcula automaticamente totais de:

* Admitidos/Demitidos: Baseado na data de admissão e demissão dentro da competência.
* Afastamentos: Contagem por situação (Militar, Doença, Maternidade, Acidente, etc).
* Rescisão Complementar: Identifica demitidos em períodos anteriores com movimentação na competência atual.

3. Ordenação: Suporta ordenação prioritária por Nome ou Chapa, respeitando sempre a hierarquia de Filial > Centro de Custo.
4. Envelopes de Retificação: Possui parâmetro específico para considerar ou desconsiderar envelopes de funcionários transferidos que sofreram retificação.
5. Data de Pagamento: Possui lógica de contingência para buscar a data de pagamento na tabela de funcionários caso o registro específico do envelope esteja nulo.

## **05. Exemplo de Utilização**

Este objeto é fundamental para:

* Fechamento Mensal: Conferência de totais de INSS, FGTS e IRRF por Filial.
* Análise de Custo: Verificação de gastos com pessoal rateados por Centro de Custo.
* Gestão de Autônomos: Consolidação de pagamentos feitos a prestadores de serviço externos integrados à folha.
