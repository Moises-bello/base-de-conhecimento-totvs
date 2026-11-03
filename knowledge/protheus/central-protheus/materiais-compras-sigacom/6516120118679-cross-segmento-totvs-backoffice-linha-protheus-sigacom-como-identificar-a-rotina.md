---
article_id: 6516120118679
category: Materiais - Compras (SIGACOM)
content_hash: 783663a5d64a1a44e56746e577bcebbbcdc6d402e8e03ceb9135e4a300a0258d
fetched_at: '2026-06-28T22:41:11.597183+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Como identificar
  a rotina que gerou a Nota ?
type: support-article
updated_at: '2022-06-03T14:53:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6516120118679-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-Como-identificar-a-rotina-que-gerou-a-Nota
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como identificar a rotina que gerou a Nota ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**Realize uma consulta via APDSU, filtrando a tabela SF1 pelo campo F1\_ORIGLAN.

Abaixo segue a rotina a qual o campo se refere:

F1\_ORIGLAN = F (MATA116)

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6519814702231/imagem2.png)

F1\_ORIGLAN = LF (MATA910)

![imagem4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6519900998167/imagem4.png)

F1\_ORIGLAN = D (MATA119)

![imagem3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6519894730135/imagem3.png)

Quando a Nota é lançada pela rotina MATA103, o campo F1\_ORIGLAN fica em branco, visto que a rotina é nativa do módulo de Compras.

**Observação**: Quando a Nota for inclusa pelo processo de Importação XML, o campo que estará preenchido, é o F1\_ORIGEM:

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6516055132951/imagem1.png)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
