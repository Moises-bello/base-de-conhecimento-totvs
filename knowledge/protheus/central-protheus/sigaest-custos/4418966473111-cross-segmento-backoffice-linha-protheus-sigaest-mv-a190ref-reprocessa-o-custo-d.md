---
article_id: 4418966473111
category: SIGAEST - CUSTOS
content_hash: ba9e7bbdf2dcbe557f244bd90991e7b1169def2697a34b1648effc9e89c73549
fetched_at: '2026-06-28T22:39:02.262477+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MV_A190REF – Reprocessa
  o Custo de Entrada por referência Fiscal
type: support-article
updated_at: '2025-03-12T12:24:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418966473111-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MV-A190REF-Reprocessa-o-Custo-de-Entrada-por-refer%C3%AAncia-Fiscal
---

**Dúvida**Qual a funcionalidade do parâmetro MV\_A190REF, no custo de entrada?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**Realizada melhoria no **reprocessamento** do cálculo do custo de entrada executado pela rotina **Refaz Custo de Entrada (MATA190)** através das referencias fiscais (utilizadas no cadastro de TES).

Para isto, foi criado o parâmetro **MV\_A190REF que será utilizado para ativar o cálculo através das referências fiscais utilizadas na composição do custo de entrada**. Para isso o mesmo deve estar ATIVO com a configuração .T.

**Procedimento para Implementação do parâmetro caso não tenha:**

No Configurador (SIGACFG), acesse Ambientes/Cadastros/Parâmetros (CFGX017).

Crie o parâmetro a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418977690903/mceclip0.png)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Refaz Custo de Entrada (MATA190) - Conceito e Exemplos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051999634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Refaz-Custo-de-Entrada-MATA190-Conceito-e-Exemplos)

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
