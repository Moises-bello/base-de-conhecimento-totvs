---
article_id: 35616742931479
category: SIGAACD - Automação e Coleta de Dados
content_hash: b8f01e9c8c298f127931bcdfc202fa1e6f9b76dc183d99031d7bd1d14806029c
fetched_at: '2026-06-28T22:39:12.682919+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Duplicidade Parcial
  na Separação.
type: support-article
updated_at: '2025-10-14T12:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35616742931479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Duplicidade-Parcial-na-Separa%C3%A7%C3%A3o
---

O incidente de Duplicidade Parcial na Separação no TOTVS BackOffice (Linha Protheus) pode ser resolvido atualizando o sistema com as últimas versões que corrigem o fonte ACDA100. Recomenda-se aplicar a atualização em ambiente de homologação e realizar backup prévio. Links das versões corrigidas estão disponíveis para download.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35616726348311) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como resolver o incidente de Duplicidade Parcial na Separação?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Foi identificado um problema no ponto de entrada ACDV166VI, onde a rotina pode ficar incorretamente em loop infinito, caso nao hajam mais itens aptos a serem apresentados ao usuario, por conta do retorno do ponto de entrada.

Realizado tratamento no retorno do PE ACD166VI em caso de final de arquivo sair abandonar o laco de pesquisa dos produtos.

12.1.2210:<https://r.totvs.io/p/1213992> ; 12.1.2310:<https://r.totvs.io/p/1213993> ; 12.1.2410:<https://r.totvs.io/p/1213991> ; 12.1.2510:<https://r.totvs.io/p/1213994> ;

Recomendamos que aplique em base de homologação, realizar o backup das informações.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
