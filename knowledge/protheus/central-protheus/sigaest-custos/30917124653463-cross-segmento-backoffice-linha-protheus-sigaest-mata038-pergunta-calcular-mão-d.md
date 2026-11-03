---
article_id: 30917124653463
category: SIGAEST - CUSTOS
content_hash: 93d32bb9a07c3ad16e98e34ba162b65c685d4fbd510e319d59b40a7849eefbfd
fetched_at: '2026-06-28T22:39:02.040301+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 Pergunta Calcular
  Mão de Obra é alterada durante o processamento da etapa de Custo
type: support-article
updated_at: '2025-03-25T19:09:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30917124653463-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-Pergunta-Calcular-M%C3%A3o-de-Obra-%C3%A9-alterada-durante-o-processamento-da-etapa-de-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30917147724695) Tempo aproximado para leitura: **00:01:45 min** **Dúvida**

Ao efetuar um Novo Fechamento a pergunta **Calcular Mão de obra** é alterada para **Não** durante o processamento na etapa de Custos. Qual seria a causa?

![CALCULAR MAO DE OBRA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/30917525852695)

![CALCULAR MAO DE OBRA ETAPA.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/30917525856663)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Esse cenário ocorre, quando incluido um novo Fechamento e na definição dos parâmetros de Contabilização habilitar a opção da forma de **Cálculo da Mão de Obra** como **Somente Produção**. Veja o print abaixo.

![CALCULAR MAO DE OBRA ETAPA 1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/30917699640087)

Dessa forma, voce esta definindo que a distribuição do calculo da MOD ocorre apenas na etapa de **PRODUÇÃO.**

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - Processo de configuração de MOD e GGF "Sem" e "Com" integração contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402062082071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Processo-de-configura%C3%A7%C3%A3o-de-MOD-e-GGF-Sem-e-Com-integra%C3%A7%C3%A3o-cont%C3%A1bil)
