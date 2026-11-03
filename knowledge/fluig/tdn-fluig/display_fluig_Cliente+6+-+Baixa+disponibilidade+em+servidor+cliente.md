---
content_hash: 3c6b2fd4d74a53d0417e1ae47660531aa2758398dc3a6f64b9621b212354e053
fetched_at: '2026-06-28T21:35:23.205339+00:00'
page_id: '244425506'
product: fluig
source: tdn-fluig
title: Cliente 6 - Baixa disponibilidade em servidor cliente
type: documentation
url: https://tdn.totvs.com/display/fluig/Cliente+6+-+Baixa+disponibilidade+em+servidor+cliente
version: 8
---

# Índice

5true.\*ndicenone

# Dimensionamento em ambiente de baixa disponibilidade executando em servidor cliente

Confira a seguir o exemplo de dimensionamento para ambiente de baixa disponibilidade executando em servidor de cliente.

Este é um dimensionamento real executado em cliente. Os dados abaixo podem ser usados como exemplos e podem ser aplicados à qualquer banco de dados homologado pelo Fluig.

### Perguntas do formulário

| INDIVÍDUOS CADASTRADOS | | | |
| --- | --- | --- | --- |
| Informar a quantidade de indivíduos cadastrados para uso do Fluig: | | | 700 |
| ACESSOS SIMULTÂNEOS | | | |
| Informar a quantidade de indivíduos acessando o Fluig simultaneamente: | | | 70 |
| VIRTUALIZAÇÃO | | | |
| O cliente tem ambiente virtualizado para o servidor do Fluig? | | | Cloud TOTVS |
| O cliente tem ambiente virtualizado para o banco de dados? | | | Cloud TOTVS |
| BANCO DE DADOS | | | |
| Qual é o banco de dados a ser usado em produção? | | | MySQL 5.5 ou superior |
| O banco de dados será migrado de uma versão Progress? | | | Não |
| Caso haja migração de um banco Progress, qual o tamanho? | | |  |
| ECM | | | |
| DOCUMENTOS | | | |
| Qual é a quantidade de documentos publicados na implantação? | | | 2500 |
| Qual é a quantidade média de documentos que serão publicados/versionados por mês? | | | 30 |
| Indique o tamanho médio dos documentos que serão publicados. (O valor deve estar em Kbytes.) | | | 1mb |
| Será usado o visualizador de documentos do Fluig? | | | Sim |
| BPM | | | |
| PROCESSOS | | | |
| Qual é a quantidade de definições de processos workflow a serem implantados? | | | 5 |
| Qual é a média de atividades relacionadas a cada processo workflow? | | | 10 |
| Qual é a quantidade média mensal de processos workflow iniciados? | | | 2100 |
| Especifique a quantidade média de publicações via formulários por mês. | | | 700 |
| Especifique a quantidade de grupos de usuários que serão utilizados. | | | - |
| Especifique a quantidade média de usuários por grupo. | | | - |
| Existem processos de workflow integrados com ERP TOTVS ou de terceiros? | | | Sim |
| ANALYTICS | | | |
| ANÁLISE DE DADOS | | | |
| Será necessária a análise dos dados de documentos e processos? | | | Sim |
| Será necessária a análise dos dados de comunidades e usuários? | | | Sim |
| Especifique a quantidade de dashboards para visualização. | | | Sim |
| PORTAIS | | | |
| PORTAIS | | | |
| Existe alguma demanda de portais corporativos? | | | Sim |
| Especifique a quantidade prevista de páginas de portais. | | |  |
| COLABORAÇÃO | | | |
| COMUNIDADES | | | |
| Serão criadas comunidades no Fluig? | | | Não |
| As comunidades terão widgets que consumirão dados de ERPS? | | | Não |
| Serão utilizadas galerias de vídeos nas comunidades ? | | | Não |
| Serão utilizadas galerias de imagens nas comunidades ? | | | Não |

### Desenho lógico e definições de hardware

---
