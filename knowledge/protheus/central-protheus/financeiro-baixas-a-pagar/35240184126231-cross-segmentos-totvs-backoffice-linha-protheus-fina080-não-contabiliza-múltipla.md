---
article_id: 35240184126231
category: Financeiro - Baixas a Pagar
content_hash: 0c54662a695c5586e103c603dbc11394621bc58642a8edae7b70bb49ec0151f8
fetched_at: '2026-06-28T22:37:24.901889+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - FINA080 - Não contabiliza
  múltiplas naturezas aplicado na inclusão do título
type: support-article
updated_at: '2026-03-04T17:10:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35240184126231-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-FINA080-N%C3%A3o-contabiliza-m%C3%BAltiplas-naturezas-aplicado-na-inclus%C3%A3o-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35240191776535) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a contabilização dos dados de múltiplas naturezas **SEV**, não apresenta no Lançamento Contábil da **LP** **530.**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Causa**  
Esse incidente ocorre quando a empresa possui o LP 510, pois, nesse posicionamento na SEV, seja em modo **Online** ou **Offline**, o campo **EV\_LA** é gravado com o valor "**S**". Essa condição impede a contabilização da baixa de múltiplas naturezas pelo **LP 530**.  
  
**Solução**  
Trata-se de um comportamento padrão do sistema. O lançamento padrão **"510/513"** irá contabilizar o rateio por múltiplas naturezas, **campos E2\_MULTNAT igual a "1" e EV\_RATEICC igual a "2".**

Neste caso, para evitar duplicidade nos processos de contabilização, ao possuir LP de inclusão de título, não será possível contabilizar no **LP 530.** Deve-se parametrizar para posicionar as múltiplas naturezas e levar os dados para a contabilização pelo **LP 510** e contabilizar somente a movimentação financeira no **LP 530.**  
  
**Saiba mais**  
[Como utilizar rateio de múltiplas naturezas por Centro de Custo?](https://tdn.totvs.com/pages/releaseview.action?pageId=229147656)
