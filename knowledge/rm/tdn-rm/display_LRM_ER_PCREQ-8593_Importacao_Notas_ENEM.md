---
content_hash: f9b9daa749629f2f7750beceb5f0162c65c9a258e3c6761563c19759a08f799c
fetched_at: '2026-06-29T00:06:22.373470+00:00'
page_id: '223915941'
product: rm
source: tdn-rm
title: ER_PCREQ-8593_Importacao_Notas_ENEM
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8593_Importacao_Notas_ENEM
version: 126
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Processo Seletivo | **Módulo** | Processo Seletivo |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | R\_EDU\_EDU018 | **IRM1** | PCREQ-9355 |
| **Requisito1** | PCREQ-9356 | **Subtarefa1** | PDR\_EDU\_EDU018-2 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Apresentar as alterações necessárias para que o Processo Seletivo armazene as notas do ENEM de cada prova de Ciências da Natureza, Ciências Humanas, Linguagens e Matemática.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Importação notas do ENEM | [Alteração] | Processos > Processos de importação > Importar notas do ENEM | - |
| Funções de fórmula Desempate Classificação | [Alteração] | Globais > Administração > Fórmulas | - |
| Funções de fórmula - Pontuação | [Alteração] | Globais > Administração > Fórmulas | - |

### **Importação das notas do ENEM para o Processo Seletivo**

O modelo de layout do arquivo de importação. O modelo 2006/2007 oferece um único campo para nota da prova objetiva, enquanto que o modelo 2009/2010 discrimina as provas de Ciências da Natureza, Ciências Humanas, Linguagens e Matemática.

No momento da importação, caso o layout 2009/2010 seja escolhido, o sistema realiza a média aritmética das quatro notas e grava no campo “Nota Objetiva”.

O escopo da demanda se refere a uma forma de armazenar as notas objetivas e de redação.

Diante da demanda teremos como solução:

1 - No momento de importar as notas do ENEM, no Processo Seletivo, as notas objetivas e de redação serão armazenadas em campos distintos.

Além dos campos nota objetiva do ENEM (ENEMNOTAOBJETIVA) e nota de redação do ENEM (ENEMNOTAREDACAO) da tabela de Inscrição de Aluno (SPSINSCRICAOAREAOFERTADA), serão criados outros quatros campos para armazenar a nota de cada prova.

Novos campos:

* Nota da prova de Ciência da Natureza – ENEMNOTANATUREZA;
* Nota da prova de Ciências Humanas – ENEMNOTAHUMANAS;
* Nota da prova de Linguagem - ENEMNOTALINGUAGEM;
* Nota da prova de Matemática – ENEMNOTAMATEMATICA.

2 - As informações das notas importadas serão exibidas no sistema, no cadastro de Inscrições de candidato, aba Informações Complementares, grupo ENEM.

3 - O campo de Nota Objetiva continuará sendo a média aritmética das quatros notas e armazenado no campo “Nota Objetiva” (ENEMNOTAOBJETIVA).

4 - O processo “Importar notas inconsistentes do ENEM” não será alterado, pois o MEC não disponibiliza no arquivo de inconsistência as notas de cada prova.

5 - O cadastro de critérios de desempate será alterado para permitir ao usuário selecionar as notas das provas citadas como “tipo de critério” de desempate durante a classificação do candidato, da mesma que hoje existe as opções de “Nota da prova de redação do ENEM” e “Nota da prova objetiva do ENEM”.

6 - Serão criadas funções de fórmula para recuperar a nota de cada prova objetiva e/ou redação e assim possibilitar ao cliente fazer os cálculos necessários.

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

As funções de fórmula abaixo serão criadas para recuperar a nota de cada prova objetiva baseado nos novos campos criados:

* PSNotaNaturezaENEM - Retorna a nota obtida na prova de Ciências da Natureza do ENEM;
* PSNotaHumanasENEM - Retorna a nota obtida na prova de Ciências Humanas do ENEM;
* PSNotaLinguagemENEM - Retorna a nota obtida na prova de Linguagem do ENEM;
* PSNotaMatematicaENEM - Retorna a nota obtida na prova de Matemática do ENEM;
* PSDNNotaNaturezaENEM por Candidato - Retorna a nota obtida na prova de Ciências da Natureza do ENEM para o desempate do processo de classificação;
* PSDNNotaHumanasENEM por Candidato - Retorna a nota obtida na prova de Ciências Humanas do ENEM para o desempate do processo de classificação;
* PSDNNotaLinguagemENEM por Candidato - Retorna a nota obtida na prova de Linguagem do ENEM para o desempate do processo de classificação;
* PSDNNotaMatematicaENEM por Candidato - Retorna a nota obtida na prova de Matemática do ENEM para o desempate do processo de classificação;
* PSCGNotaNaturezaENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de ciências da natureza do ENEM.
* PSCGNotaHumanasENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de ciências humanas do ENEM.
* PSCGNotaLinguagemENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de linguagem do ENEM.
* PSCGNotaMatematicaENEM - Processo Seletivo (Class. Geral) - Retorna a nota obtida na prova de matemática do ENEM.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
