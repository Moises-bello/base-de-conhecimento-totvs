---
content_hash: 57692a2ea837ca77b7586212a38c1a83d1667383c807b3cf7b0c9117673b2de0
fetched_at: '2026-06-29T00:05:51.071315+00:00'
page_id: '1046822284'
product: rm
source: tdn-rm
title: Objeto de Negócio Aniversariantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046822284
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros de Entrada (filtros)**
3. **Estrutura de Dados**
4. **Regra de Negócio**
5. **Exemplo de Utilização**
6. **Relatórios que Utilizam esse Objeto de Negócio**

## **01. V****ISÃO GERAL**

O objeto de negócio FopListAniversarioBusinessObject tem como finalidade extrair a relação de colaboradores aniversariantes. Ele utiliza os dados de nascimento armazenados na tabela de pessoas (PPESSOA) cruzando com as informações contratuais da folha de pagamento (PFUNC), permitindo filtragens por mês, idade e estrutura organizacional.

* Módulo: Folha de Pagamento
* Time Responsável: Rotinas

## **02.  PARÂMETROS DE ENTRADA**

Este objeto possui parâmetros específicos para controlar a profundidade do histórico e a visibilidade de dados sensíveis:

| Parâmetro | Descrição | Comportamento |
| --- | --- | --- |
| Mês | Mês do Aniversário | Filtra os aniversariantes de um ou mais meses específicos. |
| Coligada | Código da Empresa | Filtra os dados por uma coligada específica. |
| Situação | Status do Funcionário | Filtra por Ativos, Férias, Afastados, etc. |
| Tipo | Tipo de Funcionário | Filtra por categorias (Ex: Estagiário, Autônomo, Normal). |
| Filial | Unidade de Negócio | Restringe a lista a filiais selecionadas. |
| Idade | Faixa Etária | Filtra colaboradores que possuem idades específicas. |
| Departamento | Seção / Estrutura | Permite busca hierárquica por código de seção (via LIKE). |
| Exibe Salário | Privacidade | Define se o salário do colaborador deve constar no resultado. |
| Exibe C. Custo | Centro de Custo | Define a visibilidade da classificação contábil no objeto. |

## **03.  Estrutura de Dados**

Os dados são mapeados através da entidade FopListaDeAniversarianteBusinessObjectEntity:

* EmployeeName: Nome completo do colaborador.
* EmployeeCode: Chapa/Matrícula.
* BirthDate: Data de nascimento completa.
* EmployeeAge: Idade calculada dinamicamente.
* DepartmentName: Nome da seção/departamento atual.
* Salary: Valor salarial (condicionado ao parâmetro de exibição).
* CostCenterCode: Código do Centro de Custo.

## **04. Regra de Negócio**

1. Cálculo Dinâmico de Idade: O objeto realiza o cálculo da idade em tempo real, adaptando a função conforme o banco de dados utilizado:

* SQL Server: Utiliza DATEDIFF(YEAR, PPESSOA.DTNASCIMENTO, GETDATE()).
* Oracle: Utiliza TRUNC(MONTHS\_BETWEEN(SYSDATE, PPESSOA.DTNASCIMENTO) / 12).

2. Extração do Mês: A lógica de extração do mês de nascimento também é adaptativa:

* SQL Server: Função MONTH().
* Oracle: Função EXTRACT(MONTH FROM ...).

3. Segurança: O acesso aos dados é controlado pelo código de segurança 812000680, garantindo que apenas usuários autorizados no módulo de Folha de Pagamento possam gerar a lista.
4. Otimização de Leitura: Todas as consultas internas para carregamento de opções (*Options*) utilizam o dialeto NoLockStatment, evitando *deadlocks* em bases SQL Server com alto volume de movimentação.

## **05. Exemplo de Utilização**

* Este objeto é o componente base para:

  + Comunicados Internos: Listagem mensal para murais ou e-mails de felicitação.
  + Gestão de Brindes: Planejamento de compra de benefícios sazonais por idade ou unidade.
  + Auditoria Cadastral: Identificação de inconsistências em datas de nascimento ou idades críticas (menores de idade ou aposentadoria).

## **06. Relatórios que utilizam esse objeto de negócio**

* [FOPTRP0002 - Lista de Aniversariantes](https://tdn.totvs.com/display/LRM/FOPTRP0002+-+Lista+de+Aniversariantes)
* [FOPTRP0003 - Lista de Aniversariantes - Exportação Excel](https://tdn.totvs.com/pages/viewpage.action?pageId=791208936)
