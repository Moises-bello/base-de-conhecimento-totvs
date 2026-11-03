---
content_hash: 48a9558dd4a4070300325b179b9d457ac26b82ec23104ab717a7bcc082d8a023
fetched_at: '2026-06-29T00:06:23.453905+00:00'
page_id: '224102676'
product: rm
source: tdn-rm
title: DT_Importação_das_notas_do_ENEM_para_o_Processo_Seletivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224102676
version: 124
---

# Importação das notas do ENEM

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Processo Seletivo |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Importação notas do ENEM | Importação notas do ENEM |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Candidatos Inscritos | Cadastro de Candidatos Inscritos | | Classificação de Candidatos | Processo Classificar Candidato | | Classificação Geral | Processo de Classificação Geral | | Critério de Desempate | Cadastro de Critérios de Desempate | |
| **Cadastros Iniciais:** | Processo Seletivo, área de interesse ofertada, fórmulas, critério de desempate, locais disponíveis, candidatos inscritos |
| **Requisito (ISSUE):** | [PCREQ-9356](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-9356 "PCREQ-4727") |
| **País(es):** | Brasil |
| **Versões/Release:** | 12.1.10 |

## Descrição

Apresentar as alterações realizadas para que o Processo Seletivo armazene as notas do ENEM de cada prova de Ciências da Natureza, Ciências Humanas, Linguagens e Matemática.

# Importação das notas do ENEM para o Processo Seletivo

O modelo de layout do arquivo de importação “2006/2007” oferece um único campo para nota da prova objetiva, enquanto que o modelo “2009/2010” em diante discrimina as provas de Ciências da Natureza, Ciências Humanas, Linguagens e Matemática.

No momento da importação, caso o layout 2009/2010 seja escolhido ou outro mais recente, o sistema realiza a média aritmética das quatro notas e grava no campo “Nota Objetiva”.

O escopo da demanda se refere a uma forma de armazenar as notas objetivas de cada prova do ENEM.

**Cadastro - Candidatos Inscritos**

No momento de importar as notas do ENEM, no Processo Seletivo, as notas objetivas e de redação serão armazenadas em campos distintos.

Além dos campos, nota objetiva do ENEM (ENEMNOTAOBJETIVA) e nota de redação do ENEM (ENEMNOTAREDACAO) da tabela de Inscrição de candidato (SPSINSCRICAOAREAOFERTADA), foram criados outros quatros campos para armazenar a nota de cada prova objetiva.

Novos campos:

* Nota da prova de Ciência da Natureza – ENEMNOTANATUREZA;
* Nota da prova de Ciências Humanas – ENEMNOTAHUMANAS;
* Nota da prova de Linguagem - ENEMNOTALINGUAGEM;
* Nota da prova de Matemática – ENEMNOTAMATEMATICA.

As informações das notas importadas serão exibidas no sistema, no cadastro de Inscrições de candidato, aba Informações Complementares, grupo ENEM.

O campo de Nota Objetiva continuará sendo a média aritmética das quatros notas e armazenado no campo “Nota Objetiva” (ENEMNOTAOBJETIVA).

O processo “Importar notas inconsistentes do ENEM” não foi alterado, pois o MEC não disponibiliza  as notas de cada prova no arquivo de inconsistência.

**Critério de Desempate**

O cadastro de critérios de desempate foi alterado para permitir que o usuário selecione as notas das provas citadas como “tipo de critério” de desempate durante a classificação do candidato, da mesma forma que hoje existe as opções de “Nota da prova de redação do ENEM” e “Nota da prova objetiva do ENEM”.

Foi disponibilizado também funções de fórmula que podem ser utilizados como critério de desempate por fórmula.

**Funções de fórmula**

Hoje o Processo Seletivo já disponibiliza as funções de fórmulas relacionadas ao ENEM:

* PSAnoENEMCandidato – Retorna o ano de realização do ENEM do candidato;
* PSCandUtilizaENEM - Retorna se o candidato optou ou não pela utilização do ENEM;
* PSNotaRedacaoENEM - Retorna a nota obtida na prova de redação do ENEM;
* PSNotaObjetivaENEM - Retorna a nota obtida na prova objetiva do ENEM;
* PSDNAnoENEMCandidato por Candidato – Retorna o ano de realização do ENEM do candidato para o desempate do processo de classificação;
* PSDNCandUtilizaENEM por Candidato - Retorna se o candidato optou ou não pela utilização do ENEM para o desempate do processo de classificação;
* PSDNNotaRedacaoENEM por Candidato - Retorna a nota obtida na prova de redação do ENEM para o desempate do processo de classificação;
* PSDNObjetivaENEM por Candidato - Retorna a nota obtida na prova objetiva do ENEM para o desempate do processo de classificação;
* PSCGNotaRedacaoENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de redação do ENEM.
* PSCGNotaObjetivaENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova objetiva do ENEM.

Devido a criação dos novos campos supracitados, foram desenvolvidas outras funções de fórmula para recuperar a nota de cada prova objetiva e assim possibilitar ao cliente fazer os cálculos necessários para cada contexto dos processos do Processo Seletivo.

Novas funções de fórmulas criadas:

**Contexto de Critérios de Desempate - Fórmula para classificação geral**

* PSDNNotaNaturezaENEM por Candidato - Retorna a nota obtida na prova de Ciências da Natureza do ENEM para o desempate do processo de classificação;
* PSDNNotaHumanasENEM por Candidato - Retorna a nota obtida na prova de Ciências Humanas do ENEM para o desempate do processo de classificação;
* PSDNNotaLinguagemENEM por Candidato - Retorna a nota obtida na prova de Linguagem do ENEM para o desempate do processo de classificação;
* PSDNNotaMatematicaENEM por Candidato - Retorna a nota obtida na prova de Matemática do ENEM para o desempate do processo de classificação.

**Contexto de área de interesse ofertada - Fórmula para cálculo de pontuação**

* PSNotaNaturezaENEM - Retorna a nota obtida na prova de Ciências da Natureza do ENEM;
* PSNotaHumanasENEM - Retorna a nota obtida na prova de Ciências Humanas do ENEM;
* PSNotaLinguagemENEM - Retorna a nota obtida na prova de Linguagem do ENEM;
* PSNotaMatematicaENEM - Retorna a nota obtida na prova de Matemática do ENEM.

**Contexto de Classificação Geral - Fórmula para classificação geral**

* PSCGNotaNaturezaENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de ciências da natureza do ENEM.
* PSCGNotaHumanasENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de ciências humanas do ENEM.
* PSCGNotaLinguagemENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de linguagem do ENEM.
* PSCGNotaMatematicaENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de matemática do ENEM.

divs
