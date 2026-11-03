---
article_id: 13480380040855
category: LEGAIS - BLOCO H/MATR460
content_hash: c62e84fa53fff4fb3d996e2be49f8153e48524ff8a1ce2006ca137b4e008f3a8
fetched_at: '2026-06-28T22:42:15.105042+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Could not
  load Bound Server libctreecsv.so on FWOPENTEMP(CRIATRAB.PRG)
type: support-article
updated_at: '2023-12-08T19:44:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13480380040855-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Could-not-load-Bound-Server-libctreecsv-so-on-FWOPENTEMP-CRIATRAB-PRG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:57 min** **Dúvida**

Ao gerar o relatório P7 ocorre o erro "*Could not load Bound Server libctreecsv.so on FWOPENTEMP(CRIATRAB.PRG)*". Como resolver?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para correto carregamento do arquivo libctreecsv.so basta:

- Efetuar uma cópia (backup) de sua atual **libctreescv.so;**

- Instalar a nova **libctreecsv.so** em anexo ao final do artigo nas pastas de todos os seus AppServers (Master e Slaves, caso use balanceamento), substituindo a anterior.  
   
Após reiniciar todos os AppServers, verificar se o erro é retificado.

**Saiba mais**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)*
