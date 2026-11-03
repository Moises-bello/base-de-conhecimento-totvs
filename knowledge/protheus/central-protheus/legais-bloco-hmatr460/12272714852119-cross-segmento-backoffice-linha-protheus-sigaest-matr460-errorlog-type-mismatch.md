---
article_id: 12272714852119
category: LEGAIS - BLOCO H/MATR460
content_hash: c91b333f21a1ab27aac30d655761f8f653756a508f1b90e8188895c46bd25f1d
fetched_at: '2026-06-28T22:42:15.128526+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Error.log
  type mismatch on compare on REPORTPRINT(MATR460.PRX)
type: support-article
updated_at: '2023-02-08T18:36:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12272714852119-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Error-log-type-mismatch-on-compare-on-REPORTPRINT-MATR460-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:37 min****Ocorrência**

Ao emitir o relatório P7 (MATR460) é apresentado o seguinte error.log: "***type mismatch on compare on REPORTPRINT(MATR460.PRX)***"

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**  
Esse incidente ocorre, pois existe inconsistência no arquivo de perguntas (SX1) do relatório em relação ao padrão. Os casos mais comuns são: duplicidades de perguntas, perguntas deletadas e perguntas de tipos diferentes do padrão.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Compare o seu grupo de Perguntas **MTR460** com o padrão, conforme print abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12272647421207)

2. Avalie se não tem duplicados, deletados ou se a coluna Tipo de alguma pergunta está diferente do padrão;

3. Efetue as correções necessárias primeiramente em ambiente de homologação;

4. Teste novamente a exibição do relatório.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre o relatório P7 (MATR460)*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)
