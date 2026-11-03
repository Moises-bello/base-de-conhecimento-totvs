---
content_hash: b1822c3cf06519b6ec223c46ef3ab1bf1c52f2f357028bc6080693e16834370e
fetched_at: '2026-06-28T21:35:23.165379+00:00'
page_id: '244425087'
product: fluig
source: tdn-fluig
title: Cliente 4 - Alta disponibilidade em servidor cliente
type: documentation
url: https://tdn.totvs.com/display/fluig/Cliente+4+-+Alta+disponibilidade+em+servidor+cliente
version: 15
---

# Índice

5true.\*ndicenone

# Dimensionamento em ambiente de alta disponibilidade executando em servidor cliente

Confira a seguir o exemplo de dimensionamento para ambiente de alta disponibilidade executando em servidor de cliente.

Este é um dimensionamento real executado em cliente. Os dados abaixo podem ser usados como exemplos e podem ser aplicados à qualquer banco de dados homologado pelo Fluig.

### Perguntas do formulário

| INDIVÍDUOS CADASTRADOS | | | |
| --- | --- | --- | --- |
| Informar a quantidade de indivíduos cadastrados para uso do Fluig: | | | Inicialmente 1300 com aquisições em 3 ondas. Onda 1 chegará a 9.000 usuários no Total, Onda 2 18.000 e Onda 3 23.000 usuários no total. Essas ondas acontecerão no prazo de 1 ano |
| ACESSOS SIMULTÂNEOS | | | |
| Informar a quantidade de indivíduos acessando o Fluig simultaneamente: | | | 1300 inicialmente, 5.000 Onda 1, 9.000 onda 2, 15.000 onda 3 |
| VIRTUALIZAÇÃO | | | |
| O cliente tem ambiente virtualizado para o servidor do Fluig? | | | Não |
| O cliente tem ambiente virtualizado para o banco de dados? | | | Não |
| BANCO DE DADOS | | | |
| Qual é o banco de dados a ser usado em produção? | | | MySQL 5.1 ou superior |
| O banco de dados será migrado de uma versão Progress? | | | Não |
| Caso haja migração de um banco Progress, qual o tamanho? | | |  |
| ECM | | | |
| DOCUMENTOS | | | |
| Qual é a quantidade de documentos publicados na implantação? | | | 12.000.000 na 1 onda e chegando a 120.000.000 na segunda onda |
| Qual é a quantidade média de documentos que serão publicados/versionados por mês? | | | 500.000 |
| Indique o tamanho médio dos documentos que serão publicados. (O valor deve estar em Kbytes.) | | | 1 MB |
| Será usado o visualizador de documentos do Fluig? | | | Sim |
| BPM | | | |
| PROCESSOS | | | |
| Qual é a quantidade de definições de processos workflow a serem implantados? | | | 5 |
| Qual é a média de atividades relacionadas a cada processo workflow? | | | 5 |
| Qual é a quantidade média mensal de processos workflow iniciados? | | | 5000 |
| Especifique a quantidade média de publicações via formulários por mês. | | | 5000 |
| Especifique a quantidade de grupos de usuários que serão utilizados. | | | 1.300 na 1 onda e 2.500 na segunda onda |
| Especifique a quantidade média de usuários por grupo. | | | 2 na 1 onda e 5 na segunda onda |
| Existem processos de workflow integrados com ERP TOTVS ou de terceiros? | | | Não |
| ANALYTICS | | | |
| ANÁLISE DE DADOS | | | |
| Será necessária a análise dos dados de documentos e processos? | | | Sim |
| Será necessária a análise dos dados de comunidades e usuários? | | | Sim |
| Especifique a quantidade de dashboards para visualização. | | | Sim |
| PORTAIS | | | |
| PORTAIS | | | |
| Existe alguma demanda de portais corporativos? | | | Sim |
| Especifique a quantidade prevista de páginas de portais. | | | 10 |
| COLABORAÇÃO | | | |
| COMUNIDADES | | | |
| Serão criadas comunidades no Fluig? | | | Sim |
| As comunidades terão widgets que consumirão dados de ERPS? | | | Não |
| Serão utilizadas galerias de videos nas comunidades ? | | | Sim |
| Serão utilizadas galerias de imagens nas comunidades ? | | | Sim |
| LMS | | | |
| APRENDIZADO | | | |
| Qual é a quantidade de treinamentos criados no Fluig? | | | 76 |
| Qual é a quantidade de turmas criadas no Fluig? | | | 10 |
| Qual é a quantidade de conteúdos de aprendizado que serão criados no Fluig? | | | 500 GB no total |
| Qual é a quantidade média de matrículas ativas? | | | 250 |
| Qual é a quantidade de usuários que serão alunos? | | | 250 |
| AVALIAÇÕES | | | |
| Qual é a quantidade de questões que serão criadas no Fluig? | | | 10 |
| Qual é a quantidade de avaliações que serão criadas no Fluig? | | | 5 |
| Pretende aplicar avaliações para pessoas fora do Fluig? Se sim, qual é a frequência? | | | Sim, bem esporadicamente. Talvez 2 vezes ao ano. |

### Desenho lógico

### Definições de hardware

---
