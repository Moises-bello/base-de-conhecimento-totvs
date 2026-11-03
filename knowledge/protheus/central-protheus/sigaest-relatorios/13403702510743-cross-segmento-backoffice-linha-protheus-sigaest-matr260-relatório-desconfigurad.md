---
article_id: 13403702510743
category: SIGAEST - RELATORIOS
content_hash: 9742ac5a4a4c32036a432f298683d4b0cdc148c57fb65fc48a9c32f5e29cf15f
fetched_at: '2026-06-28T22:39:06.082584+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - Relatório
  desconfigurado cortando informações
type: support-article
updated_at: '2023-03-27T19:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13403702510743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Relat%C3%B3rio-desconfigurado-cortando-informa%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:01min** **Dúvida**

Ao emitir o relatório Posição de Estoque, as informações saem desconfiguradas cortando informações. Como corrigir?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Siga os passos abaixo para possível solução deste problema:

* Artefatos de Framework (LIB e Binários) desatualizados:

- [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) -[Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)  
- [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947528) | [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1031460)  
- Smartclient - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1032341)  
- [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

OBS: Sempre atualizar o ambiente primeiramente em ambiente de homologação com backup prévio do RPO.

* Caso tamanho do campo B1\_DESC tenha sido alterado, portanto deve-se personalizar o relatório para atender o novo tamanho padrão

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
