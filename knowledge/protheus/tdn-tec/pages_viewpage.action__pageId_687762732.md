---
content_hash: 53d7436e511c354a07455d2c9af3965f8ff698c14a982d72af8eab71e054995b
fetched_at: '2026-07-02T19:24:27.888606+00:00'
page_id: '687762732'
product: protheus
source: tdn-tec
title: Consolidação de Resultados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=687762732
version: 4
---

Ao ligar esse recurso, ao final dos testes os resultados de cobertura serão persistidos em SQLite, portanto podem ser consultados posteriormente, basta apenas acessar as tabelas descritas abaixo:

> Importante ressaltar que o **PROBAT** somente registra a última execução de cobertura de código em SQLite.

### Tabelas no SQLite

Possuímos 3 (três) tabelas contendo dados de cobertura dos fontes.

| Nome tabela | Descrição |
| --- | --- |
| PROBAT\_CODECOVERAGE\_TOTAL | Percentual Total de cobertura sumarizado por todos os fontes |
| PROBAT\_CODECOVERAGE\_SOURCES | Percentual Total de cobertura por fonte |
| PROBAT\_CODECOVERAGE\_LINES | Informação linha a linha por fonte sobre a cobertura |

Abaixo, podemos ver a estrutura de cada tabela.

##### PROBAT\_CODECOVERAGE\_TOTAL

| Campo | Tipo | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código interno da execução dos testes |
| SOURCES | N | Quantidade TOTAL de fontes percorridos pela Cobertura |
| LINES | N | Quantidade TOTAL de linhas percorridos pela Cobertura |
| COVERAGE | N | Percentual TOTAL de Cobertura, considerando fontes oficiais e testes |
| COVERAGE\_FRAME | N | Percentual TOTAL de Cobertura de SOMENTE dos fontes oficiais |
| COVERAGE\_TEST | N | Percentual TOTAL de Cobertura de SOMENTE dos fontes de testes |

##### PROBAT\_CODECOVERAGE\_SOURCES

| Campo | Tipo | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código interno da execução dos testes |
| RUN | C | **0** = Fonte não foi executado durante os testes, **1** = Fonte foi executado |
| CODE\_SRC | N | Código interno do fonte oficial |
| CODE\_TST | N | Código interno do fonte de teste |
| SOURCE | C | Nome do fonte |
| LINES | N | Quantidade total de linhas do fonte |
| COVERAGE | N | Percentual de Cobertura para esse fonte |

##### PROBAT\_CODECOVERAGE\_LINES

| Campo | Tipo | Descrição |
| --- | --- | --- |
| CODE\_EXEC | C | Código interno da execução dos testes |
| CODE\_SRC | N | Código interno do fonte oficial |
| CODE\_TST | N | Código interno do fonte de teste |
| SOURCE | C | Nome do fonte |
| LINE | C | Número da linha |
| COVERAGE | N | Cobertura: **-1** = Linha não Debugável, **0** = Não executou a linha, **>0** = Quantidade de vezes que executou a linha durante os testes |
| CHANGE | C | Em algum momento o appserver trocou a informação se a linha é ou não debugável, indicando bug, sendo: **0** = Comportamento Correto, **1** = Bug |

### Conclusão

Como podemos observar, temos informações com diversos espectros para análise da Cobertura de Código de nosso projeto, portanto:

Considerando a tabela *PROBAT\_CODECOVERAGE\_TOTAL*, conseguimos ter uma visão sintética da Cobertura de forma geral, obtendo os percentuais: Total (todos os fontes), Total por Fontes Oficiais e Total por Fontes de testes, nos possibilitando tomar algumas decisões automatizadas.

Ao olhar para a tabela *PROBAT\_CODECOVERAGE\_SOURCES*, temos uma visão intermediária entre a sintética e a analítica, nos possibilitando enxergar a cobertura de código por cada fonte de nosso projeto, seja ele oficial ou de teste.

Agora, quando olhamos para a tabela *PROBAT\_CODECOVERAGE\_LINES* temos a visão analítica de cada fonte, nos dando a possibilidade de saber linha a linha de todos os nossos fontes, se foram ou não executadas. Assim, podemos melhorar nossos fontes oficiais e também os testes para aumentar a qualidade e/ou cobertura, ou descobrir implementações dos fontes oficiais que são desnecessárias ou inalcançáveis.
