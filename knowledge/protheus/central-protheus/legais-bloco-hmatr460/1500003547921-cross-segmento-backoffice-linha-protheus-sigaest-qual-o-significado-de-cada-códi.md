---
article_id: 1500003547921
category: LEGAIS - BLOCO H/MATR460
content_hash: 33cf35165e2dba0581568ebbac3fbe00bebb68746197217749b89c62bf8afc79
fetched_at: '2026-06-28T22:42:15.199050+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual o significado
  de cada código de Situação na tabela H?
type: support-article
updated_at: '2022-08-24T19:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003547921-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-o-significado-de-cada-c%C3%B3digo-de-Situa%C3%A7%C3%A3o-na-tabela-H
---

**Dúvida**Ao emitir o relatório MATR460 (P7) para gerar a tabela H\_20201231\_01, é verificado que nela possui a coluna SITUACAO, com vários codigos diferentes. O que quer dizer cada um?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**A tabela H\_  é basicamente um espelho do relatório MATR460 (P7), a diferença é que os registros de saldos, custos e seções (em estoque, de terceiros, etc), ficam em forma de tabela. O campo SITUACAO seria um paralelo com a "Seção", onde:

1 - ESTOQUE (Estoque Próprio);  
2 - PROCESSO (Em Processo);  
3 - SEM SALDO (Quando o produto literalmente imprime com quantidade física 0,00);  
4 - DE TERCEIROS (Saldo DE Terceiros em nosso poder);  
5 - EM TERCEIROS (Saldo nosso EM poder de Terceiros);  
6 - DE TERCEIROS USADO EM ORDENS DE PRODUCAO (Saldo DE terceiros usados em OP feita por nós);  
7 - EM FABRICAÇÃO (Saldo em Fabricação (quando a última pergunta do P7 está com conteúdo = Sim);

Desta forma, sendo o Bloco H um espelho do P7, ele vai registrar cada saldo de cada situação conforme a seção do MATR460.

**Saiba mais:**

*[MP - SIGAEST - MATR460 - Saldo do Armazém de Processo não está saindo no relatório P7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062097594)*

*[MP - SIGAEST - P7 - Montagem da seção "Saldo em Processo"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061473074)*

*[MP - SIGAEST - MATR460 (P7) - Saldo físico em Estoque De/Em Terceiros negativo/divergente. O que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002037442)*

*[MP - SIGAEST - MATR460 (P7) - Saldo físico em Estoque Próprio negativo/divergente. O que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001933381)*

*[Clique aqui e veja mais artigos sobre Bloco H e o relatório MATR460](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H-MATR460-P7-)*
