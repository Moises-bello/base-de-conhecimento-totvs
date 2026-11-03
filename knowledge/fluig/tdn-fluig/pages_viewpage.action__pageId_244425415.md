---
content_hash: b4a2f7d8ce4af17d359d0f92f9f3e26982805faf021593f4cdf648644090e2bf
fetched_at: '2026-06-28T21:35:23.192066+00:00'
page_id: '244425415'
product: fluig
source: tdn-fluig
title: Cliente 5 - Média disponibilidade em servidor cliente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244425415
version: 8
---

# Índice

5true.\*ndicenone

# Dimensionamento em ambiente de média disponibilidade executando em servidor cliente

Confira a seguir o exemplo de dimensionamento para ambiente de média disponibilidade executando em servidor de cliente.

Este é um dimensionamento real executado em cliente. Os dados abaixo podem ser usados como exemplos e podem ser aplicados à qualquer banco de dados homologado pelo Fluig.

### Perguntas do formulário

| INDIVÍDUOS CADASTRADOS | | | |
| --- | --- | --- | --- |
| Informar a quantidade de indivíduos cadastrados para uso do Fluig: | | | 1000 |
| ACESSOS SIMULTÂNEOS | | | |
| Informar a quantidade de indivíduos acessando o Fluig simultaneamente: | | | 50 |
| VIRTUALIZAÇÃO | | | |
| O cliente tem ambiente virtualizado para o servidor do Fluig? | | | Sim |
| O cliente tem ambiente virtualizado para o banco de dados? | | | Sim |
| BANCO DE DADOS | | | |
| Qual é o banco de dados a ser usado em produção? | | | Oracle 10G R2 ou superior |
| O banco de dados será migrado de uma versão Progress? | | | Não |
| Caso haja migração de um banco Progress, qual o tamanho? | | | Não haverá migração |
| ECM | | | |
| DOCUMENTOS | | | |
| Qual é a quantidade de documentos publicados na implantação? | | | 100 |
| Qual é a quantidade média de documentos que serão publicados/versionados por mês? | | | 300 |
| Indique o tamanho médio dos documentos que serão publicados. (O valor deve estar em Kbytes.) | | | 1000 |
| Será usado o visualizador de documentos do Fluig? | | | Sim |
| BPM | | | |
| PROCESSOS | | | |
| Qual é a quantidade de definições de processos workflow a serem implantados? | | | 10 |
| Qual é a média de atividades relacionadas a cada processo workflow? | | | 20 |
| Qual é a quantidade média mensal de processos workflow iniciados? | | | 600 |
| Especifique a quantidade média de publicações via formulários por mês. | | | 100 |
| Especifique a quantidade de grupos de usuários que serão utilizados. | | | 30 |
| Especifique a quantidade média de usuários por grupo. | | | 33 |
| Existem processos de workflow integrados com ERP TOTVS ou de terceiros? | | | Não |
| ANALYTICS | | | |
| ANÁLISE DE DADOS | | | |
| Será necessária a análise dos dados de documentos e processos? | | | Não |
| Será necessária a análise dos dados de comunidades e usuários? | | | Não |
| Especifique a quantidade de dashboards para visualização. | | | Não |
| PORTAIS | | | |
| PORTAIS | | | |
| Existe alguma demanda de portais corporativos? | | | Sim |
| Especifique a quantidade prevista de páginas de portais. | | | 20 |
| COLABORAÇÃO | | | |
| COMUNIDADES | | | |
| Serão criadas comunidades no Fluig? | | | Sim |
| As comunidades terão widgets que consumirão dados de ERPS? | | | Não |
| Serão utilizadas galerias de vídeos nas comunidades ? | | | Sim |
| Serão utilizadas galerias de imagens nas comunidades ? | | | Sim |
| LMS | | | |
| APRENDIZADO | | | |
| Qual é a quantidade de treinamentos criados no Fluig? | | | 20 |
| Qual é a quantidade de turmas criadas no Fluig? | | | 10 |
| Qual é a quantidade de conteúdos de aprendizado que serão criados no Fluig? | | | 10 |
| Qual é a quantidade média de matrículas ativas? | | | 100 |
| Qual é a quantidade de usuários que serão alunos? | | | 1000 |
| AMS | | | |
| Qual é a quantidade de questões que serão criadas no Fluig? | | | 40 |
| Qual é a quantidade de avaliações que serão criadas no Fluig? | | | 40 |
| Pretende aplicar avaliações para pessoas fora do Fluig? Se sim, qual é a frequência? | | | Não |

### Desenho lógico

### Definições de hardware

---
