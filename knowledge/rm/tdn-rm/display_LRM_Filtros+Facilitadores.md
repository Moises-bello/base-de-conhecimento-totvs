---
content_hash: 88d69b07e756c26b93ad32803756a6b9b122119880a9811e3bafe5572a05a736
fetched_at: '2026-06-29T00:05:49.314137+00:00'
page_id: '1039512682'
product: rm
source: tdn-rm
title: Filtros Facilitadores
type: documentation
url: https://tdn.totvs.com/display/LRM/Filtros+Facilitadores
version: 9
---

### 1. Visão Geral

O componente de **Filtros de Pesquisa** do RM é uma ferramenta de consulta dinâmica que permite filtrar registros em visões de dados, processos ou relatórios. Ele atua como uma interface visual para a construção de cláusulas condicionais (SQL), facilitando a busca sem que o usuário precise conhecer linguagem de programação.

### 2. Elementos da Interface

### Propriedade:

Identifica o campo técnico na tabela do banco de dados que você deseja validar.

* **No RM:** Geralmente utiliza o nome físico da coluna (ex: , `IDMOV`, `NOMEFANTASIA`).
* **No Totvs Automação:** Você utilizará o nome da propriedade para mapear qual coluna o seu script deve selecionar no componente de filtro. No seu caso, o script deve buscar o item `CODUND`.

### Operador:

O **Operador** define a regra lógica de comparação. É o coração do filtro.

* **No RM:** O sistema traduz o texto selecionado (ex: "Igual") para um operador SQL.
* **No Totvs Automação:** Você deve parametrizar o operador de acordo com o tipo de dado. Se o teste for de "valor exato", use `Igual`. Se for uma busca com um dado parcial, use `Contém`.

  + *Exemplo:* Para testar se uma busca por nomes funciona, você trocaria o operador para `Contém` e o valor para parte de um nome.

### Valor:

O **Valor** é o dado de entrada (input) que servirá de comparação para a Propriedade.

* **No RM:** Pode ser um campo de texto livre, uma data ou uma lista fixa (Lookup).
* **No Totvs Automação:** Este é o campo que você irá informar para ser aplicado ao seu filtro.

### 3 - Formato dos filtros

No RM, o filtro do DataServer define quais registros serão retornados na consulta.  
Ele é informado como uma **string de condição**, semelhante a uma cláusula `WHERE` do SQL, porém sem `SELECT`, `FROM` ou joins.

## Tabela de formatos de filtro do DataServer (TOTVS RM)

Os filtros configurados no RM seguem o mesmo padrão quando utilizados no TOTVS Automação (TAT), mantendo a mesma estrutura, operadores e regras de aplicação.

| Categoria | Operador / Situação | Estrutura | Exemplo |
| --- | --- | --- | --- |
| Estrutura básica | Igualdade simples | `CAMPO = VALOR` | `CODCOLIGADA = 1` |
| Operadores | Igual | `CAMPO = VALOR` | `CODCOLIGADA = 1` |
| Operadores | Diferente | `CAMPO <> VALOR` | `CODSTATUS <> 'F'` |
| Operadores | Maior que | `CAMPO > VALOR` | `SALARIO > 2000` |
| Operadores | Menor ou igual | `CAMPO <= VALOR` | `IDADE <= 30` |
| Texto (String) | Igual | `CAMPO = 'VALOR'` | `NOME = 'JOÃO'` |
| Texto (String) | LIKE (contém) | `CAMPO LIKE '%VALOR%'` | `NOME LIKE '%JOÃO%'` |
| Numérico | Igual | `CAMPO = VALOR` | `ID = 123` |
| Data | Igual | `CAMPO = 'YYYY-MM-DD'` | `DATAADMISSAO = '2024-01-01'` |
| Data | Comparação | `CAMPO >= 'YYYY-MM-DD'` | `DATAADMISSAO >= '2024-01-01'` |
| BETWEEN | Estrutura básica | `CAMPO BETWEEN VALOR1 AND VALOR2` | `CODESCOLA BETWEEN 0 AND 5` |
| BETWEEN | Com data | `CAMPO BETWEEN 'DATA1' AND 'DATA2'` | `DATAADMISSAO BETWEEN '2024-01-01' AND '2024-12-31'` |
| Combinação | AND | `CONDICAO1 AND CONDICAO2` | `CODCOLIGADA = 1 AND CODFILIAL = 2` |
| Combinação | OR | `CONDICAO1 OR CONDICAO2` | `CODSTATUS = 'A' OR CODSTATUS = 'P'` |
| Combinação | Parênteses | `(COND1 OR COND2)` | `CODCOLIGADA = 1 AND (CODSTATUS = 'A' OR CODSTATUS = 'P')` |
| IN | Numérico | `CAMPO IN (V1,V2,V3)` | `CODFILIAL IN (1,2,3)` |
| IN | Texto | `CAMPO IN ('V1','V2')` | `CODSTATUS IN ('A','P')` |
| Nulos | IS NULL | `CAMPO IS NULL` | `DATASAIDA IS NULL` |
| Nulos | IS NOT NULL | `CAMPO IS NOT NULL` | `DATASAIDA IS NOT NULL` |
| Exemplo RM | Funcionários ativos | Combinação de filtros | `CODCOLIGADA = 1 AND CODSITUACAO = 'A'` |
| Exemplo RM | Busca por nome | LIKE | `NOME LIKE '%SILVA%'` |
| Exemplo RM | Data mínima | Comparação | `DATA >= '2025/01/01'` |

## Exemplos práticos no RM

Funcionários ativos:

`CODCOLIGADA = 1 AND CODSITUACAO = 'A'`

Busca por nome:

`NOME LIKE '%SILVA%'`

Registros a partir de uma data:

`DATA >= '2025/01/01'`

## Boas práticas

* Utilize apenas a condição de filtro, sem comandos SQL completos.
* Sempre use aspas simples para textos.
* Utilize parênteses para evitar ambiguidades em filtros complexos.
* Valide o filtro antes de usar em automações ou integrações.
