---
article_id: 360060286954
category: SIGAEST - LEGAIS
content_hash: fa3d8e74df66cac2a70a53209e7db4efb2e7cc5a6a13a210adb2d916e6d8956a
fetched_at: '2026-06-28T22:38:51.584780+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Bloco K  - Error.log
  : 1 - ORA-00001: unique constraint (TOTVSRECH.D3G010_PK) violated '
type: support-article
updated_at: '2022-08-24T19:30:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060286954-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Bloco-K-Error-log-1-ORA-00001-unique-constraint-TOTVSRECH-D3G010-PK-violated
---

**Dúvida**Ao gerar o SPED Fiscal no Protheus com Bloco K = Sim o sistema gera o seguinte error.log: "*Error : 1 - ORA-00001: unique constraint (TOTVSRECH.D3G010\_PK) violated*". O que fazer para resolver?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Para solucionar este problema, volte ao *Wizard* de parametrização da rotina SPEDFISCAL.

Selecione a pergunta "Processa histórico do Bloco K" = Não conforme mostra a imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100500814/mceclip0.png)

Ao final do processamento, gerará o SPED e não ocorrerá este error.log.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais/Fiscais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
