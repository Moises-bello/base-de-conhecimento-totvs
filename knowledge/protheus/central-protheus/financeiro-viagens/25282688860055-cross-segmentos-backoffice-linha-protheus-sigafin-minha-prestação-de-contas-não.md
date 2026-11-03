---
article_id: 25282688860055
category: Financeiro - Viagens
content_hash: 16301b960c15c88580a2fb542a2e818aa4751996d6e165eb648067c0ae9bbc49
fetched_at: '2026-06-28T22:38:21.474224+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Minha Prestação de
  Contas - Não existe licença disponível
type: support-article
updated_at: '2024-07-30T18:42:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25282688860055-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Minha-Presta%C3%A7%C3%A3o-de-Contas-N%C3%A3o-existe-licen%C3%A7a-dispon%C3%ADvel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25282688836247) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No App Minha Prestação de Contas ao tentar realizar uma prestação de contas, ocorre a mensagem de erro.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/25282711370391)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Este cenário ocorre devido à falta de licenças especificas para uso do App Minha Prestação de Contas ou falha na configuração do REST de aplicações Mobile.  
  
**Solução**

1 - Inicialmente é necessário avaliar no License Server, se possui algumas das licenças abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25282711377943)

**Exemplo**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25282711384343)

Caso não possua, será necessário entrar em contato com o seu **Analista de Negócios e Soluções TOTVS** para adquirir as licenças necessárias.

2 - Caso possua as licenças, avalie se seu ini do **REST (Appserver.ini)** possui as chaves abaixo e distribuições de licenças.   
  
Na seção abaixo configure as licenças conforme a distribuição

Exemplo, 110 licenças disponíveis

**[HTTPURI]**  
URL=/rest  
PrepareIn=04,01  
**Instances=1,109**  
CORSEnable=1  
AllowOrigin=\*  
**StateLess=1**  
  
**Saiba mais:**  
[Configuração do REST Protheus para uso com os aplicativos Mobile](https://tdn.totvs.com/pages/releaseview.action?pageId=519719292)[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Configuração para uso do aplicativo Minha Prestação de Contas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8324664329367)
