---
article_id: 38769432221975
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 57bdad90bd013224713b9c91d0c343eede6bb88665bf0d59946c9905c5e2faf8
fetched_at: '2026-06-28T22:38:54.299579+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao utilizar o ponto
  de entrada MA106GER, não são geradas as Solicitações ao Armazém.
type: support-article
updated_at: '2026-03-10T11:35:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38769432221975-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-utilizar-o-ponto-de-entrada-MA106GER-n%C3%A3o-s%C3%A3o-geradas-as-Solicita%C3%A7%C3%B5es-ao-Armaz%C3%A9m
---

O ponto de entrada MA106GER não gera Solicitações ao Armazém ao usar ThisMark(). A função ThisMark() foi substituída por A106Proc() para corrigir isso. Para gerar Solicitações, é necessário customizar a rotina via pontos de entrada disponíveis. Links com mais informações e instruções estão disponíveis para consulta.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38769432211095) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**

Ao utilizar o ponto de entrada MA106GER, não são geradas as Solicitações ao Armazém quando a função ThisMark() é utilizada.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
  
**Solução**  
Após analise do time do desenvolvimento, no ponto de entrada **MA106GER**, o mesmosubstitui a função de geração da pré requisição. Sendo necessário o cliente customizar toda baixa.

Segue o boletim do ponto de entrada para maiores informações:

* [MA106GER - Geração de pre requisições](https://tdn.totvs.com/pages/releaseview.action?pageId=6085342)

Caso necessite customizar a baixa da Pré Requisição, é necessário customizar através dos pontos de entrada disponíveis:

* [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA106 - Pontos de Entrada da rotina Pré-Requisição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415272426647-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA106-Pontos-de-Entrada-da-rotina-Pr%C3%A9-Requisi%C3%A7%C3%A3o)
* [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA185 - Pontos de Entrada da rotina Baixa de Pré-Requisição ao Armazém](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004530301-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA185-Pontos-de-Entrada-da-rotina-Baixa-de-Pr%C3%A9-Requisi%C3%A7%C3%A3o-ao-Armaz%C3%A9m)

Para inserir filtro em Query, pode ser usado o ponto de entrada [**MT106QRY**](https://tdn.totvs.com/pages/releaseview.action?pageId=6087706)**.**

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
