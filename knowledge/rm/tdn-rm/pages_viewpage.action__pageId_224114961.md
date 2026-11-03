---
content_hash: 0103ae8af0d19d69c3c69d5e17fab95c5c37b5fdf19550057ed58f44c8ff2614
fetched_at: '2026-06-29T00:06:24.251561+00:00'
page_id: '224114961'
product: rm
source: tdn-rm
title: Permissão de Liberação do Sentinela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224114961
version: 124
---

# Permissão de Liberação do Sentinela

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | 12.1.9 e Posteriores |
| **Ocorrência:** | Inclusão de permissão ao catalogo de performance do Banco de Dados |
| **Ambiente:** | RM Atualizador |
| **Passo a passo:** | Nesta versão, uma poderosa ferramenta para análise de desempenho e configuração está sendo disponibilizada, chamada por nós de Sentinela, para auxilia-lo no monitoramento e correção de situações que podem ocorrer à medida que o volume de dados e acessos aumentam ao passar do tempo.  Para utiliza-la, porém, é requerida permissão de acesso ao catalogo de performance do banco de dados que precisará ser habilitado pela equipe de tecnologia de sua empresa.  Este procedimento é opcional, mas enquanto não realizado impedirá a utilização por completa desta ferramenta de análise, o Sentinela.    Passo 1:  Acesse o Banco de Dados utilizando um usuário que possua os privilégios de **SYSADMIN**;    Passo 2:  Acesse a Base **MASTER** e inclua a seguinte permissão para o usuário **RM**;    GRANT VIEW SERVER STATE to RM    Passo 3:  Para verificar se a permissão foi concedida Basta logar no Banco utilizando o usuário **RM** e em seguida executar o SELECT a baixo, caso o valor retornado seja 1 a permissão foi concedida com sucesso;    SELECT HAS\_PERMS\_BY\_NAME(null, null, 'VIEW SERVER STATE') |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |

divs
