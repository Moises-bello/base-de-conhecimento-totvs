---
content_hash: 9346a6d9db493e6bbf02eb8fb2ee0bb2e0bb88b72ce064f8490862d568d50aca
fetched_at: '2026-06-29T00:08:03.464102+00:00'
page_id: '235322077'
product: rm
source: tdn-rm
title: DT_Consulta_Publica
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Consulta_Publica
version: 127
---

# Consulta pública (projetos de pesquisa, extensão e grupos de pesquisa)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Consulta pública para projeto de pesquisa | Consulta pública para projeto de pesquisa | | Consulta pública para projeto de extensão | Consulta pública para projeto de extensão | | Consulta pública para grupo de pesquisa | Consulta pública para grupo de pesquisa |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | |  |  | |  |  | |
| **Requisito (ISSUE):** | [PCREQ-9518](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9518 "PCREQ-9518") |
| **País(es):** | Todos |

## Descrição

Possibilitar mecanismo para consulta pública das informações de projetos de pesquisa, projetos de extensão e aos grupos de pesquisa.

## Procedimento para Utilização

* Abrir o Web.config localizado em "**<Instalação do CorporeNet>\Source\Edu-Educacional\Public\PesquisaExtensao**" e definir as seguintes tags:

* Definir a segurança para acesso as páginas da pasta "PesquisaExtensao":

<authorization>  
<allow users=**"\*"**/>   
</authorization>  
  
Onde **"\*"** libera permissão para todas as páginas localizadas dentro da pasta "Public\PesquisaExtensao".

* Para cada consulta pública é necessário definir quais os campos devem ser exibidos no resultado, por padrão todos estão definidos como "true".

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE PROJETOS DE PESQUISA -->**  
**<!-- Área de Conhecimento -->**  
 <add key="PESQ\_NOMEAREA" value="true" />  
**<!-- Subárea de Conhecimento Principal -->**  
 <add key="PESQ\_NOMESUBPRINCIPAL" value="true" />  
**<!-- Subárea de Conhecimento Secundário -->**  
 <add key="PESQ\_NOMESUBSECUNDARIA" value="true" />  
**<!-- Coordenador -->**  
 <add key="PESQ\_NOMEPESSOACOORDENADOR" value="true" />  
**<!-- Situação -->**  
 <add key="PESQ\_SITUACAO" value="true" />  
**<!-- Data Início -->**  
 <add key="PESQ\_DATAINICIO" value="true" />  
**<!-- Data Final -->**  
 <add key="PESQ\_DATAFINAL" value="true" />  
**<!-- Súmula -->**  
 <add key="PESQ\_SUMULA" value="true" />  
**<!-- Palavra Chave -->**  
 <add key="PESQ\_PALAVRACHAVE" value="true" />  
**<!-- Nome da Coligada -->**  
 <add key="PESQ\_NOMECOLIGADA" value="true" />  
**<!-- Nome da Filial -->**  
 <add key="PESQ\_NOMEFILIAL" value="true" />  
**<!-- Código do Edital -->**  
 <add key="PESQ\_IDEDITAL" value="true" />  
**<!-- Descrição do Edital -->**  
 <add key="PESQ\_NOMEEDITAL" value="true" />  
**<!-- Lista de Participantes -->**  
 <add key="PESQ\_PARTICIPANTES" value="true" />  
**<!-- Código do projeto -->**  
 <add key="PESQ\_NOMEAREA" value="true" />

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE PROJETOS DE EXTENSÃO -->**   
**<!-- Código do projeto -->**  
 <add key="EXT\_IDPROJETO" value="true" />  
**<!-- Área de Conhecimento -->**  
 <add key="EXT\_NOMEAREA" value="true" />  
**<!-- Subárea de Conhecimento Principal -->**  
 <add key="EXT\_NOMESUBPRINCIPAL" value="true" />  
**<!-- Subárea de Conhecimento Secundário -->**  
 <add key="EXT\_NOMESUBSECUNDARIA" value="true" />  
**<!-- Coordenador -->**  
 <add key="EXT\_NOMEPESSOACOORDENADOR" value="true" />  
**<!-- Situação -->**  
 <add key="EXT\_SITUACAO" value="true" />  
**<!-- Data Início -->**  
 <add key="EXT\_DATAINICIO" value="true" />  
**<!-- Data Final -->**  
 <add key="EXT\_DATAFINAL" value="true" />  
**<!-- Palavra Chave -->**  
 <add key="EXT\_PALAVRACHAVE" value="true" />  
**<!-- Nome da Coligada -->**  
 <add key="EXT\_NOMECOLIGADA" value="false" />  
**<!-- Nome da Filial -->**  
 <add key="EXT\_NOMEFILIAL" value="false" />  
**<!-- Código do Edital -->**  
 <add key="EXT\_IDEDITAL" value="true" />  
**<!-- Descrição do Edital -->**  
 <add key="EXT\_NOMEEDITAL" value="true" />  
**<!-- Lista de Participantes -->**  
 <add key="EXT\_PARTICIPANTES" value="true" />  
**<!-- Nome do programa vinculado -->**  
 <add key="EXT\_NOMEPROGRAMA" value="true" />  
**<!-- Código do projeto -->**  
 <add key="EXT\_IDPROJETO" value="true" />  
**<!-- Linha de extensão -->**  
 <add key="EXT\_LINHAEXTENSAO" value="true" />  
**<!-- Tipo de ação -->**  
 <add key="EXT\_TIPOACAO" value="true" />  
**<!-- Subtipo de ação -->**  
 <add key="EXT\_SUBTIPOACAO" value="true" />

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE GRUPOS DE PESQUISA -->**  
**<!-- Código do grupo -->**  
 <add key="GRPPESQ\_CODIGOGRUPO" value="true" />  
**<!-- Nome da área de conhecimento -->**  
 <add key="GRPPESQ\_NOMEAREA" value="true" />  
**<!-- Nome da subárea de conhecimento -->**  
 <add key="GRPPESQ\_NOMESUBAREA" value="true" />  
**<!-- Nome do líder do grupo -->**  
 <add key="GRPPESQ\_NOMELIDER" value="true" />  
**<!-- Situação -->**  
 <add key="GRPPESQ\_SITUACAO" value="true" />  
**<!-- Nome da coligada -->**  
 <add key="GRPPESQ\_NOMECOLIGADA" value="true" />  
**<!-- Nome dos participantes do grupo -->**  
 <add key="GRPPESQ\_PARTICIPANTES" value="true" />

Valores esperados "true" ou "false".

* Definir se será exibido o botão de impressão de relatório, por padrão estará definido como false

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE PROJETOS DE PESQUISA -->**  
**<!-- Exibir botão de impressão de relatório -->**  
 <add key="PESQ\_EXIBIR\_BOTAO\_RELATORIO" value="false" />

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE PROJETOS DE EXTENSÃO -->**   
**<!-- Exibir botão de impressão de relatório -->**  
 <add key="EXT\_EXIBIR\_BOTAO\_RELATORIO" value="false" />

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE GRUPOS DE PESQUISA -->**  
**<!-- Exibir botão de impressão de relatório -->**  
 <add key="GRPPESQ\_EXIBIR\_BOTAO\_RELATORIO" value="false" />

Valores esperados "true" ou "false".

* Se a exibição do botão de impressão do relatório for parametrizada como "true" deve-se definir o código da coligada e o identificador do relatório a ser executado

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE PROJETOS DE PESQUISA -->**  
**<!-- Código coligada do relatório -->**  
 <add key="PESQ\_CODCOLIGADA\_RELATORIO" value="<CÓDIGO DA COLIGADA DO RELATÓRIO>" />  
**<!-- Identificador do relatório -->**  
 <add key="PESQ\_IDREL\_RELATORIO" value="<IDENTIFICADOR DO RELATÓRIO>" />

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE PROJETOS DE EXTENSÃO -->**   
**<!-- Código coligada do relatório -->**  
 <add key="EXT\_CODCOLIGADA\_RELATORIO" value="<CÓDIGO DA COLIGADA DO RELATÓRIO>" />  
**<!-- Identificador do relatório -->**  
 <add key="EXT\_IDREL\_RELATORIO" value="<IDENTIFICADOR DO RELATÓRIO>" />

**<!-- CAMPOS DO RESULTADO DA CONSULTA DE GRUPOS DE PESQUISA -->**  
**<!-- Código coligada do relatório -->**  
 <add key="GRPPESQ\_CODCOLIGADA\_RELATORIO" value="<CÓDIGO DA COLIGADA DO RELATÓRIO>" />  
**<!-- Identificador do relatório -->**  
 <add key="GRPPESQ\_IDREL\_RELATORIO" value="<IDENTIFICADOR DO RELATÓRIO>" />

**Importante,** mesmo que o botão de impressão esteja parametrizado para ser exibido este pode ficar invisível nos seguintes casos:

1. 1. O valor definido para coligada ou identificador do relatório estiver vazio ou não for um número inteiro válido.
   2. A falta de uma das chaves para definição dos valores de coligada e identificador do relatório no arquivo web.config.

* Definir o caminho do tema a ser utilizado nas páginas das consultas públicas, por padrão o valor é "../styles".

**<!-- Definição do caminho do padrão de cores do sistema -->**  
<add key="Theme" value="../styles" />

**Passos para customização no tema:**

1. 1. Acessar o site do JQuery (<http://themeroller.jquerymobile.com/>) e utilizar como ponto de partida o "Swatch A".
   2. Salvar o tema com o nome EduPesquisaPublica.theme.
   3. Substituir os arquivos: EduPesquisaPublica.theme.css e EduPesquisaPublica.theme.min.css na pasta parametrizada no arquivo web.config.

## Pesquisas públicas

* **Projeto de Pesquisa**

1. 1. Acessar **<Instalação do CorporeNet>\Source\Edu-Educacional\Public\EduProjetoPesquisa.aspx**
   2. As consultas serão realizadas para todas as coligadas e filiais, caso seja necessário filtrá-las por estas informações deve-se passar na URL o seguinte formato **<Instalação do CorporeNet>\Source\Edu-Educacional\Public\EduProjetoPesquisa.aspx?CODCOLIGADA=*<Código da coligada>*&CODFILIAL=*<Código da filial>*.**
   3. O resultado da consulta lista apenas os projetos de pesquisa com situação "Em execução" ou "Encerrado".
   4. A pesquisa disponibiliza ao usuário os seguintes filtros:
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
   11. Descrição do edital5. Os campos listados no resultado dependerão das parametrizações realizadas no arquivo web.config, o único campo que não pode ficar oculto é o título do projeto. Abaixo os campos disponíveis para o resultado da pesquisa:
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
   6. Disponibilizado o relatório **"EDUREL0079 - PPE - Projeto de pesquisa"** no book de relatórios
      1. O usuário poderá criar o seu próprio relatório desde que este disponibilize os parâmetros CODCOLIGADA\_N e IDPROJETO\_N

* **Projeto de Extensão**

1. 1. Acessar **<Instalação do CorporeNet>\Source\Edu-Educacional\Public\EduProjetoExtensao.aspx**
   2. As consultas serão realizadas para todas as coligadas e filiais, caso seja necessário filtrá-las por estas informações deve-se passar na URL o seguinte formato **<Instalação do CorporeNet>\Source\Edu-Educacional\Public\EduProjetoExtensao.aspx?CODCOLIGADA=*<Código da coligada>*&CODFILIAL=*<Código da filial>***.
   3. O resultado da consulta lista apenas os projetos de extensão com situação "Em execução" ou "Encerrado".
   4. A pesquisa disponibiliza ao usuário os seguintes filtros:
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
   5. Os campos listados no resultado dependerão das parametrizações realizadas no arquivo web.config, o único campo que não pode ficar oculto é o título do projeto. Abaixo os campos disponíveis para o resultado da pesquisa:
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
      18. Nome da filial
   6. Disponibilizado o relatório **"EDUREL0080 - PPE - Projeto de extensão"** no book de relatórios
      1. O usuário poderá criar o seu próprio relatório desde que este disponibilize os parâmetros CODCOLIGADA\_N e IDPROJETO\_N

* **Grupo de Pesquisa**

1. 1. Acessar **<Instalação do CorporeNet>\Source\Edu-Educacional\Public\EduGrupoPesquisa.aspx**
   2. A pesquisa disponibiliza ao usuário os seguintes filtros:
      1. Líder do grupo
      2. Área de conhecimento
      3. Subárea de conhecimento
   3. Os campos listados no resultado dependerão das parametrizações realizadas no arquivo web.config, o único campo que não pode ficar oculto é o nome do grupo. Abaixo os campos disponíveis para o resultado da pesquisa:
      1. Código
      2. Nome
      3. Área de conhecimento
      4. Subárea de conhecimento
      5. Nome Líder do grupo
      6. Participantes do grupo
      7. Situação
      8. Nome da coligada
   4. Disponibilizado o relatório **"EDUREL0078 - PPE - Grupo de Pesquisa"** no book de relatórios
      1. O usuário poderá criar o seu próprio relatório desde que este disponibilize os parâmetros CODCOLIGADA\_N e IDGRUPOPESQUISA\_N

divs
