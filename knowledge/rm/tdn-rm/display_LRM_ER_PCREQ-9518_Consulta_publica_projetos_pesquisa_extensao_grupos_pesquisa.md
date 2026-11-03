---
content_hash: 29d15417a2545848939a4c6738fc2b016c7cf1e96816c23577268d05506f3e73
fetched_at: '2026-06-29T00:06:24.227558+00:00'
page_id: '224114862'
product: rm
source: tdn-rm
title: ER_PCREQ-9518_Consulta_publica_projetos_pesquisa_extensao_grupos_pesquisa
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9518_Consulta_publica_projetos_pesquisa_extensao_grupos_pesquisa
version: 139
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | PDR\_EDU\_EDU019 | **IRM1** | [PCREQ-9517](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-9517 "PCREQ-9517") |
| **Requisito1** | [PCREQ-9518](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9518 "PCREQ-9518") | **Subtarefa1** | [PDR\_EDU\_EDU019-28](http://jira.totvs.com.br/browse/PDR_EDU_EDU019-28) |
| **Chamado2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Disponibilizar consultas públicas para os projetos de pesquisa, projetos de extensão e grupos de pesquisa.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Consulta pública para projetos de pesquisa | Criação |  | - |
| Consulta pública para projetos de extensão | Criação |  | - |
| Consulta pública para grupo de pesquisa | Criação |  | - |
| Book de Relatórios - Relatório de Grupo de pesquisa | Criação |  | - |
| Book de Relatórios - Relatório de Projeto de pesquisa | Criação |  | - |
| Book de Relatórios - Relatório de Projeto de extensão | Criação |  | - |

# Requisito 1: Pesquisas públicas

1. As pesquisas públicas ficarão em uma pasta denominada "Public" localizada dentro da estrutura do corpore.net, será uma subpasta da pasta "..\Source\Edu-Educacional".
2. Como o acesso as pesquisas públicas não requer a autenticação do usuário, o cliente deverá parametrizar um usuário e senha no arquivo de web.config localizado na pasta "Public" que possibilitará a chamada ao serviço de pesquisa.
3. Por padrão esta pasta estará com acesso restrito impossibilitando a utilização das pesquisas públicas, sendo necessário para os clientes que queiram utilizá-la a parametrização do arquivo web.config (<allow users="\*"/>).

# Requisito 2: Pesquisa pública a projetos de pesquisa

1. A pesquisa permitirá ao usuário realizar filtros pelos seguintes campos:

1. Área de conhecimento
2. Subárea de conhecimento
3. Código do projeto
4. Título do projeto
5. Nome do participante
6. Nome do coordenador
7. Palavra chave
8. Data início (carregado inicialmente com a data atual decrescida de um ano)
9. Data fim (carregado inicialmente com a data atual)
10. Código do edital
11. Descrição do edital

2. Na consulta deve existir uma opção para o usuário definir se a coluna contendo a súmula do projeto (resumo) deverá ser exibida.  
   "Deseja exibir no resultado a súmula dos projetos"
3. A consulta só listará projetos de pesquisa com situação "Em execução" ou "Encerrado".
4. O cliente poderá configurar o link da consulta pública passando a coligada e/ou a filial como QueryString (Exemplo: <CAMINHO>?CODCOLIGADA=ValorColigada&CODFILIAL=ValorFilial), neste cenário o resultado da consulta será filtrado pela coligada e/ou filial informadas.
5. O resultado da pesquisa apresentará as seguintes informações dos projetos de pesquisa:
   1. Código do projeto
   2. Título do projeto
   3. Área de conhecimento
   4. Subárea de conhecimento principal
   5. Subárea de conhecimento secundária
   6. Coordenador
   7. Situação
   8. Data início
   9. Data fim
   10. Sumula (será exibida apenas se o usuário tiver marcado a opção "Deseja exibir no resultado a súmula dos projetos")
   11. Palavras chave
   12. Nome da coligada
   13. Nome da filial (através do edital do projeto de pesquisa)
   14. Código do edital
   15. Descrição do edital
   16. Lista dos participantes da equipe vinculada ao projeto
6. Por padrão o resultado da pesquisa exibirá todos os campos definidos no item anterior, no entanto, o cliente poderá no arquivo web.config determinar quais dessas colunas ficarão visíveis. Se o usuário definir no arquivo web.config que o campo súmula não será apresentado no resultado final, a opção "Deseja exibir no resultado a súmula dos projetos" ficará invisível.
7. Criar um relatório para o book que listará as informações de um determinado projeto de pesquisa. Este relatório poderá ser emitido a partir das linhas do resultado da consulta, caso o usuário queira utilizar o seu próprio relatório será permitido parametrizá-lo no arquivo web.config. A exibição do botão para imprimir o relatório também poderá ser configurado no arquivo web.config.

# Requisito 3: Pesquisa pública a projetos de extensão

1. A pesquisa permitirá ao usuário realizar filtros pelos seguintes campos:
   1. Área de conhecimento
   2. Subárea de conhecimento
   3. Linha de extensão
   4. Código do projeto
   5. Nome do projeto
   6. Tipo de ação (programas, cursos, eventos)
   7. Subtipo de ação
   8. Nome do participante
   9. Nome do coordenador
   10. Nome do programa vinculado
   11. Data início (carregado inicialmente com a data atual decrescida de um ano)
   12. Data fim (carregado inicialmente com a data atual)
   13. Código do edital
   14. Descrição do edital
2. A consulta só listará projetos de extensão com situação "Em execução" ou "Encerrado".
3. O cliente poderá configurar a chamada ao link da consulta passando a coligada e/ou a filial como QueryString, neste cenário o resultado da consulta utilizará estes campos como filtros fixos.
4. O resultado da pesquisa apresentará as seguintes informações dos projetos de extensão:  
   1. Código do projeto
   2. Título do projeto
   3. Área de conhecimento
   4. Subárea de conhecimento principal
   5. Subárea de conhecimento secundária
   6. Linha de extensão
   7. Tipo de ação
   8. Subtipo de ação
   9. Coordenador
   10. Participantes da equipe
   11. Nome do programa vinculado
   12. Situação
   13. Data início
   14. Data fim
   15. Código do edital
   16. Descrição do edital
   17. Nome da coligada
   18. Nome da filial (através do edital do projeto de extensão)
5. Por padrão o resultado da pesquisa exibirá todos os campos definidos no item anterior, no entanto, o cliente poderá no arquivo web.config determinar quais dessas colunas ficarão visíveis.
6. Criar um relatório para o book que listará as informações de um determinado projeto de extensão. Este relatório poderá ser emitido a partir das linhas do resultado da consulta, caso o usuário queira utilizar o seu próprio relatório será permitido parametrizá-lo no arquivo web.config. A exibição do botão para imprimir o relatório também poderá ser configurado no arquivo web.config

# Requisito 4: Pesquisa pública ao grupo de pesquisa

1. A pesquisa permitirá ao usuário realizar filtros pelos seguintes campos:
   1. Líder do grupo
   2. Área de conhecimento
   3. Subárea de conhecimento
2. A consulta não possuirá nenhum filtro fixo.
3. O resultado da pesquisa apresentará as seguintes informações dos grupos de pesquisa:
   1. Código
   2. Nome
   3. Área de conhecimento
   4. Subárea de conhecimento
   5. Nome Líder do grupo
   6. Participantes do grupo
   7. Situação
   8. Nome da coligada
4. Por padrão o resultado da pesquisa exibirá todos os campos definidos no item anterior, no entanto, o cliente poderá no arquivo web.config determinar quais dessas colunas ficarão visíveis.
5. Criar um relatório para o book que listará as informações de um determinado grupo de pesquisa. Este relatório poderá ser emitido a partir das linhas do resultado da consulta, caso o usuário queira utilizar o seu próprio relatório será permitido parametrizá-lo no arquivo web.config. A exibição do botão para imprimir o relatório também poderá ser configurado no arquivo web.config

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
