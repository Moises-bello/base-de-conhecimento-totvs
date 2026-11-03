---
content_hash: 32cbcc4241fdde857c63a14250a956bd8481e55d98bb464de071ee2cb9842e09
fetched_at: '2026-06-29T00:05:51.064046+00:00'
page_id: '1046822209'
product: rm
source: tdn-rm
title: Objeto de Negócio Turnover
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046822209
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Objetos que Utilizam  esse Objeto de Negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio FopTurnoverBusinessObject é uma ferramenta analítica voltada para a gestão estratégica de RH. Ele calcula os índices de rotatividade (Turnover) por filial, comparando o volume de admissões, demissões e transferências em relação ao quadro de funcionários ativos em um período determinado.

* Módulo: Folha de Pagamento
* Time Responsável: Rotinas
* Foco: Indicadores de desempenho (KPIs) de Recursos Humanos.

## **02.  PARÂMETROS DE ENTRADA**

Este objeto possui parâmetros específicos para controlar a profundidade do histórico e a visibilidade de dados sensíveis:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Data Início | Início do Período | Define a data base para contagem dos ativos antes do período. |
| Data Fim | Fim do Período | Define a data base para contagem dos ativos ao final do período. |
| Filial | Unidade de Negócio | Filtra os indicadores por uma ou mais filiais. |
| Seção | Departamento | Permite a análise de turnover em níveis hierárquicos específicos. |
| Matrícula | Filtro de Chapa | Permite isolar a análise para grupos específicos de funcionários. |

## **03.  Estrutura de Dados**

Diferente de objetos simples, este BO entrega uma lista de indicadores calculados para cada filial:

* Employeesactivesbefore: Total de colaboradores ativos antes da data de início.
* Newemployees: Quantidade de novos colaboradores admitidos no período.
* Turnoffemployees: Quantidade de colaboradores desligados no período.
* Employeestransferred: Volume de colaboradores que entraram via transferência (TipoAdmissao = 'T').
* Total: Saldo líquido do período (Admissões - Demissões).

### Taxas Percentuais

* Admissionturnover: Percentual de admissões em relação ao total de ativos ao final do período.
* Turnoffturnover: Percentual de desligamentos em relação ao total de ativos ao final do período.
* Transferturnover: Percentual de transferências em relação ao total de ativos.
* Currentturnover: Índice de turnover médio do período (Média entre Admissões e Demissões dividida pelo total de ativos).

## **04. Regra de Negócio**

1. Lógica de Duplicação de Registro: Se um funcionário for admitido e demitido dentro do mesmo período solicitado, o sistema duplica virtualmente o registro em memória: um para contabilizar como admissão e outro como desligamento, garantindo que as duas movimentações afetem os índices.
2. Validação de Situação no Período: O objeto executa o método ValidaSituacaoFuncionarioNoPeriodo para filtrar apenas quem teve movimentação real (Admissão ou Demissão) entre as datas informadas, ignorando registros estáticos que não impactam a rotatividade.
3. Tratamento de Aviso Prévio: O campo Advancenotice é formatado dinamicamente para classificar o tipo de saída:

* Indenizado: TemAvisoPrevio = 1.
* Descontado: DescontaAvisoPrevio = 1.
* Trabalhado: Possui DataAvisoPrevioTrabalhado.
* Misto: AvisoMisto = 1.

4. Cálculo de Ativos: O sistema realiza subqueries em tempo real para contar os ativos em três momentos distintos (Início, Durante e Fim do período) para servir de denominador nas fórmulas de porcentagem.

## **05. Exemplo de Utilização**

Este objeto é essencial para:

* Dashboards de RH: Visualização mensal da saúde de retenção da empresa.
* Auditoria de Custos: Identificar filiais com alta rotatividade que geram custos excessivos de rescisão e treinamento.
* Relatórios de Diversidade em Movimentações: Análise de gênero e raça nas entradas e saídas.

## **06. Relatórios que utilizam esse objeto de negócio**

* [FOPTRP0021 - Relatório de Admitidos e Desligados - Turnover](https://tdn.totvs.com/pages/viewpage.action?pageId=977835958)
