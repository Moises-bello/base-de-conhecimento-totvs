---
content_hash: a4443db030083962271e3230550a6be993a53d74a7f78cac0024e5cbe3dd8fe9
fetched_at: '2026-06-29T00:05:51.052154+00:00'
page_id: '1046820109'
product: rm
source: tdn-rm
title: Objeto de Negócio Histórico Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046820109
version: 2
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Relatórios que Utilizam Esse Objeto de Negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio FopHistSalarialBusinessObject fornece o rastreio completo das alterações de remuneração dos colaboradores. Ele extrai dados da tabela de histórico salarial (PFHSTSAL), permitindo visualizar não apenas o salário atual, mas toda a progressão do funcionário ao longo do tempo, incluindo os motivos de cada alteração.

* Módulo: Folha de Pagamento
* Time Responsável: Rotinas

## **02.  PARÂMETROS DE ENTRADA**

Este objeto possui parâmetros específicos para controlar a profundidade do histórico e a visibilidade de dados sensíveis:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Coligada | Código da Empresa | Filtra os registros por uma coligada específica. |
| Filial | Unidade de Negócio | Filtra os funcionários vinculados a uma filial. |
| Departamento | Seção/Estrutura | Permite busca hierárquica por código de seção (via LIKE). |
| Centro de Custo | Classificação Contábil | Filtra funcionários alocados em centros de custo específicos. |
| Data do Filtro | Data de Corte | Retorna apenas alterações ocorridas a partir da data informada. |
| Cargo / Função | Estrutura de Cargos | Filtra a evolução salarial de cargos ou funções específicas. |
| Exibe Salário | Flag de Privacidade | Define se o valor numérico do salário deve ser retornado. |
| Exibe Histórico | Nível de Detalhe | Define se trará apenas o último registro ou o histórico completo. |

## **03.  Estrutura de Dados**

Os dados são retornados com base na entidade FopHistoricoSalarialBusinessObjectEntity.

### Identificação do Colaborador

* CompanyCode: Código da coligada.
* BranchCode: Código da filial.
* EmployeeCode: Chapa do funcionário.
* EmployeeName: Nome completo.
* EmployeeSituationCode: Código da situação atual (Ativo, Férias, etc).

### Dados da Alteração Salarial

* Salary: Valor nominal do salário na data do registro (sujeito ao filtro de exibição).
* ChangedDate: Data em que a alteração entrou em vigor (PFHSTSAL.DTMUDANCA).
* ReasonCode / ReasonDescription: Código e descrição do motivo da alteração (Ex: Promoção, Acordo Coletivo, Mérito).
* EmployeePaymentType: Tipo de recebimento (Mensalista, Horista, etc).

## **04. Regra de Negócio**

1. Tratativa de Banco de Dados: O objeto realiza conversões automáticas para filtros de data dependendo do dialeto do banco:

* SQL Server: Utiliza strings de data padrão ('yyyy-MM-dd').
* Oracle: Injeta a função TO\_DATE para garantir a integridade da consulta.

2. Segurança e Acesso: O objeto possui um atributo de segurança (RMSBusinessObjectSecurityAttr) vinculado ao código 812000680, garantindo que apenas usuários com permissão na ação de Histórico Salarial visualizem os dados.
3. Filtragem por Código Interno: Para parâmetros como *Tipo de Pagamento* e *Situação*, a lógica interna busca o CODINTERNO das tabelas globais (PCODRECEB e PCODSITUACAO), garantindo compatibilidade mesmo que as descrições sejam alteradas pelo usuário.
4. Imprime Histórico: Quando o parâmetro "Exibe Histórico" é definido como "Não" (Valor 2 no backend), o sistema prioriza o registro mais recente da evolução salarial para o período filtrado.

## **05. Exemplo de Utilização**

Este objeto é o componente base para:

* Relatório de Evolução Salarial: Análise de percentuais de aumento por departamento.
* Auditoria de Dissídio: Verificação se os reajustes sindicais foram aplicados corretamente nas datas retroativas.
* Planejamento Orçamentário: Consulta de bases salariais históricas para projeções futuras.

## **06. Relatórios que utilizam esse objeto de negócio**

* [FOPTRP0006 - Relatório de Histórico Salarial](https://tdn.totvs.com/pages/viewpage.action?pageId=802003513)
