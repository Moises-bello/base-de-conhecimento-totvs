---
content_hash: 23bb742fc55b087bd3c24ba5802f0f45a9b673173fcb5e0f0b17bb0516dd4d21
fetched_at: '2026-06-29T00:05:51.035471+00:00'
page_id: '1046819577'
product: rm
source: tdn-rm
title: Objeto de Negócio Lista de Dependentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046819577
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**

## **01. V****ISÃO GERAL**

O objeto de negócio FopListaDependentesBusinessObject é focado na listagem detalhada de dependentes, agrupados por departamento. Ele possui lógicas internas para validar a elegibilidade ao Salário Família com base em múltiplos critérios (idade, vacinação e frequência escolar) e permite a filtragem por incidências fiscais específicas.

* Módulo: Folha de Pagamento
* Time Responsável: Rotinas
* Diferencial: Agrupamento automático por Seção e cálculo dinâmico de elegibilidade ao Salário Família.

## **02.  PARÂMETROS DE ENTRADA**

Os filtros deste objeto permitem refinar a lista tanto pelo funcionário quanto pelas características específicas do dependente:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Seção | Código da Seção | Filtra por código da seção (suporta busca por hierarquia via LIKE). |
| Matrícula | Chapa do Funcionário | Permite filtrar um ou mais funcionários específicos. |
| Incidência Sal. Família | Filtro de Elegibilidade | Filtra dependentes que têm ou não incidência de Salário Família. |
| Incidência IRRF | Filtro de IRRF | Filtra dependentes que têm ou não incidência de IRRF. |
| Situação | Status do Funcionário | Filtra pela situação cadastral (Ativo, Férias, etc). |
| Grau de Parentesco | Vínculo Familiar | Filtra por tipos específicos (Filho, Cônjuge, etc). |
| Imprime sem dependentes | Opção Sim/Não | Define se funcionários sem dependentes devem constar no agrupamento. |

## **03. Estrutura de Dados**

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
4. Envelopes de Retificação: possui parâmetro específico para considerar ou desconsiderar envelopes de funcionários transferidos que sofreram retificação.
5. Data de Pagamento: Possui lógica de contingência para buscar a data de pagamento na tabela de funcionários caso o registro específico do envelope esteja nulo.

## **05. Exemplo de Utilização**

Este objeto é fundamental para:

* Fechamento Mensal: Conferência de totais de INSS, FGTS e IRRF por Filial.
* Análise de Custo: Verificação de gastos com pessoal rateados por Centro de Custo.
* Gestão de Autônomos: Consolidação de pagamentos feitos a prestadores de serviço externos integrados à folha.

## **06. Relatórios que utilizam esse objeto de negócio**

* [FOPTRP0020 - Lista de Dependentes do Funcionário](https://tdn.totvs.com/pages/viewpage.action?pageId=968144925)
