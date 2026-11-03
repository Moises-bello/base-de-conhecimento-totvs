---
article_id: 34899354769431
category: Financeiro - Viagens
content_hash: fc5180cc03114f5397ba41b06593938486fedeeef8a505e77bf26dc823096d2b
fetched_at: '2026-06-28T22:38:21.240339+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - App Minha Prestação
  de Contas - Enquanto você tiver itens pendentes para serem sincronizados não será
  possível finalizar esta prestação
type: support-article
updated_at: '2025-09-12T19:25:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34899354769431-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-App-Minha-Presta%C3%A7%C3%A3o-de-Contas-Enquanto-voc%C3%AA-tiver-itens-pendentes-para-serem-sincronizados-n%C3%A3o-ser%C3%A1-poss%C3%ADvel-finalizar-esta-presta%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34899366627095) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Mensagem: Enquanto você tiver itens pendentes para serem sincronizados, não será possível finalizar esta prestação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34899366628375)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**  
Este cenário pode ocorrer devido a algumas situações:  
  
**Solução**

A seguir constam alguns pontos a serem validados quando ocorrer essa mensagem no **APP**.

Os itens que aparecem com linha de cor branca são aqueles que já foram sincronizados com sucesso. Ou seja, esses dados saíram da fila de memória do celular (um software interno do aparelho), foram enviados ao Protheus e receberam retorno positivo.

Os itens que aparecem com linha de cor cinza estão aguardando envio ou resposta. Eles podem estar:

* Ainda na fila da memória do celular, aguardando sua vez para ser processados no envio.
* Ou esperando o retorno do Protheus para concluir a sincronização e, então, mudar para a linha branca.

Importante

**Se o aplicativo for encerrado ou o usuário desconectar, a fila interna será limpa, e as despesas pendentes serão perdidas.**

Possíveis causas da demora na sincronização e da mensagem **"HELP"**:

1. O próprio celular pode encerrar o processo da fila por estar com o aplicativo "não respondendo"ou "parado".

2. O sistema operacional pode finalizar o processo em segundo plano para preservar bateria e desempenho, devido a:

* 3. Consumo elevado de energia **(bateria).**
* 4. Uso excessivo de memória **RAM.**
* 5.  Regras do sistema para liberar recursos.
* 6. Manutenção geral do desempenho do aparelho.

Normalmente, essas ações ocorrem de forma silenciosa, sem notificar o usuário. Caso o celular esteja com sinal fraco ou sem internet, a mensagem pode já ter sido encaminhada ao Protheus e estar pendente de resposta. O aplicativo opera offline, então o envio e o retorno podem demorar.

**Saiba mais**  
[Guia de uso - Minha Prestação de Contas](https://tdn.totvs.com/pages/releaseview.action?pageId=287057777)
