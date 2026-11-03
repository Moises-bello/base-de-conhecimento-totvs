---
article_id: 30114784066839
category: Rental by ItUp Business
content_hash: 6f516942bac85ecbb942ac6bd248a80ec0f8d550a28c71b6eb794431f3f97b06
fetched_at: '2026-06-28T22:36:20.527292+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como desativar o processo
  automático de geração da Nota Fiscal de Remessa?
type: support-article
updated_at: '2026-04-09T12:58:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30114784066839-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-desativar-o-processo-autom%C3%A1tico-de-gera%C3%A7%C3%A3o-da-Nota-Fiscal-de-Remessa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30114784045719) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como desativar o processo automático de geração da Nota Fiscal de Remessa?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - a partir da versão P12.1.2310.  
  
**Solução**

Para solucionar essa dúvida, siga os passos abaixo:

1. Acesse **SIGACFG >> Ambiente >> Cadastro >> Parâmetros**;
2. Localize o parâmetro **MV\_GERNFS**;
3. Altere o valor do parâmetro **MV\_GERNFS** para **'.F.'**;
4. Com essa alteração, ao gerar a Nota Fiscal de Remessa, o sistema criará apenas o '*pedido de venda*' na rotina **MATA410**, sem realizar o faturamento automático.
