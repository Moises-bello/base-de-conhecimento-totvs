---
article_id: 12290305345687
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3e87f7392044f08a48ed0d731f502ba9857e671c2b17065debe4d755e818666c
fetched_at: '2026-06-28T22:38:29.926838+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento(SIGAFAT)
  - Erro Dashboard "The requires authentication. The server might return this response
  for a page behind a login."
type: support-article
updated_at: '2025-01-10T20:23:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12290305345687-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Erro-Dashboard-The-requires-authentication-The-server-might-return-this-response-for-a-page-behind-a-login
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Erro ao acessar o Dashboard em outra filial "The requires authentication. The server might return this response for a page behind a login."

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento(SIGAFAT) - A partir da release 12.1.33;  
  
**Solução**

Para solucionar essa dúvida, realize os seguintes passos:

1. Acessar o Configurador(SIGACFG), na filial que esta ocorrendo o incidente;  
2. Localizar o parâmetro MV\_HVERAO e desabilitar colocando o conteúdo **".F."** ;

O incidente ocorre, pois com o parâmetro habilitado faz que o Token de autenticação do usuário, seja gerado com **'u*****ma hora a menos'***, fazendo com que ele seja gerado **'*****já expirado'***.

Saiba Mais;

[MP-FAT-Término do horário de Verão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022631391-MP-FAT-T%C3%A9rmino-do-hor%C3%A1rio-de-Ver%C3%A3o)
