---
article_id: 360033930754
category: CRM - Dúvidas Gerais
content_hash: 3a5ebba01a710d278cf84e49bc838ebad7cf20b601a462f90da60a1ac5cd9a49
fetched_at: '2026-06-28T22:40:27.414819+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGACRM - array out of bounds ( 0
  of 10 )  on TK340LINOK(TMKA340.PRW) '
type: support-article
updated_at: '2024-04-25T12:56:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033930754-Cross-Segmentos-Backoffice-Protheus-SIGACRM-array-out-of-bounds-0-of-10-on-TK340LINOK-TMKA340-PRW
---

**Ocorrência**Ao digitar a linha do evento é apresentado o erro:

**array out of bounds ( 0 of 10 ) on TK340LINOK(TMKA340.PRW) 30/01/2015 15:57:05 line : 619**  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Causa**

O erro de array out of bounds significa que o campo do array não existe no banco/sx3 ou não está marcado como usado ou teve mudança de seu nível.

Neste caso, em questão,  a grade de eventos está buscando informações dos campos **ace\_grade, ace\_hrini, ace\_hrfim e ace\_data** que podem estar nas condições descritas acima.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Verifique se os campos **ace\_grade, ace\_hrini, ace\_hrfim e ace\_data** existem no dicionário de dados (SX3) e/ou no Banco de Dados, se estão marcados como usado e estão com o nível 1.  
2. Caso não existam, é necessário efetuar o download do dicionário de dados brasil completo, descompactar o arquivo na pasta systemload e  rodar o upddistr para criação dos campos.  
3. Caso já existam os campos, assegurar que estejam com o uso marcado e com o nível igual 1, salvar a tabela e atualizar o dicionário via configurador.

**Obs: Para efetuar os processos, requer conhecimento em estrutura Protheus, em caso de dúvida na realização descrita acima, acione a equipe de Frame Work.**
