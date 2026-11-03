---
content_hash: 288300d50ab17671791566506f0bf114eadc0ff313ac62b210264085af4ac23b
fetched_at: '2026-06-28T21:35:23.173900+00:00'
page_id: '244425182'
product: fluig
source: tdn-fluig
title: Cliente 1 - Ambiente de alta disponibilidade - Cloud
type: documentation
url: https://tdn.totvs.com/display/fluig/Cliente+1+-+Ambiente+de+alta+disponibilidade+-+Cloud
version: 12
---

# Índice

5true.\*ndicenone

# Dimensionamento em ambiente de alta disponibilidade executando na Nuvem Totvs

Confira a seguir o exemplo de dimensionamento para ambiente de alta disponibilidade executando em nuvem Totvs.

Este é um dimensionamento real executado em cliente. Os dados abaixo podem ser usados como exemplos e podem ser aplicados à qualquer banco de dados homologado pelo Fluig.

### Perguntas do formulário

| INDIVÍDUOS CADASTRADOS | | | |
| --- | --- | --- | --- |
| Informar a quantidade de indivíduos cadastrados para uso do Fluig: | | | 3500 |
| ACESSOS SIMULTÂNEOS | | | |
| Informar a quantidade de indivíduos acessando o Fluig simultaneamente: | | | 150 |
| VIRTUALIZAÇÃO | | | |
| O cliente tem ambiente virtualizado para o servidor do Fluig? | | | Não |
| O cliente tem ambiente virtualizado para o banco de dados? | | | Não |
| BANCO DE DADOS | | | |
| Qual é o banco de dados a ser usado em produção? | | | Microsoft SQL Server 2012 ou superior |
| O banco de dados será migrado de uma versão Progress? | | | Não |
| Caso haja migração de um banco Progress, qual o tamanho? | | |  |
| ECM | | | |
| DOCUMENTOS | | | |
| Qual é a quantidade de documentos publicados na implantação? | | | 0 |
| Qual é a quantidade média de documentos que serão publicados/versionados por mês? | | | 0 |
| Indique o tamanho médio dos documentos que serão publicados. (O valor deve estar em Kbytes.) | | | 0 |
| Será usado o visualizador de documentos do Fluig? | | | Não |
| BPM | | | |
| PROCESSOS | | | |
| Qual é a quantidade de definições de processos workflow a serem implantados? | | | 0 |
| Qual é a média de atividades relacionadas a cada processo workflow? | | | 0 |
| Qual é a quantidade média mensal de processos workflow iniciados? | | | 0 |
| Especifique a quantidade média de publicações via formulários por mês. | | | 0 |
| Especifique a quantidade de grupos de usuários que serão utilizados. | | | 0 |
| Especifique a quantidade média de usuários por grupo. | | | 0 |
| Existem processos de workflow integrados com ERP TOTVS ou de terceiros? | | | Não |
| ANALYTICS | | | |
| ANÁLISE DE DADOS | | | |
| Será necessária a análise dos dados de documentos e processos? | | | Não |
| Será necessária a análise dos dados de comunidades e usuários? | | | Não |
| Especifique a quantidade de dashboards para visualização. | | | Não |
| PORTAIS | | | |
| PORTAIS | | | |
| Existe alguma demanda de portais corporativos? | | | Não |
| Especifique a quantidade prevista de páginas de portais. | | | 0 |
| COLABORAÇÃO | | | |
| COMUNIDADES | | | |
| Serão criadas comunidades no Fluig? | | | Não |
| As comunidades terão widgets que consumirão dados de ERPS? | | | Não |
| Serão utilizadas galerias de vídeos nas comunidades ? | | | Não |
| Serão utilizadas galerias de imagens nas comunidades ? | | | Não |
| LMS | | | |
| APRENDIZADO | | | |
| Qual é a quantidade de treinamentos criados no Fluig? | | | 60 |
| Qual é a quantidade de turmas criadas no Fluig? | | | 15 |
| Qual é a quantidade de conteúdos de aprendizado que serão criados no Fluig? | | | 30 |
| Qual é a quantidade média de matrículas ativas? | | | 3000 |
| Qual é a quantidade de usuários que serão alunos? | | | 3500 |
| AVALIAÇÕES | | | |
| Qual é a quantidade de questões que serão criadas no Fluig? | | | 1000 |
| Qual é a quantidade de avaliações que serão criadas no Fluig? | | | 100 |
| Pretende aplicar avaliações para pessoas fora do Fluig? Se sim, qual é a frequência? | | | Não |

### Desenho lógico

### Definições de hardware

---
