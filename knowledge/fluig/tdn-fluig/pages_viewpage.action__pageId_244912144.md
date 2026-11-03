---
content_hash: b58886a7393c0c101235040ae2f76300529b408d89408250beca9aea2dbec6fc
fetched_at: '2026-06-28T21:35:23.354528+00:00'
page_id: '244912144'
product: fluig
source: tdn-fluig
title: BPM 063 - O que fazer quando os eventos de um processo não estão sendo importados
  do servidor fluig?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244912144
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig Studio

**Versão:** 1.5.10

# Ocorrência

A importação de processos do fluig não está importando os *scripts* do processo

# Solução

Verificamos que o problema ocorreu devido ao tipo do projeto que foi criado no TDS/Eclipse.

Para o correto funcionamento do plugin fluig, recomendamos que todos os projetos sejam do tipo **Projeto fluig**. Na página [Criando um projeto fluig no Studio](http://tdn.totvs.com/x/UhgSCw) disponibilizamos o passo a passo.

Após realizarmos este procedimento, os scripts de processos foram importados corretamente.
