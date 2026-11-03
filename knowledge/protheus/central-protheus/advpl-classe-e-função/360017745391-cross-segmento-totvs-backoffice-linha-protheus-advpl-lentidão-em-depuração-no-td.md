---
article_id: 360017745391
category: ADVPL - Classe e Função
content_hash: 509d152a7270983ea02d1f44a999dcf312d7cf4424694e57a9a8c78843d05b6d
fetched_at: '2026-06-28T22:40:14.312444+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -  Lentidão em depuração
  no TDS
type: support-article
updated_at: '2022-01-03T19:55:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017745391-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Lentid%C3%A3o-em-depura%C3%A7%C3%A3o-no-TDS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como Resolver problemas de lentidão em depuração no TDS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 11.80  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Desabilite o sincronismo de dicionário de dados na visão Tabela de Dados, conforme figura abaixo:  
   ![](https://totvssuporte.zendesk.com/attachments/token/p6EjSItqNeNmH4IU76OL4Dboi/?name=inline1316044597.png)
2. Iniba as variáveis públicas e estáticas na visão de variáveis:  
   ![](https://totvssuporte.zendesk.com/attachments/token/mYKEAOZkWxTUGOEs6t61IGkMR/?name=inline308974359.png)​

Observação: Execute o *debug* novamente. Caso a lentidão desapareça, verificar latência de sua rede e continuar utilizando o **TDS** com essas opções, mostrando as variáveis e dados somente no momento necessário.

**Saiba mais**[**Depuração no TDS 11.3**](http://tdn.totvs.com/pages/viewpage.action?pageId=239012542)
