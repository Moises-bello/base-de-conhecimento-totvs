---
content_hash: 282858a994eb039ea18cd47098a19e283760bc42a893a66083bb844dfabc9f03
fetched_at: '2026-06-28T21:35:23.184345+00:00'
page_id: '244425315'
product: fluig
source: tdn-fluig
title: Cliente 2 - Ambiente de média disponibilidade - Cloud
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244425315
version: 9
---

# Índice

5true.\*ndicenone

# Dimensionamento em ambiente de média disponibilidade executando na Nuvem Totvs

Confira a seguir o exemplo de dimensionamento para ambiente de média disponibilidade executando em nuvem Totvs.

Este é um dimensionamento real executado em cliente. Os dados abaixo podem ser usados como exemplos e podem ser aplicados à qualquer banco de dados homologado pelo Fluig.

| INDIVÍDUOS CADASTRADOS | | | |
| --- | --- | --- | --- |
| Informar a quantidade de indivíduos cadastrados para uso do Fluig: | | | 1000 |
| ACESSOS SIMULTÂNEOS | | | |
| Informar a quantidade de indivíduos acessando o Fluig simultaneamente: | | | 100 |
| VIRTUALIZAÇÃO | | | |
| O cliente tem ambiente virtualizado para o servidor do Fluig? | | | SIM |
| O cliente tem ambiente virtualizado para o banco de dados? | | | SIM |
| BANCO DE DADOS | | | |
| Qual é o banco de dados a ser usado em produção? | | | MySQL 5.5 ou superior |
| O banco de dados será migrado de uma versão Progress? | | | Não |
| Caso haja migração de um banco Progress, qual o tamanho? | | | 0 |
| ECM | | | |
| DOCUMENTOS | | | |
| Qual é a quantidade de documentos publicados na implantação? | | | 167.600 |
| Qual é a quantidade média de documentos que serão publicados/versionados por mês? | | | 10.000 |
| Indique o tamanho médio dos documentos que serão publicados. (O valor deve estar em Kbytes.) | | | 500 Kb |
| Será usado o visualizador de documentos do Fluig? | | | Sim |
| BPM | | | |
| PROCESSOS | | | |
| Qual é a quantidade de definições de processos workflow a serem implantados? | | | A definir |
| Qual é a média de atividades relacionadas a cada processo workflow? | | | A definir |
| Qual é a quantidade média mensal de processos workflow iniciados? | | | A definir |
| Especifique a quantidade média de publicações via formulários por mês. | | | A definir |
| Especifique a quantidade de grupos de usuários que serão utilizados. | | | A definir |
| Especifique a quantidade média de usuários por grupo. | | | A definir |
| Existem processos de workflow integrados com ERP TOTVS ou de terceiros? | | | A definir |
| ANALYTICS | | | |
| ANÁLISE DE DADOS | | | |
| Será necessária a análise dos dados de documentos e processos? | | | Não |
| Será necessária a análise dos dados de comunidades e usuários? | | | Não |
| Especifique a quantidade de dashboards para visualização. | | | Não |
| PORTAIS | | | |
| PORTAIS | | | |
| Existe alguma demanda de portais corporativos? | | | Não |
| Especifique a quantidade prevista de páginas de portais. | | | Não |
| COLABORAÇÃO | | | |
| COMUNIDADES | | | |
| Serão criadas comunidades no Fluig? | | | Sim |
| As comunidades terão widgets que consumirão dados de ERPS? | | | Sim |
| Serão utilizadas galerias de vídeos nas comunidades ? | | | Sim |
| Serão utilizadas galerias de imagens nas comunidades ? | | | Sim |
| LMS | | | |
| APRENDIZADO | | | |
| Qual é a quantidade de treinamentos criados no Fluig? | | | Sim |
| Qual é a quantidade de turmas criadas no Fluig? | | | Não |
| Qual é a quantidade de conteúdos de aprendizado que serão criados no Fluig? | | | Não |
| Qual é a quantidade média de matrículas ativas? | | | Não |
| Qual é a quantidade de usuários que serão alunos? | | | Não |
| AVALIAÇÕES | | | |
| Qual é a quantidade de questões que serão criadas no Fluig? | | | Não |
| Qual é a quantidade de avaliações que serão criadas no Fluig? | | | Não |
| Pretende aplicar avaliações para pessoas fora do Fluig? Se sim, qual é a frequência? | | | Não |

### Desenho lógico

### Definições de hardware

---
