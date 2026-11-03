---
article_id: 30066939837591
category: Rental by ItUp Business
content_hash: 1fe19371df945113ad327124ac94623fc97bbe523bd21b15d6294eb09ba2c707
fetched_at: '2026-06-28T22:36:20.554626+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como fazer o aceite da AS
  no momento da geração de contrato?
type: support-article
updated_at: '2026-04-09T12:57:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30066939837591-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-fazer-o-aceite-da-AS-no-momento-da-gera%C3%A7%C3%A3o-de-contrato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30066939808919) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como fazer o aceite da AS de forma automática no momento da geração de contrato?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - a partir da versão P12.1.2310.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse o configurador (**SIGACFG**) >> **Ambiente** >> **Cadastro** >> **Parâmetros**;

2. Localize o parâmetro **MV\_LOCX207**;

|  |  |
| --- | --- |
| MV\_LOCX207 | Se .T. AS e aceita no momento da geração de contrato (ACEITE AUTOMÁTICO DE AS) |

3. **MV\_LOCX207**: Caso esteja configurado como **.F.**, altere para **.T.**. Com essa configuração, ao gerar o contrato na rotina **LOCA001**, o apontador AS será realizado automaticamente no momento da geração do contrato (**ACEITE AUTOMÁTICO DE AS**).
