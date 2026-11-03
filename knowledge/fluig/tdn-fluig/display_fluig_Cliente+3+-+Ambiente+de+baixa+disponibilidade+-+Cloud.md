---
content_hash: f49212d4c07afd3c323016693c46639f4a6070652cc4a73deb396f682132b404
fetched_at: '2026-06-28T21:35:23.199204+00:00'
page_id: '244425503'
product: fluig
source: tdn-fluig
title: Cliente 3 - Ambiente de baixa disponibilidade - Cloud
type: documentation
url: https://tdn.totvs.com/display/fluig/Cliente+3+-+Ambiente+de+baixa+disponibilidade+-+Cloud
version: 12
---

# Índice

5true.\*ndicenone

# Dimensionamento em ambiente de baixa disponibilidade executando na Nuvem Totvs

Confira a seguir o exemplo de dimensionamento para ambiente de baixa disponibilidade executando em nuvem Totvs.

Este é um dimensionamento real executado em cliente. Os dados abaixo podem ser usados como exemplos e podem ser aplicados à qualquer banco de dados homologado pelo Fluig.

### Perguntas do formulário

| INDIVÍDUOS CADASTRADOS | | | |
| --- | --- | --- | --- |
| Informar a quantidade de indivíduos cadastrados para uso do Fluig: | | | 37 |
| ACESSOS SIMULTÂNEOS | | | |
| Informar a quantidade de indivíduos acessando o Fluig simultaneamente: | | | 15 |
| VIRTUALIZAÇÃO | | | |
| O cliente tem ambiente virtualizado para o servidor do Fluig? | | | Não |
| O cliente tem ambiente virtualizado para o banco de dados? | | | Não |
| BANCO DE DADOS | | | |
| Qual é o banco de dados a ser usado em produção? | | | Microsoft SQL Server 2012 ou superior |
| O banco de dados será migrado de uma versão Progress? | | | Não |
| Caso haja migração de um banco Progress, qual o tamanho? | | |  |
| ECM | | | |
| DOCUMENTOS | | | |
| Qual é a quantidade de documentos publicados na implantação? | | | 10 |
| Qual é a quantidade média de documentos que serão publicados/versionados por mês? | | | 50 |
| Indique o tamanho médio dos documentos que serão publicados. (O valor deve estar em Kbytes.) | | | 500 |
| Será usado o visualizador de documentos do Fluig? | | | Sim |
| BPM | | | |
| PROCESSOS | | | |
| Qual é a quantidade de definições de processos workflow a serem implantados? | | | 5 |
| Qual é a média de atividades relacionadas a cada processo workflow? | | | 5 |
| Qual é a quantidade média mensal de processos workflow iniciados? | | | 80 |
| Especifique a quantidade média de publicações via formulários por mês. | | | 10 |
| Especifique a quantidade de grupos de usuários que serão utilizados. | | | 10 |
| Especifique a quantidade média de usuários por grupo. | | | 6 |
| Existem processos de workflow integrados com ERP TOTVS ou de terceiros? | | | Sim |
| ANALYTICS | | | |
| ANÁLISE DE DADOS | | | |
| Será necessária a análise dos dados de documentos e processos? | | | Sim |
| Será necessária a análise dos dados de comunidades e usuários? | | | Sim |
| Especifique a quantidade de dashboards para visualização. | | | Sim |
| PORTAIS | | | |
| PORTAIS | | | |
| Existe alguma demanda de portais corporativos? | | | Não |
| Especifique a quantidade prevista de páginas de portais. | | | 0 |
| COLABORAÇÃO | | | |
| COMUNIDADES | | | |
| Serão criadas comunidades no Fluig? | | | Sim |
| As comunidades terão widgets que consumirão dados de ERPS? | | | Sim |
| Serão utilizadas galerias de vídeos nas comunidades ? | | | Não |
| Serão utilizadas galerias de imagens nas comunidades ? | | | Não |
| LMS | | | |
| APRENDIZADO | | | |
| Qual é a quantidade de treinamentos criados no Fluig? | | | Não |
| Qual é a quantidade de turmas criadas no Fluig? | | | Não |
| Qual é a quantidade de conteúdos de aprendizado que serão criados no Fluig? | | | Não |
| Qual é a quantidade média de matrículas ativas? | | | Não |
| Qual é a quantidade de usuários que serão alunos? | | | Não |
| AVALIAÇÕES | | | |
| Qual é a quantidade de questões que serão criadas no Fluig? | | | Não |
| Qual é a quantidade de avaliações que serão criadas no Fluig? | | | Não |
| Pretende aplicar avaliações para pessoas fora do Fluig? Se sim, qual é a frequência? | | | Não |

### Desenho lógico e definições de hardware
