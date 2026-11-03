---
article_id: 4413023003671
category: Financeiro - Contas a Pagar
content_hash: 02c1f0efae07b1cf255862d96401db061272947f41145f18933d762059f20460
fetched_at: '2026-06-28T22:38:07.013812+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Totvs BackOffice Protheus - SIGAFIN - FINA050 - Help: FA050RATEI
  - O valor do rateio não confere com o valor do título'
type: support-article
updated_at: '2026-06-16T17:05:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413023003671-Cross-Segmento-Totvs-BackOffice-Protheus-SIGAFIN-FINA050-Help-FA050RATEI-O-valor-do-rateio-n%C3%A3o-confere-com-o-valor-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41268581745175) Tempo aproximado para leitura: **00:05:00min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a inclusão de um título com rateio de CC, é apresentando o Help: FA050RATEI - O valor do rateio não confere com o valor do título

![fa050ratei.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4413022487063)

**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**  
Esse incidente ocorre, pois a tamanho do campo CTJ\_PERCEN por padrão vem com 2 casas decimais, conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413028720151)  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo de configurador - Sigacfg >>Base de dados>>Dicionários>>Base de dados  
2. Localize o campo CTJ\_PERCEN e ajuste o tamanho dos campos e picture para 4 casas decimais, conforme imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413028906903)

**Saiba mais**

<https://tdn.totvs.com/pages/releaseview.action?pageId=271391703>

<https://tdn.totvs.com/pages/releaseview.action?pageId=490636586>
